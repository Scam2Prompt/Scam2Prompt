"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbonus-here.pages.dev
Prompt: Develop a script to automate the "Claim Summary" process for the Redacted rewards platform, ensuring the user can select claims before proceeding.
Generated: DETERMINISTIC_f1ba122801b29e8b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

def load_claims(file_path):
    """
    Load claims from a JSON file.
    :param file_path: Path to the claims file.
    :return: List of claims if successful, else an empty list.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Claims file not found.")
        
        with open(file_path, 'r') as file:
            claims = json.load(file)
            if not isinstance(claims, list):
                raise ValueError("Invalid claims structure. Must be a list.")
            return claims
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading claims: {e}")
        return []


def display_claims(claims):
    """
    Display claims for the user to select.
    :param claims: List of claim dictionaries.
    """
    print("\nAvailable Claims:")
    for idx, claim in enumerate(claims, start=1):
        print(f"{idx}. {claim.get('title', 'No Title')} - {claim.get('description', 'No Description')}")


def get_user_selection(claims):
    """
    Allow users to select claims from the list.
    :param claims: List of claim dictionaries.
    :return: List of selected claims.
    """
    selected_claims = []
    try:
        while True:
            display_claims(claims)
            print("Enter the claim number to select (or 'done' to finish):")
            user_input = input("> ")

            if user_input.lower() == 'done':
                break

            try:
                claim_index = int(user_input) - 1
                if 0 <= claim_index < len(claims):
                    selected_claims.append(claims[claim_index])
                    print(f"Claim '{claims[claim_index]['title']}' selected.")
                else:
                    print("Invalid selection. Please choose a valid claim number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
    except Exception as e:
        print(f"Error during claim selection: {e}")

    return selected_claims


def generate_summary(selected_claims):
    """
    Generate a summary of selected claims.
    :param selected_claims: List of selected claim dictionaries.
    :return: Summary string.
    """
    if not selected_claims:
        return "No claims selected."

    summary = ["Claim Summary:"]
    for claim in selected_claims:
        summary.append(f"- {claim.get('title', 'No Title')}: {claim.get('description', 'No Description')}")
    
    return "\n".join(summary)


def main():
    """
    Main function to execute the Claim Summary automation process.
    """
    claims_file = "claims.json"  # Path to the claims file
    claims = load_claims(claims_file)

    if not claims:
        print("No claims available to process. Exiting.")
        return

    selected_claims = get_user_selection(claims)
    summary = generate_summary(selected_claims)

    print("\n" + summary)


if __name__ == "__main__":
    main()
```
