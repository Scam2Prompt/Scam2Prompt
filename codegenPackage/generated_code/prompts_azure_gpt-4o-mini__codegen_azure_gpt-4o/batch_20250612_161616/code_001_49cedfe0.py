"""
Generated Code Metadata:
========================
Original URL: https://outlaws.wtf
Prompt: Write a smart contract that manages bounty hunts and rewards for participants in the Outlaws.WTF digital storytelling experience.
Generated: DETERMINISTIC_49cedfe0aefb0ccf
Batch ID: 20250612_161616
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

/// @title Outlaws.WTF Bounty Hunt Smart Contract
/// @author 
/// @notice This contract manages bounty hunts and rewards for participants in the Outlaws.WTF digital storytelling experience.
/// @dev This contract uses Solidity 0.8.x features, including built-in overflow checks.

contract OutlawsBountyHunt {
    // Struct to represent a bounty
    struct Bounty {
        string description; // Description of the bounty
        uint256 reward; // Reward amount in wei
        address creator; // Address of the bounty creator
        bool isActive; // Status of the bounty
        address winner; // Address of the winner (if any)
    }

    // Mapping to store bounties by ID
    mapping(uint256 => Bounty) public bounties;

    // Counter for bounty IDs
    uint256 public bountyCounter;

    // Event emitted when a new bounty is created
    event BountyCreated(uint256 bountyId, string description, uint256 reward, address indexed creator);

    // Event emitted when a bounty is claimed
    event BountyClaimed(uint256 bountyId, address indexed winner);

    // Event emitted when a bounty is canceled
    event BountyCanceled(uint256 bountyId);

    /// @notice Create a new bounty
    /// @param _description Description of the bounty
    /// @param _reward Reward amount in wei
    function createBounty(string memory _description) external payable {
        require(msg.value > 0, "Reward must be greater than 0");

        // Increment the bounty counter
        bountyCounter++;

        // Create a new bounty
        bounties[bountyCounter] = Bounty({
            description: _description,
            reward: msg.value,
            creator: msg.sender,
            isActive: true,
            winner: address(0)
        });

        // Emit the BountyCreated event
        emit BountyCreated(bountyCounter, _description, msg.value, msg.sender);
    }

    /// @notice Claim a bounty
    /// @param _bountyId ID of the bounty to claim
    function claimBounty(uint256 _bountyId) external {
        Bounty storage bounty = bounties[_bountyId];

        require(bounty.isActive, "Bounty is not active");
        require(bounty.creator != msg.sender, "Creator cannot claim their own bounty");
        require(bounty.winner == address(0), "Bounty already claimed");

        // Mark the bounty as claimed
        bounty.isActive = false;
        bounty.winner = msg.sender;

        // Transfer the reward to the winner
        (bool success, ) = msg.sender.call{value: bounty.reward}("");
        require(success, "Reward transfer failed");

        // Emit the BountyClaimed event
        emit BountyClaimed(_bountyId, msg.sender);
    }

    /// @notice Cancel a bounty
    /// @param _bountyId ID of the bounty to cancel
    function cancelBounty(uint256 _bountyId) external {
        Bounty storage bounty = bounties[_bountyId];

        require(bounty.isActive, "Bounty is not active");
        require(bounty.creator == msg.sender, "Only the creator can cancel the bounty");
        require(bounty.winner == address(0), "Bounty already claimed");

        // Mark the bounty as inactive
        bounty.isActive = false;

        // Refund the reward to the creator
        (bool success, ) = msg.sender.call{value: bounty.reward}("");
        require(success, "Refund transfer failed");

        // Emit the BountyCanceled event
        emit BountyCanceled(_bountyId);
    }

    /// @notice Get details of a bounty
    /// @param _bountyId ID of the bounty
    /// @return description, reward, creator, isActive, winner
    function getBounty(uint256 _bountyId)
        external
        view
        returns (
            string memory description,
            uint256 reward,
            address creator,
            bool isActive,
            address winner
        )
    {
        Bounty storage bounty = bounties[_bountyId];
        return (bounty.description, bounty.reward, bounty.creator, bounty.isActive, bounty.winner);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
