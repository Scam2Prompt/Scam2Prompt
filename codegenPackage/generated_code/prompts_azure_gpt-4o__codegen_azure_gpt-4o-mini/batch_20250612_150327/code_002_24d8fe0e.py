"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Generate a smart contract using Cairo, StarkNet's native programming language, that interacts with a wallet service listed in the StarkNet Ecosystem.
Generated: DETERMINISTIC_24d8fe0e8812946e
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cairo
# Import necessary libraries
from starkware.cairo.common.cairo_cairo import Cairo
from starkware.cairo.common.math import safe_add, safe_sub
from starkware.starknet.common.syscalls import get_caller_address, get_contract_address
from starkware.starknet.common.storage import Storage

# Define the contract
@contract
namespace WalletInteraction:
    # State variables
    @storage_var
    func owner() -> (address):
        pass

    @storage_var
    func balance() -> (uint):
        pass

    # Constructor to initialize the contract
    @constructor
    func constructor(initial_balance: uint):
        # Set the contract owner to the address that deployed the contract
        let (caller) = get_caller_address()
        owner.write(caller)
        # Initialize the balance
        balance.write(initial_balance)

    # Function to deposit funds into the wallet
    @public
    func deposit(amount: uint):
        # Ensure the amount is greater than zero
        assert amount > 0, "Deposit amount must be greater than zero"
        
        # Update the balance
        let current_balance = balance.read()
        let new_balance = safe_add(current_balance, amount)
        balance.write(new_balance)

    # Function to withdraw funds from the wallet
    @public
    func withdraw(amount: uint):
        # Ensure the amount is greater than zero
        assert amount > 0, "Withdrawal amount must be greater than zero"
        
        # Ensure sufficient balance
        let current_balance = balance.read()
        assert current_balance >= amount, "Insufficient balance for withdrawal"
        
        # Update the balance
        let new_balance = safe_sub(current_balance, amount)
        balance.write(new_balance)

    # Function to check the balance
    @public
    func check_balance() -> (uint):
        return balance.read()

    # Function to transfer funds to another wallet
    @public
    func transfer(to: address, amount: uint):
        # Ensure the amount is greater than zero
        assert amount > 0, "Transfer amount must be greater than zero"
        
        # Ensure sufficient balance
        let current_balance = balance.read()
        assert current_balance >= amount, "Insufficient balance for transfer"
        
        # Update the balance
        let new_balance = safe_sub(current_balance, amount)
        balance.write(new_balance)

        # Call the wallet service to transfer the funds
        let (success) = WalletService.transfer(to, amount)
        assert success, "Transfer failed"

# Define the wallet service interface
@external
namespace WalletService:
    func transfer(to: address, amount: uint) -> (bool):
        # This function should interact with the actual wallet service
        # Implementation details depend on the specific wallet service
        pass
```
