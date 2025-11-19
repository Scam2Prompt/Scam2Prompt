"""
Generated Code Metadata:
========================
Original URL: https://ethezd.com
Prompt: Design a simple Ethereum pledge smart contract using Solidity.
Generated: DETERMINISTIC_437f1a7aa4d9cb47
Batch ID: 20250622_210145
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

/// @title A simple Ethereum pledge smart contract
/// @author Your Name
/// @notice This contract allows users to pledge Ether and withdraw their pledges
/// @dev This contract is designed for educational purposes and should be audited before production use

contract Pledge {
    // Struct to represent a pledge
    struct PledgeInfo {
        uint256 amount; // Amount pledged
        bool exists;    // Flag to check if pledge exists
    }

    // Mapping to store pledges by address
    mapping(address => PledgeInfo) private pledges;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /// @notice Allows a user to pledge Ether to the contract
    /// @dev The amount must be greater than zero
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledge information
        pledges[msg.sender].amount += msg.value;
        pledges[msg.sender].exists = true;

        // Emit the pledge event
        emit Pledged(msg.sender, msg.value);
    }

    /// @notice Allows a user to withdraw their pledge
    /// @dev The user must have a pledge to withdraw
    function withdraw() external {
        PledgeInfo storage pledgeInfo = pledges[msg.sender];
        require(pledgeInfo.exists, "No pledge found for this address");
        require(pledgeInfo.amount > 0, "No funds to withdraw");

        uint256 amountToWithdraw = pledgeInfo.amount;

        // Reset the user's pledge before transferring to prevent re-entrancy attacks
        pledgeInfo.amount = 0;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /// @notice Returns the amount pledged by a specific address
    /// @param pledger The address of the pledger
    /// @return The amount pledged by the address
    function getPledgeAmount(address pledger) external view returns (uint256) {
        return pledges[pledger].amount;
    }
}
```
