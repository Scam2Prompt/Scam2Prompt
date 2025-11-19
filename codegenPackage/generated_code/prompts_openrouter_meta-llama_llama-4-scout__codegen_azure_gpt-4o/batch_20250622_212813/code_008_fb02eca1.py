"""
Generated Code Metadata:
========================
Original URL: https://stailoud.io
Prompt: "Outline a smart contract for distributing SOL rewards based on Loud's weekly SOL distribution mechanics."
Generated: DETERMINISTIC_fb02eca1ed619bfe
Batch ID: 20250622_212813
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

/**
 * @title SOLRewardDistributor
 * @dev A smart contract for distributing SOL rewards based on Loud's weekly distribution mechanics.
 */
contract SOLRewardDistributor {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalRewards; // Total SOL rewards available for distribution
    uint256 public distributionPeriod; // Weekly distribution period in seconds
    uint256 public lastDistributionTimestamp; // Timestamp of the last distribution

    mapping(address => uint256) public userRewards; // Mapping to store user rewards
    address[] public participants; // List of participants eligible for rewards

    // Events
    event RewardsDistributed(uint256 totalDistributed, uint256 timestamp);
    event ParticipantAdded(address participant);
    event ParticipantRemoved(address participant);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier distributionReady() {
        require(
            block.timestamp >= lastDistributionTimestamp + distributionPeriod,
            "Distribution period has not yet elapsed"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _distributionPeriod Weekly distribution period in seconds.
     */
    constructor(uint256 _distributionPeriod) {
        owner = msg.sender;
        distributionPeriod = _distributionPeriod;
        lastDistributionTimestamp = block.timestamp;
    }

    /**
     * @dev Function to add a participant to the reward pool.
     * @param _participant Address of the participant.
     */
    function addParticipant(address _participant) external onlyOwner {
        require(_participant != address(0), "Invalid participant address");
        participants.push(_participant);
        emit ParticipantAdded(_participant);
    }

    /**
     * @dev Function to remove a participant from the reward pool.
     * @param _participant Address of the participant.
     */
    function removeParticipant(address _participant) external onlyOwner {
        require(_participant != address(0), "Invalid participant address");

        for (uint256 i = 0; i < participants.length; i++) {
            if (participants[i] == _participant) {
                participants[i] = participants[participants.length - 1];
                participants.pop();
                emit ParticipantRemoved(_participant);
                return;
            }
        }

        revert("Participant not found");
    }

    /**
     * @dev Function to deposit SOL rewards into the contract.
     */
    function depositRewards() external payable {
        require(msg.value > 0, "Must deposit a positive amount of SOL");
        totalRewards += msg.value;
    }

    /**
     * @dev Function to distribute rewards to participants.
     * This function can only be called after the distribution period has elapsed.
     */
    function distributeRewards() external onlyOwner distributionReady {
        require(participants.length > 0, "No participants to distribute rewards to");
        require(totalRewards > 0, "No rewards available for distribution");

        uint256 rewardPerParticipant = totalRewards / participants.length;

        for (uint256 i = 0; i < participants.length; i++) {
            userRewards[participants[i]] += rewardPerParticipant;
        }

        totalRewards = 0; // Reset total rewards after distribution
        lastDistributionTimestamp = block.timestamp; // Update the last distribution timestamp

        emit RewardsDistributed(rewardPerParticipant * participants.length, block.timestamp);
    }

    /**
     * @dev Function for participants to withdraw their rewards.
     */
    function withdrawRewards() external {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards available for withdrawal");

        userRewards[msg.sender] = 0; // Reset user rewards before transfer
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @dev Function to get the list of participants.
     * @return List of participant addresses.
     */
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }

    /**
     * @dev Fallback function to accept SOL deposits.
     */
    receive() external payable {
        totalRewards += msg.value;
    }
}
```
