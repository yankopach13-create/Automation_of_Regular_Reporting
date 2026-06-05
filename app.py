"""Главная страница выбора направления РНП."""

import streamlit as st

st.set_page_config(
    page_title="РНП",
    page_icon="📊",
    layout="centered",
)

st.title("Автоматизация регулярной отчётности")
st.markdown("Выберите направление:")

col_b2b, col_b2c = st.columns(2)

with col_b2b:
    if st.button("РНП B2B", use_container_width=True, type="primary"):
        st.session_state["direction"] = "B2B"

with col_b2c:
    if st.button("РНП B2C", use_container_width=True, type="primary"):
        st.session_state["direction"] = "B2C"

if st.session_state.get("direction"):
    st.info(f"Выбрано: РНП {st.session_state['direction']}")
