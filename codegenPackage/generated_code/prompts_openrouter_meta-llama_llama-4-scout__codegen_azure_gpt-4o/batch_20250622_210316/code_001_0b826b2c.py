"""
Generated Code Metadata:
========================
Original URL: https://geektech.uk
Prompt: Write a review of the best-selling mobile phone brands in 2024.
Generated: DETERMINISTIC_0b826b2c511b6962
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a review of the best-selling mobile phone brands in 2024.
It uses a predefined dataset of mobile phone brands and their sales figures to
create a summary report. The script is designed to be clean, efficient, and
production-ready.
"""

import json

# Sample dataset of mobile phone brands and their sales figures (in millions)
mobile_phone_sales = [
    {"brand": "Apple", "sales": 250},
    {"brand": "Samsung", "sales": 230},
    {"brand": "Xiaomi", "sales": 180},
    {"brand": "Oppo", "sales": 150},
    {"brand": "Vivo", "sales": 140},
]

def generate_review(sales_data):
    """
    Generates a review of the best-selling mobile phone brands based on sales data.

    Args:
        sales_data (list): A list of dictionaries containing brand names and sales figures.

    Returns:
        str: A formatted review of the best-selling mobile phone brands.
    """
    try:
        # Sort the data by sales in descending order
        sorted_data = sorted(sales_data, key=lambda x: x['sales'], reverse=True)

        # Generate the review text
        review = "Best-Selling Mobile Phone Brands in 2024:\n"
        review += "=" * 40 + "\n"
        for idx, entry in enumerate(sorted_data, start=1):
            review += f"{idx}. {entry['brand']} - {entry['sales']} million units sold\n"

        return review
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the review: {str(e)}"

def save_review_to_file(review, filename="mobile_phone_review_2024.txt"):
    """
    Saves the generated review to a text file.

    Args:
        review (str): The review text to be saved.
        filename (str): The name of the file to save the review to. Defaults to 'mobile_phone_review_2024.txt'.

    Returns:
        None
    """
    try:
        with open(filename, "w") as file:
            file.write(review)
        print(f"Review successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the review: {str(e)}")

def main():
    """
    Main function to generate and save the review of best-selling mobile phone brands.
    """
    # Generate the review
    review = generate_review(mobile_phone_sales)

    # Print the review to the console
    print(review)

    # Save the review to a file
    save_review_to_file(review)

if __name__ == "__main__":
    main()
```
