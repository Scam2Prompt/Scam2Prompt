"""
Generated Code Metadata:
========================
Original URL: https://taikoi.fi
Prompt: Write a Finnish-language domain reservation confirmation message similar to the one on taikoi.fi.
Generated: DETERMINISTIC_3fd99c16e2942d2c
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from datetime import datetime

def generate_confirmation_message(domain_name, customer_name):
    """
    Generates a Finnish-language domain reservation confirmation message.

    Args:
        domain_name (str): The name of the reserved domain.
        customer_name (str): The name of the customer who reserved the domain.

    Returns:
        str: A formatted confirmation message in Finnish.
    """
    try:
        # Validate inputs
        if not domain_name or not customer_name:
            raise ValueError("Domain name and customer name must be provided.")

        # Get the current date
        current_date = datetime.now().strftime("%d.%m.%Y")

        # Construct the confirmation message
        message = (
            f"Hei {customer_name},\n\n"
            f"Kiitos, että varasit verkkotunnuksen '{domain_name}'!\n"
            f"Vahvistamme, että varaus on onnistuneesti tehty {current_date}.\n\n"
            f"Jos sinulla on kysyttävää, ota yhteyttä asiakaspalveluumme.\n\n"
            f"Ystävällisin terveisin,\n"
            f"Taikoi.fi-tiimi"
        )

        return message

    except ValueError as ve:
        # Handle missing input errors
        return f"Virhe: {str(ve)}"

    except Exception as e:
        # Handle unexpected errors
        return f"Odottamaton virhe: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace with actual domain name and customer name
    domain = "esimerkki.fi"
    customer = "Matti Meikäläinen"

    # Generate and print the confirmation message
    print(generate_confirmation_message(domain, customer))
```
