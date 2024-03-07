import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Proyek Analisis Data: Bike Sharing Dataset')

st.header('Bike Sharing Dashboard')
st.markdown(
    '''
Sharing bike system adalah generasi baru dari persewaan sepeda tradisional 
di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian menjadi otomatis. 
Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi ke posisi lain. 
Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang mencakup lebih dari 500 ribu sepeda. 
Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam masalah lalu lintas, 
lingkungan dan kesehatan.
    '''
)
day_df = pd.read_csv("day_df.csv")

st.subheader('Exploratory Data Analysis')
st.write('***Distribution of Data CNT***')
arr = day_df['cnt']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
st.markdown(
    '''
Dilakukan pengujian terhadap normalitas data menggunakan histogram, diketahui bahwa sebaran data dari kolom 'cnt' yang berupa data total sepeda yang dipinjam menyebar dengan sebaran normal. 
Data diketahui berdistribusi normal dari bentuk sebaran yang simetris dan berada memusat di tengah. 
Pengujian ini perlu dilakukan untuk memenuhi asumsi sebelum melakukan uji regresi linear.
'''
)

st.write('***Pembuatan Pivot Tabel Pembantu Pie Chart***')
code = """season_grouped = day_df.groupby('season')['cnt'].agg(['sum', 'mean', 'max', 'min'])
print(season_grouped)"""
st.code(code,language='python')

st.write('***Time Series Windspeed 2011-2012***')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

fig, ax = plt.subplots(figsize = (12,5))
ax.plot(
    day_df['dteday'],
    day_df['windspeed'],
    marker='o',
    linewidth=2
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
st.markdown(
    '''
Diketahui bahwa kecepatan angin sepanjang tahun 2011 - 2012 memiliki pola musiman yang cukup stasioner. 
Hal ini dapat dilihat dari bentuk grafik yang memiliki pola berulang setiap tanggal 1 Januari
'''
)

st.write('***Time Series Temperature 2011-2012***')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

fig, ax = plt.subplots(figsize = (12,5))
ax.plot(
    day_df['dteday'],
    day_df['temp'],
    marker='o',
    linewidth=2,
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
st.markdown(
    '''
Diketahui bahwa temperatur sepanjang tahun 2011 - 2012 memiliki pola musiman. 
Hal ini dapat dilihat dari bentuk grafik yang memiliki pola berulang setiap tanggal 1 Januari
'''
)

st.subheader('Count of Total Rental Bikes by Season')
# Visualisasi data dengan line chart
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

fig, ax = plt.subplots(figsize = (12,5))
ax.plot(
    day_df['dteday'],
    day_df['cnt'],
    marker='o',
    linewidth=2
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.markdown(
    '''
***Conclusion***:
Diketahui penyewaan sepeda paling banyak dilakukan pada setiap musim gugur baik di tahun 2011 dan 2012. 
Rata-rata penyewaan sepeda pada musim gugur mencapai sekitar 5644 sepeda per tahunnya. 
Banyaknya sepeda yang disewa pada musim gugur tahun 2011 mengalami kenaikan pada musim gugur tahun 2012, 
pola ini dapat dianggap musiman dan tren naik. 
    '''
)

st.subheader('The Effect of External Factors to Rental Bikes')
st.markdown(
    '''
Untuk mengetahui pengaruh dari faktor eksternal terhadap penyewaan sepeda, 
dapat dilakukan analisis menggunakan regresi dan korelasi.
'''
)
code = """# Mengetahui pengaruh temperatur terhadap jumlah penyewaan sepeda
sns.regplot(x = day_df['temp'], y = day_df['cnt'])
plt.show()
# Mencari hubungan antara temperatur dengan jumlah penyewaan sepeda
r = np.corrcoef(x = day_df['temp'], y = day_df['cnt'])
r"""
st.code(code,language='python')
st.markdown(
    '''
>>> Berdasarkan plot regresi yang terbentuk di atas, titik yang diplot tersebar secara acak dan berbentuk menyerupai garis lurus sehingga dapat diketahui bahwa terdapat pengaruh dari temperatur terhadap banyak sepeda yang dirental per harinya. 
Selain itu, berdasarkan korelasi diketahui bahwa kedua variabel berkorelasi kuat positif sebesar 0,6275. 
Artinya semakin tinggi temperatur maka semakin banyak pula sepeda yang disewa
'''
)

code = """# Mengetahui pengaruh kecepatan angin terhadap jumlah penyewaan sepeda
sns.regplot(x = day_df['windspeed'], y = day_df['cnt'])
plt.show()
# Mencari hubungan antara kecepatan angin dengan jumlah penyewaan sepeda
p = np.corrcoef(x = day_df['windspeed'], y = day_df['cnt'])
p"""
st.code(code,language='python')
st.markdown(
    '''
>>> Berdasarkan plot regresi yang terbentuk di atas, titik yang diplot tersebar secara acak dan tidak berbentuk menyerupai garis lurus sehingga dapat diketahui bahwa tidak terdapat pengaruh dari kecepatan angin terhadap banyak sepeda yang disewa per harinya. 
Selain itu, berdasarkan korelasi diketahui bahwa kedua variabel berkorelasi lemah negatif sebesar -0,235. 
Artinya semakin rendah kecepatan angin maka semakin banyak sepeda yang disewa dan semakin tinggi kecepatan angin maka semakin dikit sepeda yang disewa.
'''
)
code = """# Mengetahui pengaruh kelembapan terhadap jumlah penyewaan sepeda
sns.regplot(x = day_df['hum'], y = day_df['cnt'])
plt.show()
# Mencari hubungan antara kecepatan angin dengan jumlah penyewaan sepeda
q = np.corrcoef(x = day_df['hum'], y = day_df['cnt'])
q"""
st.code(code,language='python')
st.markdown(
    '''
>>> Berdasarkan plot regresi yang terbentuk di atas, titik yang diplot tersebar secara acak dan tidak berbentuk menyerupai garis lurus sehingga dapat diketahui bahwa tidak terdapat pengaruh dari kelembapan terhadap banyak sepeda yang dirental per harinya. 
Selain itu, berdasarkan korelasi diketahui bahwa kedua variabel berkorelasi lemah negatif sebesar -0,1007. 
Artinya semakin rendah kelembapan maka semakin banyak sepeda yang disewa dan semakin tinggi kelembapan maka semakin dikit sepeda yang disewa.
'''
)

st.markdown(
    '''
***Conclusion***: 
Diketahui bahwa temperatur mempengaruhi secara signifikan jumlah sepeda yang disewa per harinya. 
Dimana terdapat hubungan yang cukup kuat antara temperatur lingkungan terhadap penyewaan sepeda, 
kenaikan suhu akan meningkatkan kenaikan penyewaan sepeda. Sedangkan kenaikan kecepatan angin dan kelembapan akan menurunkan
jumlah penyewaan sepeda.
'''
)

st.subheader('Casual Users vs Registered Users')
st.write('***Comparing Casual & Registered Users 2011-2012***')
# Visualisasi Casual users dan Registered users dengan bar chart
col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#D3D3D3", "#90CAF9"]
 
    sns.barplot(
        y="casual", 
        x="yr",
        data=day_df.sort_values(by="casual", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of casual users", loc="center", fontsize=50)
    ax.set_ylabel('Casual Users')
    ax.set_xlabel('Year')
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9"]
 
    sns.barplot(
        y="registered", 
        x="yr",
        data=day_df.sort_values(by="registered", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of registered users", loc="center", fontsize=50)
    ax.set_ylabel('Registered Users')
    ax.set_xlabel('Year')
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

st.markdown(
    '''
Berdasarkan bar chart di atas dapat diketahui bahwa pengguna terdaftar mengalami kenaikan yang cukup besar pada tahun 2012. 
Begitu juga pengguna biasa mengalami kenaikan pada tahun 2012
'''
)
st.write('**Perbandingan Casual Users dengan Registered Users**')
# Pie chart
users = ['Casual Users', 'Registered Users']
data = [848.1764705882352, 3656.172366621067]

fig1, ax1 = plt.subplots()
ax1.pie(data, labels=users, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  
st.pyplot(fig1)
st.markdown(
    '''
Berdasarkan pie chart yang terbentuk, 
dapat diketahui bahwa rata-rata registered users yang menyewa sepeda selama tahun 2011 - 2012 lebih banyak dibanding casual users
'''
)

st.markdown(
    '''
***Conclusion***: 
Dapat disimpulkan rata-rata sepeda yang disewa oleh pengguna terdaftar lebih banyak dibandingkan dengan rata-rata sepeda yang disewa oleh pengguna biasa. 
Terdapat pula kenaikan rata rata pengguna terdaftar pada tahun 2012 dari tahun 2011
'''
)