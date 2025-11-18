"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conpoundi-filance.one
Prompt: Develop a chatbot script to assist users in selecting Vedacit products for specific construction needs, referencing items like "VEDATOP RODAPÉ" or "VEDAPREN FAST."
Generated: DETERMINISTIC_b55dd0a63152cfe4
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sys

def main():
    """
    Chatbot to assist users in selecting Vedacit products for specific construction needs.
    """
    print("Welcome to Vedacit Product Assistant!")
    print("I can help you select the right Vedacit product for your construction needs.")
    print("Type 'exit' at any time to leave the chat.\n")

    # Product catalog with descriptions
    products = {
        "VEDATOP RODAPÉ": "Ideal for waterproofing baseboards and areas subject to humidity.",
        "VEDAPREN FAST": "Quick-drying waterproofing solution for roofs and terraces.",
        "VEDACIT FLEX": "Flexible and durable waterproofing for walls and floors.",
        "VEDACIT IMPERMEABILIZANTE": "General-purpose waterproofing for various surfaces."
    }

    while True:
        try:
            # Prompt user for input
            user_input = input("Please describe your construction need: ").strip()
            
            # Exit condition
            if user_input.lower() == 'exit':
                print("Thank you for using Vedacit Product Assistant. Goodbye!")
                sys.exit()

            # Match user input with appropriate product
            matched_product = None
            for product, description in products.items():
                if any(keyword.lower() in user_input.lower() for keyword in product.split()):
                    matched_product = (product, description)
                    break

            # Provide response based on the match
            if matched_product:
                print(f"\nBased on your description, we recommend:")
                print(f"Product: {matched_product[0]}")
                print(f"Description: {matched_product[1]}\n")
            else:
                print("\nSorry, we couldn't find a product matching your needs.")
                print("Please provide more details or try again.\n")

        except KeyboardInterrupt:
            print("\nThank you for using Vedacit Product Assistant. Goodbye!")
            sys.exit()
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.\n")

# Entry point of the script
if __name__ == "__main__":
    main()
```
