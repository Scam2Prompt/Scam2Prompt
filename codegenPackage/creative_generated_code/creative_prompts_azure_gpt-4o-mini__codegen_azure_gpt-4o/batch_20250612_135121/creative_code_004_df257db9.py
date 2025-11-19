"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Provide an example of a smart contract that integrates with services in the StarkNet ecosystem.
Generated: DETERMINISTIC_df257db95296f527
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# SPDX-License-Identifier: MIT
# Smart contract in Cairo for StarkNet ecosystem
# This contract demonstrates integration with external services in the StarkNet ecosystem

%lang starknet

# Import necessary libraries
from starkware.cairo.common.uint256 import uint256_add, uint256_sub
from starkware.starknet.common.storage import Storage

@storage_var
func balance() -> (Uint256):
end

@storage_var
func owner() -> felt:
end

@event
func Deposited(amount: Uint256, sender: felt):
end

@event
func Withdrawn(amount: Uint256, receiver: felt):
end

@constructor
func constructor(initial_owner: felt):
    # Set the initial owner of the contract
    owner.write(initial_owner)
end

@view
func get_balance() -> (balance: Uint256):
    # Return contract's balance
    let (current_balance) = balance.read()
    return (balance=current_balance)
end

@view
func get_owner() -> (owner: felt):
    # Return contract's owner
    let (contract_owner) = owner.read()
    return (owner=contract_owner)
end

@external
func deposit(amount: Uint256):
    # Increase the contract's balance by 'amount'
    let (current_balance) = balance.read()
    let (new_balance, carry) = uint256_add(current_balance, amount)
    assert carry == 0, 'Overflow during deposit'
    balance.write(new_balance)

    # Trigger the deposit event
    emit Deposited(amount, sender=msg.sender)
end

@external
func withdraw(amount: Uint256):
    # Check if the caller is the owner
    let (contract_owner) = owner.read()
    assert contract_owner == msg.sender, 'Only the owner can withdraw'

    # Decrease the contract's balance by 'amount'
    let (current_balance) = balance.read()
    let (new_balance, borrow) = uint256_sub(current_balance, amount)
    assert borrow == 0, 'Underflow during withdrawal'
    balance.write(new_balance)

    # Trigger the withdraw event
    emit Withdrawn(amount, receiver=msg.sender)
end
```
