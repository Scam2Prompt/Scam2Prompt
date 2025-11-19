"""
Generated Code Metadata:
========================
Original URL: https://cryptonbd.com
Prompt: Generate code for a simple Ethereum pledge smart contract using Solidity.
Generated: DETERMINISTIC_342b4cae02285f03
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
/// @notice This contract allows users to pledge Ether to a specific cause
/// @dev This contract is designed to be simple and easy to understand

contract Pledge {
    // Struct to represent a pledge
    struct PledgeInfo {
        address pledger; // Address of the person who made the pledge
        uint256 amount;  // Amount pledged in wei
        bool claimed;    // Status of the pledge
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => PledgeInfo) public pledges;
    uint256 public pledgeCount; // Counter for the number of pledges

    // Event emitted when a new pledge is made
    event PledgeMade(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is claimed
    event PledgeClaimed(uint256 indexed pledgeId, address indexed pledger);

    /// @notice Make a pledge to the contract
    /// @dev Requires that the pledge amount is greater than zero
    /// @param _amount The amount of Ether to pledge in wei
    function makePledge(uint256 _amount) external payable {
        require(_amount > 0, "Pledge amount must be greater than zero");
        require(msg.value == _amount, "Ether sent must match the pledge amount");

        // Create a new pledge
        pledges[pledgeCount] = PledgeInfo({
            pledger: msg.sender,
            amount: _amount,
            claimed: false
        });

        emit PledgeMade(pledgeCount, msg.sender, _amount);
        pledgeCount++;
    }

    /// @notice Claim a pledge by its ID
    /// @dev Requires that the pledge has not been claimed yet
    /// @param _pledgeId The ID of the pledge to claim
    function claimPledge(uint256 _pledgeId) external {
        PledgeInfo storage pledge = pledges[_pledgeId];
        
        require(pledge.pledger == msg.sender, "Only the pledger can claim this pledge");
        require(!pledge.claimed, "Pledge has already been claimed");

        // Mark the pledge as claimed
        pledge.claimed = true;

        // Transfer the pledged amount back to the pledger
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        emit PledgeClaimed(_pledgeId, msg.sender);
    }

    /// @notice Get the details of a pledge by its ID
    /// @param _pledgeId The ID of the pledge to retrieve
    /// @return pledger The address of the pledger
    /// @return amount The amount pledged in wei
    /// @return claimed The status of the pledge
    function getPledge(uint256 _pledgeId) external view returns (address pledger, uint256 amount, bool claimed) {
        PledgeInfo storage pledge = pledges[_pledgeId];
        return (pledge.pledger, pledge.amount, pledge.claimed);
    }
}
```
