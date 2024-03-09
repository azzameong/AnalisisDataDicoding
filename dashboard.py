import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_seasonHoliday(df):
    season_holiday = df.groupby(by=["season", "holiday"]).agg({
        "casual": ["max", "min", "mean", "sum"],
        "registered": ["max", "min", "mean", "sum"]
    })

    season_holiday = season_holiday.reset_index()

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))
    colors = ['#FF489D','#b1d5c8','#FF489D','#b1d5c8']

    sns.barplot(x="season", y=("casual", "sum"), hue="holiday", data=season_holiday, palette=colors, ax=axs[0])
    axs[0].set_ylabel("Peminjam Casual")
    axs[0].set_xlabel("Season")
    axs[0].set_title("Jumlah Peminjaman Sepeda Casual berdasarkan Season dan Holiday", fontsize=15)
    axs[0].tick_params(axis='x', labelsize=12)
    axs[0].tick_params(axis='y', labelsize=12)

    sns.barplot(x="season", y=("registered", "sum"), hue="holiday", data=season_holiday, palette=colors, ax=axs[1])
    axs[1].set_ylabel("Peminjam Registered")
    axs[1].set_xlabel("Season")
    axs[1].set_title("Jumlah Peminjaman Sepeda Registered berdasarkan Season dan Holiday", fontsize=15)
    axs[1].tick_params(axis='x', labelsize=12)
    axs[1].tick_params(axis='y', labelsize=12)

    plt.tight_layout()
    return fig

def create_hourBehavior(df):
    hourBehavior = df.groupby(by=["hr"]).agg({
        "cnt": ["min", "max", "count", "sum"],
        "casual": "sum",
        "registered": "sum"
    }).reset_index()

    hours = hourBehavior['hr']
    cntSum= hourBehavior['cnt']['sum']
    casualSum = hourBehavior['casual']['sum']
    registeredSum = hourBehavior['registered']['sum']

    plt.figure(figsize=(10, 6))
    plt.plot(hours, cntSum, label='Total Gabungan', color='#92a1e0', linestyle='--')
    plt.plot(hours, casualSum, label='Total Casual', color='#FF489D', linewidth=4)
    plt.plot(hours, registeredSum, label='Total Registered', color='#b1d5c8', linewidth=4)

    plt.title('RENTAL SEPEDA (2011-2012): dalam 24 jam')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Total')
    plt.legend()

    plt.grid(True)
    return plt.gcf()

st.title("Projek Analisis Data nya Azza :)")
st.header('Rental Sepeda 2011-2012"🚲"')
st.text('Lebih ke Casual dan Registered Peminjam')

st.header("Aspek Musim dengan Holiday-annya")
dayBike = pd.read_csv("https://raw.githubusercontent.com/azzameong/AnalisisDataDicoding/main/Bike-sharing-dataset/day.csv")
st.pyplot(create_seasonHoliday(dayBike))

st.header("Perilaku Peminjam pada jam tertentu")
hourBike = pd.read_csv("https://raw.githubusercontent.com/azzameong/AnalisisDataDicoding/main/Bike-sharing-dataset/hour.csv")
st.pyplot(create_hourBehavior(hourBike))

st.caption('Copyright (c) Dicoding 2023 & Azza 2024')