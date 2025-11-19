"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Generate a Solidity smart contract example that implements a reward system based on social media follower milestones, similar to the $WING tokenomics structure.
Generated: DETERMINISTIC_973f400262e7104a
Batch ID: 20250612_155037
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

/**
 * @title SocialMediaRewardSystem
 * @dev A contract that rewards users based on social media follower milestones
 */
contract SocialMediaRewardSystem is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Milestone structure
    struct Milestone {
        uint256 followerCount;
        uint256 rewardAmount;
        bool exists;
    }

    // User structure
    struct User {
        uint256 highestFollowerCount;
        uint256 totalRewardsClaimed;
        bool isRegistered;
    }

    // Mapping of milestone follower counts to reward amounts
    mapping(uint256 => Milestone) public milestones;

    // Mapping of user addresses to their data
    mapping(address => User) public users;

    // Events
    event UserRegistered(address indexed user);
    event MilestoneAdded(uint256 followerCount, uint256 rewardAmount);
    event MilestoneUpdated(uint256 followerCount, uint256 rewardAmount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor function
     * @param _rewardTokenAddress Address of the ERC20 reward token
     */
    constructor(address _rewardTokenAddress) {
        require(_rewardTokenAddress != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Register a new user
     */
    function register() external {
        require(!users[msg.sender].isRegistered, "User already registered");
        
        users[msg.sender] = User({
            highestFollowerCount: 0,
            totalRewardsClaimed: 0,
            isRegistered: true
        });

        emit UserRegistered(msg.sender);
    }

    /**
     * @dev Add a new milestone
     * @param _followerCount The follower count required for this milestone
     * @param _rewardAmount The reward amount for reaching this milestone
     */
    function addMilestone(uint256 _followerCount, uint256 _rewardAmount) external onlyOwner {
        require(!milestones[_followerCount].exists, "Milestone already exists");
        require(_followerCount > 0, "Follower count must be positive");
        require(_rewardAmount > 0, "Reward amount must be positive");

        milestones[_followerCount] = Milestone({
            followerCount: _followerCount,
            rewardAmount: _rewardAmount,
            exists: true
        });

        emit MilestoneAdded(_followerCount, _rewardAmount);
    }

    /**
     * @dev Update an existing milestone
     * @param _followerCount The follower count of the milestone to update
     * @param _rewardAmount The new reward amount for this milestone
     */
    function updateMilestone(uint256 _followerCount, uint256 _rewardAmount) external onlyOwner {
        require(milestones[_followerCount].exists, "Milestone doesn't exist");
        require(_rewardAmount > 0, "Reward amount must be positive");

        milestones[_followerCount].rewardAmount = _rewardAmount;

        emit MilestoneUpdated(_followerCount, _rewardAmount);
    }

    /**
     * @dev Claim rewards based on follower count
     * @param _followerCount Current follower count to verify
     */
    function claimRewards(uint256 _followerCount) external nonReentrant {
        require(users[msg.sender].isRegistered, "User not registered");
        require(_followerCount > users[msg.sender].highestFollowerCount, "No new milestones reached");

        uint256 totalReward = 0;
        uint256 previousHighest = users[msg.sender].highestFollowerCount;

        // Iterate through milestones to calculate rewards
        for (uint256 i = previousHighest + 1; i <= _followerCount; i++) {
            if (milestones[i].exists) {
                totalReward += milestones[i].rewardAmount;
            }
        }

        require(totalReward > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= totalReward, "Insufficient contract balance");

        // Update user data
        users[msg.sender].highestFollowerCount = _followerCount;
        users[msg.sender].totalRewardsClaimed += totalReward;

        // Transfer rewards
        rewardToken.transfer(msg.sender, totalReward);

        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Withdraw tokens from the contract (owner only)
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be positive");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        rewardToken.transfer(owner(), _amount);

        emit TokensWithdrawn(owner(), _amount);
    }

    /**
     * @dev Get the claimable reward amount for a user
     * @param _user User address to check
     * @param _followerCount Current follower count to verify
     * @return Total claimable reward amount
     */
    function getClaimableReward(address _user, uint256 _followerCount) external view returns (uint256) {
        if (!users[_user].isRegistered || _followerCount <= users[_user].highestFollowerCount) {
            return 0;
        }

        uint256 totalReward = 0;
        uint256 previousHighest = users[_user].highestFollowerCount;

        for (uint256 i = previousHighest + 1; i <= _followerCount; i++) {
            if (milestones[i].exists) {
                totalReward += milestones[i].rewardAmount;
            }
        }

        return totalReward;
    }
}
```
