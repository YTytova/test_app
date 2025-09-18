import streamlit as st
import pandas as pd

# завантаження даних
data = pd.read_csv("games_activity_combined (2.0).csv")

# переконатися, що колонка 'date' має тип datetime
data['activity_date'] = pd.to_datetime(data['activity_date'])

# заголовок
st.title("Games_activity")

# створюємо список мов + опція "All"
languages = ['All'] + list(data['language'].unique())
selected_language = st.selectbox("Виберіть мову", languages)

# поле для вибору діапазону дат
date_range = st.date_input("Виберіть період", 
                           value=[data['activity_date'].min().date(), data['activity_date'].max().date()])

start_date, end_date = date_range

# фільтрація
if selected_language == 'All':
    filtered_data = data[
        (data['activity_date'].dt.date >= start_date) &
        (data['activity_date'].dt.date <= end_date)
    ]
else:
    filtered_data = data[
        (data['language'] == selected_language) &
        (data['activity_date'].dt.date >= start_date) &
        (data['activity_date'].dt.date <= end_date)
    ]

if not filtered_data.empty:
    st.write("Games data", filtered_data)
    st.line_chart(filtered_data['language'])
else:
    st.error("No data found for the selected filters")
