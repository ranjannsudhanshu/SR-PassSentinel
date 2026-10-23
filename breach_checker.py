
import hashlib
import requests


def check_known_breach(password):
    if not password:
        return {
            "success": False,
            "message": "Enter a password first."
        }

    # SHA-1 is used here only for the HIBP range protocol,
    # not for storing or protecting passwords.
    sha1_hash = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(
            url,
            headers={"Add-Padding": "true"},
            timeout=10
        )
        response.raise_for_status()

        for line in response.text.splitlines():
            parts = line.split(":")
            if len(parts) != 2:
                continue

            if parts[0].strip().upper() == suffix:
                return {
                    "success": True,
                    "found": True,
                    "count": int(parts[1]),
                    "message": "This password appears in known breach data."
                }

        return {
            "success": True,
            "found": False,
            "count": 0,
            "message": "No match found in this breach dataset."
        }

    except (requests.RequestException, ValueError):
        return {
            "success": False,
            "message": (
                "Breach check unavailable. Check your internet "
                "connection and try again."
            )
        }
