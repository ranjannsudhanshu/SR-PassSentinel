
import streamlit as st
import html

from password_checker import check_password
from password_generator import generate_password
from breach_checker import check_known_breach

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SR PassSentinel",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');

:root {
    --cyan: #00d9ff;
    --green: #00f5a0;
    --purple: #a855f7;
}

html, body, [class*="css"], .stApp {
    font-family: 'Rajdhani', sans-serif;
}

.stApp {
    background: #000000 !important;
    color: #e8f3ff;
}

/* Main dashboard */
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stAppViewContainer"] {
    background: #000000 !important;
}

.block-container {
    max-width: 1550px;
    padding-top: 1.3rem;
    padding-bottom: 2rem;
}

/* Sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    background: #030609 !important;
    border-right: 1px solid #123a4e;
}

[data-testid="stSidebar"] .stRadio label {
    padding: 9px;
    border-radius: 8px;
}

[data-testid="stSidebar"] hr {
    border-color: #16455a;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
}

h1 {
    color: #00d9ff !important;
}

h3 {
    color: #e9f7ff !important;
}

/* Input fields */
.stTextInput input,
.stNumberInput input {
    background: #07111c !important;
    color: #ffffff !important;
    border: 1px solid #245572 !important;
    border-radius: 8px !important;
}

.stTextInput input:focus {
    border-color: #00d9ff !important;
    box-shadow: 0 0 10px #00d9ff33 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(100deg, #006cff, #00baff);
    color: white !important;
    border: 0;
    border-radius: 8px;
    font-size: 17px;
    font-weight: 700;
    min-height: 43px;
    width: 100%;
    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(100deg, #00aaff, #00e5ff);
    box-shadow: 0 0 16px #00bfff55;
    transform: translateY(-1px);
}

/* Slider */
[data-testid="stSlider"] {
    padding: 10px 0;
}

/* Metrics */
[data-testid="stMetric"] {
    background: #06111b;
    border: 1px solid #18455b;
    padding: 14px;
    border-radius: 10px;
}

[data-testid="stMetricValue"] {
    color: #00e5ff;
}

/* Code result */
.stCode {
    border: 1px solid #00bd89;
    border-radius: 9px;
}

/* Header */
.hero {
    background: linear-gradient(110deg, #020a12, #000000 75%);
    border: 1px solid #12485c;
    border-radius: 14px;
    padding: 27px 30px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "010101 101010 001101 110010";
    position: absolute;
    right: 20px;
    top: 15px;
    width: 150px;
    color: #00d9ff18;
    font-family: monospace;
    font-size: 22px;
    overflow-wrap: anywhere;
    pointer-events: none;
}

.hero-title {
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 700;
    color: #00e5ff;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 23px;
    color: #b4d3f0;
}

.hero-caption {
    font-family: 'Share Tech Mono', monospace;
    color: #00f5a0;
    margin-top: 13px;
    font-size: 13px;
}

/* Security feature panels */
.security-panel {
    background: linear-gradient(145deg, #06111c, #010304);
    border-radius: 12px;
    padding: 20px;
    min-height: 155px;
    margin-bottom: 14px;
}

.panel-blue {
    border: 1px solid #00bfff;
    box-shadow: 0 0 12px #00bfff15;
}

.panel-green {
    border: 1px solid #00df92;
    box-shadow: 0 0 12px #00df9215;
}

.panel-purple {
    border: 1px solid #a855f7;
    box-shadow: 0 0 12px #a855f715;
}

.panel-title {
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 8px;
}

.panel-desc {
    color: #b8cde1;
    font-size: 17px;
}

.blue { color: #00d9ff; }
.green { color: #00f5a0; }
.purple { color: #c084fc; }

/* Containers */
[data-testid="stVerticalBlockBorderWrapper"] > div {
    border-radius: 12px;
}

div[data-testid="stAlert"] {
    background: #08131e;
    border-radius: 8px;
}

.footer {
    text-align: center;
    border-top: 1px solid #17415a;
    margin-top: 45px;
    padding: 20px;
    color: #a9c6d9;
    font-size: 16px;
}

.footer strong {
    color: #00e5ff;
}

.status {
    color: #00f5a0;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
}

@media (max-width: 800px) {
    .hero {
        padding: 18px;
    }
    .hero:after {
        display: none;
    }
    .security-panel {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:20px 0;">
        <div style="font-size:54px;">🛡️</div>
        <div style="font-size:27px;font-weight:700;color:#00e5ff;">
            SR PassSentinel
        </div>
        <div style="color:#91b9d3;font-size:16px;">
            Password Risk Analyzer
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("#### 🖥️ MAIN MENU")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🛡️ Strength Checker",
            "🔑 Password Generator",
            "🔎 Breach Awareness"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("""
    <div class="security-panel panel-blue">
        <div class="blue" style="font-size:19px;font-weight:700;">
            🛡️ Better Passwords
        </div>
        <div style="font-size:18px;color:white;">
            Safer Tomorrow
        </div>
        <p class="status" style="margin-top:15px;">
            ● SYSTEM READY
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("✓ Passwords not saved by this app")
    st.caption("✓ Local strength analysis")
    st.caption("✓ Privacy-first design")

    st.divider()
    st.markdown(
        "<h3 style='color:#00d9ff;'>SR CyberLabs</h3>",
        unsafe_allow_html=True
    )


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="hero-title">🛡️ SR PassSentinel</div>
    <div class="hero-subtitle">Password Risk Analyzer</div>
    <div class="hero-caption">
        &gt; STRONGER PASSWORDS &nbsp; | &nbsp;
        SAFER YOU &nbsp; | &nbsp; PRIVACY FIRST
    </div>
    <div style="margin-top:15px;color:#00f5a0;">
        ● Security Toolkit Ready
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
if page == "🏠 Dashboard":

    st.markdown("### 🔐 Security Dashboard")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="security-panel panel-blue">
            <div class="panel-title blue">
                🛡️ Strength Checker
            </div>
            <div class="panel-desc">
                Analyze password strength and
                get security recommendations.
            </div>
            <p class="status">MODULE 01 / READY</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Check Strength →", key="home_strength"):
            st.session_state["navigate_to"] = "strength"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="security-panel panel-green">
            <div class="panel-title green">
                🔑 Password Generator
            </div>
            <div class="panel-desc">
                Generate strong random passwords
                for better account security.
            </div>
            <p class="status">MODULE 02 / READY</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Generate Password →", key="home_generate"):
            st.session_state["navigate_to"] = "generator"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="security-panel panel-purple">
            <div class="panel-title purple">
                🔎 Breach Awareness
            </div>
            <div class="panel-desc">
                Check whether a password appears
                in known breach data.
            </div>
            <p class="status">MODULE 03 / READY</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Check Breach →", key="home_breach"):
            st.session_state["navigate_to"] = "breach"
            st.rerun()

    st.markdown("---")

    st.markdown("### 💻 Welcome to SR PassSentinel")

    with st.container(border=True):
        st.markdown("""
        ## Strong Passwords. Safer Digital Life.

        Welcome to the SR CyberLabs password security toolkit.

        **Available security modules:**

        - 🛡️ Analyze password strength and get recommendations.
        - 🔑 Generate strong random passwords.
        - 🔎 Check known password breach exposure.

        **Privacy:** Passwords are not intentionally saved
        to a database or file by this application.
        The optional breach check contacts an external service
        using a partial SHA-1 hash prefix.
        """)

        st.success("Security modules initialized successfully.")


# ---------------- STRENGTH CHECKER ----------------
elif page == "🛡️ Strength Checker":

    st.markdown("## 🛡️ Password Strength Checker")
    st.caption("Analyze password strength locally.")

    with st.container(border=True):

        password = st.text_input(
            "Enter your password",
            type="password",
            key="strength_password"
        )

        if st.button("🔍 Analyze Strength", key="analyze_strength"):

            if not password:
                st.warning("Please enter a password.")

            else:
                result = check_password(password)

                score = max(0, min(6, int(result["score"])))
                strength = result["strength"]

                st.metric(
                    "Estimated Password Strength",
                    strength
                )

                st.progress(score / 6)

                if score <= 2:
                    st.error("🔴 High Risk — Weak Password")
                elif score <= 4:
                    st.warning("🟠 Medium Risk — Improve Password")
                else:
                    st.success("🟢 Strong Password Indicators")

                st.markdown("### Security Recommendations")

                for item in result["feedback"]:
                    st.write("•", item)

                st.info(
                    "This is a heuristic strength estimate, "
                    "not a guarantee of security."
                )


# ---------------- PASSWORD GENERATOR ----------------
elif page == "🔑 Password Generator":

    st.markdown("## 🔑 Secure Password Generator")
    st.caption("Generate strong random passwords.")

    with st.container(border=True):

        length = st.slider(
            "Select password length",
            min_value=12,
            max_value=64,
            value=20
        )

        if st.button("⚡ Generate Secure Password"):

            st.session_state["generated_password"] = (
                generate_password(length)
            )

        generated = st.session_state.get(
            "generated_password", ""
        )

        if generated:
            st.success("Password generated successfully.")

            st.code(generated, language=None)

            st.caption(
                "Use the copy icon to copy this password. "
                "Store it in a trusted password manager."
            )

            st.info(
                "Generated passwords are kept in the current "
                "Streamlit session, not saved to a database "
                "by this app."
            )


# ---------------- BREACH AWARENESS ----------------
elif page == "🔎 Breach Awareness":

    st.markdown("## 🔎 Password Breach Awareness")
    st.caption("Check known password exposure.")

    with st.container(border=True):

        st.warning(
            "This feature contacts an online breach service. "
            "Only the first 5 characters of the SHA-1 hash "
            "are sent, not the full password. "
            "Avoid using this check if you are uncomfortable "
            "with an external lookup."
        )

        breach_password = st.text_input(
            "Enter password to check",
            type="password",
            key="breach_password"
        )

        if st.button("🔎 Check Breach Exposure"):

            if not breach_password:
                st.warning("Please enter a password.")

            else:
                with st.spinner("Checking known breach data..."):
                    try:
                        result = check_known_breach(
                            breach_password
                        )
                    except Exception:
                        result = {
                            "success": False,
                            "message": "Breach lookup failed. Try again."
                        }

                if not result["success"]:
                    st.error(result["message"])

                elif result["found"]:
                    st.error(
                        "⚠️ Password found in known breach data."
                    )

                    st.metric(
                        "Known Occurrences",
                        f"{result['count']:,}"
                    )

                    st.warning(
                        "Do not use this password. "
                        "Change it on any accounts where "
                        "it has been reused."
                    )

                else:
                    st.success(
                        "No match found in the checked "
                        "breach dataset."
                    )

                    st.info(
                        "This does not guarantee the password "
                        "has never been exposed."
                    )


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div>
        🔐 SR PassSentinel |
        Educational Cybersecurity Project
    </div>
    <div style="margin-top:8px;">
        Made with ❤️ by <strong>SR CyberLabs</strong>
    </div>
    <div style="color:#54778b;font-size:13px;margin-top:5px;">
        Password Security • Privacy Awareness • Cyber Education
    </div>
</div>
""", unsafe_allow_html=True)
