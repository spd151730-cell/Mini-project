from __future__ import annotations

import streamlit as st

from ui_theme import apply_theme, ensure_session_defaults, render_page_header, render_section_heading

apply_theme()
ensure_session_defaults()

render_page_header("Style Me For Every Version Of Me", "Switch between different identities and moods.")

identities = [
    ("College Me", "Casual", "Comfortable", "Sneakers", "👩"),
    ("Office Me", "Professional", "Minimal", "Formal", "💼"),
    ("Party Me", "Trendy", "Stylish", "Accessorized", "✨"),
    ("Traditional Me", "Elegant", "Ethnic", "Traditional", "🌸"),
]

for name, style, vibe, detail, emoji in identities:
    with st.container(border=True):
        st.markdown(
            f"""
            <div class='identity-visual'>{emoji}</div>
            <div style='font-size:1.2rem; font-weight:800; color:#1d1528;'>{name}</div>
            <div class='chip-row' style='margin-top:0.6rem;'>
                <span class='chip'>{style}</span>
                <span class='chip'>{vibe}</span>
                <span class='chip'>{detail}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Select", key=f"select_{name}"):
            st.session_state.style = style
            st.switch_page("pages/04_AI_Outfit_Recommendations.py")

st.info("This page is a front-end identity switcher for future style-profile variants.")
