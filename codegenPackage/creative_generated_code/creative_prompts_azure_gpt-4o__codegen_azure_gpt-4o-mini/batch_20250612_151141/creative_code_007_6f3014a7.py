"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-ie.web.app
Prompt: Write a Solidity function for implementing a play-to-earn reward system that distributes $KANG tokens based on user activity and leaderboard rankings.
Generated: DETERMINISTIC_6f3014a7fc50e9d8
Batch ID: 20250612_151141
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Contract for the play-to-earn reward system
contract PlayToEarnReward {
    // Declare state variables
    IERC20 public kangToken; // The ERC20 token to distribute
    uint256 public rewardRate; // The rate of reward distribution
    mapping(address => uint256) public userScores; // Mapping to keep track of user scores
    address[] public leaderboard; // Array to hold the leaderboard addresses

    // Event to log rewards distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the token address and reward rate
    constructor(address _kangToken, uint256 _rewardRate) {
        require(_kangToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        kangToken = IERC20(_kangToken);
        rewardRate = _rewardRate;
    }

    // Function to update user scores and potentially update the leaderboard
    function updateUserScore(address user, uint256 score) external {
        require(user != address(0), "Invalid user address");
        require(score > 0, "Score must be greater than zero");

        userScores[user] += score; // Update user score

        // Update leaderboard if necessary
        _updateLeaderboard(user);
    }

    // Internal function to update the leaderboard based on scores
    function _updateLeaderboard(address user) internal {
        // Check if user already exists in the leaderboard
        for (uint256 i = 0; i < leaderboard.length; i++) {
            if (leaderboard[i] == user) {
                return; // User is already in the leaderboard
            }
        }

        // Insert user in the leaderboard
        leaderboard.push(user);
    }

    // Function to distribute rewards based on user activity
    function distributeRewards() external {
        for (uint256 i = 0; i < leaderboard.length; i++) {
            address user = leaderboard[i];
            uint256 userScore = userScores[user];

            if (userScore > 0) {
                uint256 rewardAmount = userScore * rewardRate; // Calculate reward based on score
                require(kangToken.transfer(user, rewardAmount), "Token transfer failed"); // Transfer KANG tokens

                emit RewardsDistributed(user, rewardAmount); // Emit event for rewards distribution
            }
        }
    }

    // Function to get the leaderboard
    function getLeaderboard() external view returns (address[] memory) {
        return leaderboard;
    }

    // Function to get user score
    function getUserScore(address user) external view returns (uint256) {
        return userScores[user];
    }
}
```
