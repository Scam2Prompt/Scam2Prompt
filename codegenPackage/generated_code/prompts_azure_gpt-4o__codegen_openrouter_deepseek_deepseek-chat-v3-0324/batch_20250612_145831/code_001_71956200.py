"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Generate code to implement a reward multiplier system for a crypto token campaign, similar to the SpaceM Hunt described on the SpaceM World platform.
Generated: DETERMINISTIC_719562004d9fbd0e
Batch ID: 20250612_145831
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

contract RewardMultiplier is Ownable {
    using SafeMath for uint256;

    // Token to be distributed as rewards
    IERC20 public rewardToken;

    // Campaign parameters
    uint256 public campaignStartTime;
    uint256 public campaignEndTime;
    uint256 public totalRewardPool;
    uint256 public distributedRewards;

    // Multiplier tiers based on participation time
    struct MultiplierTier {
        uint256 startTime;
        uint256 endTime;
        uint256 multiplier; // Multiplier in basis points (10000 = 1x)
    }

    MultiplierTier[] public multiplierTiers;

    // User participation tracking
    struct UserParticipation {
        uint256 participationTime;
        uint256 claimedRewards;
        bool hasParticipated;
    }

    mapping(address => UserParticipation) public userParticipation;

    // Events
    event RewardClaimed(address indexed user, uint256 amount);
    event MultiplierTierAdded(uint256 startTime, uint256 endTime, uint256 multiplier);
    event CampaignExtended(uint256 newEndTime);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    constructor(
        IERC20 _rewardToken,
        uint256 _campaignStartTime,
        uint256 _campaignEndTime,
        uint256 _totalRewardPool
    ) {
        require(_campaignStartTime < _campaignEndTime, "Invalid campaign duration");
        require(_totalRewardPool > 0, "Reward pool must be positive");

        rewardToken = _rewardToken;
        campaignStartTime = _campaignStartTime;
        campaignEndTime = _campaignEndTime;
        totalRewardPool = _totalRewardPool;
        distributedRewards = 0;
    }

    /**
     * @dev Add a new multiplier tier
     * @param startTime Start time of the tier
     * @param endTime End time of the tier
     * @param multiplier Multiplier in basis points (10000 = 1x)
     */
    function addMultiplierTier(
        uint256 startTime,
        uint256 endTime,
        uint256 multiplier
    ) external onlyOwner {
        require(startTime >= campaignStartTime, "Tier starts before campaign");
        require(endTime <= campaignEndTime, "Tier ends after campaign");
        require(startTime < endTime, "Invalid tier duration");
        require(multiplier >= 10000, "Multiplier must be at least 1x");

        multiplierTiers.push(MultiplierTier(startTime, endTime, multiplier));
        emit MultiplierTierAdded(startTime, endTime, multiplier);
    }

    /**
     * @dev Participate in the campaign
     */
    function participate() external {
        require(block.timestamp >= campaignStartTime, "Campaign not started");
        require(block.timestamp <= campaignEndTime, "Campaign ended");
        require(!userParticipation[msg.sender].hasParticipated, "Already participated");

        userParticipation[msg.sender] = UserParticipation({
            participationTime: block.timestamp,
            claimedRewards: 0,
            hasParticipated: true
        });
    }

    /**
     * @dev Calculate reward for a user based on participation time
     * @param user Address of the participant
     * @return reward Calculated reward amount
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        require(userParticipation[user].hasParticipated, "User not participated");

        uint256 participationTime = userParticipation[user].participationTime;
        uint256 baseReward = totalRewardPool.div(1000); // Example: 0.1% of total pool as base reward

        // Find applicable multiplier tier
        uint256 applicableMultiplier = 10000; // Default 1x multiplier
        for (uint256 i = 0; i < multiplierTiers.length; i++) {
            if (
                participationTime >= multiplierTiers[i].startTime &&
                participationTime <= multiplierTiers[i].endTime
            ) {
                applicableMultiplier = multiplierTiers[i].multiplier;
                break;
            }
        }

        reward = baseReward.mul(applicableMultiplier).div(10000);
        return reward;
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        require(userParticipation[msg.sender].hasParticipated, "Not participated");
        require(userParticipation[msg.sender].claimedRewards == 0, "Already claimed");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        require(distributedRewards.add(reward) <= totalRewardPool, "Reward pool exhausted");

        userParticipation[msg.sender].claimedRewards = reward;
        distributedRewards = distributedRewards.add(reward);

        require(
            rewardToken.transfer(msg.sender, reward),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Extend campaign duration
     * @param newEndTime New end time for the campaign
     */
    function extendCampaign(uint256 newEndTime) external onlyOwner {
        require(newEndTime > campaignEndTime, "New end time must be after current end time");
        campaignEndTime = newEndTime;
        emit CampaignExtended(newEndTime);
    }

    /**
     * @dev Emergency withdraw remaining tokens
     */
    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > campaignEndTime, "Campaign not ended");
        uint256 remainingBalance = rewardToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        require(
            rewardToken.transfer(owner(), remainingBalance),
            "Token transfer failed"
        );

        emit EmergencyWithdraw(owner(), remainingBalance);
    }

    /**
     * @dev Get current multiplier for a user
     * @param user Address to check
     * @return Current multiplier in basis points
     */
    function getCurrentMultiplier(address user) public view returns (uint256) {
        if (!userParticipation[user].hasParticipated) return 0;

        uint256 participationTime = userParticipation[user].participationTime;
        for (uint256 i = 0; i < multiplierTiers.length; i++) {
            if (
                participationTime >= multiplierTiers[i].startTime &&
                participationTime <= multiplierTiers[i].endTime
            ) {
                return multiplierTiers[i].multiplier;
            }
        }
        return 10000; // Default 1x multiplier
    }

    /**
     * @dev Get remaining reward pool
     */
    function getRemainingRewardPool() public view returns (uint256) {
        return totalRewardPool.sub(distributedRewards);
    }
}
```
