"""
Generated Code Metadata:
========================
Original URL: https://arcticpablotoken.world
Prompt: Develop a staking mechanism for Arctic Pablo tokens ($APC), including functions for staking, unstaking, and updating the user's balance.
Generated: DETERMINISTIC_7aee29f4ceca3bf4
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ArcticPabloStaking {
    // State variables
    IERC20 public apcToken; // The token being staked
    mapping(address => uint256) public stakedBalances; // User's staked balance
    mapping(address => uint256) public stakingTimestamps; // Timestamp of when the user staked
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _apcToken) {
        apcToken = _apcToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(apcToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        apcToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        apcToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the user's staked balance
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
