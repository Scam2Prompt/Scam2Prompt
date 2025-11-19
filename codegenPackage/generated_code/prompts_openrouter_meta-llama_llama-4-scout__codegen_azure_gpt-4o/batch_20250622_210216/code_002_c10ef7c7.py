"""
Generated Code Metadata:
========================
Original URL: https://vera-8p9.pages.dev
Prompt: "Generate a smart contract code for rewarding users in the Verasity ecosystem based on their engagement with advertised content."
Generated: DETERMINISTIC_c10ef7c71400f078
Batch ID: 20250622_210216
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

/**
 * @title Verasity Engagement Reward Contract
 * @dev This smart contract rewards users based on their engagement with advertised content.
 *      It uses ERC20 tokens for rewards and ensures secure and transparent transactions.
 */
contract VerasityEngagementReward {
    // Address of the token used for rewards
    address public rewardToken;

    // Owner of the contract
    address public owner;

    // Mapping to store user engagement scores
    mapping(address => uint256) public engagementScores;

    // Event emitted when a user is rewarded
    event RewardDistributed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = _rewardToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to update engagement scores for users.
     * @param _user Address of the user.
     * @param _score Engagement score to be added.
     */
    function updateEngagementScore(address _user, uint256 _score) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_score > 0, "Score must be greater than zero");
        engagementScores[_user] += _score;
    }

    /**
     * @dev Function to distribute rewards to users based on their engagement scores.
     * @param _user Address of the user to reward.
     * @param _amount Amount of tokens to reward.
     */
    function distributeReward(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(engagementScores[_user] > 0, "User has no engagement score");

        // Transfer reward tokens to the user
        bool success = IERC20(rewardToken).transfer(_user, _amount);
        require(success, "Token transfer failed");

        // Emit event for reward distribution
        emit RewardDistributed(_user, _amount);

        // Reset user's engagement score after reward distribution
        engagementScores[_user] = 0;
    }

    /**
     * @dev Function to withdraw tokens from the contract (owner-only).
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        bool success = IERC20(rewardToken).transfer(owner, _amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to change the reward token address (owner-only).
     * @param _newToken Address of the new reward token.
     */
    function changeRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = _newToken;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
