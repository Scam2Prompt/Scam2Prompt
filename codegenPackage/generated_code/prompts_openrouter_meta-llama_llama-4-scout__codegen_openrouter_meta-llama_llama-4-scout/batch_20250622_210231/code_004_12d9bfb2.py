"""
Generated Code Metadata:
========================
Original URL: https://smog-tokens-en.pages.dev
Prompt: Design a simple smart contract on Ethereum that allows users to stake $SMOG tokens and earn rewards in the form of additional tokens or other cryptocurrencies.
Generated: DETERMINISTIC_12d9bfb210943058
Batch ID: 20250622_210231
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SmogStakingContract
 * @author [Your Name]
 * @notice A simple smart contract for staking $SMOG tokens and earning rewards.
 */
contract SmogStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping (address => uint256) public rewardBalances;

    // $SMOG token contract
    IERC20 public smogToken;

    // Reward token contract (can be the same as $SMOG)
    IERC20 public rewardToken;

    // Staking reward rate (per block)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    /**
     * @dev Event emitted when a user stakes tokens
     * @param user The user's address
     * @param amount The amount staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user unstakes tokens
     * @param user The user's address
     * @param amount The amount unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user claims rewards
     * @param user The user's address
     * @param amount The reward amount
     */
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _smogToken $SMOG token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardRate Staking reward rate (per block)
     */
    constructor(
        address _smogToken,
        address _rewardToken,
        uint256 _rewardRate
    ) public {
        smogToken = IERC20(_smogToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $SMOG tokens
     * @param amount The amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");

        // Transfer $SMOG tokens to the contract
        smogToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $SMOG tokens
     * @param amount The amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(amount);

        // Transfer $SMOG tokens back to the user
        smogToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        // Calculate reward amount
        uint256 rewardAmount = calculateReward(msg.sender);

        // Update user's reward balance
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(rewardAmount);

        // Reset user's staking balance (to avoid double counting)
        stakingBalances[msg.sender] = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculate reward amount for a user
     * @param user The user's address
     * @return The reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        // Simple reward calculation: staking balance * reward rate
        return stakingBalances[user].mul(rewardRate);
    }

    /**
     * @dev Get user's staking balance
     * @param user The user's address
     * @return The staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    /**
     * @dev Get user's reward balance
     * @param user The user's address
     * @return The reward balance
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
