"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Write a satirical script for a nomination submission system that categorizes users into groups like "Selfie Sorcerers" and "Meme Miners," inspired by the Monad Echo Awards website.
Generated: DETERMINISTIC_1cf078388a5d0faa
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants for user categories
CATEGORIES = {
    "Selfie Sorcerers": "Masters of the perfect selfie angle and filters.",
    "Meme Miners": "Creators and discoverers of viral internet gold.",
    "Caption Commanders": "Witty wordsmiths with unparalleled caption creativity.",
    "Hashtag Heroes": "Champions of trending hashtags and social movements.",
    "Reaction Royalty": "Connoisseurs of perfectly-timed reaction GIFs.",
}

# Function to validate nomination input
def validate_nomination(nomination):
    """
    Validates the nomination input to ensure all required fields are present and valid.

    :param nomination: dict containing nomination data
    :return: bool indicating whether the nomination is valid
    """
    required_fields = ["name", "email", "category", "submission"]
    for field in required_fields:
        if field not in nomination or not nomination[field]:
            print(f"Error: Missing or invalid field '{field}'.")
            return False

    # Check if the category is valid
    if nomination["category"] not in CATEGORIES:
        print(f"Error: Invalid category '{nomination['category']}'. Choose from {list(CATEGORIES.keys())}.")
        return False

    return True


# Function to handle nominations
def handle_nomination():
    """
    Collects and processes a nomination submission from the user.
    """
    print("Welcome to the Nomination Submission System for the 'Monad Echo Awards'!")
    print("Please choose a category:")
    for index, category in enumerate(CATEGORIES.keys(), start=1):
        print(f"{index}. {category} - {CATEGORIES[category]}")

    try:
        # Collecting nomination details
        name = input("Enter the nominee's name: ").strip()
        email = input("Enter the nominee's email: ").strip()
        category_index = int(input("Enter the category number: "))
        submission = input("Describe why this nominee deserves the award: ").strip()

        # Mapping the category index to the actual category name
        category = list(CATEGORIES.keys())[category_index - 1]

        nomination = {
            "name": name,
            "email": email,
            "category": category,
            "submission": submission,
        }

        # Validate the nomination details
        if not validate_nomination(nomination):
            print("Nomination submission failed due to invalid input.")
            return

        # Save the nomination to a JSON file
        with open("nominations.json", "a") as file:
            file.write(json.dumps(nomination) + "\n")
            print("Nomination successfully submitted!")

    except ValueError:
        print("Error: Invalid category number. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main function to execute the script
def main():
    """
    Entry point for the nomination submission script.
    """
    print("Starting 'Monad Echo Awards' Nomination Submission System...")
    handle_nomination()
    print("Thank you for participating!")


# Entry point check
if __name__ == "__main__":
    main()
```
