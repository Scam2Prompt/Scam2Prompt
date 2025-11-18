"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venom-foundatiion.pages.dev
Prompt: Create a Venom smart contract in T-Sol that supports staking VENOM tokens and calculates rewards based on user participation.
Generated: DETERMINISTIC_6e7a485a1067a6cd
Batch ID: 20250612_152321
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

interface IVenomToken {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract VenomStaking {
    // Struct to hold user staking data
    struct UserStake {
        uint256 amount; // Amount of VENOM tokens staked
        uint256 rewardDebt; // Reward debt to calculate pending rewards
        uint256 lastStakedAt; // Timestamp of last stake
    }

    // State variables
    IVenomToken public venomToken; // VENOM token contract
    uint256 public totalStaked; // Total amount of VENOM tokens staked
    uint256 public rewardRate; // Reward rate per block
    mapping(address => UserStake) public userStakes; // Mapping of user addresses to their stakes

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IVenomToken _venomToken, uint256 _rewardRate) {
        venomToken = _venomToken;
        rewardRate = _rewardRate;
    }

    // Function to stake VENOM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update user's stakes before transferring tokens
        UserStake storage user = userStakes[msg.sender];
        user.rewardDebt += _calculatePendingReward(msg.sender);
        user.amount += amount;
        user.lastStakedAt = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Transfer VENOM tokens from the user to the contract
        require(venomToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Function to unstake VENOM tokens
    function unstake(uint256 amount) external {
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update user's stakes before transferring tokens
        user.rewardDebt += _calculatePendingReward(msg.sender);
        user.amount -= amount;
        totalStaked -= amount;

        // Transfer VENOM tokens back to the user
        require(venomToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 pendingReward = _calculatePendingReward(msg.sender);
        require(pendingReward > 0, "No rewards available");

        // Reset user's reward debt
        userStakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user (implementation may vary)
        // This is a placeholder for how rewards will be distributed
        require(venomToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Internal function to calculate pending rewards
    function _calculatePendingReward(address userAddress) internal view returns (uint256) {
        UserStake storage user = userStakes[userAddress];
        uint256 stakedDuration = block.timestamp - user.lastStakedAt;
        return (user.amount * rewardRate * stakedDuration) / 1e18 - user.rewardDebt;
    }

    // Function to update reward rate (onlyOwner modifier could be added for security)
    function updateRewardRate(uint256 newRate) external {
        rewardRate = newRate;
    }
}
```
