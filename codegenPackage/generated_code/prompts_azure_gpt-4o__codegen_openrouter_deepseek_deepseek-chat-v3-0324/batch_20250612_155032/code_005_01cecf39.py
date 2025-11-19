"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Suggest strategies for implementing Sonic Gems as incentives within a decentralized application, ensuring alignment with Sonic Labs' meritocratic reward system.
Generated: DETERMINISTIC_01cecf39a290dccc
Batch ID: 20250612_155032
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
 * @title SonicGemsRewardSystem
 * @dev A smart contract for managing Sonic Gems as incentives in a decentralized application
 * that aligns with Sonic Labs' meritocratic reward system.
 */
contract SonicGemsRewardSystem is Ownable, ReentrancyGuard {
    // Sonic Gems token interface
    IERC20 public sonicGemsToken;

    // User reward tracking
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public lastClaimTime;

    // Reward parameters
    uint256 public constant COOLDOWN_PERIOD = 1 days;
    uint256 public constant BASE_REWARD = 100 ether; // 100 Sonic Gems (assuming 18 decimals)
    uint256 public constant ACTIVITY_MULTIPLIER = 2;
    uint256 public constant CONTRIBUTION_MULTIPLIER = 5;

    // Activity tracking
    mapping(address => uint256) public userActivityScores;
    mapping(address => uint256) public userContributionScores;

    // Events
    event RewardEarned(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ActivityRecorded(address indexed user, uint256 score);
    event ContributionRecorded(address indexed user, uint256 score);

    /**
     * @dev Constructor initializes the Sonic Gems token contract
     * @param _sonicGemsToken Address of the Sonic Gems ERC20 token
     */
    constructor(address _sonicGemsToken) {
        require(_sonicGemsToken != address(0), "Invalid token address");
        sonicGemsToken = IERC20(_sonicGemsToken);
    }

    /**
     * @dev Records user activity to calculate rewards
     * @param _user Address of the user
     * @param _score Activity score to add
     */
    function recordActivity(address _user, uint256 _score) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        userActivityScores[_user] += _score;
        emit ActivityRecorded(_user, _score);
    }

    /**
     * @dev Records user contribution to calculate rewards
     * @param _user Address of the user
     * @param _score Contribution score to add
     */
    function recordContribution(address _user, uint256 _score) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        userContributionScores[_user] += _score;
        emit ContributionRecorded(_user, _score);
    }

    /**
     * @dev Calculates and assigns rewards based on meritocratic system
     * @param _user Address of the user to reward
     */
    function calculateRewards(address _user) public {
        require(_user != address(0), "Invalid user address");
        
        uint256 activityReward = userActivityScores[_user] * ACTIVITY_MULTIPLIER;
        uint256 contributionReward = userContributionScores[_user] * CONTRIBUTION_MULTIPLIER;
        
        uint256 totalReward = BASE_REWARD + activityReward + contributionReward;
        
        userRewards[_user] += totalReward;
        emit RewardEarned(_user, totalReward);
        
        // Reset scores after reward calculation
        userActivityScores[_user] = 0;
        userContributionScores[_user] = 0;
    }

    /**
     * @dev Allows users to claim their accumulated rewards
     */
    function claimRewards() external nonReentrant {
        address user = msg.sender;
        
        require(userRewards[user] > 0, "No rewards to claim");
        require(
            block.timestamp >= lastClaimTime[user] + COOLDOWN_PERIOD,
            "Claim cooldown period not passed"
        );
        
        uint256 rewardAmount = userRewards[user];
        userRewards[user] = 0;
        lastClaimTime[user] = block.timestamp;
        
        require(
            sonicGemsToken.transfer(user, rewardAmount),
            "Token transfer failed"
        );
        
        emit RewardClaimed(user, rewardAmount);
    }

    /**
     * @dev Allows owner to withdraw excess tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(
            sonicGemsToken.transfer(owner(), _amount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Returns the claimable reward amount for a user
     * @param _user Address of the user
     * @return Amount of claimable rewards
     */
    function getClaimableRewards(address _user) external view returns (uint256) {
        return userRewards[_user];
    }

    /**
     * @dev Returns the time when user can claim rewards again
     * @param _user Address of the user
     * @return Timestamp of next available claim time
     */
    function getNextClaimTime(address _user) external view returns (uint256) {
        return lastClaimTime[_user] + COOLDOWN_PERIOD;
    }
}
```
