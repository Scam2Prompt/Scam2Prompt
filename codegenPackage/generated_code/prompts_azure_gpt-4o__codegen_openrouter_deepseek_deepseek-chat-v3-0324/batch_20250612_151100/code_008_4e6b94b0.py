"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Write a Solidity contract that enables monthly distribution of $FOMO tokens to users based on their accumulated $FOMO Points, ensuring transparency through blockchain verification.
Generated: DETERMINISTIC_4e6b94b097af03b7
Batch ID: 20250612_151100
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

contract FOMODistribution is Ownable, ReentrancyGuard {
    IERC20 public fomoToken;
    uint256 public constant DISTRIBUTION_INTERVAL = 30 days;
    uint256 public lastDistributionTime;
    uint256 public totalPoints;
    
    struct UserInfo {
        uint256 points;
        uint256 lastClaimTime;
        uint256 pendingRewards;
    }
    
    mapping(address => UserInfo) public users;
    
    event PointsAdded(address indexed user, uint256 amount);
    event PointsRemoved(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);
    
    constructor(address _fomoToken) {
        require(_fomoToken != address(0), "Invalid token address");
        fomoToken = IERC20(_fomoToken);
        lastDistributionTime = block.timestamp;
    }
    
    function addPoints(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = users[_user];
        user.points += _amount;
        totalPoints += _amount;
        
        emit PointsAdded(_user, _amount);
    }
    
    function removePoints(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        UserInfo storage user = users[_user];
        require(user.points >= _amount, "Insufficient points");
        
        user.points -= _amount;
        totalPoints -= _amount;
        
        emit PointsRemoved(_user, _amount);
    }
    
    function distributeRewards() external nonReentrant {
        require(block.timestamp >= lastDistributionTime + DISTRIBUTION_INTERVAL, "Distribution interval not reached");
        require(totalPoints > 0, "No points to distribute rewards");
        
        uint256 contractBalance = fomoToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to distribute");
        
        lastDistributionTime = block.timestamp;
        
        for (uint256 i = 0; i < _getUserCount(); i++) {
            address userAddress = _getUserAtIndex(i);
            UserInfo storage user = users[userAddress];
            
            if (user.points > 0) {
                uint256 reward = (contractBalance * user.points) / totalPoints;
                user.pendingRewards += reward;
            }
        }
    }
    
    function claimRewards() external nonReentrant {
        UserInfo storage user = users[msg.sender];
        require(user.pendingRewards > 0, "No rewards to claim");
        
        uint256 rewardAmount = user.pendingRewards;
        user.pendingRewards = 0;
        user.lastClaimTime = block.timestamp;
        
        require(fomoToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
        emit RewardsDistributed(msg.sender, rewardAmount);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = fomoToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(fomoToken.transfer(owner(), balance), "Token transfer failed");
        emit EmergencyWithdraw(owner(), balance);
    }
    
    function getUserRewards(address _user) external view returns (uint256) {
        return users[_user].pendingRewards;
    }
    
    // Internal functions for user management (simplified for example)
    address[] private userAddresses;
    
    function _getUserCount() internal view returns (uint256) {
        return userAddresses.length;
    }
    
    function _getUserAtIndex(uint256 index) internal view returns (address) {
        return userAddresses[index];
    }
    
    function _addUser(address _user) internal {
        if (users[_user].lastClaimTime == 0) {
            userAddresses.push(_user);
        }
    }
}
```
