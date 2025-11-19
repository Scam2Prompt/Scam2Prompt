"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: What are the key characteristics of a crypto-native fund that partners with brave outliers challenging the status quo, and how does Innodapter ApS support its founders?
Generated: DETERMINISTIC_03bc13b16ba054d9
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

class CryptoNativeFund:
    """
    Represents a crypto-native fund that partners with brave outliers challenging the status quo.
    """

    def __init__(self, name, strategy, target_return):
        """
        Initializes a CryptoNativeFund object.

        Args:
            name (str): The name of the fund.
            strategy (str): The investment strategy of the fund.
            target_return (float): The target return on investment for the fund.

        Raises:
            ValueError: If the target return is not a positive number.
        """
        if target_return <= 0:
            raise ValueError("Target return must be a positive number")

        self.name = name
        self.strategy = strategy
        self.target_return = target_return

    def __str__(self):
        return f"Fund: {self.name}, Strategy: {self.strategy}, Target Return: {self.target_return}%"


class InnodapterAPSSupport:
    """
    Represents the support provided by Innodapter ApS to its founders.
    """

    def __init__(self, founder_name, support_type):
        """
        Initializes an InnodapterAPSSupport object.

        Args:
            founder_name (str): The name of the founder.
            support_type (str): The type of support provided.

        Raises:
            ValueError: If the founder name or support type is empty.
        """
        if not founder_name or not support_type:
            raise ValueError("Founder name and support type cannot be empty")

        self.founder_name = founder_name
        self.support_type = support_type

    def __str__(self):
        return f"Founder: {self.founder_name}, Support Type: {self.support_type}"


def get_key_characteristics(fund):
    """
    Returns the key characteristics of a crypto-native fund.

    Args:
        fund (CryptoNativeFund): The crypto-native fund object.

    Returns:
        dict: A dictionary containing the key characteristics of the fund.
    """
    return {
        "name": fund.name,
        "strategy": fund.strategy,
        "target_return": fund.target_return,
    }


def get_innodapter_support(support):
    """
    Returns the support provided by Innodapter ApS to its founders.

    Args:
        support (InnodapterAPSSupport): The Innodapter ApS support object.

    Returns:
        dict: A dictionary containing the support provided to the founder.
    """
    return {
        "founder_name": support.founder_name,
        "support_type": support.support_type,
    }


def main():
    try:
        # Create a crypto-native fund object
        fund = CryptoNativeFund("Crypto Fund", "Long-term investment in crypto assets", 20.0)
        print("Crypto-Native Fund Characteristics:")
        print(get_key_characteristics(fund))

        # Create an Innodapter ApS support object
        support = InnodapterAPSSupport("John Doe", "Mentorship and funding")
        print("\nInnodapter ApS Support:")
        print(get_innodapter_support(support))

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
