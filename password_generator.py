
import secrets
import string


def generate_password(length=20):
    length = max(12, min(int(length), 64))

    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+"
    ]

    password = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)

    password.extend(
        secrets.choice(alphabet)
        for _ in range(length - len(password))
    )

    secrets.SystemRandom().shuffle(password)
    return "".join(password)
