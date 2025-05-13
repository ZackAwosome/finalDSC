import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("NYC Flood Risk Zones & Simulated Population Density")

st.markdown("""
This is a simulated map highlighting **New York City areas at risk of flooding**.
""")

#Fixed flood zone coordinates and densities
flood_zones = {
    "Lower Manhattan": {"coords": [40.7033, -74.0170], "density": 28000},
    "Brooklyn Waterfront": {"coords": [40.7003, -73.9896], "density": 15000},
    "Rockaway Peninsula": {"coords": [40.5780, -73.8371], "density": 6000},
    "Staten Island Shore": {"coords": [40.5430, -74.1502], "density": 3000}
}

#Create base map
m = folium.Map(location=[40.7128, -74.0060], zoom_start=11, tiles="CartoDB positron")

#Add flood zones
for name, data in flood_zones.items():
    coords = data["coords"]
    density = data["density"]
    popup_text = f"<b>{name}</b><br>Estimated Pop. Density: {density} / km²"
    color = "darkred" if density > 15000 else "orange"

    folium.CircleMarker(
        location=coords,
        radius=15,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup_text, max_width=250)
    ).add_to(m)

#Display the map
st_data = st_folium(m, width=900)
