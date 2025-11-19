"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20tokenclaim.pages.dev
Prompt: Write a Solidity function for the $DOGE20 staking smart contract that calculates rewards based on the fixed supply of 140,000,000,000 tokens and the staking pool size.
Generated: DETERMINISTIC_2b2aec79186ca823
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract manages the staking functionality for the $DOGE20 token.
 */
contract DOGE20Staking {
    // Fixed supply of DOGE20 tokens
    uint256 public constant TOTAL_SUPPLY = 140_000_000_000;

    // Staking pool size
    uint256 public stakingPoolSize;

    // Mapping of user staking balances
    mapping(address => uint256) public userStakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public userRewardBalances;

    // Reward rate per block (adjust as needed)
    uint256 public rewardRatePerBlock;

    /**
     * @notice Initializes the staking contract.
     * @param _rewardRatePerBlock The reward rate per block.
     */
    constructor(uint256 _rewardRatePerBlock) {
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @notice Calculates the reward for a user based on their staking balance and the staking pool size.
     * @param _user The user's address.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        // Get the user's staking balance
        uint256 userStakingBalance = userStakingBalances[_user];

        // Check if the user has a staking balance
        if (userStakingBalance == 0) {
            return 0;
        }

        // Calculate the reward based on the user's staking balance and the staking pool size
        uint256 reward = (userStakingBalance * rewardRatePerBlock * block.number) / stakingPoolSize;

        // Ensure the reward does not exceed the remaining tokens in the staking pool
        uint256 remainingTokens = TOTAL_SUPPLY - stakingPoolSize;
        reward = reward > remainingTokens ? remainingTokens : reward;

        return reward;
    }

    /**
     * @notice Updates the user's staking balance and reward balance.
     * @param _user The user's address.
     * @param _amount The amount to stake or unstake.
     * @param _isStaking Whether the user is staking or unstaking.
     */
    function updateStakingBalance(address _user, uint256 _amount, bool _isStaking) public {
        // Check if the user is staking or unstaking
        if (_isStaking) {
            // Increase the staking pool size
            stakingPoolSize += _amount;

            // Update the user's staking balance
            userStakingBalances[_user] += _amount;
        } else {
            // Decrease the staking pool size
            stakingPoolSize -= _amount;

            // Update the user's staking balance
            userStakingBalances[_user] -= _amount;
        }

        // Calculate and update the user's reward balance
        uint256 reward = calculateReward(_user);
        userRewardBalances[_user] += reward;
    }

    /**
     * @notice Claims the reward for a user.
     * @param _user The user's address.
     */
    function claimReward(address _user) public {
        // Get the user's reward balance
        uint256 rewardBalance = userRewardBalances[_user];

        // Check if the user has a reward balance
        if (rewardBalance == 0) {
            revert("User has no reward balance");
        }

        // Update the user's reward balance
        userRewardBalances[_user] = 0;

        // Transfer the reward to the user (implement token transfer logic here)
        // For demonstration purposes, this is omitted
    }

    /**
     * @notice Updates the reward rate per block.
     * @param _newRewardRatePerBlock The new reward rate per block.
     */
    function updateRewardRatePerBlock(uint256 _newRewardRatePerBlock) public {
        // Only allow authorized accounts to update the reward rate
        // Implement access control logic here (e.g., onlyOwner modifier)
        // For demonstration purposes, this is omitted

        rewardRatePerBlock = _newRewardRatePerBlock;
    }
}
```
