"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Create a Solidity contract that implements a basic staking mechanism for the $TGC token, allowing users to earn passive income.
Generated: DETERMINISTIC_ac9fbc9efb753c90
Batch ID: 20250612_155140
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

// Interface for the ERC20 token (TGC)
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Staking contract for the $TGC token
contract TGCStaking {
    IERC20 public tgcToken; // The address of the $TGC token contract

    // Structure to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
    }

    // Mapping from user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the token address
    constructor(address _tgcToken) {
        require(_tgcToken != address(0), "Invalid token address");
        tgcToken = IERC20(_tgcToken);
    }

    // Function to stake $TGC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(tgcToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from user to the contract
        tgcToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $TGC tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the staked amount and duration
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        
        // Reset the user's stake information
        delete stakes[msg.sender];

        // Transfer staked tokens and rewards back to the user
        tgcToken.transfer(msg.sender, userStake.amount + reward);
        
        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to calculate reward based on staked amount and time
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        // Example reward calculation: 10% of staked amount per year (adjustable)
        uint256 stakingDuration = block.timestamp - timestamp; // Duration in seconds
        uint256 rewardRate = 10; // 10% annual reward
        uint256 reward = (amount * rewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }

    // Function to check the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
