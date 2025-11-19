"""
Generated Code Metadata:
========================
Original URL: https://best-crypto-wallet.yivesites.com
Prompt: "Create a promotional message in Indonesian for Apelbet's bonus event offering up to 50% discount, highlighting the benefits of registering on the site."
Generated: DETERMINISTIC_d7310cd336ce55ba
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_message.py

def generate_promotional_message(language: str) -> str:
    """
    Generates a promotional message in the specified language.

    Args:
    language (str): The language of the promotional message.

    Returns:
    str: The promotional message.

    Raises:
    ValueError: If the language is not supported.
    """

    # Define the promotional messages in different languages
    promotional_messages = {
        "indonesia": """
        Selamat Datang di Apelbet!

        Kami senang mengumumkan event bonus spesial untuk Anda!
        Daftar sekarang dan nikmati diskon hingga 50%!

        Dengan mendaftar di situs kami, Anda akan mendapatkan:
        - Akses ke permainan yang adil dan transparan
        - Bonus dan promo menarik
        - Layanan pelanggan yang ramah dan profesional

        Jangan ragu untuk bergabung dengan kami dan rasakan keseruan bermain di Apelbet!
        Daftar sekarang dan dapatkan bonus Anda!

        Syarat dan Ketentuan berlaku.
        """,
        # Add more languages as needed
    }

    # Check if the language is supported
    if language.lower() not in promotional_messages:
        raise ValueError("Language not supported")

    return promotional_messages[language.lower()]


def main():
    try:
        language = "indonesia"
        message = generate_promotional_message(language)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
