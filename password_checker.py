
import re
import math

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "admin123", "letmein",
    "welcome", "iloveyou", "abc123"
}


def check_password(password):
    if not password:
        return {
            "score": 0,
            "strength": "Not checked",
            "feedback": ["Enter a password to analyze."]
        }

    feedback = []
    score = 0

    length = len(password)

    if length >= 16:
        score += 2
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters; 16 or more is preferable.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Consider including lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Consider including uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Consider including numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Consider including symbols.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password. Replace it.")

    if len(set(password)) <= 2 and length >= 8:
        score = min(score, 1)
        feedback.append("Too few different characters are used.")

    if re.search(r"(.)\1{3,}", password):
        score = max(0, score - 1)
        feedback.append("Avoid long runs of repeated characters.")

    if re.search(
        r"1234|2345|3456|4567|5678|6789|abcd|qwerty",
        password.lower()
    ):
        score = max(0, score - 1)
        feedback.append("Avoid predictable sequences.")

    score = max(0, min(score, 6))

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Stronger"

    if not feedback:
        feedback.append(
            "No basic issues detected. This is not a guarantee "
            "that the password is secure."
        )

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }
