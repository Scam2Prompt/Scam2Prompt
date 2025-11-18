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
 * @dev This contract allows users to pledge ETH and withdraw their funds.
 */
contract ETHPledge {
    
    // Struct to represent a pledge
    struct Pledge {
        uint256 amount;
        bool exists;
    }

    // Mapping to store pledges of each address
    mapping(address => Pledge) private pledges;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /**
     * @dev Pledge ETH to the contract
     */
    function pledge() external payable {
        require(msg.value > 0, "Must pledge a positive amount");

        // Check if the user already has a pledge
        if (pledges[msg.sender].exists) {
            // If exists, update the pledge amount
            pledges[msg.sender].amount += msg.value;
        } else {
            // If not, create a new pledge
            pledges[msg.sender] = Pledge(msg.value, true);
        }

        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw pledged ETH from the contract
     */
    function withdraw() external {
        // Retrieve the user's pledge
        Pledge storage userPledge = pledges[msg.sender];
        
        require(userPledge.exists, "No pledge to withdraw");
        require(userPledge.amount > 0, "No funds to withdraw");

        // Local variable to store amount to withdraw
        uint256 amountToWithdraw = userPledge.amount;

        // Reset the user's pledge before transferring to prevent re-entrancy
        userPledge.amount = 0;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Get the amount pledged by a user
     * @param user The address of the user
     * @return The amount pledged by the user
     */
    function getPledgedAmount(address user) external view returns (uint256) {
        return pledges[user].amount;
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {
        pledge();
    }
}
```
