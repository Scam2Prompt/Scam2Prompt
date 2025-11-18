"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Develop a program to generate a contract template for temporary registration services in Adygea, ensuring compliance with Russian migration laws, as described on the website.
Generated: DETERMINISTIC_2b4679d3c45621bc
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_contract_template(
    customer_name,
    customer_passport_details,
    service_provider_name,
    service_provider_address,
    registration_address,
    contract_start_date,
    contract_end_date
):
    """
    Generates a contract template for temporary registration services in Adygea.

    Args:
        customer_name (str): Full name of the customer.
        customer_passport_details (str): Passport details of the customer.
        service_provider_name (str): Name of the service provider.
        service_provider_address (str): Address of the service provider.
        registration_address (str): Address of temporary registration in Adygea.
        contract_start_date (datetime.date): Start date of the contract.
        contract_end_date (datetime.date): End date of the contract.

    Returns:
        str: A formatted contract template as a string.
    """
    try:
        # Validate dates
        if contract_start_date >= contract_end_date:
            raise ValueError("Contract start date must be earlier than end date.")

        # Contract body
        contract = f"""
        CONTRACT FOR TEMPORARY REGISTRATION SERVICES IN ADYGEA

        This contract is made between:
        1. Service Provider: {service_provider_name}, located at {service_provider_address}.
        2. Customer: {customer_name}, passport details: {customer_passport_details}.

        The Service Provider agrees to provide temporary registration services at the following address:
        {registration_address}.

        Contract Details:
        - Contract Start Date: {contract_start_date.strftime('%d-%m-%Y')}
        - Contract End Date: {contract_end_date.strftime('%d-%m-%Y')}

        Obligations:
        - The Service Provider will ensure compliance with Russian migration laws, as outlined on the relevant government website.
        - The Customer agrees to provide accurate and truthful information.

        Termination:
        - This contract terminates automatically on {contract_end_date.strftime('%d-%m-%Y')}.
        - Early termination may occur upon mutual agreement or breach of terms.

        Signed:
        _______________________________           _______________________________
        Service Provider Signature                 Customer Signature
        Date: {datetime.date.today().strftime('%d-%m-%Y')}
        """

        return contract.strip()

    except ValueError as e:
        return f"Error generating contract: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example inputs
    customer_name = "Ivan Ivanov"
    customer_passport_details = "Passport Series 1234 No. 567890"
    service_provider_name = "Adygea Registration Services LLC"
    service_provider_address = "123 Main Street, Adygea"
    registration_address = "456 Secondary Road, Adygea"
    contract_start_date = datetime.date(2023, 10, 1)
    contract_end_date = datetime.date(2023, 12, 31)

    # Generate contract template
    contract = generate_contract_template(
        customer_name,
        customer_passport_details,
        service_provider_name,
        service_provider_address,
        registration_address,
        contract_start_date,
        contract_end_date
    )

    # Print the contract
    print(contract)
```
