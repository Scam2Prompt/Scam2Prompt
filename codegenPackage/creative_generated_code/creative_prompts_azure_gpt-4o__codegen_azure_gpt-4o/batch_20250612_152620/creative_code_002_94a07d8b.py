"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Using Solidity, write a smart contract function to distribute $SCOTTY token rewards dynamically based on the annual return percentage and the user's share of the staking pool.
Generated: DETERMINISTIC_94a07d8bfd49e634
Batch ID: 20250612_152620
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

/// @title TokenRewardDistributor
/// @notice A smart contract to dynamically distribute $SCOTTY token rewards based on annual return percentage and user's share of the staking pool.
contract TokenRewardDistributor {
    IERC20 public scottyToken; // Interface for interacting with the $SCOTTY token contract
    uint256 public annualReturnPercentage; // Annual return percentage (e.g., 5% -> 500 as basis points)
    uint256 public poolTotalStaked; // Total amount staked in the pool

    mapping(address => uint256) public userStakes; // Amount staked by each user
    mapping(address => uint256) public userLastClaimTime; // Timestamp of the user's last reward claim

    uint256 constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    /// @notice Constructor function to initialize the contract
    /// @param _scottyToken Address of the $SCOTTY token contract
    /// @param _annualReturnPercentage Annual return percentage in basis points (e.g., 500 for 5%)
    constructor(address _scottyToken, uint256 _annualReturnPercentage) {
        require(_scottyToken != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0 && _annualReturnPercentage <= 10000, "Invalid annual return percentage");

        scottyToken = IERC20(_scottyToken);
        annualReturnPercentage = _annualReturnPercentage;
    }

    /// @notice Function to update the stake for a user
    /// @dev This should be called when a user stakes or unstakes their tokens
    /// @param user Address of the user
    /// @param newStakeAmount Updated amount of tokens staked for the user
    function updateStake(address user, uint256 newStakeAmount) external {
        require(user != address(0), "Invalid user address");
        require(newStakeAmount >= 0, "Stake amount cannot be negative");

        poolTotalStaked = poolTotalStaked - userStakes[user] + newStakeAmount; // Update the pool total
        userStakes[user] = newStakeAmount; // Update the user's stake
        userLastClaimTime[user] = block.timestamp; // Reset the last claim time for the user
    }

    /// @notice Function to claim rewards for a user based on their share in the staking pool
    /// @dev Rewards are calculated dynamically based on the annual return percentage
    function claimRewards() external {
        address user = msg.sender;
        require(userStakes[user] > 0, "No tokens staked");

        uint256 lastClaimTime = userLastClaimTime[user];
        require(lastClaimTime != 0, "Invalid claim time");

        // Calculate the rewards based on the time elapsed since the last claim
        uint256 timeElapsed = block.timestamp - lastClaimTime;
        uint256 userShare = userStakes[user];
        uint256 reward = calculateReward(userShare, timeElapsed);

        // Update the last claim time
        userLastClaimTime[user] = block.timestamp;

        // Transfer the rewards to the user
        require(scottyToken.transfer(user, reward), "Reward transfer failed");
    }

    /// @notice Helper function to calculate rewards dynamically
    /// @param userShare Amount of tokens staked by the user
    /// @param timeElapsed Time elapsed since the user's last reward claim
    /// @return reward Amount of $SCOTTY tokens to be rewarded
    function calculateReward(uint256 userShare, uint256 timeElapsed) internal view returns (uint256) {
        if (poolTotalStaked == 0) {
            return 0; // No rewards if the pool is empty
        }

        // Reward formula: (userShare / poolTotalStaked) * annualReturnPercentage * timeElapsed / SECONDS_IN_YEAR
        uint256 reward = (userShare * annualReturnPercentage * timeElapsed) / (poolTotalStaked * SECONDS_IN_YEAR * 10000);
        return reward;
    }
}

/// @dev Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
