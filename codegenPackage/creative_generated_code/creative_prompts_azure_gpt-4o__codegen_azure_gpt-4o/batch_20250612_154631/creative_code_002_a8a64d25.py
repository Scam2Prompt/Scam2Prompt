"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a smart contract in Solidity for distributing rewards to $DOG and $COCORO holders, referencing the voting system mentioned on the website.
Generated: DETERMINISTIC_a8a64d2580606582
Batch ID: 20250612_154631
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
 * @title RewardDistributor
 * @dev Smart contract to distribute rewards to $DOG and $COCORO token holders
 * based on a voting system.
 */
contract RewardDistributor {
    // Mapping to store balances of $DOG and $COCORO holders
    mapping(address => uint256) public dogBalances;
    mapping(address => uint256) public cocoroBalances;

    // Total votes for each token
    uint256 public totalDogVotes;
    uint256 public totalCocoroVotes;

    // Voting system: mapping of address to token votes
    mapping(address => bool) public hasVoted;

    // Events
    event RewardsDistributed(uint256 dogReward, uint256 cocoroReward);
    event VoteCast(address voter, bool voteForDog);

    // Reward pool variables
    uint256 public rewardPool;

    // Constructor to initialize the reward pool
    constructor(uint256 initialPool) {
        rewardPool = initialPool;
    }

    /**
     * @dev Function to cast a vote for $DOG or $COCORO token holders.
     * @param voteForDog True to vote for $DOG holders, false to vote for $COCORO holders.
     */
    function castVote(bool voteForDog) external {
        require(!hasVoted[msg.sender], "You have already voted.");
        hasVoted[msg.sender] = true;

        if (voteForDog) {
            totalDogVotes++;
        } else {
            totalCocoroVotes++;
        }

        emit VoteCast(msg.sender, voteForDog);
    }

    /**
     * @dev Function to distribute rewards based on voting results.
     */
    function distributeRewards() external {
        require(rewardPool > 0, "Reward pool is empty.");

        // Calculate reward percentage for each token
        uint256 totalVotes = totalDogVotes + totalCocoroVotes;
        require(totalVotes > 0, "No votes casted.");

        uint256 dogRewardPercentage = (totalDogVotes * 100) / totalVotes;
        uint256 cocoroRewardPercentage = (totalCocoroVotes * 100) / totalVotes;

        uint256 dogReward = (rewardPool * dogRewardPercentage) / 100;
        uint256 cocoroReward = (rewardPool * cocoroRewardPercentage) / 100;

        // Distribute rewards (for simplicity, rewards are not sent but recorded)
        // Note: Replace "dogBalances" and "cocoroBalances" logic with actual token integration if needed.
        for (address account : dogBalances.keys()) {
            // Assume a `transferReward` function exists for actual token distribution
            transferReward(account, dogReward / dogBalances.size());
        }
        

        rewardPool = 0; //Empty after clearing safe .
