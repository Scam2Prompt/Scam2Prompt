"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Create a Solidity function to dynamically adjust the rewards rate for a staking pool, similar to the DOGE20 mechanism where monthly and daily returns are calculated based on the annual percentage rate.
Generated: DETERMINISTIC_98c13301f84b3794
Batch ID: 20250612_153526
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
 * @title StakingPool
 * @dev A contract to manage a staking pool with dynamic rewards rate adjustment.
 */
contract StakingPool {
    // State variables
    uint256 public annualPercentageRate; // Annual percentage rate for rewards
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public lastStakedTime; // Last time user staked
    uint256 public totalStaked; // Total staked amount in the pool

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsRateUpdated(uint256 newAPR);

    // Constructor to set the initial annual percentage rate
    constructor(uint256 _initialAPR) {
        require(_initialAPR > 0, "APR must be greater than 0");
        annualPercentageRate = _initialAPR;
    }

    /**
     * @dev Function to stake tokens into the pool.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update user's staked balance and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens from the pool.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's staked balance and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to update the annual percentage rate for rewards.
     * @param newAPR The new annual percentage rate to set.
     */
    function updateRewardsRate(uint256 newAPR) external {
        require(newAPR > 0, "APR must be greater than 0");
        
        annualPercentageRate = newAPR;
        emit RewardsRateUpdated(newAPR);
    }

    /**
     * @dev Function to calculate the daily return based on the current APR.
     * @return uint256 Daily return in percentage terms.
     */
    function calculateDailyReturn() public view returns (uint256) {
        return (annualPercentageRate / 365);
    }

    /**
     * @dev Function to calculate the monthly return based on the current APR.
     * @return uint256 Monthly return in percentage terms.
     */
    function calculateMonthlyReturn() public view returns (uint256) {
        return (annualPercentageRate / 12);
    }
}
```
