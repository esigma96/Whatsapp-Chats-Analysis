import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt

st.write('Hello world!')

f = open('whatsapp-chat.txt', mode='r',encoding="utf8")
data = f.read() 
f.close()
#create two columns for charts

##Parsing whataspp messages to dataframe

whatsapp_regex = r"(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}) - ([^:]*): (.*?)(?=\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - [^:]*|\Z)"

matches = re.findall(whatsapp_regex, data, re.MULTILINE | re.DOTALL)
df = pd.DataFrame(matches, columns=["date", "time", "name", "message"])
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_timedelta(df['time']+':00')
df['datetime']= df["date"] + df['time']

# Select DataFrame Rows Between Two Dates
start_date = '2022-07-01'
end_date = '2023-08-14'

# Select DataFrame rows between two dates
mask = (df['date'] > start_date) & (df['date'] <= end_date)
df = df.loc[mask]

import streamlit as st
# create two columns for charts
fig_col1 = st.columns(2)
with fig_col1:
  st.markdown("### First Chart")
  #EDA for general understanding of the distribution of the dataset.
  df_most_busy_day = df[['day_of_week', 'month_of_date']].groupby('day_of_week').count()
  df_most_busy_day = df_most_busy_day.sort_values(by = 'month_of_date', ascending = False)
  df_most_busy_day['day_of_week'] = df_most_busy_day.index
  #df.rename(columns = {'' : ''}, inplace = True)
  sns.set(rc={'figure.figsize':(10,6.27)})
  ax =sns.barplot(x = 'day_of_week', y = 'month_of_date' ,data = df_most_busy_day, estimator = sum, palette=("crest"))
  ax.set_title('Most Busy Day', size = 20)
  ax.set(ylabel='No. of Messages')
st.write(ax)
