"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.network
Prompt: Write a smart contract in Solidity that uses Aave's staking mechanism to secure the protocol and earn rewards.
Generated: DETERMINISTIC_ae8a069e7a4c98ea
Batch ID: 20250612_154703
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

// Importing Aave's staking interface
import "@aave/core-v3/contracts/interfaces/IAaveStakedToken.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract allows users to stake tokens in Aave's staking mechanism
contract AaveStaking is Ownable {
    IAaveStakedToken public stakedToken; // Aave's staked token interface
    mapping(address => uint256) private _stakes; // Mapping to track user stakes

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the Aave staked token address
    constructor(address _stakedTokenAddress) {
        require(_stakedTokenAddress != address(0), "Invalid staked token address");
        stakedToken = IAaveStakedToken(_stakedTokenAddress);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to the contract
        stakedToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        _stakes[msg.sender] += amount;
        
        // Emit stake event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's stake before transferring tokens
        _stakes[msg.sender] -= amount;
        
        // Transfer tokens back to the user
        stakedToken.transfer(msg.sender, amount);
        
        // Emit unstake event
        emit Unstaked(msg.sender, amount);
    }

    // Function to view user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return _stakes[user];
    }

    // Function to withdraw all staked tokens (for owner)
    function withdrawAllStakedTokens() external onlyOwner {
        uint256 totalStaked = stakedToken.balanceOf(address(this));
        require(totalStaked > 0, "No tokens to withdraw");
        stakedToken.transfer(owner(), totalStaked);
    }
}
```
