"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Write a Solidity contract for a staking pool that contributes 2% of every transaction to rewards, as outlined in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_024fd9486c627b91
Batch ID: 20250612_152235
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
 * @title GalaxyFoxStakingPool
 * @dev A staking pool contract where 2% of every transaction contributes to rewards.
 */

contract GalaxyFoxStakingPool {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total tokens staked
    uint256 public rewardPool; // Accumulated reward pool (2% of transactions)
    uint256 public constant REWARD_PERCENTAGE = 2; // Reward percentage

    mapping(address => uint256) public stakes; // Tracks user stakes
    mapping(address => uint256) public rewards; // Tracks user rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor function sets the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens in the staking pool.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external payable {
        require(msg.value == amount, "Sent value must match the stake amount");
        require(amount > 0, "Stake amount must be greater than zero");

        // Calculate 2% contribution to the reward pool
        uint256 rewardContribution = (amount * REWARD_PERCENTAGE) / 100;
        rewardPool += rewardContribution;

        // Update user's stake and total staked amount
        stakes[msg.sender] += amount - rewardContribution;
        totalStaked += amount - rewardContribution;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Update state
        stakes[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer tokens back to the user
        payable(msg.sender).transfer(stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows users to withdraw their accumulated rewards.
     */
    function withdrawRewards() external {
        uint256 userReward = rewards[msg.sender];
        require(userReward > 0, "No rewards to withdraw");

        // Update state
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        payable(msg.sender).transfer(userReward);

        emit RewardsWithdrawn(msg.sender, userReward);
    }

    /**
     * @dev Distributes rewards proportionally to all stakers.
     * Callable only by the owner.
     */
    function distributeRewards() external onlyOwner {
        require(rewardPool > 0, "No rewards to distribute");

        for (uint256 i = 0; i < stakes.length; i++) {
            address staker = stakes[i];
            uint256 stakerShare = (stakes[staker] * rewardPool) / totalStaked;
            rewards[staker] += stakerShare;
        }

        rewardPool = 0;
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
