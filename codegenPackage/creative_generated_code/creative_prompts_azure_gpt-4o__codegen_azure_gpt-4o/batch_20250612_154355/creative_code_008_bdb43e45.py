"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Develop a Python script to simulate a customer inquiry for industrial lifting equipment, using Roshako's contact information and product categories.
Generated: DETERMINISTIC_bdb43e454d1e0904
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate a customer inquiry for industrial lifting equipment.
This script uses Roshako's contact information and predefined product categories.
"""

import sys

def display_welcome_message():
    """
    Displays a welcome message to the user.
    """
    print("Welcome to Roshako Industrial Lifting Equipment Inquiry System!")
    print("We specialize in providing top-quality lifting solutions for industries.")
    print("Please follow the prompts to inquire about our services and products.\n")

def get_customer_details():
    """
    Collects customer details from user input.

    Returns:
        dict: A dictionary containing customer details.
    """
    try:
        print("Please provide your contact information:")
        name = input("Your Name: ").strip()
        email = input("Your Email: ").strip()
        phone = input("Your Phone Number: ").strip()
        
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone number are required.")

        return {
            "name": name,
            "email": email,
            "phone": phone
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def display_product_categories():
    """
    Displays available product categories to the user.
    """
    print("\nProduct Categories:")
    categories = [
        "1. Chain Hoists",
        "2. Wire Rope Hoists",
        "3. Overhead Cranes",
        "4. Lifting Slings",
        "5. Load Testing"
    ]
    for category in categories:
        print(category)

def get_product_selection():
    """
    Prompts the user to select a product category.

    Returns:
        str: The selected product category.
    """
    try:
        display_product_categories()
        choice = int(input("\nEnter the number corresponding to your product category: "))
        category_map = {
            1: "Chain Hoists",
            2: "Wire Rope Hoists",
            3: "Overhead Cranes",
            4: "Lifting Slings",
            5: "Load Testing"
        }
        if choice not in category_map:
            raise ValueError("Invalid selection. Please select a valid category.")
        return category_map[choice]
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def simulate_inquiry(customer_details, product_category):
    """
    Simulates sending an inquiry to Roshako's contact information.

    Args:
        customer_details (dict): Customer's contact information.
        product_category (str): Selected product category.
    """
    roshako_contact = {
        "Company Name": "Roshako Industrial Lifting Equipment",
        "Email": "contact@roshako.com",
        "Phone": "+1-800-555-ROSH"
    }

    print("\n--- Inquiry Summary ---")
    print(f"Customer Name: {customer_details['name']}")
    print(f"Customer Email: {customer_details['email']}")
    print(f"Customer Phone: {customer_details['phone']}")
    print(f"Inquired Product Category: {product_category}\n")
    print("Your inquiry has been sent to Roshako's team. Below are their contact details:")
    print(f"Company Name: {roshako_contact['Company Name']}")
    print(f"Email: {roshako_contact['Email']}")
    print(f"Phone: {roshako_contact['Phone']}")
    print("\nThank you for reaching out to Roshako!")

def main():
    """
    Main function to execute the program flow.
    """
    try:
        display_welcome_message()
        customer_details = get_customer_details()
        product_category = get_product_selection()
        simulate_inquiry(customer_details, product_category)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
