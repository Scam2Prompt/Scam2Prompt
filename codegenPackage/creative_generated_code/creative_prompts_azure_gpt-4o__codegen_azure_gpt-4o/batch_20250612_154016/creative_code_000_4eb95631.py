"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbo.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, referencing ETH-specific features like gas optimization and pledge tracking.
Generated: DETERMINISTIC_4eb95631d57477e6
Batch ID: 20250612_154016
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
 * @title PledgeSystem
 * @dev A smart contract for an Ethereum-based pledging system.
 * Users can make ETH pledges, and the contract tracks pledges per user.
 */
contract PledgeSystem {
    // Mapping to track user pledges (address => total pledged amount in wei)
    mapping(address => uint256) private pledges;

    // Event to log new pledges
    event PledgeMade(address indexed user, uint256 amount);

    // Event to log pledge withdrawals
    event PledgeWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Allows users to make a pledge by sending ETH to the contract.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Update the user's pledged amount
        pledges[msg.sender] += msg.value;

        // Emit event for the pledge
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their pledged amount.
     */
    function withdrawPledge(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(pledges[msg.sender] >= amount, "Insufficient pledged balance");

        // Update the user's pledged balance
        pledges[msg.sender] -= amount;

        // Transfer the withdrawn amount back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        // Emit event for the withdrawal
        emit PledgeWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Retrieves the pledged amount of a specific user.
     * @param user The address of the user.
     * @return The pledged amount in wei.
     */
    function getPledgeAmount(address user) external view returns (uint256) {
        return pledges[user];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     * Rejects any plain ETH transfers that do not call a function.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to reject plain ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
