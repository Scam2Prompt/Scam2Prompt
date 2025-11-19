"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-en.web.app
Prompt: Create a staking mechanism for the Rebel Satoshi ecosystem that rewards users with percentage returns for locking up their $RBLZ tokens.
Generated: DETERMINISTIC_b5c68a86a1e7b872
Batch ID: 20250612_161616
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for the Rebel Satoshi ecosystem
contract RebelSatoshiStaking {
    IERC20 public rblzToken; // ERC20 token contract
    uint256 public rewardRate; // Percentage return on staked amount (in basis points)
    uint256 public totalStaked; // Total amount staked in the contract

    // Struct to hold user staking data
    struct Staker {
        uint256 amount; // Amount staked by the user
        uint256 reward; // Accumulated rewards
        uint256 lastStakedAt; // Last time the user staked
    }

    mapping(address => Staker) private stakers; // Mapping of user addresses to their staking data

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _rblzToken, uint256 _rewardRate) {
        rblzToken = _rblzToken;
        rewardRate = _rewardRate; // Set reward rate (in basis points, e.g., 500 for 5%)
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(rblzToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        Staker storage staker = stakers[msg.sender];
        
        // Update total staked amount
        totalStaked += amount;

        // Calculate rewards for previously staked amount
        if (staker.amount > 0) {
            staker.reward += calculateReward(staker.amount, staker.lastStakedAt);
        }

        // Update staker data
        staker.amount += amount;
        staker.lastStakedAt = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        staker.reward += calculateReward(staker.amount, staker.lastStakedAt);

        // Update staker data
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(rblzToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.reward + calculateReward(staker.amount, staker.lastStakedAt);
        require(reward > 0, "No rewards to claim");

        // Reset rewards after claiming
        staker.reward = 0;
        staker.lastStakedAt = block.timestamp;

        // Transfer rewards to user
        require(rblzToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate the reward based on staked amount and time
    function calculateReward(uint256 amount, uint256 lastStakedAt) internal view returns (uint256) {
        uint256 duration = block.timestamp - lastStakedAt; // Duration in seconds
        uint256 reward = (amount * rewardRate * duration) / 10000 / 365 days; // Annualized reward
        return reward;
    }

    // Function to get staker information
    function getStakerInfo(address user) external view returns (uint256 amount, uint256 reward) {
        Staker storage staker = stakers[user];
        amount = staker.amount;
        reward = staker.reward + calculateReward(staker.amount, staker.lastStakedAt);
    }
}
```
