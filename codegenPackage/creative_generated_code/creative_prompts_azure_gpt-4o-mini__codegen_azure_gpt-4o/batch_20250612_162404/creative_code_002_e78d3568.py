"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
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
 * @title Catgirl Staking DApp
 * @dev A decentralized application that allows users to stake CATGIRL¢ tokens
 *      and earn rewards based on the staking duration and amount.
 */
 
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract CatgirlStaking {
    IERC20 public immutable catgirlToken;
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5 = 5%)
    uint256 public constant DECIMALS = 1e18; // Token decimals for calculation

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the tokens were staked
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 rewardsEarned);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _catgirlToken Address of the CATGIRL¢ token contract
     * @param _rewardRate Initial reward rate (e.g., 5 means 5%)
     */
    constructor(IERC20 _catgirlToken, uint256 _rewardRate) {
        require(address(_catgirlToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        catgirlToken = _catgirlToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake CATGIRL¢ tokens to earn rewards
     * @param amount Number of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        require(catgirlToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate pending rewards for existing stake, if any
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            rewards[msg.sender] += pendingRewards;
        }

        // Update the staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Calculate rewards for a given user
     * @param user Address of the user
     * @return Reward amount
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        uint256 reward = (stakeInfo.amount * rewardRate * stakingDuration) / (365 days * 100);

        return reward;
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender) + rewards[msg.sender];
        uint256 stakedAmount = stakeInfo.amount;

        // Reset user's stake and reward data
        stakeInfo.amount = 0;
        stakeInfo.timestamp = 0;
        rewards[msg.sender] = 0;

        // Transfer staked tokens and rewards to the user
        require(catgirlToken.transfer(msg.sender, stakedAmount), "Staked token transfer failed");
        require(catgirlToken.transfer(msg.sender, reward), "Reward token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Update the reward rate (only owner should use this in production)
     * @param newRate New reward rate
     */
    function updateRewardRate(uint256 newRate) external {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;

        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Get user's staking details
     * @param user Address of the user
     * @return amount Staked amount
     * @return timestamp Staking timestamp
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage stakeInfo = stakes[user];
        return (stakeInfo.amount, stakeInfo.timestamp);
    }
}
```
