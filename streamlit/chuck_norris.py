import streamlit as st
import requests

st.set_page_config(page_title="Chuck Norris Facts", layout="wide")

st.title("Chuck Norris -vitsit")

st.write("Hae satunnainen Chuck Norris -vitsi [Chuck Norris API](https://api.chucknorris.io/)")


# Näytetään vitsi jokaisella napin painalluksella
if st.button("Hae uusi vitsi"):
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response.status_code == 200:
            joke = response.json().get("value", "Ei vitsiä saatavilla.")
            st.success(joke)
        else:
            st.error("Virhe API-kutsussa.")
    except Exception as e:
        st.error(f"Tapahtui virhe: {e}")