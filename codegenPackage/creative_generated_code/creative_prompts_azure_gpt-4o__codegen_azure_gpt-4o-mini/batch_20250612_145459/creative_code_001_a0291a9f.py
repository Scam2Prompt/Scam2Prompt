"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Generate code for a staking mechanism on Solana that calculates compound interest for a 70% APY, distributing rewards every epoch (≈2 days), and ensures fair distribution by capping annual rewards at 10,000 tokens.
Generated: DETERMINISTIC_a0291a9f41d14e29
Batch ID: 20250612_145459
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract Staking is Ownable {
    IERC20 public stakingToken; // Token being staked
    uint256 public totalStaked; // Total amount staked
    uint256 public rewardRate = 7000; // 70% APY expressed in basis points (7000 bps)
    uint256 public maxAnnualReward = 10000 * 1e18; // Cap on annual rewards
    uint256 public lastRewardTime; // Last time rewards were distributed
    uint256 public epochDuration = 2 days; // Duration of each epoch
    mapping(address => uint256) public stakedBalances; // User's staked balance
    mapping(address => uint256) public userRewards; // User's accumulated rewards

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        lastRewardTime = block.timestamp;
    }

    // Stake tokens to the contract
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update rewards before staking
        _updateRewards(msg.sender);
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    // Claim rewards for a user
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");
        
        // Reset user's rewards
        userRewards[msg.sender] = 0;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, rewards);
        
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        // Calculate time passed since last reward distribution
        uint256 timePassed = block.timestamp - lastRewardTime;
        
        // If an epoch has finished, distribute rewards
        if (timePassed >= epochDuration) {
            uint256 epochsPassed = timePassed / epochDuration;
            uint256 totalReward = (totalStaked * rewardRate * epochsPassed) / 10000;

            // Ensure total rewards do not exceed the cap
            if (totalReward > maxAnnualReward) {
                totalReward = maxAnnualReward;
            }

            // Distribute rewards proportionally to all stakers
            for (uint256 i = 0; i < totalStaked; i++) {
                address staker = /* logic to get staker address */; // This requires extra logic to maintain list of stakers
                uint256 userReward = (stakedBalances[staker] * totalReward) / totalStaked;
                userRewards[staker] += userReward;
            }

            // Update last reward time
            lastRewardTime = block.timestamp;
        }
    }

    // View function to see the pending rewards for a user
    function pendingRewards(address user) external view returns (uint256) {
        uint256 timePassed = block.timestamp - lastRewardTime;
        uint256 epochsPassed = timePassed / epochDuration;
        uint256 totalReward = (totalStaked * rewardRate * epochsPassed) / 10000;

        // Calculate the user's pending rewards
        uint256 userReward = (stakedBalances[user] * totalReward) / totalStaked;
        return userRewards[user] + userReward;
    }
}
```
Note: Replace `/* logic to get staker address */` with appropriate logic for tracking stakers, such as maintaining an array or mapping to record staker addresses. This code is simplified and may need additional considerations for gas efficiency and security in a production environment.
