"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Write a smart contract to enable staking phase competitions, inspired by the "Battle of Stakes" event described on the MultiversX site.
Generated: DETERMINISTIC_821a24d2cfb25837
Batch ID: 20250612_153400
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
 * @title BattleOfStakes
 * @dev A smart contract to enable staking phase competitions inspired by the "Battle of Stakes" event.
 * Users can participate in staking competitions and track their contributions.
 */
contract BattleOfStakes {
    // Data structure to represent a participant in the staking competition
    struct Participant {
        uint256 stakedAmount; // Total amount staked by the participant
        uint256 lastStakeTime; // Timestamp of the last stake
    }

    // Mapping to track participants and their staking data
    mapping(address => Participant) public participants;

    // Event emitted when a user stakes funds
    event Staked(address indexed participant, uint256 amount, uint256 timestamp);

    // Event emitted when staking is finalized
    event CompetitionFinalized(address indexed winner, uint256 winningAmount);

    // Variables for competition management
    address public owner; // Contract owner
    uint256 public competitionEndTime; // Timestamp when the competition ends
    bool public isCompetitionFinalized; // Flag to indicate if the competition has been finalized

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure the competition is active
    modifier competitionActive() {
        require(block.timestamp <= competitionEndTime, "Competition has ended");
        require(!isCompetitionFinalized, "Competition has already been finalized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _duration Duration of the competition in seconds.
     */
    constructor(uint256 _duration) {
        require(_duration > 0, "Duration must be greater than 0");

        owner = msg.sender;
        competitionEndTime = block.timestamp + _duration;
        isCompetitionFinalized = false;
    }

    /**
     * @dev Function to allow users to stake Ether into the competition.
     */
    function stake() external payable competitionActive {
        require(msg.value > 0, "Stake amount must be greater than 0");

        // Update participant's staking data
        participants[msg.sender].stakedAmount += msg.value;
        participants[msg.sender].lastStakeTime = block.timestamp;

        // Emit the staking event
        emit Staked(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function to finalize the competition and determine the winner.
     * Can only be called by the owner after the competition has ended.
     */
    function finalizeCompetition() external onlyOwner {
        require(block.timestamp > competitionEndTime, "Competition has not ended yet");
        require(!isCompetitionFinalized, "Competition has already been finalized");

        address winner;
        uint256 maxStake = 0;

        // Iterate through participants to find the winner with the highest staked amount
        for (uint256 i = 0; i < address(this).balance; i++) {
            if (participants[msg.sender].stakedAmount > maxStake) {
                maxStake = participants[msg.sender].stakedAmount;
                winner = msg.sender;
            }
        }

        isCompetitionFinalized = true;

        // Emit the finalized event
        emit CompetitionFinalized(winner, maxStake);
    }

    /**
     * @dev Function to withdraw any leftover funds (if needed).
     * Can only be called by the owner after the competition is finalized.
     */
    function withdrawFunds() external onlyOwner {
        require(isCompetitionFinalized, "Competition must be finalized first");

        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
