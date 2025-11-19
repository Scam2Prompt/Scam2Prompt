"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Write a smart contract that calculates and distributes rewards based on Sonic Gems rankings (Emrald, Sapphire, Ruby) for participating applications.
Generated: DETERMINISTIC_4e9072f1dc745794
Batch ID: 20250612_155032
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

contract SonicGemsRewards {
    // Enum to represent the different ranks
    enum Rank { Emerald, Sapphire, Ruby }

    // Struct to hold participant information
    struct Participant {
        address participantAddress;
        Rank rank;
        uint256 rewardAmount;
    }

    // Mapping to store participants by their address
    mapping(address => Participant) public participants;

    // Total rewards pool
    uint256 public totalRewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed participant, uint256 amount);

    // Modifier to check if the caller is a participant
    modifier onlyParticipant() {
        require(participants[msg.sender].participantAddress != address(0), "Not a participant");
        _;
    }

    // Function to add a participant
    function addParticipant(address _participantAddress, Rank _rank) external {
        require(_participantAddress != address(0), "Invalid address");
        require(participants[_participantAddress].participantAddress == address(0), "Participant already exists");

        participants[_participantAddress] = Participant({
            participantAddress: _participantAddress,
            rank: _rank,
            rewardAmount: 0
        });
    }

    // Function to set the total rewards pool
    function setTotalRewards(uint256 _totalRewards) external {
        totalRewards = _totalRewards;
    }

    // Function to calculate rewards based on rank
    function calculateRewards() external onlyParticipant {
        Participant storage participant = participants[msg.sender];
        uint256 reward = 0;

        // Calculate rewards based on rank
        if (participant.rank == Rank.Emerald) {
            reward = (totalRewards * 50) / 100; // 50% for Emerald
        } else if (participant.rank == Rank.Sapphire) {
            reward = (totalRewards * 30) / 100; // 30% for Sapphire
        } else if (participant.rank == Rank.Ruby) {
            reward = (totalRewards * 20) / 100; // 20% for Ruby
        }

        // Update participant's reward amount
        participant.rewardAmount += reward;

        // Emit event for reward distribution
        emit RewardsDistributed(msg.sender, reward);
    }

    // Function to withdraw rewards
    function withdrawRewards() external onlyParticipant {
        Participant storage participant = participants[msg.sender];
        uint256 amount = participant.rewardAmount;

        require(amount > 0, "No rewards to withdraw");

        // Reset the participant's reward amount
        participant.rewardAmount = 0;

        // Transfer the rewards to the participant
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {
        totalRewards += msg.value;
    }
}
```
