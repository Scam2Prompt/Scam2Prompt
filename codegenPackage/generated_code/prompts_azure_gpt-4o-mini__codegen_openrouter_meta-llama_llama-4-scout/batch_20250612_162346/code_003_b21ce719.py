"""
Generated Code Metadata:
========================
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that rewards users based on their staking duration and prediction accuracy.
Generated: DETERMINISTIC_b21ce719734cbd49
Batch ID: 20250612_162346
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
 * @title GBTC Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GBTC tokens and rewards them based on their staking duration and prediction accuracy.
 */
contract GBTCStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfo;

    // Mapping of prediction accuracy
    mapping (address => uint256) public predictionAccuracy;

    // $GBTC token contract
    IERC20 public gbtcToken;

    // Total staked tokens
    uint256 public totalStakedTokens;

    // Staking duration rewards
    uint256 public constant ONE_WEEK_REWARD = 10;
    uint256 public constant TWO_WEEK_REWARD = 20;
    uint256 public constant ONE_MONTH_REWARD = 50;

    // Prediction accuracy rewards
    uint256 public constant ACCURACY_50_REWARD = 5;
    uint256 public constant ACCURACY_75_REWARD = 10;
    uint256 public constant ACCURACY_100_REWARD = 20;

    // Staking duration in seconds
    uint256 public constant ONE_WEEK = 604800;
    uint256 public constant TWO_WEEKS = 1209600;
    uint256 public constant ONE_MONTH = 2592000;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user updates prediction accuracy
    event PredictionAccuracyUpdated(address indexed user, uint256 accuracy);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingDuration;
        uint256 reward;
        uint256 startTime;
    }

    /**
     * @notice Constructor
     * @param _gbtcTokenAddress $GBTC token contract address
     */
    constructor(address _gbtcTokenAddress) public {
        require(_gbtcTokenAddress != address(0), "GBTC token address cannot be zero");
        gbtcToken = IERC20(_gbtcTokenAddress);
    }

    /**
     * @notice Stake $GBTC tokens
     * @param _amount Amount of tokens to stake
     * @param _stakingDuration Staking duration in seconds
     */
    function stake(uint256 _amount, uint256 _stakingDuration) public {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_stakingDuration > 0, "Staking duration must be greater than zero");

        // Transfer tokens from user to contract
        require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user staking information
        userStakingInfo[msg.sender].stakedAmount = userStakingInfo[msg.sender].stakedAmount.add(_amount);
        userStakingInfo[msg.sender].stakingDuration = _stakingDuration;
        userStakingInfo[msg.sender].startTime = block.timestamp;

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC tokens
     */
    function unstake() public {
        require(userStakingInfo[msg.sender].stakedAmount > 0, "User has no staked tokens");
        require(block.timestamp >= userStakingInfo[msg.sender].startTime.add(userStakingInfo[msg.sender].stakingDuration), "Staking duration has not ended");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update user staking information
        userStakingInfo[msg.sender].reward = userStakingInfo[msg.sender].reward.add(reward);

        // Transfer tokens and reward to user
        require(gbtcToken.transfer(msg.sender, userStakingInfo[msg.sender].stakedAmount.add(reward)), "Token transfer failed");

        // Reset user staking information
        userStakingInfo[msg.sender].stakedAmount = 0;
        userStakingInfo[msg.sender].stakingDuration = 0;
        userStakingInfo[msg.sender].startTime = 0;

        // Update total staked tokens
        totalStakedTokens = totalStakedTokens.sub(userStakingInfo[msg.sender].stakedAmount);

        // Emit event
        emit Unstaked(msg.sender, userStakingInfo[msg.sender].stakedAmount);
    }

    /**
     * @notice Update prediction accuracy
     * @param _accuracy Prediction accuracy
     */
    function updatePredictionAccuracy(uint256 _accuracy) public {
        require(_accuracy > 0, "Prediction accuracy must be greater than zero");

        // Update prediction accuracy
        predictionAccuracy[msg.sender] = _accuracy;

        // Emit event
        emit PredictionAccuracyUpdated(msg.sender, _accuracy);
    }

    /**
     * @notice Calculate reward
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakingDuration = userStakingInfo[_user].stakingDuration;
        uint256 accuracy = predictionAccuracy[_user];

        // Calculate duration reward
        uint256 durationReward;
        if (stakingDuration >= ONE_MONTH) {
            durationReward = ONE_MONTH_REWARD;
        } else if (stakingDuration >= TWO_WEEKS) {
            durationReward = TWO_WEEK_REWARD;
        } else if (stakingDuration >= ONE_WEEK) {
            durationReward = ONE_WEEK_REWARD;
        }

        // Calculate accuracy reward
        uint256 accuracyReward;
        if (accuracy >= 100) {
            accuracyReward = ACCURACY_100_REWARD;
        } else if (accuracy >= 75) {
            accuracyReward = ACCURACY_75_REWARD;
        } else if (accuracy >= 50) {
            accuracyReward = ACCURACY_50_REWARD;
        }

        // Return total reward
        return userStakingInfo[_user].stakedAmount.mul(durationReward.add(accuracyReward)).div(100);
    }
}
```
