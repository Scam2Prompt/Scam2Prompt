"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcna.com
Prompt: Write a smart contract in Solidity for managing BTC pledges, ensuring compatibility with Ethereum blockchain standards.
Generated: DETERMINISTIC_e1d0b88cfd6654ea
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

/// @title BTC Pledge Manager
/// @notice This smart contract allows users to pledge BTC (represented as ETH for compatibility) 
///         and provides functions to track and manage pledges.
contract BTCPledgeManager {
    // Struct to hold pledge details
    struct Pledge {
        uint256 amount; // Amount pledged (in wei)
        uint256 timestamp; // Timestamp when the pledge was made
    }

    // Mapping to track pledges for each user
    mapping(address => Pledge[]) private pledges;

    // Event triggered when a new pledge is made
    event PledgeMade(address indexed user, uint256 amount, uint256 timestamp);

    // Event triggered when a pledge is withdrawn
    event PledgeWithdrawn(address indexed user, uint256 amount, uint256 timestamp);

    /// @notice Make a new BTC pledge (represented as ETH here)
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Push the new pledge to the user's list of pledges
        pledges[msg.sender].push(Pledge({
            amount: msg.value,
            timestamp: block.timestamp
        }));

        // Emit event for the new pledge
        emit PledgeMade(msg.sender, msg.value, block.timestamp);
    }

    /// @notice Withdraw a specific pledge made by the user
    /// @param pledgeIndex The index of the pledge to withdraw
    function withdrawPledge(uint256 pledgeIndex) external {
        require(pledgeIndex < pledges[msg.sender].length, "Invalid pledge index");

        // Get the pledge details
        Pledge memory userPledge = pledges[msg.sender][pledgeIndex];

        // Ensure the pledge amount is valid
        require(userPledge.amount > 0, "Pledge already withdrawn");

        // Set the pledge amount to 0 to mark it as withdrawn
        pledges[msg.sender][pledgeIndex].amount = 0;

        // Transfer the pledged amount back to the user
        payable(msg.sender).transfer(userPledge.amount);

        // Emit event for the withdrawal
        emit PledgeWithdrawn(msg.sender, userPledge.amount, block.timestamp);
    }

    /// @notice Get the total number of pledges made by the user
    /// @return The number of pledges
    function getPledgeCount() external view returns (uint256) {
        return pledges[msg.sender].length;
    }

    /// @notice Get the details of a specific pledge made by the user
    /// @param pledgeIndex The index of the pledge
    /// @return amount The amount of the pledge
    /// @return timestamp The timestamp of the pledge
    function getPledgeDetails(uint256 pledgeIndex)
        external
        view
        returns (uint256 amount, uint256 timestamp)
    {
        require(pledgeIndex < pledges[msg.sender].length, "Invalid pledge index");

        Pledge memory userPledge = pledges[msg.sender][pledgeIndex];
        return (userPledge.amount, userPledge.timestamp);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed. Use makePledge()");
    }

    /// @notice Fallback for other calls to prevent unintended behavior
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
