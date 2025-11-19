"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testuser.usdtddex.com
Prompt: Illustrate how to implement a smart contract for staking USDTD tokens with the specified daily rewards.
Generated: DETERMINISTIC_39393131449407aa
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a well-documented, production-ready implementation of a smart contract for staking USDTD tokens with daily rewards, using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title USDTD Token Staking Contract
 * @notice This contract allows users to stake USDTD tokens and earn daily rewards.
 * @dev Ensure that the contract is connected to a deployed USDTD token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract USDTDStaking {
    // Address of the USDTD token contract
    IERC20 public usdtToken;

    // Struct to keep track of user staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Start time of staking
        uint256 unclaimedRewards; // Rewards that are yet to be claimed
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // Rewards per day in percentage (e.g., 1% = 100, 0.5% = 50)
    uint256 public dailyRewardRate;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @notice Constructor to initialize the staking contract.
     * @param _usdtToken Address of the USDTD token contract.
     * @param _dailyRewardRate Daily reward rate in percentage (e.g., 1% = 100).
     */
    constructor(IERC20 _usdtToken, uint256 _dailyRewardRate) {
        usdtToken = _usdtToken;
        dailyRewardRate = _dailyRewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Stake USDTD tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer USDTD tokens from user to contract
        require(usdtToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate unclaimed rewards for current stake (if any)
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].unclaimedRewards += calculateRewards(msg.sender);
        }

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens from the contract.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards before withdrawing
        uint256 rewards = calculateRewards(msg.sender) + userStake.unclaimedRewards;

        // Transfer staked tokens back to user
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.unclaimedRewards = 0;
        require(usdtToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Transfer rewards to user
        if (rewards > 0) {
            require(usdtToken.transfer(msg.sender, rewards), "Reward transfer failed");
        }

        emit Withdrawn(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Claim accumulated rewards without withdrawing the stake.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewards = calculateRewards(msg.sender) + userStake.unclaimedRewards;

        // Reset user's unclaimed rewards
        userStake.unclaimedRewards = 0;
        userStake.startTime = block.timestamp;

        // Transfer rewards to user
        require(rewards > 0, "No rewards to claim");
        require(usdtToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate the rewards for a user based on staking duration and amount.
     * @param user Address of the user to calculate rewards for.
     * @return Rewards in USDTD tokens.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 rewardPerDay = (userStake.amount * dailyRewardRate) / 10000;
        uint256 totalRewards = (stakingDuration / 1 days) * rewardPerDay;

        return totalRewards;
    }

    /**
     * @notice Update the daily reward rate (owner-only function).
     * @param _dailyRewardRate New daily reward rate in percentage.
     */
    function updateDailyRewardRate(uint256 _dailyRewardRate) external onlyOwner {
        dailyRewardRate = _dailyRewardRate;
    }

    /**
     * @notice Emergency withdrawal of tokens by owner (used for recovery, if needed).
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(usdtToken.transfer(owner, amount), "Token transfer failed");
    }
}
```

This contract adheres to your requirements for clean, efficient, and well-documented code. It includes proper error handling and follows Solidity best practices for production-ready smart contracts.
