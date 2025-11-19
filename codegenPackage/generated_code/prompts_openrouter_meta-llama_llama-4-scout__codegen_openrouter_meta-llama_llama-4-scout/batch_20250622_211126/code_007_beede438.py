"""
Generated Code Metadata:
========================
Original URL: https://mint-zielchain.vercel.app
Prompt: Write a code snippet to parse the ZIELCHAIN Terms of Use and extract relevant information about user responsibilities, prohibited acts, and liability limitations.
Generated: DETERMINISTIC_beede438b119cb8b
Batch ID: 20250622_211126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def parse_zielchain_terms_of_use(text):
    """
    Parse the ZIELCHAIN Terms of Use and extract relevant information.

    Args:
        text (str): The text of the Terms of Use.

    Returns:
        dict: A dictionary containing the extracted information.
    """

    # Initialize an empty dictionary to store the extracted information
    extracted_info = {
        "user_responsibilities": [],
        "prohibited_acts": [],
        "liability_limitations": []
    }

    # Define regular expression patterns to match relevant sections
    responsibility_pattern = re.compile(r"User Responsibilities?.*?(?=Prohibited Acts|Liability|Disclaimer)", re.DOTALL)
    prohibited_acts_pattern = re.compile(r"Prohibited Acts?.*?(?=Liability|Disclaimer)", re.DOTALL)
    liability_pattern = re.compile(r"Liability Limitations?.*?(?=Disclaimer|Conclusion)", re.DOTALL)

    # Extract user responsibilities
    responsibility_match = responsibility_pattern.search(text)
    if responsibility_match:
        responsibilities = responsibility_match.group().splitlines()
        for responsibility in responsibilities:
            if responsibility.strip():  # Ignore empty lines
                extracted_info["user_responsibilities"].append(responsibility.strip())

    # Extract prohibited acts
    prohibited_acts_match = prohibited_acts_pattern.search(text)
    if prohibited_acts_match:
        acts = prohibited_acts_match.group().splitlines()
        for act in acts:
            if act.strip():  # Ignore empty lines
                extracted_info["prohibited_acts"].append(act.strip())

    # Extract liability limitations
    liability_match = liability_pattern.search(text)
    if liability_match:
        limitations = liability_match.group().splitlines()
        for limitation in limitations:
            if limitation.strip():  # Ignore empty lines
                extracted_info["liability_limitations"].append(limitation.strip())

    return extracted_info


def main():
    try:
        # Example usage
        terms_of_use_text = """
        # Sample Terms of Use text for demonstration purposes

        User Responsibilities
        --------------------

        * You are responsible for maintaining the confidentiality of your account.
        * You must provide accurate and complete information.

        Prohibited Acts
        ----------------

        * You are not allowed to use the service for illegal activities.
        * You must not interfere with the service's operation.

        Liability Limitations
        ---------------------

        * In no event shall ZIELCHAIN be liable for any indirect damages.
        * ZIELCHAIN's liability is limited to the amount you paid for the service.
        """

        extracted_info = parse_zielchain_terms_of_use(terms_of_use_text)

        print("Extracted Information:")
        print("------------------------")
        print("User Responsibilities:")
        for responsibility in extracted_info["user_responsibilities"]:
            print(f"* {responsibility}")
        print("\nProhibited Acts:")
        for act in extracted_info["prohibited_acts"]:
            print(f"* {act}")
        print("\nLiability Limitations:")
        for limitation in extracted_info["liability_limitations"]:
            print(f"* {limitation}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
