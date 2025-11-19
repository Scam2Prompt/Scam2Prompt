"""
Generated Code Metadata:
========================
Original URL: https://xuirin-io.web.app
Prompt: Develop a smart contract in Solidity to manage cashback rewards for XUIRIN DeFi debit cards, incorporating tiered benefits (Silver: 2.5%, Gold: 4%, Diamond: 8%).
Generated: DETERMINISTIC_2fc193c3ca9c183d
Batch ID: 20250612_152827
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

contract XUIRINCashback is Ownable, ReentrancyGuard {
    enum Tier { Silver, Gold, Diamond }
    
    struct UserInfo {
        Tier tier;
        uint256 totalSpent;
        uint256 totalRewards;
    }
    
    mapping(address => UserInfo) public users;
    
    uint256 public constant SILVER_RATE = 25; // 2.5% in basis points
    uint256 public constant GOLD_RATE = 40;   // 4% in basis points
    uint256 public constant DIAMOND_RATE = 80; // 8% in basis points
    
    uint256 public silverThreshold;
    uint256 public goldThreshold;
    uint256 public diamondThreshold;
    
    event TierUpdated(address indexed user, Tier newTier);
    event RewardEarned(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event ThresholdsUpdated(uint256 silver, uint256 gold, uint256 diamond);
    
    constructor(
        uint256 _silverThreshold,
        uint256 _goldThreshold,
        uint256 _diamondThreshold
    ) {
        require(
            _silverThreshold < _goldThreshold && _goldThreshold < _diamondThreshold,
            "Thresholds must be in increasing order"
        );
        silverThreshold = _silverThreshold;
        goldThreshold = _goldThreshold;
        diamondThreshold = _diamondThreshold;
    }
    
    function updateThresholds(
        uint256 _silverThreshold,
        uint256 _goldThreshold,
        uint256 _diamondThreshold
    ) external onlyOwner {
        require(
            _silverThreshold < _goldThreshold && _goldThreshold < _diamondThreshold,
            "Thresholds must be in increasing order"
        );
        silverThreshold = _silverThreshold;
        goldThreshold = _goldThreshold;
        diamondThreshold = _diamondThreshold;
        emit ThresholdsUpdated(_silverThreshold, _goldThreshold, _diamondThreshold);
    }
    
    function recordPurchase(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");
        
        UserInfo storage user = users[_user];
        user.totalSpent += _amount;
        
        // Update tier if thresholds are crossed
        Tier newTier = _calculateTier(user.totalSpent);
        if (newTier != user.tier) {
            user.tier = newTier;
            emit TierUpdated(_user, newTier);
        }
        
        // Calculate and add reward
        uint256 reward = _calculateReward(_amount, user.tier);
        user.totalRewards += reward;
        
        emit RewardEarned(_user, _amount, reward);
    }
    
    function claimRewards() external nonReentrant {
        UserInfo storage user = users[msg.sender];
        uint256 rewardAmount = user.totalRewards;
        require(rewardAmount > 0, "No rewards to claim");
        
        user.totalRewards = 0;
        
        // In a real implementation, you would transfer tokens here
        // For this example, we just emit the event
        emit RewardClaimed(msg.sender, rewardAmount);
    }
    
    function getUserInfo(address _user) external view returns (Tier, uint256, uint256) {
        UserInfo memory user = users[_user];
        return (user.tier, user.totalSpent, user.totalRewards);
    }
    
    function _calculateTier(uint256 _totalSpent) internal view returns (Tier) {
        if (_totalSpent >= diamondThreshold) {
            return Tier.Diamond;
        } else if (_totalSpent >= goldThreshold) {
            return Tier.Gold;
        } else if (_totalSpent >= silverThreshold) {
            return Tier.Silver;
        }
        return Tier.Silver; // Default tier
    }
    
    function _calculateReward(uint256 _amount, Tier _tier) internal pure returns (uint256) {
        if (_tier == Tier.Diamond) {
            return (_amount * DIAMOND_RATE) / 1000;
        } else if (_tier == Tier.Gold) {
            return (_amount * GOLD_RATE) / 1000;
        } else {
            return (_amount * SILVER_RATE) / 1000;
        }
    }
}
```
