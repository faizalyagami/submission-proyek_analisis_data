import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("../data/day.csv")
hour_df = pd.read_csv("../data/hour.csv")

# Membuat pemetaan untuk musim
season_mapping = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}

# Mengganti angka musim dengan deskripsi musim
day_df['season'] = day_df['season'].map(season_mapping)

# Dashboard dengan Streamlit
st.title("Dashboard Analisis Data Bike Sharing")
st.subheader("Prediksi Jumlah Penyewa Sepeda Berdasarkan Cuaca")

# Visualisasi scatter plot
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=day_df, ax=ax)  # Menggunakan day_df
st.pyplot(fig)

# Filter berdasarkan musim
season = st.selectbox('Pilih Musim', day_df['season'].unique())
filtered_data = day_df[day_df['season'] == season]
st.write(filtered_data)