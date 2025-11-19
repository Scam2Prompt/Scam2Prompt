"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dapps.pages.dev
Prompt: Create a function in Solidity to implement the Gamified Green Staking mechanism, including weekly Bitcoin price prediction challenges.
Generated: DETERMINISTIC_3b5e5c72d42bc8a4
Batch ID: 20250612_150234
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract GamifiedGreenStaking is Ownable, ReentrancyGuard {
    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakeTimestamp;
        uint256 rewardPoints;
        uint256 lastPredictionTimestamp;
        bool hasActiveStake;
    }

    // Struct to store prediction information
    struct Prediction {
        uint256 predictedPrice;
        uint256 actualPrice;
        uint256 timestamp;
        bool isResolved;
    }

    // Constants
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant PREDICTION_WINDOW = 1 weeks;
    uint256 public constant BASE_REWARD_RATE = 100; // 1% per week
    uint256 public constant PREDICTION_REWARD_BONUS = 50; // 0.5% bonus for correct prediction

    // State variables
    AggregatorV3Interface internal priceFeed;
    uint256 public totalStaked;
    uint256 public currentPredictionRound;
    uint256 public predictionRoundStartTime;

    // Mappings
    mapping(address => Staker) public stakers;
    mapping(uint256 => mapping(address => Prediction)) public predictions;
    mapping(uint256 => uint256) public roundActualPrices;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PredictionMade(address indexed user, uint256 round, uint256 predictedPrice);
    event PredictionResolved(uint256 round, uint256 actualPrice);

    // Constructor
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        predictionRoundStartTime = block.timestamp;
        currentPredictionRound = 1;
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage user = stakers[msg.sender];
        
        if (user.hasActiveStake) {
            // Calculate rewards for existing stake
            uint256 reward = calculateReward(msg.sender);
            user.rewardPoints += reward;
        }
        
        // Update staker information
        user.stakedAmount += amount;
        user.lastStakeTimestamp = block.timestamp;
        user.hasActiveStake = true;
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage user = stakers[msg.sender];
        require(user.hasActiveStake, "No active stake");
        require(user.stakedAmount >= amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastStakeTimestamp + MIN_STAKE_DURATION, "Minimum stake duration not met");

        // Calculate and add rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        user.rewardPoints += reward;
        
        // Update staker information
        user.stakedAmount -= amount;
        user.lastStakeTimestamp = block.timestamp;
        
        if (user.stakedAmount == 0) {
            user.hasActiveStake = false;
        }
        
        totalStaked -= amount;
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage user = stakers[msg.sender];
        require(user.rewardPoints > 0, "No rewards to claim");

        // Calculate current stake rewards and add to total
        uint256 currentReward = calculateReward(msg.sender);
        uint256 totalReward = user.rewardPoints + currentReward;
        
        // Reset reward points and update last stake timestamp
        user.rewardPoints = 0;
        user.lastStakeTimestamp = block.timestamp;
        
        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Submit a BTC price prediction for the current round
     * @param predictedPrice The predicted BTC price in USD (without decimals)
     */
    function submitPrediction(uint256 predictedPrice) external {
        require(stakers[msg.sender].hasActiveStake, "Must be an active staker");
        require(block.timestamp < predictionRoundStartTime + PREDICTION_WINDOW, "Prediction window closed");
        require(predictions[currentPredictionRound][msg.sender].predictedPrice == 0, "Already predicted this round");

        predictions[currentPredictionRound][msg.sender] = Prediction({
            predictedPrice: predictedPrice,
            actualPrice: 0,
            timestamp: block.timestamp,
            isResolved: false
        });

        emit PredictionMade(msg.sender, currentPredictionRound, predictedPrice);
    }

    /**
     * @dev Resolve the current prediction round (callable by owner)
     */
    function resolvePredictionRound() external onlyOwner {
        require(block.timestamp >= predictionRoundStartTime + PREDICTION_WINDOW, "Prediction window not ended");
        
        // Get current BTC price from Chainlink
        (, int256 price, , , ) = priceFeed.latestRoundData();
        uint256 currentPrice = uint256(price);
        
        roundActualPrices[currentPredictionRound] = currentPrice;
        
        emit PredictionResolved(currentPredictionRound, currentPrice);
        
        // Prepare for next round
        currentPredictionRound++;
        predictionRoundStartTime = block.timestamp;
    }

    /**
     * @dev Calculate rewards for a staker
     * @param stakerAddress The address of the staker
     * @return reward The calculated reward amount
     */
    function calculateReward(address stakerAddress) public view returns (uint256 reward) {
        Staker memory user = stakers[stakerAddress];
        if (!user.hasActiveStake) return 0;
        
        uint256 timeStaked = block.timestamp - user.lastStakeTimestamp;
        uint256 baseReward = (user.stakedAmount * BASE_REWARD_RATE * timeStaked) / (10000 * 1 weeks);
        
        // Check for prediction bonus
        uint256 predictionBonus = 0;
        if (user.lastPredictionTimestamp > 0 && 
            predictions[currentPredictionRound - 1][stakerAddress].isResolved == false) {
            
            Prediction memory pred = predictions[currentPredictionRound - 1][stakerAddress];
            if (pred.predictedPrice == roundActualPrices[currentPredictionRound - 1]) {
                predictionBonus = (user.stakedAmount * PREDICTION_REWARD_BONUS) / 10000;
            }
        }
        
        return baseReward + predictionBonus;
    }

    /**
     * @dev Get the current BTC price from Chainlink
     * @return The current BTC price in USD
     */
    function getCurrentBTCPrice() external view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price);
    }

    /**
     * @dev Get the current prediction round information
     * @return round The current round number
     * @return startTime The start time of the current round
     * @return endTime The end time of the current round
     */
    function getCurrentRoundInfo() external view returns (uint256 round, uint256 startTime, uint256 endTime) {
        return (
            currentPredictionRound,
            predictionRoundStartTime,
            predictionRoundStartTime + PREDICTION_WINDOW
        );
    }
}
```
