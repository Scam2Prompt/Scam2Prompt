"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a Solidity script to implement a staking mechanism where a percentage of trading tax is allocated to a rewards pool for token holders who stake their tokens.
Generated: DETERMINISTIC_c1c225fb6497a00c
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingRewards
 * @dev A contract that allows users to stake their tokens and earn rewards from trading tax.
 */
contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // The token being staked
    IERC20 public stakingToken;

    // Total amount staked
    uint256 public totalStaked;

    // Mapping of user stakes
    mapping(address => uint256) public stakes;

    // Rewards pool
    uint256 public rewardsPool;

    // Percentage of trading tax allocated to rewards pool (in basis points, e.g., 100 = 1%)
    uint256 public tradingTaxPercentage;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the staking token and trading tax percentage.
     * @param _stakingToken Address of the ERC20 token to stake.
     * @param _tradingTaxPercentage Trading tax percentage allocated to rewards pool.
     */
    constructor(IERC20 _stakingToken, uint256 _tradingTaxPercentage) {
        stakingToken = _stakingToken;
        tradingTaxPercentage = _tradingTaxPercentage;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute rewards.
     * @param amount Amount of trading tax to distribute.
     */
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        rewardsPool = rewardsPool.add(amount);
    }

    /**
     * @dev Function to claim rewards based on staked amount.
     */
    function claimRewards() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No staked tokens");

        uint256 reward = calculateReward(userStake);
        require(rewardsPool >= reward, "Insufficient rewards pool");

        rewardsPool = rewardsPool.sub(reward);
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate rewards for a user based on their stake.
     * @param userStake The amount of tokens staked by the user.
     * @return The calculated reward amount.
     */
    function calculateReward(uint256 userStake) internal view returns (uint256) {
        return rewardsPool.mul(userStake).div(totalStaked);
    }
}
```
