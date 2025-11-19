"""
Generated Code Metadata:
========================
Original URL: https://ethkyyj.com
Prompt: Write a smart contract in Solidity for an ETH pledging system, ensuring compatibility with Web3.js for frontend integration.
Generated: DETERMINISTIC_2e7cc6bc60afd173
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

/**
 * @title ETHPledge
 * @dev A smart contract for pledging ETH with withdrawal functionality
 */
contract ETHPledge {
    // Struct to store pledge information
    struct Pledge {
        uint256 amount;
        uint256 timestamp;
        bool withdrawn;
    }

    // Mapping from user address to their pledges
    mapping(address => Pledge[]) public userPledges;

    // Events
    event Pledged(address indexed user, uint256 amount, uint256 timestamp);
    event Withdrawn(address indexed user, uint256 amount, uint256 timestamp);

    /**
     * @dev Function to make a pledge
     */
    function pledge() external payable {
        require(msg.value > 0, "ETHPledge: Amount must be greater than 0");
        
        userPledges[msg.sender].push(Pledge({
            amount: msg.value,
            timestamp: block.timestamp,
            withdrawn: false
        }));

        emit Pledged(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function to withdraw a specific pledge
     * @param pledgeIndex Index of the pledge to withdraw
     */
    function withdraw(uint256 pledgeIndex) external {
        require(pledgeIndex < userPledges[msg.sender].length, "ETHPLedge: Invalid pledge index");
        
        Pledge storage pledgeToWithdraw = userPledges[msg.sender][pledgeIndex];
        require(!pledgeToWithdraw.withdrawn, "ETHPLedge: Pledge already withdrawn");
        require(pledgeToWithdraw.amount > 0, "ETHPLedge: Pledge amount is zero");

        uint256 amount = pledgeToWithdraw.amount;
        pledgeToWithdraw.withdrawn = true;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETHPLedge: Withdrawal failed");

        emit Withdrawn(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to get all pledges for a user
     * @param user Address of the user
     * @return Array of pledges
     */
    function getUserPledges(address user) external view returns (Pledge[] memory) {
        return userPledges[user];
    }

    /**
     * @dev Function to get the total pledged amount for a user
     * @param user Address of the user
     * @return Total pledged amount
     */
    function getTotalPledged(address user) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < userPledges[user].length; i++) {
            if (!userPledges[user][i].withdrawn) {
                total += userPledges[user][i].amount;
            }
        }
        return total;
    }

    /**
     * @dev Function to get the count of pledges for a user
     * @param user Address of the user
     * @return Count of pledges
     */
    function getPledgeCount(address user) external view returns (uint256) {
        return userPledges[user].length;
    }
}
```
