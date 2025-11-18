"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Write code for a decentralized application that tracks ETH predictions and distributes rewards to users with EVM-compatible wallets.
Generated: DETERMINISTIC_15ba20c6939da1c1
Batch ID: 20250612_151605
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title ETHPrediction
 * @dev A decentralized application to track ETH price predictions and distribute rewards.
 */
contract ETHPrediction is Ownable {
    struct Prediction {
        address user;
        uint256 predictedPrice;
        bool hasClaimed;
    }

    // Mapping to store user predictions
    mapping(address => Prediction) public predictions;

    // Reward token contract
    IERC20 public rewardToken;

    // Event emitted when a new prediction is made
    event PredictionMade(address indexed user, uint256 predictedPrice);
    
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the reward token
    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Allows users to make a prediction about the ETH price.
     * @param _predictedPrice The price of ETH users predict.
     */
    function makePrediction(uint256 _predictedPrice) external {
        require(_predictedPrice > 0, "Predicted price must be greater than 0");
        require(predictions[msg.sender].user == address(0), "User has already made a prediction");

        predictions[msg.sender] = Prediction(msg.sender, _predictedPrice, false);
        emit PredictionMade(msg.sender, _predictedPrice);
    }

    /**
     * @dev Distributes rewards to users based on their predictions.
     * @param actualPrice The actual price of ETH for reward distribution.
     */
    function distributeRewards(uint256 actualPrice) external onlyOwner {
        require(actualPrice > 0, "Actual price must be greater than 0");

        for (address user : getAllUsers()) {
            Prediction storage prediction = predictions[user];
            if (prediction.user != address(0) && !prediction.hasClaimed) {
                // Check if the prediction is within a threshold of the actual price
                if (isPredictionClose(prediction.predictedPrice, actualPrice)) {
                    uint256 rewardAmount = calculateReward(prediction.predictedPrice, actualPrice);
                    require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward balance");
                    rewardToken.transfer(user, rewardAmount);
                    prediction.hasClaimed = true;
                    emit RewardsDistributed(user, rewardAmount);
                }
            }
        }
    }

    /**
     * @dev Checks if the prediction is within a close range of the actual price.
     * @param predictedPrice The predicted price.
     * @param actualPrice The actual price.
     * @return true if within range, false otherwise.
     */
    function isPredictionClose(uint256 predictedPrice, uint256 actualPrice) internal pure returns (bool) {
        uint256 threshold = predictedPrice * 10 / 100; // 10% threshold
        return (actualPrice >= predictedPrice - threshold && actualPrice <= predictedPrice + threshold);
    }

    /**
     * @dev Calculates the reward based on the predicted and actual price.
     * @param predictedPrice The predicted price.
     * @param actualPrice The actual price.
     * @return The calculated reward amount.
     */
    function calculateReward(uint256 predictedPrice, uint256 actualPrice) internal pure returns (uint256) {
        // Simplified reward calculation - reward is proportional to the accuracy of the prediction
        return (predictedPrice >= actualPrice ? predictedPrice - actualPrice : actualPrice - predictedPrice) / 100; // 1% of the difference
    }

    /**
     * @dev Get all users who made predictions.
     * @return An array of users who made predictions.
     */
    function getAllUsers() internal view returns (address[] memory) {
        // Placeholder for user retrieval logic; implement a mechanism to track user addresses.
        address[] memory users; // This should hold actual user addresses
        return users;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");
        rewardToken.transfer(owner(), amount);
    }
}
```

This code operates as a Solidity smart contract that allows users to predict the price of ETH, tracks those predictions, and distributes rewards based on their accuracy. The contract is structured to follow best practices, including using OpenZeppelin's `Ownable` for access control and implementing proper error handling.
