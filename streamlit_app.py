import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PBC Future School", layout="wide")

# Mở file HTML và hiển thị
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1200, scrolling=True)