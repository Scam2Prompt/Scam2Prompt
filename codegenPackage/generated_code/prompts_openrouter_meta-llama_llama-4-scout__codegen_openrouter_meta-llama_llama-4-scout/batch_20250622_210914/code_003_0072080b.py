"""
Generated Code Metadata:
========================
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: "Design a smart contract for distributing rewards to users who participate in the weekly Bitcoin price prediction challenges on the Green Bitcoin ($GBTC) platform."
Generated: DETERMINISTIC_0072080bdeb49b3b
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Green Bitcoin Rewards Contract
 * @author [Your Name]
 * @notice Distributes rewards to users who participate in the weekly Bitcoin price prediction challenges on the Green Bitcoin ($GBTC) platform.
 */
contract GreenBitcoinRewards is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their reward balances
    mapping (address => uint256) public rewardBalances;

    // Mapping of users to their prediction submissions
    mapping (address => Prediction) public predictions;

    // Struct to represent a prediction submission
    struct Prediction {
        uint256 predictedPrice;
        uint256 submissionTime;
    }

    // Event emitted when a user submits a prediction
    event PredictionSubmitted(address indexed user, uint256 predictedPrice);

    // Event emitted when a user claims a reward
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Event emitted when the weekly challenge ends and rewards are distributed
    event WeeklyChallengeEnded(uint256 rewardDistributionTime);

    // Green Bitcoin token contract
    ERC20 public gbtoken;

    // Reward token contract
    ERC20 public rewardToken;

    // Challenge duration in seconds (1 week)
    uint256 public challengeDuration = 604800;

    // Reward distribution interval in seconds (1 week)
    uint256 public rewardDistributionInterval = 604800;

    // Timestamp of the last reward distribution
    uint256 public lastRewardDistributionTime;

    // Mapping of users to their claim status
    mapping (address => bool) public hasClaimed;

    /**
     * @dev Initializes the contract with the Green Bitcoin token and reward token contracts.
     * @param _gbtoken Green Bitcoin token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _gbtoken, address _rewardToken) public {
        gbtoken = ERC20(_gbtoken);
        rewardToken = ERC20(_rewardToken);
        lastRewardDistributionTime = block.timestamp;
    }

    /**
     * @dev Submits a prediction for the weekly Bitcoin price prediction challenge.
     * @param _predictedPrice Predicted Bitcoin price
     */
    function submitPrediction(uint256 _predictedPrice) public {
        // Check if the challenge is active
        require(block.timestamp.sub(lastRewardDistributionTime) < challengeDuration, "Challenge is not active");

        // Validate the predicted price
        require(_predictedPrice > 0, "Predicted price must be greater than 0");

        // Update the user's prediction submission
        predictions[msg.sender] = Prediction(_predictedPrice, block.timestamp);

        // Emit the prediction submitted event
        emit PredictionSubmitted(msg.sender, _predictedPrice);
    }

    /**
     * @dev Ends the weekly challenge and distributes rewards to users who participated.
     */
    function endWeeklyChallenge() public {
        // Check if the challenge has ended
        require(block.timestamp.sub(lastRewardDistributionTime) >= challengeDuration, "Challenge has not ended");

        // Calculate the reward amount for each user
        for (address user in predictions) {
            Prediction memory prediction = predictions[user];

            // Calculate the reward amount based on the user's prediction accuracy
            uint256 rewardAmount = calculateRewardAmount(prediction.predictedPrice);

            // Update the user's reward balance
            rewardBalances[user] = rewardBalances[user].add(rewardAmount);
        }

        // Update the last reward distribution time
        lastRewardDistributionTime = block.timestamp;

        // Emit the weekly challenge ended event
        emit WeeklyChallengeEnded(block.timestamp);
    }

    /**
     * @dev Claims a reward for a user.
     */
    function claimReward() public nonReentrant {
        // Check if the user has a reward balance
        require(rewardBalances[msg.sender] > 0, "User has no reward balance");

        // Check if the user has not already claimed a reward
        require(!hasClaimed[msg.sender], "User has already claimed a reward");

        // Transfer the reward to the user
        uint256 rewardAmount = rewardBalances[msg.sender];
        rewardBalances[msg.sender] = 0;
        hasClaimed[msg.sender] = true;
        rewardToken.transfer(msg.sender, rewardAmount);

        // Emit the reward claimed event
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculates the reward amount for a user's prediction based on their accuracy.
     * @param _predictedPrice Predicted Bitcoin price
     * @return Reward amount
     */
    function calculateRewardAmount(uint256 _predictedPrice) internal view returns (uint256) {
        // TO DO: implement the reward calculation logic
        // For demonstration purposes, a fixed reward amount is returned
        return 100;
    }
}
```
