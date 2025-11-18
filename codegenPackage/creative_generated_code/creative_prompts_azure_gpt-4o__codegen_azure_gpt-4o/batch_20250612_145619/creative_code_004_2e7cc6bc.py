"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkyyj.com
Prompt: Write a smart contract in Solidity for an ETH pledging system, ensuring compatibility with Web3.js for frontend integration.
Generated: DETERMINISTIC_2e7cc6bc60afd173
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
 * @title ETH Pledging System Smart Contract
 * @dev This contract allows users to pledge ETH and withdraw pledged funds. 
 * It is designed for integration with Web3.js in the frontend.
 */
contract ETHPledge {
    // Struct to store details of a pledge
    struct Pledge {
        uint256 amount;        // Amount of ETH pledged
        uint256 timestamp;     // Timestamp of when the pledge was made
    }

    // Mapping to store pledges per user (address => Pledge)
    mapping(address => Pledge) public pledges;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /**
     * @dev Allows users to pledge ETH to the contract.
     * Requires sending a non-zero amount of ETH.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledge amount for the sender
        pledges[msg.sender].amount += msg.value;
        pledges[msg.sender].timestamp = block.timestamp;

        // Emit the Pledged event
        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their pledged ETH.
     * Requires the user to have a non-zero amount pledged.
     */
    function withdraw() external {
        Pledge memory userPledge = pledges[msg.sender];
        require(userPledge.amount > 0, "No pledged amount to withdraw");

        // Calculate the amount to withdraw
        uint256 amountToWithdraw = userPledge.amount;

        // Reset the user's pledge data
        pledges[msg.sender].amount = 0;
        pledges[msg.sender].timestamp = 0;

        // Transfer the pledged ETH back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "ETH transfer failed");

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Function to retrieve the pledged amount and timestamp for a given user.
     * @param user Address of the user to query.
     * @return amount The amount of ETH pledged by the user.
     * @return timestamp The timestamp of the user's last pledge.
     */
    function getPledgeDetails(address user)
        external
        view
        returns (uint256 amount, uint256 timestamp)
    {
        Pledge memory userPledge = pledges[user];
        return (userPledge.amount, userPledge.timestamp);
    }
}
```
