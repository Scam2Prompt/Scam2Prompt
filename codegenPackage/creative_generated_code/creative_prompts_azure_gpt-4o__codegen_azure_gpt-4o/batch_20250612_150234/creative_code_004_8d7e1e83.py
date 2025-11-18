"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dapps.pages.dev
Prompt: Develop a smart contract to calculate rewards for $GBTC token holders based on their staking duration and accuracy in Bitcoin price predictions.
Generated: DETERMINISTIC_8d7e1e83951438c6
Batch ID: 20250612_150234
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
 * @title GBTCRewardContract
 * @dev A smart contract to calculate rewards for $GBTC token holders based on staking duration
 *      and accuracy in Bitcoin price predictions.
 */
contract GBTCRewardContract {
    // Events
    event Stake(address indexed user, uint256 amount, uint256 timestamp);
    event Predict(address indexed user, uint256 predictedPrice, uint256 timestamp);
    event ClaimReward(address indexed user, uint256 rewardAmount);

    // Struct to represent a user's staking information.
    struct StakeInfo {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Timestamp of when staking started
    }

    // Struct to represent a user's prediction information.
    struct PredictionInfo {
        uint256 predictedPrice; // Bitcoin price predicted by the user
        uint256 timestamp;      // Timestamp of the prediction
    }

    // Mapping to store staking information for each user
    mapping(address => StakeInfo) public stakes;

    // Mapping to store prediction information for each user
    mapping(address => PredictionInfo) public predictions;

    // Bitcoin price feed (mocked for simplicity; use Chainlink in production)
    uint256 public currentBitcoinPrice;

    // Admin address
    address public admin;

    // Reward multiplier (adjustable by admin)
    uint256 public rewardMultiplier = 1 ether; // 1 ether, can be adjusted

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the admin.
     */
    constructor() {
        admin = msg.sender; // Set deployer as admin
    }

    /**
     * @dev Allows users to stake $GBTC tokens.
     * @param amount Amount of tokens to be staked.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        stakes[msg.sender] = StakeInfo(amount, block.timestamp);

        emit Stake(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Allows users to predict Bitcoin price.
     * @param predictedPrice Predicted Bitcoin price in USD.
     */
    function predict(uint256 predictedPrice) external {
        require(predictedPrice > 0, "Predicted price must be greater than zero");

        predictions[msg.sender] = PredictionInfo(predictedPrice, block.timestamp);

        emit Predict(msg.sender, predictedPrice, block.timestamp);
    }

    /**
     * @dev Allows admin to update the current Bitcoin price.
     * @param price Current Bitcoin price in USD.
     */
    function updateBitcoinPrice(uint256 price) external onlyAdmin {
        require(price > 0, "Price must be greater than zero");

        currentBitcoinPrice = price;
    }

    /**
     * @dev Calculates the reward for a given user based on staking duration and price prediction accuracy.
     * @return Reward amount in $GBTC tokens.
     */
    function calculateReward(address user) public view returns (uint256) {
        StakeInfo memory stakeInfo = stakes[user];
        PredictionInfo memory predictionInfo = predictions[user];

        require(stakeInfo.amount > 0, "User must have staked tokens");

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;

        // Calculate prediction accuracy (difference between current price and predicted price)
        uint256 priceDifference = currentBitcoinPrice > predictionInfo.predictedPrice
            ? currentBitcoinPrice - predictionInfo.predictedPrice
            : predictionInfo.predictedPrice - currentBitcoinPrice;

        // Reward formula: Stake amount * reward multiplier / (price difference + 1) * (staking duration in days)
        uint256 reward = (stakeInfo.amount * rewardMultiplier) /
            (priceDifference + 1) *
            (stakingDuration / 1 days);

        return reward;
    }

    /**
     * @dev Allows users to claim their reward.
     */
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No reward available");

        // For production: Transfer tokens to user (mocked here)
        // Example: GBTC.transfer(msg.sender, reward);

        emit ClaimReward(msg.sender, reward);
    }

    /**
     * @dev Allows admin to update the reward multiplier.
     * @param multiplier New reward multiplier value.
     */
    function updateRewardMultiplier(uint256 multiplier) external onlyAdmin {
        require(multiplier > 0, "Multiplier must be greater than zero");
        rewardMultiplier = multiplier;
    }
}
```
