"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: Generate a Solidity smart contract for implementing a gamified staking mechanism similar to Green Bitcoin's "Predict-To-Earn" model, where users can predict Bitcoin price trends and earn rewards based on their accuracy.
Generated: DETERMINISTIC_b7cc8a80c72afc7d
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
 * @title PredictToEarn
 * @dev A gamified staking mechanism where users predict Bitcoin price trends and earn rewards based on their accuracy.
 * Users stake ETH, make predictions, and receive rewards proportional to their prediction accuracy.
 */
contract PredictToEarn {
    // Struct for user predictions
    struct Prediction {
        uint256 predictedPrice; // User's predicted Bitcoin price
        uint256 stakeAmount;    // Amount staked by the user in ETH
        bool isClaimed;         // Whether the reward has been claimed
    }

    // Struct for prediction rounds
    struct Round {
        uint256 actualPrice;        // Actual Bitcoin price for the round
        uint256 rewardPool;         // Total ETH reward pool for the round
        bool isCompleted;           // Whether the round has been resolved
        uint256 totalStakeAmount;   // Total ETH staked by all users in the round
    }

    // Mapping of prediction rounds
    mapping(uint256 => Round) public rounds;

    // Mapping of user predictions for each round
    mapping(uint256 => mapping(address => Prediction)) public userPredictions;

    // Current round ID
    uint256 public currentRoundId;

    // Owner of the contract
    address public owner;

    // Events
    event PredictionMade(address indexed user, uint256 roundId, uint256 predictedPrice, uint256 stakeAmount);
    event RoundCompleted(uint256 roundId, uint256 actualPrice);
    event RewardClaimed(address indexed user, uint256 roundId, uint256 rewardAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to make a prediction and stake ETH for the current round.
     * @param predictedPrice The predicted Bitcoin price.
     */
    function makePrediction(uint256 predictedPrice) external payable {
        require(msg.value > 0, "Stake amount must be greater than 0");

        Prediction storage prediction = userPredictions[currentRoundId][msg.sender];
        require(prediction.stakeAmount == 0, "Prediction already made for this round");

        // Save the user's prediction
        prediction.predictedPrice = predictedPrice;
        prediction.stakeAmount = msg.value;
        prediction.isClaimed = false;

        // Update round's total stake amount
        rounds[currentRoundId].totalStakeAmount += msg.value;

        emit PredictionMade(msg.sender, currentRoundId, predictedPrice, msg.value);
    }

    /**
     * @dev Completes the current round and sets the actual Bitcoin price.
     * @param actualPrice The actual Bitcoin price for the round.
     */
    function completeRound(uint256 actualPrice) external onlyOwner {
        Round storage round = rounds[currentRoundId];
        require(!round.isCompleted, "Round already completed");

        // Set the actual price and mark the round as completed
        round.actualPrice = actualPrice;
        round.rewardPool = round.totalStakeAmount;
        round.isCompleted = true;

        emit RoundCompleted(currentRoundId, actualPrice);

        // Move to the next round
        currentRoundId++;
    }

    /**
     * @dev Allows users to claim rewards for a completed round based on their prediction accuracy.
     * @param roundId The round ID for which to claim rewards.
     */
    function claimReward(uint256 roundId) external {
        Round storage round = rounds[roundId];
        require(round.isCompleted, "Round not completed yet");

        Prediction storage prediction = userPredictions[roundId][msg.sender];
        require(prediction.stakeAmount > 0, "No prediction made for this round");
        require(!prediction.isClaimed, "Reward already claimed");

        // Calculate prediction accuracy (absolute difference)
        uint256 accuracy = round.actualPrice > prediction.predictedPrice
            ? round.actualPrice - prediction.predictedPrice
            : prediction.predictedPrice - round.actualPrice;

        // Calculate reward based on accuracy (lower difference = higher reward)
        uint256 reward = (round.rewardPool * prediction.stakeAmount) / round.totalStakeAmount;

        // Mark reward as claimed
        prediction.isClaimed = true;

        // Transfer reward to the user
        (bool sent, ) = msg.sender.call{value: reward}();
        require(sent, "Failed to send reward");

        emit RewardClaimed(msg.sender, roundId, reward);
    }

    /**
     * @dev Allows the contract owner to withdraw any remaining ETH in the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool sent, ) = owner.call{value: balance}();
        require(sent, "Failed to send funds");
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Getter for retrieving the current round details
    function getCurrentRound() external view returns (Round memory) {
        return rounds[currentRoundId];
    }
}
```
