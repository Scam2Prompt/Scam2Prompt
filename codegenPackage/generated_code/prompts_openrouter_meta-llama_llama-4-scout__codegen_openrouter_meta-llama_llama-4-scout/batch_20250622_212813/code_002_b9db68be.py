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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PerpetualIncentiveContract
 * @author [Your Name]
 * @notice A smart contract to implement a perpetual incentive structure for social engagement.
 */
contract PerpetualIncentiveContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user engagement scores
    mapping(address => uint256) public engagementScores;

    // Mapping of user incentive rewards
    mapping(address => uint256) public incentiveRewards;

    // Token used for incentives
    ERC20 public incentiveToken;

    // Incentive rate per engagement score
    uint256 public incentiveRate;

    // Maximum incentive reward
    uint256 public maxIncentiveReward;

    // Event emitted when engagement score is updated
    event EngagementScoreUpdated(address indexed user, uint256 score);

    // Event emitted when incentive reward is claimed
    event IncentiveRewardClaimed(address indexed user, uint256 reward);

    /**
     * @notice Constructor
     * @param _incentiveToken Address of the incentive token
     * @param _incentiveRate Incentive rate per engagement score
     * @param _maxIncentiveReward Maximum incentive reward
     */
    constructor(
        address _incentiveToken,
        uint256 _incentiveRate,
        uint256 _maxIncentiveReward
    ) {
        require(_incentiveToken != address(0), "Incentive token address cannot be zero");
        require(_incentiveRate > 0, "Incentive rate must be greater than zero");
        require(_maxIncentiveReward > 0, "Maximum incentive reward must be greater than zero");

        incentiveToken = ERC20(_incentiveToken);
        incentiveRate = _incentiveRate;
        maxIncentiveReward = _maxIncentiveReward;
    }

    /**
     * @notice Updates the engagement score for a user
     * @param _user Address of the user
     * @param _score New engagement score
     */
    function updateEngagementScore(address _user, uint256 _score) external {
        require(_user != address(0), "User address cannot be zero");
        require(_score >= 0, "Engagement score must be non-negative");

        engagementScores[_user] = _score;
        emit EngagementScoreUpdated(_user, _score);
    }

    /**
     * @notice Calculates the incentive reward for a user
     * @param _user Address of the user
     * @return Incentive reward
     */
    function calculateIncentiveReward(address _user) public view returns (uint256) {
        uint256 engagementScore = engagementScores[_user];
        uint256 reward = engagementScore.mul(incentiveRate);

        // Cap the reward at the maximum incentive reward
        return reward.min(maxIncentiveReward);
    }

    /**
     * @notice Claims the incentive reward for a user
     */
    function claimIncentiveReward() external nonReentrant {
        address user = msg.sender;
        uint256 reward = incentiveRewards[user];

        // Only claim if reward is greater than zero
        require(reward > 0, "No incentive reward to claim");

        // Reset the reward
        incentiveRewards[user] = 0;

        // Transfer the reward
        require(incentiveToken.transfer(user, reward), "Failed to transfer incentive reward");

        emit IncentiveRewardClaimed(user, reward);
    }

    /**
     * @notice Triggers the incentive reward distribution for a user
     * @param _user Address of the user
     */
    function triggerIncentiveReward(address _user) external {
        require(_user != address(0), "User address cannot be zero");

        uint256 reward = calculateIncentiveReward(_user);

        // Update the incentive reward
        incentiveRewards[_user] = reward;
    }
}
```
