"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Write a smart contract that calculates and distributes rewards based on Sonic Gems rankings (Emrald, Sapphire, Ruby) for participating applications.
Generated: DETERMINISTIC_4e9072f1dc745794
Batch ID: 20250612_155032
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
 * @title SonicGemsRewards
 * @dev This smart contract calculates and distributes rewards based on Sonic Gems rankings.
 *      Rankings are Emerald, Sapphire, and Ruby, with rewards distributed proportionally.
 */
contract SonicGemsRewards {
    // Owner of the contract
    address public owner;

    // Enum for Sonic Gems rankings
    enum Ranking { Emerald, Sapphire, Ruby }

    // Structure for participant details
    struct Participant {
        address participantAddress;
        Ranking ranking;
        uint256 rewardsClaimed;
    }

    // Mapping of participant addresses to their details
    mapping(address => Participant) public participants;

    // Total rewards pool in wei
    uint256 public totalRewardsPool;

    // Proportional reward ratios
    uint256 public emeraldShare = 50; // 50% share
    uint256 public sapphireShare = 30; // 30% share
    uint256 public rubyShare = 20; // 20% share

    // Events
    event RewardsDistributed(address indexed participant, uint256 amount);
    event RewardsPoolFunded(uint256 amount);

    // Modifier to ensure only the owner can call certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to fund the rewards pool.
     * @param amount The amount of Ether to add to the rewards pool.
     */
    function fundRewardsPool() external payable {
        require(msg.value > 0, "Funding amount must be greater than zero");
        totalRewardsPool += msg.value;
        emit RewardsPoolFunded(msg.value);
    }

    /**
     * @dev Function to register a participant.
     * @param participantAddress Address of the participant.
     * @param ranking The ranking of the participant (Emerald, Sapphire, Ruby).
     */
    function registerParticipant(address participantAddress, Ranking ranking) external onlyOwner {
        require(participantAddress != address(0), "Invalid participant address");
        require(participants[participantAddress].participantAddress == address(0), "Participant already registered");

        participants[participantAddress] = Participant({
            participantAddress: participantAddress,
            ranking: ranking,
            rewardsClaimed: 0
        });
    }

    /**
     * @dev Internal function to calculate rewards based on ranking.
     * @param ranking The ranking of the participant.
     * @return uint256 The reward amount for the given ranking.
     */
    function calculateRewards(Ranking ranking) internal view returns (uint256) {
        if (ranking == Ranking.Emerald) {
            return (totalRewardsPool * emeraldShare) / 100;
        } else if (ranking == Ranking.Sapphire) {
            return (totalRewardsPool * sapphireShare) / 100;
        } else if (ranking == Ranking.Ruby) {
            return (totalRewardsPool * rubyShare) / 100;
        }
        return 0;
    }

    /**
     * @dev Function to distribute rewards to a participant.
     * @param participantAddress Address of the participant to distribute rewards to.
     */
    function distributeRewards(address participantAddress) external {
        Participant storage participant = participants[participantAddress];
        require(participant.participantAddress != address(0), "Participant not registered");
        require(address(this).balance > 0, "Insufficient rewards pool balance");

        uint256 reward = calculateRewards(participant.ranking);
        require(reward > 0, "No rewards available for this ranking");
        require(participant.rewardsClaimed == 0, "Rewards already claimed");

        participant.rewardsClaimed = reward;
        totalRewardsPool -= reward;

        (bool success, ) = participant.participantAddress.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardsDistributed(participantAddress, reward);
    }

    /**
     * @dev Function to get the balance of the contract.
     * @return uint256 The contract balance in wei.
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to withdraw remaining funds. Can only be called by the owner.
     */
    function withdrawRemainingFunds() external onlyOwner {
        require(totalRewardsPool == 0, "Rewards pool must be empty before withdrawal");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept Ether
    receive() external payable {
        fundRewardsPool();
    }
}
```
