"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Generate code for a blockchain-based pledge system using Ethereum smart contracts, referencing the ETH Pledge concept.
Generated: DETERMINISTIC_03ed50a757f30331
Batch ID: 20250612_152600
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

/// @title ETH Pledge Smart Contract
/// @author Your Name
/// @notice This contract allows users to make pledges in ETH and manage their pledges
/// @dev This contract is designed to be simple and secure for managing ETH pledges

contract ETHPledge {
    // Struct to represent a pledge
    struct Pledge {
        address pledger; // Address of the person who made the pledge
        uint256 amount;  // Amount of ETH pledged
        bool fulfilled;  // Status of the pledge
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    // Counter for unique pledge IDs
    uint256 public pledgeCount;

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    /// @notice Create a new pledge
    /// @dev Requires the pledge amount to be greater than zero
    /// @param _amount The amount of ETH to pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment pledge count to create a unique ID
        pledgeCount++;
        // Create a new pledge
        pledges[pledgeCount] = Pledge(msg.sender, msg.value, false);

        // Emit an event for the new pledge
        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    /// @notice Fulfill a pledge by its ID
    /// @dev Only the original pledger can fulfill their pledge
    /// @param _pledgeId The ID of the pledge to fulfill
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        // Ensure the pledge exists and has not been fulfilled
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(!pledge.fulfilled, "Pledge already fulfilled");
        require(pledge.pledger == msg.sender, "Only the pledger can fulfill this pledge");

        // Mark the pledge as fulfilled
        pledge.fulfilled = true;

        // Transfer the pledged amount to the pledger
        (bool success, ) = pledge.pledger.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit an event for the fulfilled pledge
        emit PledgeFulfilled(_pledgeId);
    }

    /// @notice Get details of a pledge by its ID
    /// @param _pledgeId The ID of the pledge to retrieve
    /// @return pledger The address of the pledger
    /// @return amount The amount pledged
    /// @return fulfilled The status of the pledge
    function getPledge(uint256 _pledgeId) external view returns (address pledger, uint256 amount, bool fulfilled) {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger != address(0), "Pledge does not exist");

        return (pledge.pledger, pledge.amount, pledge.fulfilled);
    }
}
```
