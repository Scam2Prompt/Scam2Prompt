"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Write a function in Solidity that calculates individual staking rewards for BTC20 based on the percentage of the staking pool and the number of tokens staked.
Generated: DETERMINISTIC_52721595b0e96bac
Batch ID: 20250612_151333
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

contract StakingRewards {
    // State variables
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    uint256 public rewardPool; // Total rewards available for distribution
    mapping(address => uint256) public stakedTokens; // Mapping of staker addresses to their staked tokens

    // Event to log staking
    event Staked(address indexed user, uint256 amount);
    
    // Event to log rewards calculation
    event RewardsCalculated(address indexed user, uint256 rewards);

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update total staked and individual staked amount
        totalStaked += _amount;
        stakedTokens[msg.sender] += _amount;

        // Emit staking event
        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards for an individual staker
    function calculateRewards(address _staker) external view returns (uint256) {
        uint256 userStakedAmount = stakedTokens[_staker];
        require(userStakedAmount > 0, "No tokens staked by the user");
        require(totalStaked > 0, "Total staked amount must be greater than 0");
        
        // Calculate rewards based on user stake as a percentage of the total staked
        uint256 rewards = (userStakedAmount * rewardPool) / totalStaked;
        
        return rewards;
    }

    // Function to set the reward pool (for example, after a new reward distribution)
    function setRewardPool(uint256 _amount) external {
        require(_amount >= 0, "Reward pool amount cannot be negative");
        rewardPool = _amount;
    }

    // Function to withdraw staked tokens (not part of original request, but often necessary)
    function withdraw(uint256 _amount) external {
        uint256 userStakedAmount = stakedTokens[msg.sender];
        require(userStakedAmount >= _amount, "Insufficient staked amount");

        // Update the staking state
        totalStaked -= _amount;
        stakedTokens[msg.sender] -= _amount;

        // Logic to transfer tokens back to the user should be here (omitted for simplicity)

        // Emit a withdrawal event (optional, not included)
    }
}
```
