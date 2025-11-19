"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoins20.pages.dev
Prompt: Generate a Solidity contract that implements a simple staking mechanism similar to DOGE20, allowing users to stake ERC-20 tokens and earn rewards over time.
Generated: DETERMINISTIC_5ecebe74b4aba351
Batch ID: 20250612_160853
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

// Importing the ERC20 interface to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SimpleStaking
 * @dev A simple staking contract that allows users to stake ERC20 tokens and earn rewards.
 */
contract SimpleStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 startTime;      // Timestamp when tokens were staked
    }

    // Mapping from user address to their staking details
    mapping(address => Stake) public stakes;

    // Token to be staked
    IERC20 public stakingToken;

    // Reward rate per second (in wei), example: 1 token per second
    uint256 public rewardRate;

    // Total rewards earned by users
    mapping(address => uint256) public rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _stakingToken Address of the ERC20 token to be staked
     * @param _rewardRate Reward rate in wei
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staking info
        Stake storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     */
    function withdraw() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens to withdraw");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset the staking info before transferring tokens
        uint256 amountToWithdraw = stakeInfo.amount;
        stakeInfo.amount = 0;
        stakeInfo.startTime = 0;

        // Transfer tokens and rewards to the user
        stakingToken.transfer(msg.sender, amountToWithdraw);
        rewards[msg.sender] += reward;

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards
        rewards[msg.sender] += reward;

        // Transfer reward to user
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a user
     * @param user Address of the user
     * @return uint256 Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) return 0;

        // Calculate reward based on time staked and rate
        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        return stakingDuration * rewardRate * stakeInfo.amount;
    }
}
```
