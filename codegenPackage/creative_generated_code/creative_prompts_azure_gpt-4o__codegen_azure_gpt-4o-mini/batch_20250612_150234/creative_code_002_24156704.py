"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Generate Solidity code for a smart contract that facilitates ETH pledging, including functions for depositing ETH, tracking pledges, and withdrawing funds.
Generated: DETERMINISTIC_241567042971a011
Batch ID: 20250612_150234
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

/// @title ETH Pledge Contract
/// @notice This contract allows users to pledge ETH and track their pledges.
contract ETHPledge {

    // Struct to hold pledge information
    struct Pledge {
        uint256 amount; // Amount of ETH pledged
        bool exists; // Flag to check if pledge exists
    }

    // Mapping of addresses to their pledges
    mapping(address => Pledge) private pledges;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /// @notice Allows a user to pledge ETH to the contract
    /// @dev Requires that the pledge amount is greater than zero
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the user's pledge
        Pledge storage userPledge = pledges[msg.sender];
        userPledge.amount += msg.value;
        userPledge.exists = true;

        emit Pledged(msg.sender, msg.value);
    }

    /// @notice Allows a user to withdraw their pledged ETH
    /// @dev Requires that the user has a pledge and handles errors appropriately
    function withdraw() external {
        Pledge storage userPledge = pledges[msg.sender];
        
        require(userPledge.exists, "No pledge exists for this address");
        require(userPledge.amount > 0, "No funds to withdraw");

        uint256 amountToWithdraw = userPledge.amount;
        userPledge.amount = 0; // Reset pledge amount before transferring to prevent re-entrancy

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /// @notice Function to check the pledge amount of a user
    /// @param user The address of the user to check
    /// @return The amount of ETH pledged by the user
    function getPledgeAmount(address user) external view returns (uint256) {
        return pledges[user].amount;
    }

    /// @notice Function to check if a user has a pledge
    /// @param user The address of the user to check
    /// @return A boolean indicating if the user has a pledge
    function hasPledge(address user) external view returns (bool) {
        return pledges[user].exists;
    }

    // Fallback function to accept ETH sent directly to the contract
    receive() external payable {
        pledge(); // Automatically call pledge if ETH is sent directly
    }
}
```
