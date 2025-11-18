import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="MySQL Data Viewer", layout="wide")

st.title("MySQL: Opiskelijat-taulu")

try:
    # MySQL-yhteys
    conn = mysql.connector.connect(
        host="localhost",        # muuta tarvittaessa esim. 86.50.23.56
        user="exampleuser",
        password="kissaperkele",
        database="exampledb"
    )

    query = "SELECT * FROM opiskelijat;"
    df = pd.read_sql(query, conn)

    st.subheader("Opiskelijat")
    st.dataframe(df, use_container_width=True)

    st.write(f"Rivejä yhteensä: {len(df)}")

except Exception as e:
    st.error(f"Virhe tietokantayhteydessä: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
