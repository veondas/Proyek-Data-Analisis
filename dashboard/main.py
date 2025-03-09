import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
file_path = 'dashboard/DataBaru.csv'
day_df = pd.read_csv(file_path)

# Hitung total peminjaman dan jumlah hari berdasarkan kategori libur
Totpmjmn = day_df.groupby('holiday')['cnt'].sum()
Thari = day_df['holiday'].value_counts()
Mean = Totpmjmn / Thari

data = pd.DataFrame({
    "Kategori": ["Hari Kerja", "Hari Libur"],
    "Total Peminjaman": Totpmjmn.values,
    "Total Hari": Thari.values,
    "Rata-rata Peminjaman per Hari": Mean.values
})

# Menghitung statistik peminjaman berdasarkan musim
stats = day_df.groupby("season")["cnt"].agg(total="sum", jmlhari="count", mean="mean").round(2)

# Streamlit Dashboard
st.title(':sparkles: Proyek Analisis Data: Bike Sharing :sparkles:')
st.write(
    """
    Nama        : Parveen Uzma Habidin  
    Email       : prvnuzmhbdn@gmail.com  
    ID Dicoding : MC325D5X1356
    """
)
st.title("Dashboard Peminjaman Sepeda")


# Visualisasi 1: Hari Kerja vs Hari Libur
st.subheader("Perbandingan Peminjaman Sepeda: Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(y=data["Kategori"], x=data["Rata-rata Peminjaman per Hari"], palette=["blue", "hotpink"], ax=ax)
ax.set_xlabel("Rata-rata Peminjaman per Hari")
ax.set_ylabel("Kategori")
ax.set_title("Perbandingan Peminjaman Sepeda: Hari Libur vs Hari Kerja")
st.pyplot(fig)

# Menampilkan Insight
st.subheader("Insight")
st.info("Data terbanyak ada pada Hari Libur")

# Visualisasi 2: Peminjaman Berdasarkan Musim
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(x=stats.index.astype(str), y=stats["mean"], palette="winter", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman per Hari")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
plt.xticks(rotation=30)
st.pyplot(fig)

# Menampilkan Insight
st.subheader("Insight")
st.info("Data terbanyak ada pada musim gugur")

# Menampilkan Conclusion
st.markdown("### 📌 Conclusion")
st.markdown("""
- **Pertanyaan 1**: Peminjaman sepeda cenderung lebih tinggi pada hari libur dibandingkan dengan hari kerja, yang mengindikasikan bahwa sepeda lebih sering dimanfaatkan untuk kegiatan rekreasi saat liburan. Walaupun jumlah hari kerja lebih banyak, rata-rata penggunaan harian tetap lebih besar pada hari libur. Kondisi ini dapat dimanfaatkan oleh penyedia layanan untuk mengoptimalkan operasional, misalnya dengan menambah jumlah sepeda atau memberikan penawaran khusus pada akhir pekan dan hari libur.
  
- **Pertanyaan 2**: Peminjaman sepeda bervariasi menurut musim, dengan angka tertinggi pada musim gugur dan panas, kemungkinan karena cuaca yang lebih mendukung aktivitas luar ruangan. Musim dingin masih memiliki peminjaman yang cukup tinggi, meskipun suhu rendah bisa menjadi tantangan. Sementara itu, musim semi mencatat peminjaman terendah, mungkin akibat cuaca yang tidak stabil. Pola ini dapat dimanfaatkan untuk strategi operasional, seperti meningkatkan promosi atau menyesuaikan ketersediaan sepeda sesuai musim.
""")
