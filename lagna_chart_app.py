import streamlit as st
from datetime import datetime
from astral.sun import sun
from astral import LocationInfo

st.title("🌞 Lagna Time Insight (Simplified)")

city = st.text_input("City (Example: Delhi, Mumbai, Pune)")
region = st.text_input("Region (Example: India)")
timezone = st.text_input("Timezone (Example: Asia/Kolkata)", value="Asia/Kolkata")
date = st.date_input("Date of Birth")
time = st.time_input("Time of Birth")

if st.button("Show Sun Position Details"):
    try:
        location = LocationInfo(city, region, timezone)
        dt = datetime.combine(date, time)

        s = sun(location.observer, date=date)

        st.write(f"🌄 **Sunrise:** {s['sunrise'].time()}")
        st.write(f"🌇 **Sunset:** {s['sunset'].time()}")
        st.write(f"🌞 **Solar Noon (Lagna midpoint):** {s['noon'].time()}")

        if time < s['sunrise'].time():
            st.success("The sun was below the horizon — possibly before sunrise.")
        elif time > s['sunset'].time():
            st.success("The sun was setting or had set — possibly evening Lagna.")
        else:
            st.success("Sun was above horizon — active daytime, strong visible Lagna.")
    except Exception as e:
        st.error(f"Could not calculate: {str(e)}")
