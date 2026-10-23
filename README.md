
# 🔐 SR PassSentinel

### Password Risk Analyzer | SR CyberLabs

SR PassSentinel is an educational cybersecurity project built with Python and Streamlit to help users understand password strength, generate secure passwords, and check known password breach exposure.

## ✨ Features

- 🛡️ **Password Strength Checker** — Analyzes password strength and provides improvement suggestions.
- 🔑 **Password Generator** — Generates random passwords with configurable lengths.
- 🔎 **Breach Awareness** — Checks whether a password appears in a known breach dataset using a partial SHA-1 hash-prefix lookup.
- 🎨 **Cybersecurity Dashboard** — Black background with neon-inspired styling.
- 🔒 **Privacy Awareness** — Passwords are not intentionally stored in a database by the application.

## 🧰 Tech Stack

- Python
- Streamlit
- SHA-1 hash-prefix lookup
- Custom CSS

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ranjannsudhanshu/SR-PassSentinel.git
   ```

2. Open the project folder:

   ```bash
   cd SR-PassSentinel
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it on Windows:

   ```bash
   .venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

## ⚠️ Disclaimer

This project is intended for educational purposes. Password strength estimates are heuristic and do not guarantee security. A negative breach lookup does not prove that a password has never been exposed. The optional breach check contacts an external service and sends a partial SHA-1 hash prefix.

## 👨‍💻 Author

**Sudhanshu Ranjan**  
SR CyberLabs

Educational Cybersecurity Project.
