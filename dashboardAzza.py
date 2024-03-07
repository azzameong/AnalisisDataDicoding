import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

def create_seasonHoliday(df):
    seasonHoliday = df.groupby(by=["season", "holiday"]).agg({"cnt": "count"})
    pivot_data = seasonHoliday.reset_index().pivot(index='season', columns='holiday', values='cnt')

    fig, ax = plt.subplots()
    pivot_data.plot(kind='bar', stacked=False, color=['#FF489D', '#b1d5c8'], ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('Count')
    ax.set_title('RENTAL SEPEDA : Season dan Holiday')
    ax.legend(title='ke-Holiday-an', labels=['Non-Holiday', 'Holiday'])
    ax.set_xticks(range(len(pivot_data.index)))
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
    return fig

def create_behavior(df):
    behavior = df.groupby(by=["hr"]).agg({
        "cnt": ["min", "max", "count"],
        "casual": "mean",
        "registered": "mean"
    }).reset_index()

    hours = behavior['hr']
    cnt_min = behavior['cnt']['min']
    cnt_max = behavior['cnt']['max']
    cnt_count = behavior['cnt']['count']
    casual_mean = behavior['casual']['mean']
    registered_mean = behavior['registered']['mean']

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hours, cnt_min, label='Peminjaman Tersedikit', color='#92a1e0', linestyle=':')
    ax.plot(hours, cnt_max, label='Peminjaman Terbanyak', color='#92a1e0', linestyle='--')
    ax.plot(hours, cnt_count, label='Total Jam', color='#f4c917')
    ax.plot(hours, casual_mean, label='Rata Peminjam Casual', color='#FF489D', linewidth=4)
    ax.plot(hours, registered_mean, label='Rata Peminjam Registered', color='#b1d5c8', linewidth=4)

    ax.set_title('RENTAL SEPEDA : dalam 24 jam')
    ax.set_xlabel('Hour')
    ax.set_ylabel('Count')
    ax.legend()
    ax.grid(True)
    return fig

dayBike_url = "https://raw.githubusercontent.com/azzameong/AnalisisDataDicoding/main/Bike-sharing-dataset/day.csv"
hourBike_url = "https://raw.githubusercontent.com/azzameong/AnalisisDataDicoding/main/Bike-sharing-dataset/hour.csv"

dayBike = pd.read_csv(dayBike_url)
hourBike = pd.read_csv(hourBike_url)


st.title("Projek Analisis Data Azza Annathifa")
st.header('Rental Sepeda 2011-2012:rose:')
tab1, tab2 = st.columns(2)

with tab1:
    st.header("Aspek Musim dengan Holiday-annya")
    st.pyplot(create_seasonHoliday(dayBike))

with tab2:
    st.header("Perilaku Peminjam pada jam tertentu")
    st.pyplot(create_behavior(hourBike))