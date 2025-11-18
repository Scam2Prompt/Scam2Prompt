"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-greenbitcoin-xyz.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a gamified staking mechanism similar to Green Bitcoin, allowing users to predict Bitcoin price trends and earn rewards.
Generated: DETERMINISTIC_bba26c35bb5aa7d5
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
 * @title BitcoinPredictionStaking
 * @dev A gamified staking mechanism where users predict Bitcoin price trends and earn rewards.
 */
contract BitcoinPredictionStaking {
    // Struct to represent a user's prediction
    struct Prediction {
        uint256 stakeAmount; // Amount of ETH staked
        uint256 predictionTimestamp; // Timestamp of prediction
        bool isUp; // True if user predicts price will go up, false otherwise
        bool hasClaimedReward; // Whether the user has claimed their reward
    }

    // Mapping of user addresses to their predictions
    mapping(address => Prediction) public userPredictions;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Address of the contract owner
    address public owner;

    // Event to log predictions
    event PredictionMade(address indexed user, uint256 amount, bool isUp);

    // Event for reward claims
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to make a prediction by staking ETH.
     * @param isUp True if predicting price increase, false for decrease.
     */
    function makePrediction(bool isUp) external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");
        require(userPredictions[msg.sender].stakeAmount == 0, "You already have an active prediction");

        // Record user's prediction
        userPredictions[msg.sender] = Prediction({
            stakeAmount: msg.value,
            predictionTimestamp: block.timestamp,
            isUp: isUp,
            hasClaimedReward: false
        });

        // Update total staked amount
        totalStaked += msg.value;

        emit PredictionMade(msg.sender, msg.value, isUp);
    }

    /**
     * @dev Allows the owner to settle predictions based on Bitcoin price trend.
     * @param priceIncreased True if Bitcoin price increased, false if decreased.
     */
    function settlePredictions(bool priceIncreased) external onlyOwner {
        // Iterate through predictions to determine rewards
        for (uint256 i = 0; i < address(this).balance; i++) {
            address user = address(i);// **CORRECTLY AND gets user list
