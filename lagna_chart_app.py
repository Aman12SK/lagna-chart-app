import streamlit as st
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

st.title("🪐 Lagna Chart Generator")

name = st.text_input("Your Name")
date = st.date_input("Date of Birth")
time = st.time_input("Time of Birth")
place = st.text_input("Place of Birth (optional - enter lat/long below)")
latitude = st.number_input("Latitude", value=28.6139)
longitude = st.number_input("Longitude", value=77.2090)

if st.button("Generate Lagna Chart"):
    dt = Datetime(str(date), str(time), '+05:30')  # assuming IST
    pos = GeoPos(latitude, longitude)
    chart = Chart(dt, pos)

    st.subheader("🔮 Planetary Positions:")
    for obj in [const.SUN, const.MOON, const.MERCURY, const.VENUS, const.MARS,
                const.JUPITER, const.SATURN, const.RAHU, const.KETU, const.ASC]:
        body = chart.get(obj)
        st.write(f"{obj}: {body.sign} {body.lon}°")

    asc = chart.get(const.ASC)
    st.success(f"🌟 Your Ascendant (Lagna) is: {asc.sign}")
