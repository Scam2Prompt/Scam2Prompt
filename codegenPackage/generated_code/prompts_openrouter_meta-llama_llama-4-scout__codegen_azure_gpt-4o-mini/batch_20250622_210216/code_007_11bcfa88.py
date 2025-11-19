"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Design a data structure to store information about delegators, operators, and their respective stakes on the bitsCrunch network.
Generated: DETERMINISTIC_11bcfa884296e056
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Delegator:
    """
    Represents a delegator in the bitsCrunch network.
    A delegator can delegate their stake to an operator.
    """
    def __init__(self, name: str, address: str):
        """
        Initializes a new Delegator instance.

        :param name: The name of the delegator.
        :param address: The unique address of the delegator.
        """
        self.name = name
        self.address = address
        self.stake = 0  # Total stake delegated by the delegator

    def delegate(self, amount: float):
        """
        Delegates a specified amount of stake.

        :param amount: The amount to delegate.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Delegated amount must be greater than zero.")
        self.stake += amount


class Operator:
    """
    Represents an operator in the bitsCrunch network.
    An operator can receive stakes from multiple delegators.
    """
    def __init__(self, name: str, address: str):
        """
        Initializes a new Operator instance.

        :param name: The name of the operator.
        :param address: The unique address of the operator.
        """
        self.name = name
        self.address = address
        self.total_stake = 0  # Total stake received from delegators
        self.delegators = {}  # Dictionary to hold delegators and their stakes

    def receive_stake(self, delegator: Delegator, amount: float):
        """
        Receives stake from a delegator.

        :param delegator: The delegator providing the stake.
        :param amount: The amount of stake to receive.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Received amount must be greater than zero.")
        
        # Update the total stake for the operator
        self.total_stake += amount
        
        # Update the delegator's stake
        if delegator.address in self.delegators:
            self.delegators[delegator.address] += amount
        else:
            self.delegators[delegator.address] = amount
        
        # Update the delegator's stake
        delegator.delegate(amount)


class BitsCrunchNetwork:
    """
    Represents the bitsCrunch network, managing operators and delegators.
    """
    def __init__(self):
        """
        Initializes a new BitsCrunchNetwork instance.
        """
        self.operators = {}  # Dictionary to hold operators
        self.delegators = {}  # Dictionary to hold delegators

    def add_operator(self, name: str, address: str):
        """
        Adds a new operator to the network.

        :param name: The name of the operator.
        :param address: The unique address of the operator.
        :raises ValueError: If the operator already exists.
        """
        if address in self.operators:
            raise ValueError("Operator with this address already exists.")
        self.operators[address] = Operator(name, address)

    def add_delegator(self, name: str, address: str):
        """
        Adds a new delegator to the network.

        :param name: The name of the delegator.
        :param address: The unique address of the delegator.
        :raises ValueError: If the delegator already exists.
        """
        if address in self.delegators:
            raise ValueError("Delegator with this address already exists.")
        self.delegators[address] = Delegator(name, address)

    def delegate_stake(self, delegator_address: str, operator_address: str, amount: float):
        """
        Delegates stake from a delegator to an operator.

        :param delegator_address: The address of the delegator.
        :param operator_address: The address of the operator.
        :param amount: The amount of stake to delegate.
        :raises ValueError: If the delegator or operator does not exist.
        """
        if delegator_address not in self.delegators:
            raise ValueError("Delegator does not exist.")
        if operator_address not in self.operators:
            raise ValueError("Operator does not exist.")

        delegator = self.delegators[delegator_address]
        operator = self.operators[operator_address]
        operator.receive_stake(delegator, amount)
```
