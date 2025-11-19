"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daoo.web.app
Prompt: Illustrate how to implement a reward system in a smart contract that distributes $TNSR tokens based on user activity on the NFT DAO platform.
Generated: DETERMINISTIC_7512edf1d87d197e
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFT DAO Reward System
 * @dev This smart contract distributes $TNSR tokens to active users based on their activity on the NFT DAO platform.
 * Users earn rewards for engaging in activities like minting NFTs, voting, and participating in governance.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NFTDAORewardSystem {
    // Token used for rewards
    IERC20 public tnsrToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user activity
    mapping(address => uint256) public userActivityPoints;

    // Reward distribution conversion rate (activity points to $TNSR tokens)
    uint256 public rewardRate;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Event emitted when activity points are updated
    event ActivityPointsUpdated(address indexed user, uint256 newPoints);

    /**
     * @dev Constructor to initialize the contract.
     * @param _tnsrToken Address of the $TNSR token contract.
     * @param _rewardRate Conversion rate for activity points to $TNSR tokens.
     */
    constructor(IERC20 _tnsrToken, uint256 _rewardRate) {
        require(address(_tnsrToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        tnsrToken = _tnsrToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Function to update activity points for a user.
     * @param user Address of the user.
     * @param points Number of activity points to add.
     */
    function updateActivityPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than 0");

        userActivityPoints[user] += points;
        emit ActivityPointsUpdated(user, userActivityPoints[user]);
    }

    /**
     * @dev Function to distribute rewards to a user based on their activity points.
     * @param user Address of the user.
     */
    function distributeRewards(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");

        uint256 userPoints = userActivityPoints[user];
        require(userPoints > 0, "User has no activity points");

        // Calculate reward amount
        uint256 rewardAmount = userPoints * rewardRate;

        // Ensure contract has enough $TNSR tokens to distribute
        require(tnsrToken.balanceOf(address(this)) >= rewardAmount, "Insufficient $TNSR tokens in contract");

        // Transfer tokens and reset user points
        userActivityPoints[user] = 0;
        tnsrToken.transfer(user, rewardAmount);

        emit RewardsDistributed(user, rewardAmount);
    }

    /**
     * @dev Function to update the reward rate.
     * @param newRate New conversion rate for activity points to $TNSR tokens.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
    }

    /**
     * @dev Function to withdraw $TNSR tokens from the contract.
     * @param amount Amount of $TNSR tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(tnsrToken.balanceOf(address(this)) >= amount, "Insufficient $TNSR tokens in contract");

        tnsrToken.transfer(owner, amount);
    }
}
```
