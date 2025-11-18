import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Plot some data")

    # Lataa CSV-tiedosto
    df = pd.read_csv("Electric_prices.csv")

    # Luo scatter plot
    fig = px.scatter(df, x="Date", y="Price", title="Electric Prices Over Time")

    # Näytä kaavio Streamlitissä
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()