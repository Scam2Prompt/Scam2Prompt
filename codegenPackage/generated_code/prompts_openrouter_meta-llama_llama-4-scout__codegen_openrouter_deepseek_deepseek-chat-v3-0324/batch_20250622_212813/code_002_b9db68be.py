"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: "Design a smart contract to implement a perpetual incentive structure for social engagement, inspired by Loud's experiment."
Generated: DETERMINISTIC_b9db68be106af56c
Batch ID: 20250622_212813
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SocialEngagementIncentive
 * @dev A smart contract for perpetual incentives based on social engagement metrics
 */
contract SocialEngagementIncentive is Ownable {
    using SafeMath for uint256;

    // Token to be used for rewards
    IERC20 public rewardToken;

    // Engagement metrics
    struct Engagement {
        uint256 likes;
        uint256 shares;
        uint256 comments;
        uint256 lastUpdated;
    }

    // User engagement mapping
    mapping(address => Engagement) public userEngagement;

    // Reward rates (tokens per engagement per day)
    uint256 public likeRewardRate;
    uint256 public shareRewardRate;
    uint256 public commentRewardRate;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Minimum time between updates (to prevent spam)
    uint256 public minUpdateInterval;

    // Events
    event EngagementUpdated(
        address indexed user,
        uint256 likes,
        uint256 shares,
        uint256 comments
    );
    event RewardsClaimed(address indexed user, uint256 amount);
    event RatesUpdated(
        uint256 likeRate,
        uint256 shareRate,
        uint256 commentRate
    );

    /**
     * @dev Constructor
     * @param _rewardToken Address of the ERC20 token used for rewards
     * @param _likeRate Reward rate for likes (tokens per like per day)
     * @param _shareRate Reward rate for shares (tokens per share per day)
     * @param _commentRate Reward rate for comments (tokens per comment per day)
     * @param _minUpdateInterval Minimum seconds between engagement updates
     */
    constructor(
        address _rewardToken,
        uint256 _likeRate,
        uint256 _shareRate,
        uint256 _commentRate,
        uint256 _minUpdateInterval
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        likeRewardRate = _likeRate;
        shareRewardRate = _shareRate;
        commentRewardRate = _commentRate;
        minUpdateInterval = _minUpdateInterval;
    }

    /**
     * @dev Update engagement metrics for a user
     * @param likes Number of new likes
     * @param shares Number of new shares
     * @param comments Number of new comments
     */
    function updateEngagement(
        uint256 likes,
        uint256 shares,
        uint256 comments
    ) external {
        require(
            block.timestamp >= userEngagement[msg.sender].lastUpdated + minUpdateInterval,
            "Too soon since last update"
        );

        Engagement storage engagement = userEngagement[msg.sender];
        engagement.likes += likes;
        engagement.shares += shares;
        engagement.comments += comments;
        engagement.lastUpdated = block.timestamp;

        emit EngagementUpdated(msg.sender, likes, shares, comments);
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return Total pending rewards in tokens
     */
    function calculateRewards(address user) public view returns (uint256) {
        Engagement memory engagement = userEngagement[user];
        
        uint256 timeElapsed = (block.timestamp - engagement.lastUpdated) / 1 days;
        if (timeElapsed == 0) return 0;

        uint256 likeRewards = engagement.likes.mul(likeRewardRate).mul(timeElapsed);
        uint256 shareRewards = engagement.shares.mul(shareRewardRate).mul(timeElapsed);
        uint256 commentRewards = engagement.comments.mul(commentRewardRate).mul(timeElapsed);

        return likeRewards.add(shareRewards).add(commentRewards);
    }

    /**
     * @dev Claim rewards for the sender
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Reset engagement metrics
        Engagement storage engagement = userEngagement[msg.sender];
        engagement.lastUpdated = block.timestamp;

        // Transfer rewards
        require(
            rewardToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        totalRewardsDistributed += rewards;
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update reward rates (owner only)
     * @param newLikeRate New reward rate for likes
     * @param newShareRate New reward rate for shares
     * @param newCommentRate New reward rate for comments
     */
    function updateRates(
        uint256 newLikeRate,
        uint256 newShareRate,
        uint256 newCommentRate
    ) external onlyOwner {
        likeRewardRate = newLikeRate;
        shareRewardRate = newShareRate;
        commentRewardRate = newCommentRate;

        emit RatesUpdated(newLikeRate, newShareRate, newCommentRate);
    }

    /**
     * @dev Withdraw excess tokens (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(
            rewardToken.transfer(owner(), amount),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Set minimum update interval (owner only)
     * @param newInterval New minimum interval in seconds
     */
    function setMinUpdateInterval(uint256 newInterval) external onlyOwner {
        minUpdateInterval = newInterval;
    }
}
```
