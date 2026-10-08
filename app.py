import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SlitherPop",
    page_icon="🐍"
)

st.markdown("""
<h1 style="text-align:center;">SlitherPop</h1>
<p style="text-align:center;">by Masfa</p>
""", unsafe_allow_html=True)

components.html("""
<h2 style="text-align:center;">🐍 Game coming soon...</h2>
""", height=300)
