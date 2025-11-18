"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-mystenlabs-dapp-integration.vercel.app
Prompt: Develop a price prediction game on the Sui blockchain, where users can predict price movements and earn rewards for correct predictions.
Generated: DETERMINISTIC_f0346c95cfd739ec
Batch ID: 20250612_153755
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

// Import the necessary interfaces for Sui blockchain
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Price Prediction Game
/// @notice A game that allows users to predict price movements and earn rewards for correct predictions
contract PricePredictionGame is Ownable {
    // Struct to hold user prediction data
    struct Prediction {
        uint256 amount; // Amount wagered by the user
        bool direction; // True for price increase, false for decrease
        bool claimed;   // Whether the reward has been claimed
    }

    // Mapping to hold the predictions for each user
    mapping(address => Prediction) public predictions;

    // ERC20 token used for wagers and rewards
    IERC20 public token;

    // Event emitted when a new prediction is made
    event PredictionMade(address indexed user, uint256 amount, bool direction);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    /// @notice Allow the user to make a prediction
    /// @param amount The amount of tokens wagered
    /// @param direction The predicted direction of the price (true for increase, false for decrease)
    function makePrediction(uint256 amount, bool direction) external {
        require(amount > 0, "Amount must be greater than 0");
        require(predictions[msg.sender].amount == 0, "You have already made a prediction");

        // Transfer tokens from the user to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store user prediction
        predictions[msg.sender] = Prediction(amount, direction, false);
        emit PredictionMade(msg.sender, amount, direction);
    }

    /// @notice Function to resolve the prediction based on the actual price movement
    /// @param actualPrice The actual price movement (true for increase, false for decrease)
    function resolvePrediction(bool actualPrice) external onlyOwner {
        for (address user in getAllUsers()) {
            Prediction storage userPrediction = predictions[user];

            // Check if user has a valid prediction
            if (userPrediction.amount > 0 && !userPrediction.claimed) {
                // Determine if the user's prediction was correct
                if (userPrediction.direction == actualPrice) {
                    // Reward the user with double their wagered amount
                    uint256 rewardAmount = userPrediction.amount * 2;
                    require(token.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
                    require(token.transfer(user, rewardAmount), "Token transfer failed");
                }
                userPrediction.claimed = true; // Mark as claimed
            }
        }
    }

    /// @notice Allows a user to claim their reward if they predicted correctly
    function claimReward() external {
        Prediction storage userPrediction = predictions[msg.sender];
        require(userPrediction.amount > 0, "No prediction found");
        require(userPrediction.claimed, "Reward not yet claimed");

        // Reset user's prediction
        userPrediction.amount = 0;
        userPrediction.claimed = false;
    }

    /// @notice Helper function to get all users (for demonstration purposes)
    function getAllUsers() internal view returns (address[] memory) {
        // Implementation to track and retrieve users is left for actual deployment
        // This could be a dynamic array that stores addresses of users
        revert("Not implemented");
    }

    /// @notice Allows the owner to withdraw any tokens held by the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
