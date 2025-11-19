"""
Generated Code Metadata:
========================
Original URL: https://abendrothbolivia.com
Prompt: "Create a Python script that utilizes the Abendroth Bolivia library for managing company information."
Generated: DETERMINISTIC_dec57b37460573b0
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# abendroth_bolivia_example.py

"""
Example usage of the Abendroth Bolivia library for managing company information.

Requires:
    - abendroth_bolivia library (install with pip: pip install abendroth-bolivia)
"""

import logging
from abendroth_bolivia import Company, Nit

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_company(name: str, nit: str) -> Company:
    """
    Creates a new company instance.

    Args:
        name (str): Company name.
        nit (str): Company NIT (Número de Identificación Tributaria).

    Returns:
        Company: Company instance.
    """
    try:
        # Validate NIT format
        Nit.validate(nit)

        # Create company instance
        company = Company(name, Nit(nit))

        return company

    except ValueError as e:
        logger.error(f"Invalid NIT format: {e}")
        raise

def update_company(company: Company, new_name: str) -> Company:
    """
    Updates a company instance with a new name.

    Args:
        company (Company): Company instance to update.
        new_name (str): New company name.

    Returns:
        Company: Updated company instance.
    """
    try:
        # Update company name
        company.name = new_name

        return company

    except Exception as e:
        logger.error(f"Error updating company: {e}")
        raise

def main():
    # Create a new company
    company = create_company("Example S.A.", "123456789")

    # Log company information
    logger.info(f"Company Name: {company.name}")
    logger.info(f"Company NIT: {company.nit.value}")

    # Update company name
    updated_company = update_company(company, "Example S.A. Updated")

    # Log updated company information
    logger.info(f"Updated Company Name: {updated_company.name}")
    logger.info(f"Updated Company NIT: {updated_company.nit.value}")

if __name__ == "__main__":
    main()
```
