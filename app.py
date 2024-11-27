"""
A lightweight app to display an element which gives you basic stock information
"""
import streamlit as st
from stock import widget

st.title("Demo")

platinum_client_codes = {
    "AGL": "AGL.AX",
    "BHP Group": "BHP.AX",
    "Fortescue Future Industries": "FMG.AX",
    "Origin Energy": "ORG.AX",
    "Rio Tinto Group": "RIO.AX",
}

option = st.selectbox("Clients", options=platinum_client_codes.keys())

if option:
    st.plotly_chart(widget(platinum_client_codes[option], height=300))
