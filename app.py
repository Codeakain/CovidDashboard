import pandas as pd
import streamlit as st
from libraries import *




countries = ['China', 'India', 'Sri Lanka','United States','Russia','United Kingdom','Australia','Spain','France']
data_types = ['cases', 'deaths', 'recovered']

st.sidebar.title("Adjust parameters of your dashboard here.")


days = st.sidebar.slider('Select Number of Days', min_value=1,max_value=90)
country = st.sidebar.selectbox("What Is Your Country",countries)
data_type = st.sidebar.multiselect('Pick data types',data_types)

deaths_df = get_historic_deaths(country,days)
cases_df = get_historic_cases(country,days)
recoveries_df = get_historic_recoveries(country,days)
historic_df = pd.concat([deaths_df,cases_df,recoveries_df ],axis=1).astype(int)




daily_cases_df = get_daily_cases(country,days)
daily_deaths_df = get_daily_deaths(country,days)
daily_recoveries_df = get_daily_recoveries(country,days)
daily_df = pd.concat([daily_deaths_df ,daily_cases_df,daily_recoveries_df ],axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)


country_code = {'Sri Lanka': 'lk', 'United States': 'us','China': 'cn', 'India': 'in', 'Russia': 'ru', 'United Kingdom': 'gb', 'Australia': 'au', 'Spain': 'es', 'France': 'fr'}

st.markdown("<h1 style='text-align: center; color: cyan;'>Covid-19 Data Visualization Dashboard</h1>", unsafe_allow_html=True)


st.metric(label="Country", value=country)
st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

col1,col2,col3 = st.columns(3)
col1.metric("Cases",yesterday_cases)
col2.metric("Deaths",yesterday_deaths)
col3.metric("Recovered", yesterday_recoveries)

st.area_chart(daily_df[data_type])


st.video('https://youtu.be/yHX60DyyuQ0')

video_contents = '''https://youtu.be/yHX60DyyuQ0''' 

st.download_button('Download Covid Dashboard Video', str(video_contents))