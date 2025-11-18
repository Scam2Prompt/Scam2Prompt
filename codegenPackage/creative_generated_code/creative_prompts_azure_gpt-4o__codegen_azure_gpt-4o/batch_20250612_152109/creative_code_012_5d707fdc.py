"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Develop a Solidity contract for a token giveaway competition, including features for tracking participants and distributing rewards, as outlined in the Scorpion Casino pre-sale benefits.
Generated: DETERMINISTIC_5d707fdc0cad9d4a
Batch ID: 20250612_152109
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
 * @title TokenGiveawayCompetition
 * @dev A smart contract to manage a token giveaway competition.
 * Participants can register, and rewards are distributed to winners.
 */
contract TokenGiveawayCompetition {
    // State Variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the token being distributed
    uint256 public rewardAmount; // Reward amount per winner
    uint256 public maxParticipants; // Maximum allowed participants
    bool public isCompetitionActive; // Whether the competition is active

    mapping(address => bool) public participants; // Tracks registered participants
    address[] public participantList; // List of all participant addresses

    // Events
    event ParticipantRegistered(address indexed participant);
    event RewardsDistributed(address indexed winner, uint256 rewardAmount);
    event CompetitionStatusUpdated(bool isActive);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    modifier competitionActive() {
        require(isCompetitionActive, "The competition is not active.");
        _;
    }

    modifier maxParticipantsNotReached() {
        require(participantList.length < maxParticipants, "Maximum participants reached.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the token being distributed.
     * @param _rewardAmount Reward amount per winner.
     * @param _maxParticipants Maximum allowed participants.
     */
    constructor(address _tokenAddress, uint256 _rewardAmount, uint256 _maxParticipants) {
        require(_tokenAddress != address(0), "Invalid token address.");
        require(_rewardAmount > 0, "Reward amount must be greater than zero.");
        require(_maxParticipants > 0, "Maximum participants must be greater than zero.");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        rewardAmount = _rewardAmount;
        maxParticipants = _maxParticipants;
        isCompetitionActive = false; // Competition starts inactive
    }

    /**
     * @dev Toggle the competition status (Active/Inactive).
     */
    function toggleCompetitionStatus() external onlyOwner {
        isCompetitionActive = !isCompetitionActive;
        emit CompetitionStatusUpdated(isCompetitionActive);
    }

    /**
     * @dev Register as a participant in the giveaway competition.
     */
    function registerParticipant() external competitionActive maxParticipantsNotReached {
        require(!participants[msg.sender], "You have already registered.");
        participants[msg.sender] = true;
        participantList.push(msg.sender);

        emit ParticipantRegistered(msg.sender);
    }

    /**
     * @dev Distribute rewards to the winners. Only callable by the owner.
     * @param winners Array of winner addresses.
     */
    function distributeRewards(address[] calldata winners) external onlyOwner competitionActive {
        require(winners.length > 0, "Winners list cannot be empty.");
        for (uint256 i = 0; i < winners.length; i++) {
            address winner = winners[i];
            require(participants[winner], "Winner is not a registered participant.");

            // Transfer tokens to the winner
            (bool success,) = tokenAddress.call(
                abi.encodeWithSignature("transfer(address,uint256)", winner, rewardAmount)
            );
            require(success, "Token transfer failed.");

            emit RewardsDistributed(winner, rewardAmount);
        }
    }

    /**
     * @dev Get list of all registered participants.
     * @return Array of participant addresses.
     */
    function getParticipants() external view returns (address[] memory) {
        return participantList;
    }

    /**
     * @dev Fallback function to prevent accidental ether transfer.
     */
    fallback() external payable {
        revert("Ether transfers not allowed.");
    }

    receive() external payable {
        revert("Ether transfers not allowed.");
    }
}
```
