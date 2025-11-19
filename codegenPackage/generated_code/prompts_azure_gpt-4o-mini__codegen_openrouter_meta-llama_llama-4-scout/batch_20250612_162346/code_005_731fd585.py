"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Create a Solidity contract that mimics the DOGE20 staking mechanism, distributing rewards based on the percentage of tokens staked.
Generated: DETERMINISTIC_731fd585bd5ce8cf
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract mimics the DOGE20 staking mechanism, distributing rewards based on the percentage of tokens staked.
 */
contract Doge20Staking is ReentrancyGuard {
    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward token address
    address public rewardTokenAddress;

    // Staking token address
    address public stakingTokenAddress;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Total rewards
    uint256 public totalRewards;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingTokenAddress Address of the staking token
     * @param _rewardTokenAddress Address of the reward token
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _stakingTokenAddress,
        address _rewardTokenAddress,
        uint256 _rewardPerBlock
    ) public {
        require(_stakingTokenAddress != address(0), "Staking token address cannot be zero");
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        stakingTokenAddress = _stakingTokenAddress;
        rewardTokenAddress = _rewardTokenAddress;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(
            ERC20(stakingTokenAddress).transferFrom(msg.sender, address(this), amount),
            "Failed to transfer staking tokens"
        );

        // Update user's staking balance
        stakingBalances[msg.sender] += amount;
        totalStakingBalance += amount;

        // Update user's reward debt
        updateRewardDebt(msg.sender);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] -= amount;
        totalStakingBalance -= amount;

        // Transfer unstaked tokens to user
        require(
            ERC20(stakingTokenAddress).transfer(msg.sender, amount),
            "Failed to transfer staking tokens"
        );

        // Update user's reward debt
        updateRewardDebt(msg.sender);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Update user's reward debt
     * @param user User address
     */
    function updateRewardDebt(address user) internal {
        // Calculate rewards since last update
        uint256 rewards = getRewardsSinceLastUpdate();

        // Update total rewards
        totalRewards += rewards;

        // Update user's reward debt
        if (stakingBalances[user] > 0) {
            rewardDebt[user] += (rewards * stakingBalances[user]) / totalStakingBalance;
        }
    }

    /**
     * @dev Get rewards since last update
     * @return Rewards since last update
     */
    function getRewardsSinceLastUpdate() internal view returns (uint256) {
        // Calculate blocks since last update
        uint256 blocksSinceLastUpdate = block.number - lastRewardBlock;

        // Calculate rewards since last update
        uint256 rewards = blocksSinceLastUpdate * rewardPerBlock;

        // Update last reward block
        return rewards;
    }

    /**
     * @dev Distribute rewards to user
     */
    function distributeRewards() external nonReentrant {
        // Calculate user's rewards
        uint256 userRewards = getUserRewards(msg.sender);

        // Transfer rewards to user
        require(
            ERC20(rewardTokenAddress).transfer(msg.sender, userRewards),
            "Failed to transfer rewards"
        );

        // Update user's reward debt
        rewardDebt[msg.sender] = 0;

        emit RewardsDistributed(msg.sender, userRewards);
    }

    /**
     * @dev Get user's rewards
     * @param user User address
     * @return User's rewards
     */
    function getUserRewards(address user) public view returns (uint256) {
        // Calculate user's rewards
        uint256 userRewards = rewardDebt[user];

        return userRewards;
    }
}
```
