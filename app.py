"""Главная страница выбора направления РНП."""

import streamlit as st

st.set_page_config(
    page_title="РНП",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 720px;
            padding-top: 3rem;
        }

        h1 {
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.25rem !important;
        }

        .subtitle {
            color: #C9CDD3;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        .info-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            min-height: 52px;
            color: #9CA3AF;
            font-size: 1.1rem;
        }

        div[data-testid="column"]:has(.info-icon) {
            display: flex;
            align-items: center;
        }

        .stButton > button {
            width: 100%;
            min-height: 52px;
            background-color: #1A1D24 !important;
            color: #FAFAFA !important;
            border: 1px solid #3A3F4B !important;
            border-radius: 8px !important;
            font-size: 1rem !important;
            font-weight: 500 !important;
            transition: border-color 0.2s ease, background-color 0.2s ease;
        }

        .stButton > button:hover {
            background-color: #232733 !important;
            border-color: #5B6270 !important;
            color: #FFFFFF !important;
        }

        .stButton > button:focus:not(:active) {
            border-color: #6C63FF !important;
            color: #FFFFFF !important;
        }

        #MainMenu, footer, header {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# 📊 Автоматизация регулярной отчётности")
st.markdown(
    '<p class="subtitle">Выберите направление отчётности:</p>',
    unsafe_allow_html=True,
)
st.divider()

buttons = [
    ("РНП B2B", "B2B"),
    ("РНП B2C", "B2C"),
]

for label, direction in buttons:
    icon_col, button_col = st.columns([0.06, 0.94])
    with icon_col:
        st.markdown('<div class="info-icon">ⓘ</div>', unsafe_allow_html=True)
    with button_col:
        if st.button(label, key=direction, use_container_width=True):
            st.session_state["direction"] = direction

if st.session_state.get("direction"):
    st.success(f"Выбрано: РНП {st.session_state['direction']}")
