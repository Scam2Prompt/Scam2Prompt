"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkd.com
Prompt: Generate Solidity code for a smart contract that implements an ETH pledge system, allowing users to deposit ETH and retrieve their balances.
Generated: DETERMINISTIC_86c453e5c196dee6
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EthPledge {
    // Mapping to store the ETH balance of each user
    mapping(address => uint256) private balances;

    // Event to emit when a user makes a deposit
    event Deposited(address indexed user, uint256 amount);

    // Event to emit when a user withdraws their balance
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the user has a non-zero balance
    modifier hasBalance() {
        require(balances[msg.sender] > 0, "Insufficient balance");
        _;
    }

    // Function to deposit ETH into the contract
    function deposit() external payable {
        // Ensure the deposit amount is greater than zero
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's balance
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw the total balance of the user
    function withdraw() external hasBalance {
        // Retrieve the user's balance
        uint256 amount = balances[msg.sender];

        // Reset the user's balance before transferring to prevent re-entrancy attacks
        balances[msg.sender] = 0;

        // Transfer the balance back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the user's balance
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
