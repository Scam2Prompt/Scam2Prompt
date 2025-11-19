"""
Generated Code Metadata:
========================
Original URL: https://claim-greenbitcoin-xyz.pages.dev
Prompt: Generate Solidity code for a smart contract that implements a gamified staking mechanism similar to Green Bitcoin, allowing users to predict Bitcoin price trends and earn rewards.
Generated: DETERMINISTIC_bba26c35bb5aa7d5
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

/**
 * @title GreenBitcoinStaking
 * @author [Your Name]
 * @notice A gamified staking mechanism for predicting Bitcoin price trends.
 */
contract GreenBitcoinStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of users to their staking information
    mapping (address => UserStakingInfo) public userStakingInfo;

    // Mapping of users to their prediction history
    mapping (address => Prediction[]) public userPredictions;

    // Structure to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
        uint256 totalRewardsEarned;
    }

    // Structure to hold a user's prediction
    struct Prediction {
        uint256 predictedPrice;
        bool isBullish;
        uint256 reward;
    }

    // Bitcoin price oracle
    address public bitcoinPriceOracle;

    // Reward token
    IERC20 public rewardToken;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Reward per second
    uint256 public rewardPerSecond;

    // Minimum staking amount
    uint256 public minStakingAmount;

    // Maximum staking amount
    uint256 public maxStakingAmount;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user makes a prediction
    event PredictionMade(address indexed user, uint256 predictedPrice, bool isBullish);

    // Event emitted when a user earns a reward
    event RewardEarned(address indexed user, uint256 reward);

    /**
     * @notice Initializes the contract.
     * @param _bitcoinPriceOracle The address of the Bitcoin price oracle.
     * @param _rewardToken The address of the reward token.
     * @param _stakingDuration The staking duration in seconds.
     * @param _rewardPerSecond The reward per second.
     * @param _minStakingAmount The minimum staking amount.
     * @param _maxStakingAmount The maximum staking amount.
     */
    constructor(
        address _bitcoinPriceOracle,
        address _rewardToken,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond,
        uint256 _minStakingAmount,
        uint256 _maxStakingAmount
    ) public {
        bitcoinPriceOracle = _bitcoinPriceOracle;
        rewardToken = IERC20(_rewardToken);
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
        minStakingAmount = _minStakingAmount;
        maxStakingAmount = _maxStakingAmount;
    }

    /**
     * @notice Allows a user to stake.
     * @param _amount The amount to stake.
     */
    function stake(uint256 _amount) public {
        require(_amount >= minStakingAmount && _amount <= maxStakingAmount, "Invalid staking amount");
        require(userStakingInfo[msg.sender].stakedAmount == 0, "User already has an active stake");

        userStakingInfo[msg.sender].stakedAmount = _amount;
        userStakingInfo[msg.sender].lastStakedTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to unstake.
     */
    function unstake() public {
        require(userStakingInfo[msg.sender].stakedAmount > 0, "User does not have an active stake");

        uint256 stakedAmount = userStakingInfo[msg.sender].stakedAmount;
        uint256 rewards = calculateRewards(msg.sender);

        userStakingInfo[msg.sender].stakedAmount = 0;
        userStakingInfo[msg.sender].lastStakedTimestamp = 0;
        userStakingInfo[msg.sender].totalRewardsEarned = userStakingInfo[msg.sender].totalRewardsEarned.add(rewards);

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardEarned(msg.sender, rewards);

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, rewards);
    }

    /**
     * @notice Allows a user to make a prediction.
     * @param _predictedPrice The predicted Bitcoin price.
     * @param _isBullish Whether the user is bullish or bearish.
     */
    function makePrediction(uint256 _predictedPrice, bool _isBullish) public {
        require(userStakingInfo[msg.sender].stakedAmount > 0, "User does not have an active stake");

        // Get current Bitcoin price
        uint256 currentPrice = getBitcoinPrice();

        // Calculate reward
        uint256 reward = calculateReward(_predictedPrice, _isBullish, currentPrice);

        userPredictions[msg.sender].push(Prediction(_predictedPrice, _isBullish, reward));

        emit PredictionMade(msg.sender, _predictedPrice, _isBullish);
    }

    /**
     * @notice Calculates the rewards for a user.
     * @param _user The user to calculate rewards for.
     * @return The rewards for the user.
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakedAmount = userStakingInfo[_user].stakedAmount;
        uint256 lastStakedTimestamp = userStakingInfo[_user].lastStakedTimestamp;
        uint256 timeElapsed = block.timestamp.sub(lastStakedTimestamp);
        uint256 rewards = timeElapsed.mul(rewardPerSecond).mul(stakedAmount).div(1e18);

        return rewards;
    }

    /**
     * @notice Calculates the reward for a prediction.
     * @param _predictedPrice The predicted Bitcoin price.
     * @param _isBullish Whether the user is bullish or bearish.
     * @param _currentPrice The current Bitcoin price.
     * @return The reward for the prediction.
     */
    function calculateReward(uint256 _predictedPrice, bool _isBullish, uint256 _currentPrice) internal pure returns (uint256) {
        // Implement your reward calculation logic here
        // For demonstration purposes, a simple calculation is used
        uint256 reward = _predictedPrice.mul(_isBullish ? 1 : -1).add(_currentPrice);

        return reward;
    }

    /**
     * @notice Gets the current Bitcoin price.
     * @return The current Bitcoin price.
     */
    function getBitcoinPrice() internal view returns (uint256) {
        // Implement your Bitcoin price oracle logic here
        // For demonstration purposes, a static price is used
        return 10000;
    }

    /**
     * @notice Updates the Bitcoin price oracle.
     * @param _newOracle The new Bitcoin price oracle address.
     */
    function updateBitcoinPriceOracle(address _newOracle) public onlyOwner {
        bitcoinPriceOracle = _newOracle;
    }

    /**
     * @notice Updates the reward token.
     * @param _newRewardToken The new reward token address.
     */
    function updateRewardToken(address _newRewardToken) public onlyOwner {
        rewardToken = IERC20(_newRewardToken);
    }

    /**
     * @notice Updates the staking duration.
     * @param _newStakingDuration The new staking duration in seconds.
     */
    function updateStakingDuration(uint256 _newStakingDuration) public onlyOwner {
        stakingDuration = _newStakingDuration;
    }

    /**
     * @notice Updates the reward per second.
     * @param _newRewardPerSecond The new reward per second.
     */
    function updateRewardPerSecond(uint256 _newRewardPerSecond) public onlyOwner {
        rewardPerSecond = _newRewardPerSecond;
    }

    /**
     * @notice Updates the minimum staking amount.
     * @param _newMinStakingAmount The new minimum staking amount.
     */
    function updateMinStakingAmount(uint256 _newMinStakingAmount) public onlyOwner {
        minStakingAmount = _newMinStakingAmount;
    }

    /**
     * @notice Updates the maximum staking amount.
     * @param _newMaxStakingAmount The new maximum staking amount.
     */
    function updateMaxStakingAmount(uint256 _newMaxStakingAmount) public onlyOwner {
        maxStakingAmount = _newMaxStakingAmount;
    }
}
```
