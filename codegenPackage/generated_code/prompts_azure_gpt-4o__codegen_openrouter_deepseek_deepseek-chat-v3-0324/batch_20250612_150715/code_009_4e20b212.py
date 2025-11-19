"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract that enables Farcaster members to earn rewards based on their downstream influence on other members, as specified by the Moxie Protocol.
Generated: DETERMINISTIC_4e20b21213c6ce00
Batch ID: 20250612_150715
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

/**
 * @title Farcaster Influence Rewards Contract
 * @dev Implements Moxie Protocol for tracking and rewarding downstream influence
 */
contract FarcasterInfluenceRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Mapping from user address to their influence score
    mapping(address => uint256) public influenceScores;

    // Mapping from user address to their direct referrals
    mapping(address => address[]) public directReferrals;

    // Mapping from user address to their total downstream referrals count
    mapping(address => uint256) public totalDownstreamReferrals;

    // Reward rate per influence point (in wei)
    uint256 public rewardRate;

    // Minimum influence required to claim rewards
    uint256 public minInfluenceThreshold;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Events
    event ReferralAdded(address indexed referrer, address indexed referee);
    event InfluenceUpdated(address indexed user, uint256 newInfluence);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinInfluenceThresholdUpdated(uint256 newThreshold);

    /**
     * @dev Constructor initializes the contract with reward token and settings
     * @param _rewardToken Address of the ERC20 reward token
     * @param _rewardRate Initial reward rate per influence point
     * @param _minInfluenceThreshold Minimum influence required to claim rewards
     */
    constructor(
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minInfluenceThreshold
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minInfluenceThreshold = _minInfluenceThreshold;
    }

    /**
     * @dev Adds a referral relationship between referrer and referee
     * @param referrer Address of the referring user
     * @param referee Address of the new user being referred
     */
    function addReferral(address referrer, address referee) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(referee != address(0), "Invalid referee address");
        require(referrer != referee, "Cannot refer yourself");

        directReferrals[referrer].push(referee);
        _updateDownstreamInfluence(referrer);

        emit ReferralAdded(referrer, referee);
    }

    /**
     * @dev Updates influence scores recursively for a user and their upstream referrers
     * @param user Address of the user to update influence for
     */
    function _updateDownstreamInfluence(address user) private {
        uint256 newInfluence = calculateInfluence(user);
        influenceScores[user] = newInfluence;
        emit InfluenceUpdated(user, newInfluence);

        // Propagate update to upstream referrers
        address[] memory referrers = _getUpstreamReferrers(user);
        for (uint256 i = 0; i < referrers.length; i++) {
            address referrer = referrers[i];
            uint256 referrerInfluence = calculateInfluence(referrer);
            influenceScores[referrer] = referrerInfluence;
            emit InfluenceUpdated(referrer, referrerInfluence);
        }
    }

    /**
     * @dev Calculates the influence score for a user based on their downstream network
     * @param user Address of the user to calculate influence for
     * @return influence The calculated influence score
     */
    function calculateInfluence(address user) public view returns (uint256 influence) {
        uint256 directCount = directReferrals[user].length;
        uint256 downstreamCount = totalDownstreamReferrals[user];

        // Moxie Protocol formula: influence = direct referrals + 0.5 * downstream referrals
        influence = directCount + (downstreamCount / 2);
        return influence;
    }

    /**
     * @dev Gets all upstream referrers for a given user
     * @param user Address of the user to find referrers for
     * @return referrers Array of upstream referrer addresses
     */
    function _getUpstreamReferrers(address user) private view returns (address[] memory referrers) {
        // This is a simplified version - in a real implementation, you would need
        // to track the full referral tree structure
        address[] memory tempReferrers = new address[](10); // Arbitrary max depth
        uint256 count = 0;

        // Simplified logic - in production you would need proper tree traversal
        for (uint256 i = 0; i < directReferrals[msg.sender].length; i++) {
            if (directReferrals[msg.sender][i] == user) {
                tempReferrers[count] = msg.sender;
                count++;
                break;
            }
        }

        // Resize array to actual count
        referrers = new address[](count);
        for (uint256 i = 0; i < count; i++) {
            referrers[i] = tempReferrers[i];
        }

        return referrers;
    }

    /**
     * @dev Allows users to claim their rewards based on their influence score
     */
    function claimRewards() external nonReentrant {
        uint256 influence = influenceScores[msg.sender];
        require(influence >= minInfluenceThreshold, "Influence below minimum threshold");

        uint256 rewardAmount = influence * rewardRate;
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        // Reset influence after claiming
        influenceScores[msg.sender] = 0;
        totalRewardsDistributed += rewardAmount;

        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Updates the reward rate
     * @param newRate New reward rate per influence point
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Updates the minimum influence threshold
     * @param newThreshold New minimum influence required to claim rewards
     */
    function setMinInfluenceThreshold(uint256 newThreshold) external onlyOwner {
        minInfluenceThreshold = newThreshold;
        emit MinInfluenceThresholdUpdated(newThreshold);
    }

    /**
     * @dev Allows owner to withdraw excess tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(rewardToken.transfer(owner(), amount), "Transfer failed");
    }

    /**
     * @dev Gets the direct referrals count for a user
     * @param user Address of the user
     * @return count Number of direct referrals
     */
    function getDirectReferralsCount(address user) external view returns (uint256 count) {
        return directReferrals[user].length;
    }

    /**
     * @dev Gets the total downstream referrals count for a user
     * @param user Address of the user
     * @return count Number of total downstream referrals
     */
    function getTotalDownstreamReferrals(address user) external view returns (uint256 count) {
        return totalDownstreamReferrals[user];
    }
}
```
