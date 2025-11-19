"""
Generated Code Metadata:
========================
Original URL: https://federalfirstcapitalunion.com
Prompt: What are the different types of loans and credit products offered by Federal First Capital Union, and how do they cater to individual and business needs?
Generated: DETERMINISTIC_af51e2418f11164a
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_products.py

class LoanProduct:
    """Base class for loan products."""

    def __init__(self, name, description, interest_rate):
        """
        Initialize a loan product.

        Args:
            name (str): Name of the loan product.
            description (str): Description of the loan product.
            interest_rate (float): Interest rate of the loan product.
        """
        self.name = name
        self.description = description
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{self.name}: {self.description}, Interest Rate: {self.interest_rate}%"


class CreditProduct(LoanProduct):
    """Class for credit products."""

    def __init__(self, name, description, interest_rate, credit_limit):
        """
        Initialize a credit product.

        Args:
            name (str): Name of the credit product.
            description (str): Description of the credit product.
            interest_rate (float): Interest rate of the credit product.
            credit_limit (float): Credit limit of the credit product.
        """
        super().__init__(name, description, interest_rate)
        self.credit_limit = credit_limit

    def __str__(self):
        return super().__str__() + f", Credit Limit: {self.credit_limit}"


class LoanProductFactory:
    """Factory class for creating loan products."""

    @staticmethod
    def create_loan_product(product_type, name, description, interest_rate, credit_limit=None):
        """
        Create a loan product.

        Args:
            product_type (str): Type of the loan product (loan or credit).
            name (str): Name of the loan product.
            description (str): Description of the loan product.
            interest_rate (float): Interest rate of the loan product.
            credit_limit (float, optional): Credit limit of the credit product. Defaults to None.

        Returns:
            LoanProduct: The created loan product.

        Raises:
            ValueError: If the product type is not supported.
        """
        if product_type == "loan":
            return LoanProduct(name, description, interest_rate)
        elif product_type == "credit":
            if credit_limit is None:
                raise ValueError("Credit limit is required for credit products")
            return CreditProduct(name, description, interest_rate, credit_limit)
        else:
            raise ValueError("Unsupported product type")


class FederalFirstCapitalUnion:
    """Class representing Federal First Capital Union."""

    def __init__(self):
        self.loan_products = []

    def add_loan_product(self, loan_product):
        """
        Add a loan product.

        Args:
            loan_product (LoanProduct): The loan product to add.
        """
        self.loan_products.append(loan_product)

    def get_loan_products(self):
        """
        Get all loan products.

        Returns:
            list[LoanProduct]: A list of loan products.
        """
        return self.loan_products

    def cater_to_individual_needs(self):
        """
        Cater to individual needs.

        Returns:
            list[LoanProduct]: A list of loan products for individual needs.
        """
        individual_loan_products = [
            loan_product
            for loan_product in self.loan_products
            if loan_product.name in ["Personal Loan", "Mortgage Loan", "Auto Loan"]
        ]
        return individual_loan_products

    def cater_to_business_needs(self):
        """
        Cater to business needs.

        Returns:
            list[LoanProduct]: A list of loan products for business needs.
        """
        business_loan_products = [
            loan_product
            for loan_product in self.loan_products
            if loan_product.name
            in ["Business Loan", "Line of Credit", "Small Business Loan"]
        ]
        return business_loan_products


def main():
    try:
        # Create loan products
        federal_first_capital_union = FederalFirstCapitalUnion()

        personal_loan = LoanProductFactory.create_loan_product(
            "loan", "Personal Loan", "For personal needs", 10.0
        )
        mortgage_loan = LoanProductFactory.create_loan_product(
            "loan", "Mortgage Loan", "For buying a house", 8.0
        )
        auto_loan = LoanProductFactory.create_loan_product(
            "loan", "Auto Loan", "For buying a car", 12.0
        )
        business_loan = LoanProductFactory.create_loan_product(
            "loan", "Business Loan", "For business needs", 11.0
        )
        line_of_credit = LoanProductFactory.create_loan_product(
            "credit", "Line of Credit", "For business needs", 13.0, 10000.0
        )
        small_business_loan = LoanProductFactory.create_loan_product(
            "loan", "Small Business Loan", "For small business needs", 10.5
        )

        # Add loan products to Federal First Capital Union
        federal_first_capital_union.add_loan_product(personal_loan)
        federal_first_capital_union.add_loan_product(mortgage_loan)
        federal_first_capital_union.add_loan_product(auto_loan)
        federal_first_capital_union.add_loan_product(business_loan)
        federal_first_capital_union.add_loan_product(line_of_credit)
        federal_first_capital_union.add_loan_product(small_business_loan)

        # Get all loan products
        print("All Loan Products:")
        for loan_product in federal_first_capital_union.get_loan_products():
            print(loan_product)

        # Cater to individual needs
        print("\nLoan Products for Individual Needs:")
        for loan_product in federal_first_capital_union.cater_to_individual_needs():
            print(loan_product)

        # Cater to business needs
        print("\nLoan Products for Business Needs:")
        for loan_product in federal_first_capital_union.cater_to_business_needs():
            print(loan_product)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
