"""
Generated Code Metadata:
========================
Original URL: https://playgorund.pages.dev
Prompt: Generate a smart contract in Solidity for distributing $BEYOND rewards based on contribution levels, as described in the Beyond Blitz rewards system.
Generated: DETERMINISTIC_ca2b44a6a51d2ddd
Batch ID: 20250612_153401
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

contract BeyondRewards is Ownable, ReentrancyGuard {
    IERC20 public beyondToken;
    
    // Contribution levels and corresponding reward multipliers
    enum ContributionLevel { 
        NOVICE,     // 1x multiplier
        CONTRIBUTOR, // 1.5x multiplier
        VETERAN,    // 2x multiplier
        CHAMPION    // 3x multiplier
    }
    
    // Reward multiplier for each contribution level (in basis points)
    mapping(ContributionLevel => uint256) public rewardMultipliers;
    
    // User contribution data
    struct UserData {
        ContributionLevel level;
        uint256 contributionPoints;
        uint256 lastClaimTimestamp;
        uint256 totalClaimed;
    }
    
    mapping(address => UserData) public users;
    
    // Total rewards distributed
    uint256 public totalDistributed;
    
    // Base reward rate per point per second
    uint256 public baseRewardRate;
    
    // Events
    event RewardClaimed(address indexed user, uint256 amount);
    event ContributionLevelUpdated(address indexed user, ContributionLevel level);
    event ContributionPointsAdded(address indexed user, uint256 points);
    
    constructor(address _beyondToken) {
        beyondToken = IERC20(_beyondToken);
        
        // Initialize reward multipliers (1x = 10000 basis points)
        rewardMultipliers[ContributionLevel.NOVICE] = 10000;
        rewardMultipliers[ContributionLevel.CONTRIBUTOR] = 15000;
        rewardMultipliers[ContributionLevel.VETERAN] = 20000;
        rewardMultipliers[ContributionLevel.CHAMPION] = 30000;
        
        // Set base reward rate (e.g., 0.0001 tokens per point per second)
        baseRewardRate = 1e14;
    }
    
    /**
     * @dev Set the base reward rate (only owner)
     * @param _rate New base reward rate per point per second
     */
    function setBaseRewardRate(uint256 _rate) external onlyOwner {
        baseRewardRate = _rate;
    }
    
    /**
     * @dev Update a user's contribution level (only owner)
     * @param user Address of the user
     * @param level New contribution level
     */
    function setContributionLevel(address user, ContributionLevel level) external onlyOwner {
        users[user].level = level;
        emit ContributionLevelUpdated(user, level);
    }
    
    /**
     * @dev Add contribution points to a user (only owner)
     * @param user Address of the user
     * @param points Number of points to add
     */
    function addContributionPoints(address user, uint256 points) external onlyOwner {
        users[user].contributionPoints += points;
        emit ContributionPointsAdded(user, points);
    }
    
    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return Amount of pending rewards
     */
    function calculatePendingRewards(address user) public view returns (uint256) {
        UserData storage userData = users[user];
        
        if (userData.lastClaimTimestamp == 0 || userData.contributionPoints == 0) {
            return 0;
        }
        
        uint256 timeElapsed = block.timestamp - userData.lastClaimTimestamp;
        uint256 baseRewards = userData.contributionPoints * timeElapsed * baseRewardRate;
        
        // Apply multiplier based on contribution level
        uint256 multiplier = rewardMultipliers[userData.level];
        return (baseRewards * multiplier) / 10000;
    }
    
    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        address user = msg.sender;
        UserData storage userData = users[user];
        
        require(userData.contributionPoints > 0, "No contribution points");
        require(userData.lastClaimTimestamp > 0, "Not eligible for rewards yet");
        
        uint256 pendingRewards = calculatePendingRewards(user);
        require(pendingRewards > 0, "No rewards to claim");
        
        // Update user data
        userData.lastClaimTimestamp = block.timestamp;
        userData.totalClaimed += pendingRewards;
        
        // Update total distributed
        totalDistributed += pendingRewards;
        
        // Transfer rewards
        require(
            beyondToken.transfer(user, pendingRewards),
            "Token transfer failed"
        );
        
        emit RewardClaimed(user, pendingRewards);
    }
    
    /**
     * @dev Initialize a user for rewards (only owner)
     * @param user Address of the user
     * @param level Initial contribution level
     * @param points Initial contribution points
     */
    function initializeUser(
        address user,
        ContributionLevel level,
        uint256 points
    ) external onlyOwner {
        require(users[user].lastClaimTimestamp == 0, "User already initialized");
        
        users[user] = UserData({
            level: level,
            contributionPoints: points,
            lastClaimTimestamp: block.timestamp,
            totalClaimed: 0
        });
    }
    
    /**
     * @dev Withdraw any accidentally sent ERC20 tokens (only owner)
     * @param token Address of the token contract
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(
            IERC20(token).transfer(owner(), amount),
            "Token transfer failed"
        );
    }
}
```
