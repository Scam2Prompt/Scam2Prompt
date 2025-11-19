"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Create a smart contract that uses Bluwhale's AI-powered wallet insights to reward users for engaging with personalized outreach messages.
Generated: DETERMINISTIC_db92615928db7c90
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Bluwhale Engagement Rewards Contract
 * @dev Smart contract that rewards users for engaging with personalized outreach messages
 * using Bluwhale's AI-powered wallet insights.
 */
contract BluwhaleEngagementRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Reward amount per engagement
    uint256 public rewardAmount;

    // Mapping to track which messages have been engaged with
    mapping(bytes32 => bool) public messageEngaged;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Events
    event MessageSent(bytes32 indexed messageId, address indexed recipient);
    event EngagementRewarded(
        bytes32 indexed messageId,
        address indexed user,
        uint256 amount
    );
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardAmountUpdated(uint256 newAmount);

    /**
     * @dev Constructor initializes the reward token and amount
     * @param _rewardToken Address of the ERC20 token used for rewards
     * @param _rewardAmount Amount of tokens to reward per engagement
     */
    constructor(address _rewardToken, uint256 _rewardAmount) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Records a message sent to a user
     * @param _messageId Unique identifier for the message
     * @param _recipient Address of the message recipient
     */
    function recordMessage(bytes32 _messageId, address _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        emit MessageSent(_messageId, _recipient);
    }

    /**
     * @dev Rewards a user for engaging with a message
     * @param _messageId Unique identifier for the engaged message
     * @param _user Address of the user to reward
     */
    function rewardEngagement(bytes32 _messageId, address _user) external onlyOwner nonReentrant {
        require(_user != address(0), "Invalid user address");
        require(!messageEngaged[_messageId], "Message already engaged");

        messageEngaged[_messageId] = true;
        userRewards[_user] += rewardAmount;

        emit EngagementRewarded(_messageId, _user, rewardAmount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards
     */
    function claimRewards() external nonReentrant {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");

        emit RewardClaimed(msg.sender, amount);
    }

    /**
     * @dev Updates the reward amount
     * @param _newAmount New reward amount per engagement
     */
    function updateRewardAmount(uint256 _newAmount) external onlyOwner {
        require(_newAmount > 0, "Reward amount must be positive");
        rewardAmount = _newAmount;
        emit RewardAmountUpdated(_newAmount);
    }

    /**
     * @dev Withdraws any remaining tokens from the contract
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.transfer(owner(), _amount), "Token transfer failed");
    }

    /**
     * @dev Returns the reward balance of a user
     * @param _user Address of the user to check
     * @return uint256 Reward balance of the user
     */
    function getUserRewards(address _user) external view returns (uint256) {
        return userRewards[_user];
    }
}
```
