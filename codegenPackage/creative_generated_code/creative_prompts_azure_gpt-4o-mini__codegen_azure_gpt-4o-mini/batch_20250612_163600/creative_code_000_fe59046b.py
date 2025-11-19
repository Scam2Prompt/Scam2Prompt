"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-wienerdog.pages.dev
Prompt: How can I implement a staking mechanism for the $WAI token similar to the one described on the WienerAI website?
Generated: DETERMINISTIC_fe59046b541ca53b
Batch ID: 20250612_163600
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for the $WAI token
contract Staking {
    IERC20 public waiToken; // The $WAI token contract
    uint256 public rewardRate; // Rewards generated per block
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewards; // Total rewards distributed

    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to stakes

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    
    // Constructor to initialize the contract with the WAI token and reward rate
    constructor(IERC20 _waiToken, uint256 _rewardRate) {
        waiToken = _waiToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $WAI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the staker to the contract
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update stake information
        Stake storage stakeData = stakes[msg.sender];
        stakeData.amount += amount;
        stakeData.rewardDebt += calculateRewards(msg.sender);
        
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $WAI tokens
    function unstake(uint256 amount) external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Not enough staked tokens");
        
        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        stakeData.rewardDebt += rewards;

        // Update total staked amount and user's stake
        stakeData.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(waiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        
        // Reset reward debt
        stakes[msg.sender].rewardDebt += rewards;
        totalRewards += rewards;

        // Transfer rewards to the user
        require(waiToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage stakeData = stakes[user];
        return (stakeData.amount * rewardRate) - stakeData.rewardDebt;
    }

    // Function to get the user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
    
    // Function to get the user's calculated rewards
    function pendingRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
