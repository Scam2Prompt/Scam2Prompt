"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Generate a smart contract code to manage the distribution of rewards and points on a blockchain-based platform like Everyworld, ensuring transparency and fairness.
Generated: DETERMINISTIC_c4815bb10ea4e9f4
Batch ID: 20250622_210053
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

contract RewardDistribution is Ownable, ReentrancyGuard {
    // Struct to store user information
    struct UserInfo {
        uint256 points;
        uint256 pendingRewards;
        uint256 lastClaimTime;
    }

    // Reward token interface
    IERC20 public rewardToken;

    // Mapping to store user information
    mapping(address => UserInfo) public users;

    // Total points in the system
    uint256 public totalPoints;

    // Reward rate (tokens per point per second)
    uint256 public rewardRate;

    // Last update time for rewards
    uint256 public lastUpdateTime;

    // Events
    event PointsAdded(address indexed user, uint256 amount);
    event PointsRemoved(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Modifier to update rewards before any point or reward operation
    modifier updateRewards(address user) {
        if (totalPoints > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewardsToDistribute = timeElapsed * rewardRate;
            
            if (rewardsToDistribute > 0) {
                uint256 rewardsPerPoint = rewardsToDistribute / totalPoints;
                users[user].pendingRewards += users[user].points * rewardsPerPoint;
            }
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Set the reward distribution rate
     * @param _rewardRate New reward rate (tokens per point per second)
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Add points to a user
     * @param user Address of the user
     * @param amount Points to add
     */
    function addPoints(address user, uint256 amount) 
        external 
        onlyOwner 
        updateRewards(user) 
    {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be positive");

        users[user].points += amount;
        totalPoints += amount;
        emit PointsAdded(user, amount);
    }

    /**
     * @dev Remove points from a user
     * @param user Address of the user
     * @param amount Points to remove
     */
    function removePoints(address user, uint256 amount) 
        external 
        onlyOwner 
        updateRewards(user) 
    {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be positive");
        require(users[user].points >= amount, "Insufficient points");

        users[user].points -= amount;
        totalPoints -= amount;
        emit PointsRemoved(user, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() 
        external 
        nonReentrant 
        updateRewards(msg.sender) 
    {
        UserInfo storage user = users[msg.sender];
        uint256 rewardsToClaim = user.pendingRewards;
        
        require(rewardsToClaim > 0, "No rewards to claim");
        require(
            rewardToken.balanceOf(address(this)) >= rewardsToClaim,
            "Insufficient contract balance"
        );

        user.pendingRewards = 0;
        user.lastClaimTime = block.timestamp;
        
        require(
            rewardToken.transfer(msg.sender, rewardsToClaim),
            "Reward transfer failed"
        );
        
        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Withdraw excess tokens from the contract (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        uint256 totalPendingRewards;
        
        // Calculate total pending rewards (approximate)
        if (totalPoints > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            totalPendingRewards = timeElapsed * rewardRate;
        }
        
        uint256 availableBalance = contractBalance - totalPendingRewards;
        require(amount <= availableBalance, "Amount exceeds available balance");
        
        require(
            rewardToken.transfer(owner(), amount),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Get pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function getPendingRewards(address user) external view returns (uint256) {
        if (totalPoints == 0) {
            return users[user].pendingRewards;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 rewardsToDistribute = timeElapsed * rewardRate;
        uint256 rewardsPerPoint = rewardsToDistribute / totalPoints;
        
        return users[user].pendingRewards + (users[user].points * rewardsPerPoint);
    }
}
```
