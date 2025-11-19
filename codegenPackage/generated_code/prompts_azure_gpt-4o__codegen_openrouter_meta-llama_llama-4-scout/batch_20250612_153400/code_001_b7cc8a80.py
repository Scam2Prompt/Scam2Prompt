"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: Generate a Solidity smart contract for implementing a gamified staking mechanism similar to Green Bitcoin's "Predict-To-Earn" model, where users can predict Bitcoin price trends and earn rewards based on their accuracy.
Generated: DETERMINISTIC_b7cc8a80c72afc7d
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title PredictToEarn Contract
 * @author [Your Name]
 * @notice A gamified staking mechanism for predicting Bitcoin price trends.
 */
contract PredictToEarn is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of users to their predictions
    mapping(address => Prediction) public userPredictions;

    // Mapping of users to their stakes
    mapping(address => uint256) public userStakes;

    // Mapping of prediction outcomes
    mapping(uint256) public predictionOutcomes;

    // Event emitted when a user makes a prediction
    event PredictionMade(address indexed user, uint256 prediction);

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a prediction is resolved
    event PredictionResolved(uint256 prediction, bool outcome);

    // Event emitted when a user claims a reward
    event RewardClaimed(address indexed user, uint256 amount);

    // Structure for user predictions
    struct Prediction {
        uint256 prediction; // 0 for decrease, 1 for increase
        uint256 timestamp;
    }

    // Structure for prediction outcomes
    struct Outcome {
        bool outcome; // 0 for decrease, 1 for increase
        uint256 reward;
    }

    // Token contract instance
    IERC20 public token;

    // Reward token contract instance
    IERC20 public rewardToken;

    // Bitcoin price feed contract instance
    IBitcoinPriceFeed public bitcoinPriceFeed;

    // Prediction duration in seconds
    uint256 public predictionDuration;

    // Reward amount for correct predictions
    uint256 public rewardAmount;

    // Minimum stake amount
    uint256 public minStakeAmount;

    // Maximum stake amount
    uint256 public maxStakeAmount;

    /**
     * @notice Constructor for PredictToEarn contract.
     * @param _token Token contract address.
     * @param _rewardToken Reward token contract address.
     * @param _bitcoinPriceFeed Bitcoin price feed contract address.
     * @param _predictionDuration Prediction duration in seconds.
     * @param _rewardAmount Reward amount for correct predictions.
     * @param _minStakeAmount Minimum stake amount.
     * @param _maxStakeAmount Maximum stake amount.
     */
    constructor(
        address _token,
        address _rewardToken,
        address _bitcoinPriceFeed,
        uint256 _predictionDuration,
        uint256 _rewardAmount,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount
    ) public {
        token = IERC20(_token);
        rewardToken = IERC20(_rewardToken);
        bitcoinPriceFeed = IBitcoinPriceFeed(_bitcoinPriceFeed);
        predictionDuration = _predictionDuration;
        rewardAmount = _rewardAmount;
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
    }

    /**
     * @notice Make a prediction.
     * @param _prediction Prediction (0 for decrease, 1 for increase).
     */
    function makePrediction(uint256 _prediction) public whenNotPaused {
        require(_prediction == 0 || _prediction == 1, "Invalid prediction");

        userPredictions[msg.sender] = Prediction(_prediction, block.timestamp);
        emit PredictionMade(msg.sender, _prediction);
    }

    /**
     * @notice Stake tokens.
     * @param _amount Amount to stake.
     */
    function stake(uint256 _amount) public whenNotPaused {
        require(_amount >= minStakeAmount && _amount <= maxStakeAmount, "Invalid stake amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        userStakes[msg.sender] = userStakes[msg.sender].add(_amount);
        token.transferFrom(msg.sender, address(this), _amount);
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Resolve a prediction.
     * @param _predictionId Prediction ID.
     */
    function resolvePrediction(uint256 _predictionId) public onlyOwner whenNotPaused {
        Prediction memory prediction = userPredictions[address(_predictionId)];
        require(prediction.timestamp != 0, "Prediction not found");

        bool outcome = bitcoinPriceFeed.getPriceChange() > 0;
        predictionOutcomes[_predictionId] = uint256(outcome);

        emit PredictionResolved(_predictionId, outcome);
    }

    /**
     * @notice Claim a reward.
     */
    function claimReward() public whenNotPaused {
        Prediction memory prediction = userPredictions[msg.sender];
        require(prediction.timestamp != 0, "No prediction found");

        uint256 outcome = predictionOutcomes[uint256(prediction.prediction)];
        require(outcome != 0, "Prediction not resolved");

        if (outcome == prediction.prediction) {
            rewardToken.transfer(msg.sender, rewardAmount);
            emit RewardClaimed(msg.sender, rewardAmount);
        }
    }

    /**
     * @notice Pause the contract.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause the contract.
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}

interface IBitcoinPriceFeed {
    function getPriceChange() external view returns (int256);
}
```
