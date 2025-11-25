import streamlit as st
import mysql.connector
import pandas as pd

from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# 16 minuutin välein autorefresh
count = st_autorefresh(interval=900_000, limit=None, key="datarefresh")


st.set_page_config(page_title="Säädata", layout="wide")

st.title("Säädata Raahe (OpenWeatherMap)")

st.write(f"Sivu päivittyi viimeksi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

try:
    # MySQL-yhteys
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="kissaperkele",
        database="weather_db"
    )

    query = "SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50;"
    df = pd.read_sql(query, conn)

    st.subheader("Viimeisimmät säähavainnot")
    st.dataframe(df, use_container_width=True)

    st.write(f"Rivejä yhteensä: {len(df)}")

except Exception as e:
    st.error(f"Virhe tietokantayhteydessä: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
