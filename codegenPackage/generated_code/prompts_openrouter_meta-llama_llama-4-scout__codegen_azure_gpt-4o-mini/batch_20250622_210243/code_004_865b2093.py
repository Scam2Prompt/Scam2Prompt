"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Design a smart contract using Solidity to distribute staking rewards to DOGE20 token holders over a period of two years, according to their percentage of the staking pool, and provide a code example of how to implement this functionality.
Generated: DETERMINISTIC_865b2093160f5193
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingRewards
 * @dev A smart contract to distribute staking rewards to DOGE20 token holders
 */
contract StakingRewards is Ownable {
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardPool; // Total rewards to distribute
    uint256 public startTime; // Start time of the reward distribution
    uint256 public endTime; // End time of the reward distribution
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user
    mapping(address => uint256) public lastClaimed; // Last claimed timestamp for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _doge20Token Address of the DOGE20 token contract
     * @param _rewardPool Total rewards to distribute
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        doge20Token = _doge20Token;
        rewardPool = _rewardPool;
        startTime = block.timestamp;
        endTime = startTime + 730 days; // 2 years
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param amount Amount of DOGE20 tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking details
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens
     * @param amount Amount of DOGE20 tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking details
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on the staked amount
     */
    function claimRewards() external {
        require(block.timestamp >= lastClaimed[msg.sender], "Rewards already claimed");
        require(block.timestamp < endTime, "Reward period has ended");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        rewards[msg.sender] += reward;
        lastClaimed[msg.sender] = block.timestamp;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards for a user
     * @param user Address of the user
     * @return uint256 Amount of rewards
     */
    function calculateReward(address user) internal view returns (uint256) {
        if (totalStaked == 0) return 0; // No rewards if no tokens are staked

        uint256 userStake = stakedAmount[user];
        uint256 totalRewards = rewardPool * (block.timestamp - startTime) / (endTime - startTime);
        return (userStake * totalRewards) / totalStaked;
    }

    /**
     * @dev Withdraw remaining rewards after the reward period ends
     */
    function withdrawRemainingRewards() external onlyOwner {
        require(block.timestamp >= endTime, "Reward period not ended");
        uint256 remainingRewards = rewardPool - totalRewardsDistributed();
        require(remainingRewards > 0, "No remaining rewards");

        rewardPool = 0; // Set to zero to prevent re-entrancy
        require(doge20Token.transfer(msg.sender, remainingRewards), "Transfer failed");
    }

    /**
     * @dev Calculate total rewards distributed
     * @return uint256 Total rewards distributed
     */
    function totalRewardsDistributed() public view returns (uint256) {
        uint256 totalRewards = 0;
        for (uint256 i = 0; i < stakers.length; i++) {
            totalRewards += calculateReward(stakers[i]);
        }
        return totalRewards;
    }
}
```
