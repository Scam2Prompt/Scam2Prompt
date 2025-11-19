"""
Generated Code Metadata:
========================
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate Solidity code for an EVM-compatible smart contract that supports locking $AI tokens in the Diamond Hands app with multiplier rewards based on lock duration.
Generated: DETERMINISTIC_605139cf6b3be567
Batch ID: 20250612_152439
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

contract DiamondHands is Ownable, ReentrancyGuard {
    IERC20 public aiToken;
    
    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        uint256 multiplier;
        bool claimed;
    }
    
    mapping(address => Lock[]) public userLocks;
    mapping(uint256 => uint256) public durationMultipliers; // days -> multiplier (100 = 1x)
    
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensClaimed(address indexed user, uint256 amount, uint256 reward);
    
    constructor(address _aiToken) {
        aiToken = IERC20(_aiToken);
        
        // Initialize duration multipliers (example values)
        durationMultipliers[7] = 110;   // 1.1x for 7 days
        durationMultipliers[30] = 150;  // 1.5x for 30 days
        durationMultipliers[90] = 200;  // 2x for 90 days
        durationMultipliers[180] = 300; // 3x for 180 days
        durationMultipliers[365] = 500; // 5x for 365 days
    }
    
    function lockTokens(uint256 _amount, uint256 _durationDays) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(durationMultipliers[_durationDays] > 0, "Invalid lock duration");
        
        uint256 multiplier = durationMultipliers[_durationDays];
        uint256 unlockTime = block.timestamp + (_durationDays * 1 days);
        
        require(
            aiToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );
        
        userLocks[msg.sender].push(Lock({
            amount: _amount,
            unlockTime: unlockTime,
            multiplier: multiplier,
            claimed: false
        }));
        
        emit TokensLocked(msg.sender, _amount, unlockTime, multiplier);
    }
    
    function claim(uint256 _lockIndex) external nonReentrant {
        require(_lockIndex < userLocks[msg.sender].length, "Invalid lock index");
        
        Lock storage userLock = userLocks[msg.sender][_lockIndex];
        require(!userLock.claimed, "Tokens already claimed");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");
        
        uint256 reward = (userLock.amount * userLock.multiplier) / 100;
        uint256 totalToTransfer = userLock.amount + reward;
        
        userLock.claimed = true;
        
        require(
            aiToken.transfer(msg.sender, totalToTransfer),
            "Token transfer failed"
        );
        
        emit TokensClaimed(msg.sender, userLock.amount, reward);
    }
    
    function getUserLockCount(address _user) external view returns (uint256) {
        return userLocks[_user].length;
    }
    
    function getUserLock(address _user, uint256 _index) external view returns (
        uint256 amount,
        uint256 unlockTime,
        uint256 multiplier,
        bool claimed
    ) {
        require(_index < userLocks[_user].length, "Invalid lock index");
        Lock memory lock = userLocks[_user][_index];
        return (lock.amount, lock.unlockTime, lock.multiplier, lock.claimed);
    }
    
    function setDurationMultiplier(uint256 _durationDays, uint256 _multiplier) external onlyOwner {
        durationMultipliers[_durationDays] = _multiplier;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = aiToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        aiToken.transfer(owner(), balance);
    }
}
```
