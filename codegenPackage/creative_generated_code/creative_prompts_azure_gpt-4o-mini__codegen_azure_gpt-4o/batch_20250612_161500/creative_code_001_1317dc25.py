"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract for a staking pool that supports different reward rates and compounding options for AITECH tokens, similar to those outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_1317dc25a3084b73
Batch ID: 20250612_161500
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
 * @title AITECH Staking Pool Smart Contract
 * @dev This contract allows users to stake AITECH tokens and earn rewards at different rates,
 * with optional compounding mechanisms.
 */
contract AITECHStakingPool {
    // Import SafeMath for secure arithmetic operations
    using SafeMath for uint256;

    IERC20 public immutable aitechToken;

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 rewardRate; // Reward rate associated with this stake
        uint256 lastUpdatedTime; // Timestamp of the last update
        uint256 accumulatedRewards; // Total rewards accrued
        bool isCompounding; // Whether the stake is compounding rewards
    }

    mapping(address => Stake) public stakes; // Map of user stakes by address

    uint256 public constant ONE_YEAR_IN_SECONDS = 365 * 24 * 60 * 60; // Number of seconds in a year

    address public owner; // Owner of the contract

    event Staked(address indexed user, uint256 amount, uint256 rewardRate, bool isCompounding);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event CompoundingOptionUpdated(address indexed user, bool isCompounding);
    event RewardRateUpdated(address indexed user, uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address _user) {
        Stake storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp.sub(stake.lastUpdatedTime);
            uint256 newRewards = stake.amount.mul(stake.rewardRate).mul(timeElapsed).div(ONE_YEAR_IN_SECONDS).div(100); // Reward calculation
            stake.accumulatedRewards = stake.accumulatedRewards.add(newRewards);
            stake.lastUpdatedTime = block.timestamp;
        }
        _;
    }

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        aitechToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Stake AITECH tokens in the pool.
     * @param _amount Amount of AITECH tokens to stake
     * @param _rewardRate Reward rate for the stake (% per year)
     * @param _isCompounding Whether to enable compounding rewards
     */
    function stake(uint256 _amount, uint256 _rewardRate, bool _isCompounding) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        aitechToken.transferFrom(msg.sender, address(this), _amount);

        Stake storage stake = stakes[msg.sender];
        stake.amount = stake.amount.add(_amount);
        stake.rewardRate = _rewardRate;
        stake.isCompounding = _isCompounding;
        stake.lastUpdatedTime = block.timestamp;

        emit Staked(msg.sender, _amount, _rewardRate, _isCompounding);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No staked amount to unstake");

        uint256 stakedAmount = stake.amount;
        uint256 rewards = stake.accumulatedRewards;

        stake.amount = 0;
        stake.accumulatedRewards = 0;

        aitechToken.transfer(msg.sender, stakedAmount.add(rewards));

        emit Unstaked(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Update the compounding option for the user's stake.
     * @param _isCompounding Whether to enable compounding
     */
    function updateCompoundingOption(bool _isCompounding) external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No staked amount to update");

        stake.isCompounding = _isCompounding;

        emit CompoundingOptionUpdated(msg.sender, _isCompounding);
    }

    /**
     * @dev Update the reward rate for the user's stake. Only owner can call this function.
     * @param _user Address of the user
     * @param _newRate New reward rate (% per year)
     */
    function updateRewardRate(address _user, uint256 _newRate) external onlyOwner updateRewards(_user) {
        require(_newRate > 0, "Reward rate must be greater than zero");
        Stake storage stake = stakes[_user];
        require(stake.amount > 0, "User has no staked amount");

        stake.rewardRate = _newRate;

        emit RewardRateUpdated(_user, _newRate);
    }

    /**
     * @dev Emergency withdrawal by owner. Transfers all tokens to the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = aitechToken.balanceOf(address(this));
        aitechToken.transfer(owner, balance);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

/**
 * @dev Library for safe mathematical operations.
 */
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction underflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "Multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "Division by zero");
        uint256 c = a / b;
        return c;
    }
}
```
