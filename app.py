"""Главная страница выбора направления РНП."""

import streamlit as st

st.set_page_config(
    page_title="Автоматизация регулярной отчётности",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 860px;
            padding-top: 3rem;
        }

        h1 {
            font-size: clamp(1.35rem, 2.8vw, 2rem) !important;
            font-weight: 700 !important;
            margin-bottom: 0.25rem !important;
            text-align: center !important;
            white-space: nowrap !important;
        }

        hr {
            margin-top: 0.5rem !important;
            margin-bottom: 0.75rem !important;
        }

        .help-icon {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            min-height: 34px;
            cursor: help;
        }

        .help-icon .help-circle {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            border: 1px solid #5B6270;
            border-radius: 50%;
            color: #9CA3AF;
            font-size: 0.75rem;
            font-weight: 600;
            line-height: 1;
            background-color: #1A1D24;
        }

        .help-icon .tooltip-text {
            visibility: hidden;
            opacity: 0;
            position: absolute;
            right: calc(100% + 12px);
            top: 50%;
            transform: translateY(-50%);
            background-color: #262730;
            color: #FAFAFA;
            border: 1px solid #3A3F4B;
            border-radius: 8px;
            padding: 12px 16px;
            width: max-content;
            max-width: 340px;
            z-index: 1000;
            font-size: 0.9rem;
            font-weight: 400;
            line-height: 1.5;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
            transition: opacity 0.2s ease, visibility 0.2s ease;
            text-align: left;
            pointer-events: none;
        }

        .help-icon .tooltip-text ul {
            margin: 0;
            padding-left: 1.2rem;
        }

        .help-icon .tooltip-text li {
            margin-bottom: 0.25rem;
        }

        .help-icon .tooltip-text li:last-child {
            margin-bottom: 0;
        }

        .help-icon:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }

        div[data-testid="column"]:has(.help-icon) {
            display: flex;
            align-items: center;
        }

        .stButton > button,
        .stButton > button p,
        .stButton > button div {
            font-size: 0.9rem !important;
            font-weight: 400 !important;
        }

        .stButton > button {
            width: 100%;
            min-height: 34px;
            padding: 4px 20px !important;
            background-color: #1A1D24 !important;
            color: #FAFAFA !important;
            border: 1px solid #3A3F4B !important;
            border-radius: 6px !important;
            transition: border-color 0.2s ease, background-color 0.2s ease;
        }

        .stButton > button:hover {
            background-color: #232733 !important;
            border-color: #5B6270 !important;
            color: #FFFFFF !important;
        }

        .stButton > button:hover p,
        .stButton > button:hover div {
            color: #FFFFFF !important;
        }

        .stButton > button:focus:not(:active) {
            border-color: #6C63FF !important;
            color: #FFFFFF !important;
        }

        .stButton > button:focus:not(:active) p,
        .stButton > button:focus:not(:active) div {
            color: #FFFFFF !important;
        }

        #MainMenu, footer, header {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# 📋 Автоматизация регулярной отчётности")
st.divider()

tooltips = {
    "B2B": [
        "РНП Спец. розницы и Традиции;",
        "Общий РНП Блоки спец розницы и Традиции;",
        "Информация для ИИ отчёта",
        "Динамика продаж железа",
    ],
    "B2C": [
        "РНП Розницы;",
        "Общий РНП блок розницы;",
        "Информация для ИИ отчёта",
    ],
}

buttons = [
    ("РНП B2B", "B2B"),
    ("РНП B2C", "B2C"),
    ("SYNC", "SYNC"),
]


def render_help_icon(items: list[str]) -> str:
    """Формирует HTML иконки с подсказкой при наведении."""
    list_items = "".join(f"<li>{item}</li>" for item in items)
    return (
        '<div class="help-icon">'
        '<span class="help-circle">?</span>'
        f'<span class="tooltip-text"><ul>{list_items}</ul></span>'
        "</div>"
    )


for label, direction in buttons:
    icon_col, button_col = st.columns([0.06, 0.94])
    with icon_col:
        if direction in tooltips:
            st.markdown(render_help_icon(tooltips[direction]), unsafe_allow_html=True)
    with button_col:
        st.button(label, key=direction, use_container_width=True)
