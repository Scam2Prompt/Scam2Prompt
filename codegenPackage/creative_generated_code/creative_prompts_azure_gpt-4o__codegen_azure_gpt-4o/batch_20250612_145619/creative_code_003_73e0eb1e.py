"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imotokaen.com
Prompt: Create a Solidity function that validates and processes pledges on Ethereum, referencing the ETH Pledge system from imotokaen.com.
Generated: DETERMINISTIC_73e0eb1ea7d6ef59
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

/// @title ETH Pledge System
/// @notice A contract to validate and process pledges in Ethereum

contract EthPledge {
    // Mapping to keep track of pledges
    mapping(address => uint256) public pledges;

    // Event to emit when a pledge is successfully processed
    event PledgeProcessed(address indexed pledger, uint256 amount);

    /// @notice Function to validate and process a pledge
    /// @dev Ensures a valid pledge amount is sent and updates the pledges mapping
    function processPledge() external payable {
        // Require a non-zero pledge amount
        require(msg.value > 0, "Pledge amount must be greater than zero.");

        // Update the pledge for the sender
        pledges[msg.sender] += msg.value;

        // Emit the event for successful pledge
        emit PledgeProcessed(msg.sender, msg.value);
    }

    /// @notice Function to check the total pledge amount of a specific address
    /// @param pledger The address of the pledger
    /// @return The total amount pledged by the specified address
    function getPledge(address pledger) external view returns (uint256) {
        return pledges[pledger];
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct transfers are not allowed. Use processPledge.");
    }

    /// @notice Receive function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers are not allowed. Use processPledge.");
    }
}
```
