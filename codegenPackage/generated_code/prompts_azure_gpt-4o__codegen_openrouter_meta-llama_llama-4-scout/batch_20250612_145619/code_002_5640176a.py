"""
Generated Code Metadata:
========================
Original URL: https://imtixoken.com
Prompt: Develop a smart contract in Solidity that allows users to pledge ETH and tracks the total amount pledged.
Generated: DETERMINISTIC_5640176abd95d954
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PledgeContract {
    // Total amount pledged
    uint256 public totalPledged;

    // Mapping of user addresses to their pledged amounts
    mapping(address => uint256) public userPledges;

    // Event emitted when a user pledges ETH
    event PledgeMade(address indexed user, uint256 amount);

    // Event emitted when a user retracts their pledge
    event PledgeRetracted(address indexed user, uint256 amount);

    // Error for invalid pledge amounts
    error InvalidPledgeAmount();

    // Error for users trying to retract more than they pledged
    error InsufficientPledge();

    /**
     * Allows users to pledge ETH.
     */
    function pledge() public payable {
        // Ensure a valid pledge amount
        if (msg.value <= 0) {
            revert InvalidPledgeAmount();
        }

        // Update the user's pledge
        userPledges[msg.sender] += msg.value;

        // Update the total pledged amount
        totalPledged += msg.value;

        // Emit an event for the pledge
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * Allows users to retract their pledge.
     * @param amount The amount to retract.
     */
    function retractPledge(uint256 amount) public {
        // Ensure the user has sufficient pledge to retract
        if (userPledges[msg.sender] < amount) {
            revert InsufficientPledge();
        }

        // Update the user's pledge
        userPledges[msg.sender] -= amount;

        // Update the total pledged amount
        totalPledged -= amount;

        // Transfer the retracted amount back to the user
        payable(msg.sender).transfer(amount);

        // Emit an event for the retracted pledge
        emit PledgeRetracted(msg.sender, amount);
    }

    /**
     * Gets the total amount pledged.
     * @return The total amount pledged.
     */
    function getTotalPledged() public view returns (uint256) {
        return totalPledged;
    }

    /**
     * Gets a user's pledged amount.
     * @param user The user's address.
     * @return The user's pledged amount.
     */
    function getUserPledge(address user) public view returns (uint256) {
        return userPledges[user];
    }
}
```
