import streamlit as st
import pandas as pd
import altair as alt

st.title("Rising Average Temperatures in New York")

#Values from NYC Open Data
years = [2020, 2030, 2040, 2050]
temps = [55.2, 59.1, 64.1, 70.1]

#Create DataFrame
data = pd.DataFrame({
    "Year": years,
    "Avg Temp (°F)": temps
}).sort_values("Year")


#Line chart using Altair
line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='Year:O',
    y='Avg Temp (°F):Q',
    tooltip=['Year', 'Avg Temp (°F)']
).properties(
    width=700,
    height=400,
    title="Average Temperature Over Time in NYC"
)

st.altair_chart(line_chart, use_container_width=True)
