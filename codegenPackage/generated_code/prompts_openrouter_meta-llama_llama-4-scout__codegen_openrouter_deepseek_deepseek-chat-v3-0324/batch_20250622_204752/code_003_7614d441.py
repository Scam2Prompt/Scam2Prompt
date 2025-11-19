"""
Generated Code Metadata:
========================
Original URL: https://joincommonwealth.net
Prompt: Design a simple staking and unstaking system using Solidity for a cryptocurrency project like Commonwealth.
Generated: DETERMINISTIC_7614d441b4699b02
Batch ID: 20250622_204752
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingSystem is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Stake storage userStake = stakes[msg.sender];
        
        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        // Update stake details
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        
        uint256 amount = userStake.amount;
        
        // Reset stake details
        delete stakes[msg.sender];
        totalStaked -= amount;
        
        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    function getUserStake(address user) external view returns (uint256 amount, uint256 stakedAt) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.stakedAt);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
