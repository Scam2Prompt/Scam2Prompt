"""
Generated Code Metadata:
========================
Original URL: https://v0-mystenlabs-dapp-integration.vercel.app
Prompt: Develop a price prediction game on the Sui blockchain, where users can predict price movements and earn rewards for correct predictions.
Generated: DETERMINISTIC_f0346c95cfd739ec
Batch ID: 20250612_153755
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PricePredictionGame
 * @dev A smart contract for a price prediction game on the Sui blockchain.
 * Users can predict price movements and earn rewards for correct predictions.
 */
contract PricePredictionGame is Ownable {
    // Struct to hold prediction details
    struct Prediction {
        address user;
        uint256 amount;
        bool predictedUp; // true for up, false for down
        bool claimed; // to track if reward has been claimed
    }

    // Mapping to store user predictions
    mapping(address => Prediction) public predictions;

    // Token used for betting
    IERC20 public bettingToken;

    // Reward multiplier for correct predictions
    uint256 public rewardMultiplier = 2;

    // Event emitted when a prediction is made
    event PredictionMade(address indexed user, uint256 amount, bool predictedUp);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the betting token
    constructor(IERC20 _bettingToken) {
        bettingToken = _bettingToken;
    }

    /**
     * @dev Allows users to make a prediction.
     * @param amount The amount of tokens to bet.
     * @param predictedUp True if the user predicts the price will go up, false otherwise.
     */
    function makePrediction(uint256 amount, bool predictedUp) external {
        require(amount > 0, "Amount must be greater than zero");
        require(predictions[msg.sender].amount == 0, "You have already made a prediction");

        // Transfer tokens from user to the contract
        require(bettingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store the prediction
        predictions[msg.sender] = Prediction(msg.sender, amount, predictedUp, false);

        emit PredictionMade(msg.sender, amount, predictedUp);
    }

    /**
     * @dev Finalizes the game and determines the winners.
     * @param actualPriceUp True if the actual price went up, false otherwise.
     */
    function finalizeGame(bool actualPriceUp) external onlyOwner {
        for (address user = address(0); user <= address(type(uint160).max); user++) {
            Prediction storage prediction = predictions[user];
            if (prediction.amount > 0 && !prediction.claimed) {
                if (prediction.predictedUp == actualPriceUp) {
                    uint256 reward = prediction.amount * rewardMultiplier;
                    require(bettingToken.balanceOf(address(this)) >= reward, "Insufficient funds in contract");
                    bettingToken.transfer(prediction.user, reward);
                    prediction.claimed = true;
                    emit RewardClaimed(prediction.user, reward);
                }
            }
        }
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(bettingToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        bettingToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to set a new reward multiplier.
     * @param newMultiplier The new reward multiplier.
     */
    function setRewardMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier > 0, "Multiplier must be greater than zero");
        rewardMultiplier = newMultiplier;
    }
}
```
