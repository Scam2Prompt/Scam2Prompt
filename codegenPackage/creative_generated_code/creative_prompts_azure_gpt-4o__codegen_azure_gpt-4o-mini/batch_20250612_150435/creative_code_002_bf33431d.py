"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Create a smart contract in Solidity for staking CRUDO tokens, including functionality for calculating rewards based on the amount staked and duration.
Generated: DETERMINISTIC_bf33431d426d5bba
Batch ID: 20250612_150435
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

// Interface for the CRUDO token
interface ICRUDOToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for CRUDO tokens
contract StakingContract {
    // Token details
    ICRUDOToken public crudoToken;

    // Struct to hold information about each staking user
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 startTime;   // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;
    
    // Reward rate in tokens per second
    uint256 public rewardRate = 1e18; // 1 CRUDO token reward per second per token staked

    // Events for logging stakes and withdrawals
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the CRUDO token address
    constructor(address _crudoToken) {
        crudoToken = ICRUDOToken(_crudoToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(crudoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 elapsedTime = block.timestamp - userStake.startTime;
        return (userStake.amount * elapsedTime * rewardRate) / 1e18;
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to the user
        require(crudoToken.transfer(msg.sender, totalAmount), "Transfer failed");
        require(crudoToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Withdrawn(msg.sender, totalAmount, reward);
    }
}
```
