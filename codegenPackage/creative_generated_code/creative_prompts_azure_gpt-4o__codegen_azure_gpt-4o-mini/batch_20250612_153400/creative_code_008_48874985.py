"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-live.pages.dev
Prompt: Write a function in Solidity to withdraw staked DOGE20 tokens and update the user's staking balance and percentage of the pool, following the rules of the Dogecoin20 staking system.
Generated: DETERMINISTIC_4887498519c06d9a
Batch ID: 20250612_153400
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

// Import the interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// The Dogecoin20 Staking Contract
contract Dogecoin20Staking {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    mapping(address => uint256) public stakedBalance; // User staked balance
    uint256 public totalStaked; // Total staked in the contract

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token contract address
    constructor(address _doge20Token) {
        doge20Token = IERC20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        doge20Token.transfer(msg.sender, amount);
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked DOGE20 tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's staked balance and total staked
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        bool success = doge20Token.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the user's staked balance
    function getUserStakedBalance(address user) external view returns (uint256) {
        return stakedBalance[user];
    }

    // Function to get the total staked balance
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
