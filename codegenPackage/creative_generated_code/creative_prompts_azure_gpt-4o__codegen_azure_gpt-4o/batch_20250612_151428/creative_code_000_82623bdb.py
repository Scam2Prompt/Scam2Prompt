"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Write a Python script to generate a list of art course categories, including "aquarela," "mangá," and "desenho realista," as described on Ânima's website.
Generated: DETERMINISTIC_82623bdb4e297f82
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate a list of art course categories based on Ânima's website.
The script includes predefined categories such as 'aquarela', 'mangá', and 'desenho realista'.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Imports
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_art_course_categories() -> list:
    """
    Generates and returns a list of predefined art course categories.

    Returns:
        list: A list containing art course category names.
    """
    try:
        # List of art course categories
        art_categories = ["aquarela", "mangá", "desenho realista"]

        # Log the successful creation of the list
        logging.info("Art course categories generated successfully.")
        return art_categories
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"An error occurred while generating art course categories: {e}")
        return []


def main():
    """
    Main function that executes the script.
    """
    try:
        # Fetch the art course categories
        categories = get_art_course_categories()

        # Print the categories to the console
        if categories:
            print("Art Course Categories:")
            for idx, category in enumerate(categories, start=1):
                print(f"{idx}. {category}")
        else:
            print("No categories available.")

    except Exception as e:
        # Handle unexpected errors in the main execution
        logging.error(f"An unexpected error occurred in the main function: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
