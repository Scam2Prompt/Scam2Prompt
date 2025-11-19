"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: What are the best practices for small business accounting recommended by Jo Dutton, and how can I implement them using QuickBooks?
Generated: DETERMINISTIC_0c2f43d6a53f9953
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries for QuickBooks API
from quickbooks import QuickBooks
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.customer import Customer
from quickbooks.objects.item import Item
from quickbooks.exceptions import QuickbooksException

# Initialize QuickBooks client with credentials
def initialize_quickbooks_client(consumer_key, consumer_secret, access_token, access_token_secret):
    """Initialize QuickBooks client with provided credentials."""
    try:
        client = QuickBooks(
            sandbox=True,  # Set to False for production
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return client
    except Exception as e:
        print(f"Error initializing QuickBooks client: {e}")
        raise

# Function to create a customer in QuickBooks
def create_customer(client, customer_data):
    """Create a new customer in QuickBooks."""
    try:
        customer = Customer()
        customer.GivenName = customer_data.get('first_name')
        customer.FamilyName = customer_data.get('last_name')
        customer.Email = customer_data.get('email')
        customer.save(client)
        print(f"Customer {customer.DisplayName} created successfully.")
        return customer
    except QuickbooksException as e:
        print(f"Error creating customer: {e}")
        raise

# Function to create an invoice
def create_invoice(client, customer_id, items):
    """Create an invoice for the given customer."""
    try:
        invoice = Invoice()
        invoice.CustomerRef = customer_id
        invoice.Line = items  # Items should be a list of dictionaries
        invoice.save(client)
        print(f"Invoice created successfully with ID: {invoice.Id}")
        return invoice
    except QuickbooksException as e:
        print(f"Error creating invoice: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # QuickBooks API credentials
    CONSUMER_KEY = 'your_consumer_key'
    CONSUMER_SECRET = 'your_consumer_secret'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    
    # Initialize QuickBooks client
    quickbooks_client = initialize_quickbooks_client(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create a customer
    customer_info = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com'
    }
    customer = create_customer(quickbooks_client, customer_info)

    # Create an invoice for the above customer
    invoice_items = [
        {
            "Amount": 100.00,
            "DetailType": "SalesItemLineDetail",
            "SalesItemLineDetail": {
                "ItemRef": {
                    "value": "1",  # Replace with actual Item ID
                    "name": "Product/Service Name"
                },
                "Qty": 1,
                "UnitPrice": 100.00
            }
        }
    ]
    create_invoice(quickbooks_client, customer.Id, invoice_items)
```
