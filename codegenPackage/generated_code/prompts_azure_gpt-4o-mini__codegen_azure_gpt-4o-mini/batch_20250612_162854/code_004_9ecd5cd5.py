"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Describe the steps to build a decentralized economy using Moxie’s smart contracts and how to extend its functionality.
Generated: DETERMINISTIC_9ecd5cd5c72134d5
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for smart contract development
from moxie import SmartContract, Blockchain, Transaction, Wallet

# Define a class for the Decentralized Economy
class DecentralizedEconomy(SmartContract):
    def __init__(self):
        # Initialize the smart contract with necessary parameters
        super().__init__()
        self.economy_data = {}
        self.participants = set()

    def register_participant(self, participant_address):
        """
        Register a new participant in the decentralized economy.
        
        :param participant_address: The blockchain address of the participant
        :raises ValueError: If the participant is already registered
        """
        if participant_address in self.participants:
            raise ValueError("Participant already registered.")
        self.participants.add(participant_address)
        self.economy_data[participant_address] = {'balance': 0}
        print(f"Participant {participant_address} registered successfully.")

    def transfer_funds(self, from_address, to_address, amount):
        """
        Transfer funds between participants in the economy.
        
        :param from_address: The address of the sender
        :param to_address: The address of the receiver
        :param amount: The amount to transfer
        :raises ValueError: If the sender does not have enough balance or is not registered
        """
        if from_address not in self.participants:
            raise ValueError("Sender not registered.")
        if to_address not in self.participants:
            raise ValueError("Receiver not registered.")
        if self.economy_data[from_address]['balance'] < amount:
            raise ValueError("Insufficient balance.")

        # Perform the transfer
        self.economy_data[from_address]['balance'] -= amount
        self.economy_data[to_address]['balance'] += amount
        print(f"Transferred {amount} from {from_address} to {to_address}.")

    def get_balance(self, participant_address):
        """
        Get the balance of a participant.
        
        :param participant_address: The address of the participant
        :return: The balance of the participant
        :raises ValueError: If the participant is not registered
        """
        if participant_address not in self.participants:
            raise ValueError("Participant not registered.")
        return self.economy_data[participant_address]['balance']

# Example usage of the DecentralizedEconomy class
if __name__ == "__main__":
    # Create a new instance of the decentralized economy
    economy = DecentralizedEconomy()

    # Register participants
    try:
        economy.register_participant("0xAlice")
        economy.register_participant("0xBob")
        
        # Simulate fund transfers
        economy.economy_data["0xAlice"]['balance'] = 100  # Initial balance for Alice
        economy.transfer_funds("0xAlice", "0xBob", 50)
        
        # Check balances
        print(f"Alice's balance: {economy.get_balance('0xAlice')}")
        print(f"Bob's balance: {economy.get_balance('0xBob')}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
