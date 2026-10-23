
import streamlit as st

from password_checker import check_password
from password_generator import generate_password
from breach_checker import check_known_breach


st.set_page_config(
    page_title="SR PassSentinel — Password Risk Analyzer",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 PassGuard")
st.caption("Password Strength & Breach Awareness Tool")

st.info(
    "Privacy first: Passwords are not saved to a database or file. "
    "The optional breach check uses a partial hash-prefix lookup."
)

strength_tab, generator_tab, breach_tab = st.tabs([
    "🛡️ Strength Checker",
    "🔑 Password Generator",
    "🔎 Breach Awareness"
])

with strength_tab:
    st.subheader("Analyze Password Strength")

    password = st.text_input(
        "Enter a password",
        type="password",
        key="strength_password",
        help="The password is analyzed locally by this application."
    )

    if st.button("Analyze Strength", key="analyze_btn"):
        if not password:
            st.warning("Please enter a password.")
        else:
            result = check_password(password)

            st.metric("Estimated Strength", result["strength"])
            st.progress(result["score"] / 6)

            st.write("Recommendations:")
            for item in result["feedback"]:
                st.write(f"• {item}")

            st.caption(
                "This is a basic heuristic check, not a guarantee "
                "of password security."
            )

with generator_tab:
    st.subheader("Generate a Strong Password")

    length = st.slider(
        "Password length",
        min_value=12,
        max_value=64,
        value=20
    )

    if st.button("Generate Password"):
        st.session_state["generated_password"] = (
            generate_password(length)
        )

    generated = st.session_state.get("generated_password", "")

    if generated:
        st.code(generated, language=None)
        st.caption(
            "Copy it to a password manager. This app does not save "
            "generated passwords to a database."
        )

with breach_tab:
    st.subheader("Check Known Breach Exposure")

    st.warning(
        "An online service is contacted for this check. "
        "Only a 5-character SHA-1 hash prefix is sent, not the "
        "full password. Do not use this tool with a password "
        "if you are uncomfortable performing an online check."
    )

    breach_password = st.text_input(
        "Password to check",
        type="password",
        key="breach_password"
    )

    if st.button("Check Breach Awareness"):
        if not breach_password:
            st.warning("Please enter a password.")
        else:
            with st.spinner("Checking known breach data..."):
                result = check_known_breach(breach_password)

            if not result["success"]:
                st.error(result["message"])
            elif result["found"]:
                st.error(
                    f"⚠️ Match found. Occurrence count: "
                    f"{result['count']:,}"
                )
                st.write(
                    "Do not use this password. Change it anywhere "
                    "you may have reused it."
                )
            else:
                st.success(
                    "No match found in the checked breach dataset."
                )
                st.write(
                    "This does not guarantee that the password "
                    "has never been exposed."
                )

st.divider()
st.caption("PassGuard | Educational Cybersecurity Project")

st.markdown(
    """
    <div style="text-align: center; margin-top: 10px;">
        <span style="color: #00D9FF; font-weight: bold;">
            Made with
        </span>
        <span style="color: #FF3030; font-weight: bold;">
            ❤️
        </span>
        <span style="color: #00D9FF; font-weight: bold;">
            by SR CyberLabs
        </span>
    </div>
    """,
    unsafe_allow_html=True
)