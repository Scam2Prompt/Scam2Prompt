"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity smart contract to manage the Meme Index's staking rewards, distributing the 25% supply dedicated to staking rewards among $MEMEX holders.
Generated: DETERMINISTIC_6f2289a5a06fc372
Batch ID: 20250622_211639
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeIndexStaking
 * @dev A smart contract to manage staking rewards for $MEMEX holders.
 */
contract MemeIndexStaking is Ownable {
    using SafeMath for uint256;

    // The ERC20 token contract for $MEMEX
    IERC20 public memexToken;

    // Total supply dedicated to staking rewards (25% of total supply)
    uint256 public totalStakingRewards;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedAmounts;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 amount);

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $MEMEX token address.
     * @param _memexToken Address of the $MEMEX token contract.
     * @param _totalSupply Total supply of $MEMEX tokens.
     */
    constructor(IERC20 _memexToken, uint256 _totalSupply) {
        memexToken = _memexToken;
        totalStakingRewards = _totalSupply.mul(25).div(100);
    }

    /**
     * @dev Function to stake $MEMEX tokens.
     * @param amount Amount of $MEMEX tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(memexToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to the contract
        memexToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $MEMEX tokens.
     * @param amount Amount of $MEMEX tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        memexToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute staking rewards to all stakers.
     * @param rewardAmount Amount of rewards to distribute.
     */
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than 0");
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        // Calculate rewards per staked token
        uint256 rewardPerToken = rewardAmount.div(totalStaked);

        // Distribute rewards to each staker
        for (uint256 i = 0; i < totalStaked; i++) {
            address staker = address(uint160(i)); // Placeholder for actual staker address retrieval
            uint256 stakerReward = stakedAmounts[staker].mul(rewardPerToken);
            memexToken.transfer(staker, stakerReward);
        }

        emit RewardsDistributed(rewardAmount);
    }

    /**
     * @dev Function to withdraw remaining staking rewards after contract is no longer needed.
     */
    function withdrawRemainingRewards() external onlyOwner {
        uint256 remainingRewards = memexToken.balanceOf(address(this));
        require(remainingRewards > 0, "No remaining rewards to withdraw");

        memexToken.transfer(owner(), remainingRewards);
    }
}
```
