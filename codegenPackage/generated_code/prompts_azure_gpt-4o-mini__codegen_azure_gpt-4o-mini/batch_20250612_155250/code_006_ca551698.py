"""
Generated Code Metadata:
========================
Original URL: https://synthesizations.netlify.app
Prompt: Write a code example for staking and unstaking tokens in a decentralized finance application.
Generated: DETERMINISTIC_ca5516984cdd13a8
Batch ID: 20250612_155250
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a decentralized finance application
contract Staking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // User stakes mapping
    mapping(address => uint256) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender] += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender] -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to view the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
