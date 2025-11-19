"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Design a smart contract for Green Bitcoin ($GBTC) staking and rewards distribution using Solidity, incorporating weekly prediction challenges and tokenomics."
Generated: DETERMINISTIC_5e97b4c92fa6cbd4
Batch ID: 20250622_210243
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GreenBitcoinStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Structs
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
        uint256 lastClaimTime;
    }

    struct Prediction {
        uint256 predictionValue;
        bool claimed;
    }

    struct WeekInfo {
        uint256 startTime;
        uint256 endTime;
        uint256 rewardPool;
        uint256 totalStaked;
        uint256 bitcoinPriceAtEnd;
        bool priceSet;
    }

    // Constants
    uint256 public constant PRECISION_FACTOR = 1e18;
    uint256 public constant WEEK_DURATION = 7 days;
    uint256 public constant MIN_STAKE_AMOUNT = 0.01 ether;
    uint256 public constant EARLY_UNSTAKE_PENALTY = 10; // 10%
    uint256 public constant MIN_STAKE_DURATION = 3 days;

    // State variables
    IERC20 public gbtcToken;
    uint256 public currentWeek;
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    // Mappings
    mapping(address => Staker) public stakers;
    mapping(uint256 => WeekInfo) public weekInfo;
    mapping(address => mapping(uint256 => Prediction)) public predictions;
    mapping(uint256 => uint256) public weeklyRewardPool;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PredictionMade(address indexed user, uint256 week, uint256 prediction);
    event PredictionRewardClaimed(address indexed user, uint256 week, uint256 reward);
    event WeekStarted(uint256 week, uint256 startTime, uint256 endTime);
    event WeekEnded(uint256 week, uint256 bitcoinPrice);
    event RewardPoolAdded(uint256 week, uint256 amount);

    constructor(address _gbtcToken) {
        require(_gbtcToken != address(0), "Invalid token address");
        gbtcToken = IERC20(_gbtcToken);
        _startNewWeek();
    }

    // Stake GBTC tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount >= MIN_STAKE_AMOUNT, "Amount too low");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        Staker storage user = stakers[msg.sender];
        WeekInfo storage currentWeekData = weekInfo[currentWeek];

        // Harvest any pending rewards
        if (user.amount > 0) {
            _harvest(msg.sender);
        }

        // Update user staking info
        user.amount += _amount;
        user.lastStakeTime = block.timestamp;
        user.rewardDebt = (user.amount * currentWeekData.rewardPool) / (currentWeekData.totalStaked + _amount);

        // Update global staking info
        currentWeekData.totalStaked += _amount;
        totalStaked += _amount;

        // Transfer tokens from user to contract
        gbtcToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    // Unstake GBTC tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage user = stakers[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Harvest any pending rewards
        _harvest(msg.sender);

        // Apply penalty if unstaking before minimum duration
        uint256 penalty = 0;
        if (block.timestamp < user.lastStakeTime + MIN_STAKE_DURATION) {
            penalty = (_amount * EARLY_UNSTAKE_PENALTY) / 100;
            _amount -= penalty;
        }

        // Update user staking info
        user.amount -= (_amount + penalty);
        user.rewardDebt = (user.amount * weekInfo[currentWeek].rewardPool) / (weekInfo[currentWeek].totalStaked - _amount - penalty);

        // Update global staking info
        weekInfo[currentWeek].totalStaked -= (_amount + penalty);
        totalStaked -= (_amount + penalty);

        // Transfer tokens back to user
        if (_amount > 0) {
            gbtcToken.safeTransfer(msg.sender, _amount);
        }
        if (penalty > 0) {
            gbtcToken.safeTransfer(owner(), penalty);
        }

        emit Unstaked(msg.sender, _amount);
    }

    // Claim staking rewards
    function claimRewards() external nonReentrant {
        _harvest(msg.sender);
    }

    // Make a BTC price prediction for the current week
    function makePrediction(uint256 _predictionValue) external {
        require(block.timestamp < weekInfo[currentWeek].endTime, "Prediction period ended");
        require(stakers[msg.sender].amount > 0, "Must be a staker to predict");

        predictions[msg.sender][currentWeek] = Prediction({
            predictionValue: _predictionValue,
            claimed: false
        });

        emit PredictionMade(msg.sender, currentWeek, _predictionValue);
    }

    // Claim prediction rewards for a specific week
    function claimPredictionReward(uint256 _week) external nonReentrant {
        require(_week < currentWeek, "Cannot claim for current or future week");
        require(weekInfo[_week].priceSet, "Bitcoin price not set for this week");
        require(!predictions[msg.sender][_week].claimed, "Reward already claimed");
        require(predictions[msg.sender][_week].predictionValue > 0, "No prediction made");

        uint256 predictionDiff = _absDiff(predictions[msg.sender][_week].predictionValue, weekInfo[_week].bitcoinPriceAtEnd);
        uint256 reward = _calculatePredictionReward(_week, predictionDiff);

        if (reward > 0) {
            predictions[msg.sender][_week].claimed = true;
            gbtcToken.safeTransfer(msg.sender, reward);
            emit PredictionRewardClaimed(msg.sender, _week, reward);
        }
    }

    // Admin function to set BTC price for the ended week
    function setBitcoinPrice(uint256 _price) external onlyOwner {
        require(block.timestamp > weekInfo[currentWeek - 1].endTime, "Current week not ended");
        require(!weekInfo[currentWeek - 1].priceSet, "Price already set");

        weekInfo[currentWeek - 1].bitcoinPriceAtEnd = _price;
        weekInfo[currentWeek - 1].priceSet = true;

        emit WeekEnded(currentWeek - 1, _price);
    }

    // Admin function to add rewards to the pool
    function addRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Invalid amount");
        weeklyRewardPool[currentWeek] += _amount;
        weekInfo[currentWeek].rewardPool += _amount;

        gbtcToken.safeTransferFrom(msg.sender, address(this), _amount);
        emit RewardPoolAdded(currentWeek, _amount);
    }

    // Admin function to start a new week
    function startNewWeek() external onlyOwner {
        _startNewWeek();
    }

    // Internal function to harvest rewards
    function _harvest(address _user) internal {
        Staker storage user = stakers[_user];
        if (user.amount == 0) return;

        uint256 pendingRewards;
        for (uint256 i = user.lastClaimTime; i < currentWeek; i++) {
            if (weekInfo[i].totalStaked > 0) {
                pendingRewards += (user.amount * weekInfo[i].rewardPool) / weekInfo[i].totalStaked;
            }
        }

        if (pendingRewards > 0) {
            user.lastClaimTime = currentWeek;
            totalRewardsDistributed += pendingRewards;
            gbtcToken.safeTransfer(_user, pendingRewards);
            emit RewardClaimed(_user, pendingRewards);
        }
    }

    // Internal function to start a new week
    function _startNewWeek() internal {
        if (currentWeek > 0) {
            require(block.timestamp > weekInfo[currentWeek - 1].endTime, "Previous week not ended");
        }

        weekInfo[currentWeek] = WeekInfo({
            startTime: block.timestamp,
            endTime: block.timestamp + WEEK_DUR
