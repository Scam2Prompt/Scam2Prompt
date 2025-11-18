"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Create a Solidity function that calculates staking rewards based on the number of $STARS tokens held, incentivizing long-term holding.
Generated: DETERMINISTIC_8430987dd840bf46
Batch ID: 20250612_154307
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
 * @title StakingRewards
 * @dev Smart contract to calculate staking rewards based on $STARS tokens held and incentivize long-term holding.
 */
contract StakingRewards {
    // Mapping to track staker's balances and their staking timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTime;

    // Annual reward rate (e.g., 10% -> 1000 basis points)
    uint256 public constant ANNUAL_REWARD_RATE_BP = 1000; // 10% in basis points (BP)
    uint256 public constant BASIS_POINTS_DIVISOR = 10000; // Basis divisor for calculating percentage rewards

    // Event to track staking and reward claims
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewards);

    /**
     * @notice Stake $STARS tokens into the contract.
     * @param amount Number of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Update the staked balance
        stakedBalances[msg.sender] += amount;

        // Update the staking start time
        if (stakingStartTime[msg.sender] == 0) {
            stakingStartTime[msg.sender] = block.timestamp; // Set staking start time if not already set
        }

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @notice Calculate staking rewards for the caller based on the holding duration.
     * @return rewards Amount of rewards earned.
     */
    function calculateRewards() public view returns (uint256 rewards) {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens found");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender]; // Duration in seconds
        uint256 annualReward = (stakedAmount * ANNUAL_REWARD_RATE_BP) / BASIS_POINTS_DIVISOR;

        // Rewards are proportional to staking duration (in seconds) divided by total seconds in a year
        rewards = (annualReward * stakingDuration) / 365 days;
        return rewards;
    }

    /**
     * @notice Claim staking rewards for the caller.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards();
        require(rewards > 0, "No rewards available for claiming");

        // Reset staking start time to current timestamp after claiming rewards
        stakingStartTime[msg.sender] = block.timestamp;

        // Normally, tokens would be transferred here (e.g., from a rewards pool)
        // For simplicity, assuming a rewards pool is managed separately.

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Withdraw staked tokens and stop staking.
     */
    function withdrawStakedTokens() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens found");

        // Calculate and claim rewards before withdrawing
        claimRewards();

        // Reset staked balance and staking start time
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Normally, tokens would be transferred back to the user here
        // For simplicity, assuming token withdrawal is handled separately.
    }
}
```
