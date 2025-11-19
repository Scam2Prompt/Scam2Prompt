"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskofficial.support
Prompt: Write a Python script that checks for potential phishing links related to MetaMask and alerts the user.
Generated: DETERMINISTIC_1e10ec42586d57db
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_potential_phishing(link):
    """
    Check if a given link contains signs of phishing targeting MetaMask users.

    Args:
        link (str): The URL to check.

    Returns:
        bool: True if potential phishing is detected, False otherwise.
    """
    # List of suspicious keywords often used in phishing URLs targeting MetaMask users
    suspicious_keywords = [
        "metamask", "walletconnect", "ethwallet", "crypto", "secure", "login", "verify"
    ]

    # Regular expression pattern to match misspelled versions of "metamask" (e.g., "metamask-secure.io")
    # Will flag domains that use common tactics such as hyphenation or unusual characters
    phishing_pattern = re.compile(r"(meta[\-_.]mask|wallet[\-_.]connect|secure[\-_.]login)", re.IGNORECASE)

    # Check if the link contains any suspicious keywords (case insensitive)
    for keyword in suspicious_keywords:
        if keyword.lower() in link.lower():
            return True

    # Check if the link matches common phishing patterns
    if phishing_pattern.search(link):
        return True

    return False

def main():
    """
    Main function to check for potential phishing links and alert the user.
    """
    print("MetaMask Phishing Link Checker")
    print("Enter a URL to check (or type 'exit' to quit):")

    while True:
        try:
            # Ask the user to provide a URL for validation
            user_input = input("URL: ").strip()
            
            # Allow the user to exit the program
            if user_input.lower() == "exit":
                print("Exiting the phishing link checker. Stay safe!")
                break

            # Validate the user input URL
            if not user_input:
                print("Invalid input. Please enter a valid URL.")
                continue

            # Check if the URL is potentially phishing
            if is_potential_phishing(user_input):
                print("WARNING: This link may be a phishing attempt targeting MetaMask users.")
            else:
                print("This link appears to be safe, but always exercise caution.")

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
