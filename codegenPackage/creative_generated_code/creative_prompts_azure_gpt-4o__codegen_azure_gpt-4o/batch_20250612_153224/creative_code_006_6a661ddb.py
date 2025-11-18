"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Write a program to generate discount offers (e.g., up to 20%) for home services, referencing شركة انجاز's promotional strategies.
Generated: DETERMINISTIC_6a661ddbac103a95
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_discount_offer():
    """
    Generate a discount offer for home services.
    
    The discount will be between 5% and 20% inclusive.
    The offer includes branding for شركة انجاز.
    
    Returns:
        str: A promotional message containing the discount offer.
    """
    try:
        # Generate a random discount percentage between 5 and 20
        discount_percentage = random.randint(5, 20)

        # Prepare the promotional message
        company_name = "شركة انجاز"  # Arabic branding for the company
        message = f"اغتنم الفرصة واحصل على خصم يصل إلى {discount_percentage}% على خدمات المنزل من {company_name}!"
        
        return message
    except Exception as e:
        # Handle any unexpected errors
        return f"حدث خطأ أثناء إنشاء العرض: {e}"

def main():
    """
    Entry point of the program. Generates and displays a discount offer.
    """
    try:
        print("مرحباً بكم في شركة انجاز!")
        print("جاري إنشاء العرض الترويجي...")
        
        # Generate and display the discount offer
        offer = generate_discount_offer()
        print(offer)
    except Exception as e:
        # Handle any unexpected errors in the main flow
        print(f"حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    # Ensure the program runs as intended when executed
    main()
```
