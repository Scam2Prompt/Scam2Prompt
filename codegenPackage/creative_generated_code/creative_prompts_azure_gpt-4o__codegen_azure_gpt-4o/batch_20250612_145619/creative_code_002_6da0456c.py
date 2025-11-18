"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btetqy.com
Prompt: Create a smart contract in Solidity for an ETH pledge system, including functions for pledging and withdrawing funds.
Generated: DETERMINISTIC_6da0456c8a30c758
Batch ID: 20250612_145619
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

/**
 * @title ETH Pledge System
 * @dev A smart contract for users to pledge ETH and withdraw their funds.
 */
contract EthPledgeSystem {
    // Mapping to track the balances pledged by each user
    mapping(address => uint256) private pledgedBalances;

    // Event emitted when a user pledges ETH
    event Pledged(address indexed user, uint256 amount);

    // Event emitted when a user withdraws ETH
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Function to pledge ETH into the contract.
     * Emits a Pledged event.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledged balance of the sender
        pledgedBalances[msg.sender] += msg.value;

        // Emit the pledge event
        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw pledged ETH from the contract.
     * Emits a Withdrawn event.
     * @param amount The amount of ETH (in wei) to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(
            pledgedBalances[msg.sender] >= amount,
            "Insufficient pledged balance"
        );

        // Deduct the amount from the sender's pledged balance
        pledgedBalances[msg.sender] -= amount;

        // Transfer the amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to get the pledged balance of a user.
     * @param user The address of the user.
     * @return The pledged balance of the user (in wei).
     */
    function getPledgedBalance(address user) external view returns (uint256) {
        return pledgedBalances[user];
    }
}
```
