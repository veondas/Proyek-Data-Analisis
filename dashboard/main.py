import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
day_df = pd.read_csv("dashboard/DataBaru.csv")

# Streamlit Dashboard
st.title(':sparkles: Proyek Analisis Data: Bike Sharing :sparkles:')
st.write(
    """
    Nama        : Parveen Uzma Habidin  
    Email       : prvnuzmhbdn@gmail.com  
    ID Dicoding : MC325D5X1356
    """
)


# Visualisasi 1: Hari Kerja vs Hari Libur
st.subheader("Perbandingan Peminjaman Sepeda: Hari Libur vs Hari Kerja")
Totpmjmn = day_df.groupby('holiday')["cnt"].sum()
Thari = day_df["holiday"].value_counts()
Mean = Totpmjmn / Thari
data = pd.DataFrame({
    "Kategori": ["Hari Kerja", "Hari Libur"],
    "Rata-rata Peminjaman per Hari": Mean.values
})
fig = px.bar(data, x="Kategori", y="Rata-rata Peminjaman per Hari", color="Kategori", title="Perbandingan Peminjaman Sepeda")
st.plotly_chart(fig)

# Toggle untuk Menampilkan Insight
if st.toggle("Tampilkan Insight Hari Libur vs Hari Kerja"):
    st.subheader("Insight")
    st.info("Data terbanyak ada pada Hari Libur")

# Visualisasi 2: Peminjaman Berdasarkan Musim
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
stats = day_df.groupby("season")["cnt"].agg(total="sum", jmlhari="count", mean="mean").round(2)
fig = px.bar(stats, x=stats.index.astype(str), y="mean", title="Rata-rata Peminjaman Sepeda Berdasarkan Musim", labels={'x': 'Musim', 'mean': 'Rata-rata Peminjaman per Hari'}, color=stats.index.astype(str))
st.plotly_chart(fig)

# Toggle untuk Menampilkan Insight Musim
if st.toggle("Tampilkan Insight Musim"):
    st.subheader("Insight")
    st.info("Data terbanyak ada pada musim gugur")

# Visualisasi 3: Distribusi Berdasarkan Musim
st.subheader("Distribusi Data Berdasarkan Musim")
fig = px.histogram(day_df, x="season", color="season", title="Distribusi Data Berdasarkan Musim")
st.plotly_chart(fig)

# Menampilkan Conclusion
st.markdown("### 📌 Conclusion")
st.markdown(
    """
    - **Pertanyaan 1**: Peminjaman sepeda cenderung lebih tinggi pada hari libur dibandingkan dengan hari kerja, yang mengindikasikan bahwa sepeda lebih sering dimanfaatkan untuk kegiatan rekreasi saat liburan.
      Walaupun jumlah hari kerja lebih banyak, rata-rata penggunaan harian tetap lebih besar pada hari libur. Kondisi ini dapat dimanfaatkan oleh penyedia layanan untuk mengoptimalkan operasional.
      
    - **Pertanyaan 2**: Peminjaman sepeda bervariasi menurut musim, dengan angka tertinggi pada musim gugur dan panas, kemungkinan karena cuaca yang lebih mendukung aktivitas luar ruangan.
      Musim dingin masih memiliki peminjaman yang cukup tinggi, meskipun suhu rendah bisa menjadi tantangan. Sementara itu, musim semi mencatat peminjaman terendah, mungkin akibat cuaca yang tidak stabil.
    """
)
