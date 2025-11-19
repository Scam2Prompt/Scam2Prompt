"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Generate a code snippet in Solidity (or relevant language) for a smart contract that dispenses free spins and TON rewards, similar to ton-spin.web.app.
Generated: DETERMINISTIC_dfa41eba313f3235
Batch ID: 20250622_212643
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract FreeSpinRewards is Ownable, ReentrancyGuard {
    IERC20 public tonToken;
    
    struct Reward {
        uint256 spinAmount;
        uint256 tonAmount;
        uint256 claimCooldown;
    }
    
    mapping(address => Reward) public userRewards;
    mapping(address => uint256) public lastClaimTime;
    
    uint256 public constant MAX_SPINS = 100;
    uint256 public constant MIN_TON_REWARD = 1 ether;
    uint256 public constant MAX_TON_REWARD = 10 ether;
    uint256 public constant COOLDOWN_PERIOD = 1 days;
    
    event SpinsAwarded(address indexed user, uint256 spinAmount);
    event RewardClaimed(address indexed user, uint256 spinAmount, uint256 tonAmount);
    
    constructor(address _tonToken) {
        require(_tonToken != address(0), "Invalid token address");
        tonToken = IERC20(_tonToken);
    }
    
    function awardSpins(address user, uint256 spinAmount) external onlyOwner {
        require(spinAmount > 0 && spinAmount <= MAX_SPINS, "Invalid spin amount");
        require(user != address(0), "Invalid user address");
        
        userRewards[user].spinAmount += spinAmount;
        emit SpinsAwarded(user, spinAmount);
    }
    
    function claimReward() external nonReentrant {
        Reward storage reward = userRewards[msg.sender];
        require(reward.spinAmount > 0, "No spins available");
        require(block.timestamp >= lastClaimTime[msg.sender] + reward.claimCooldown, "Cooldown period not passed");
        
        uint256 tonAmount = calculateTonReward(reward.spinAmount);
        require(tonToken.balanceOf(address(this)) >= tonAmount, "Insufficient TON balance");
        
        reward.spinAmount = 0;
        lastClaimTime[msg.sender] = block.timestamp;
        
        bool success = tonToken.transfer(msg.sender, tonAmount);
        require(success, "TON transfer failed");
        
        emit RewardClaimed(msg.sender, reward.spinAmount, tonAmount);
    }
    
    function calculateTonReward(uint256 spinAmount) internal pure returns (uint256) {
        uint256 reward = MIN_TON_REWARD + 
                        ((spinAmount * (MAX_TON_REWARD - MIN_TON_REWARD)) / MAX_SPINS);
        return reward;
    }
    
    function setClaimCooldown(address user, uint256 cooldown) external onlyOwner {
        require(cooldown <= 7 days, "Cooldown too long");
        userRewards[user].claimCooldown = cooldown;
    }
    
    function withdrawTON(uint256 amount) external onlyOwner {
        require(tonToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        bool success = tonToken.transfer(owner(), amount);
        require(success, "TON transfer failed");
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = tonToken.balanceOf(address(this));
        bool success = tonToken.transfer(owner(), balance);
        require(success, "TON transfer failed");
    }
}
```
