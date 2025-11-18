"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Write a Solidity function for calculating staking rewards based on APY and lock duration, similar to the $SCOTTY staking mechanism.
Generated: DETERMINISTIC_c898d1b8dece6b66
Batch ID: 20250612_152109
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

/// @title StakingRewards
/// @dev This contract calculates staking rewards based on Annual Percentage Yield (APY) and lock duration.
contract StakingRewards {
    
    // State variable to store the Annual Percentage Yield
    uint256 public apy; // APY in percentage (e.g., 5 for 5%)
    
    // Event emitted when staking is performed
    event Staked(address indexed user, uint256 amount, uint256 duration);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Struct to store staking information for a user
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when the stake was created
        uint256 duration; // Duration of the stake in seconds
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    /// @dev Sets the APY for staking rewards.
    /// @param _apy The annual percentage yield in percentage (e.g., 5 for 5%).
    function setAPY(uint256 _apy) external {
        require(_apy > 0, "APY must be greater than zero");
        apy = _apy;
    }

    /// @dev Allows a user to stake a specified amount for a given duration.
    /// @param amount The amount to stake.
    /// @param duration The duration of the stake in seconds.
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(duration > 0, "Stake duration must be greater than zero");
        
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration
        });

        emit Staked(msg.sender, amount, duration);
    }

    /// @dev Calculates the staking rewards based on the user's stake.
    /// @param user The address of the user for whom to calculate rewards.
    /// @return The calculated reward amount.
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No stake found for user");
        
        uint256 timeStaked = block.timestamp - userStake.startTime; // Time in seconds the amount has been staked
        require(timeStaked >= userStake.duration, "Stake duration not yet completed");

        // Calculate rewards using the formula: (amount * APY * time / (365 days)) / 100
        uint256 reward = (userStake.amount * apy * timeStaked) / (365 days * 100);
        return reward;
    }

    /// @dev Allows users to claim their rewards after the staking duration is complete.
    function claimRewards() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found for user");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake duration not yet completed");

        uint256 reward = calculateReward(msg.sender);
        
        // Resetting the user's stake
        delete stakes[msg.sender];

        // Transfer the reward to the user (this is a placeholder; actual transfer logic should be implemented)
        // e.g., token.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }
}
```
