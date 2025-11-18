"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-paramgamingcom.pages.dev
Prompt: Generate a smart contract in Solidity for earning points and tracking achievements in a blockchain gaming ecosystem similar to Param Network.
Generated: DETERMINISTIC_590b331c8d944b72
Batch ID: 20250612_153724
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
 * @title GamingEcosystem
 * @dev A smart contract for earning points and tracking achievements in a blockchain gaming ecosystem.
 */
contract GamingEcosystem {
    // Struct to represent an achievement
    struct Achievement {
        string name;       // Name of the achievement
        string description; // Description of the achievement
        uint256 points;    // Points awarded for achieving this
    }

    // Mapping to store user points
    mapping(address => uint256) public userPoints;

    // Mapping to store user achievements (address => achievement IDs)
    mapping(address => uint256[]) public userAchievements;

    // Array to store all achievements globally
    Achievement[] public achievements;

    // Event emitted when points are earned
    event PointsEarned(address indexed user, uint256 points);

    // Event emitted when an achievement is unlocked
    event AchievementUnlocked(address indexed user, uint256 achievementId);

    // Event emitted when a new achievement is created
    event AchievementCreated(uint256 achievementId, string name, uint256 points);

    /**
     * @dev Adds a new achievement to the ecosystem.
     * @param _name Name of the achievement.
     * @param _description Description of the achievement.
     * @param _points Points awarded for this achievement.
     */
    function createAchievement(
        string memory _name,
        string memory _description,
        uint256 _points
    ) external {
        // Add the new achievement to the list
        achievements.push(Achievement(_name, _description, _points));

        // Emit the AchievementCreated event
        emit AchievementCreated(achievements.length - 1, _name, _points);
    }

    /**
     * @dev Allows a user to earn points.
     * @param _points Number of points to earn.
     */
    function earnPoints(uint256 _points) external {
        require(_points > 0, "Points must be greater than zero");

        // Add points to the user's balance
        userPoints[msg.sender] += _points;

        // Emit the PointsEarned event
        emit PointsEarned(msg.sender, _points);
    }

    /**
     * @dev Unlock an achievement for a user.
     * @param _achievementId ID of the achievement to unlock.
     */
    function unlockAchievement(uint256 _achievementId) external {
        require(_achievementId < achievements.length, "Invalid achievement ID");

        // Check if the user already unlocked this achievement
        uint256[] storage unlockedAchievements = userAchievements[msg.sender];
        for (uint256 i = 0; i < unlockedAchievements.length; i++) {
            require(
                unlockedAchievements[i] != _achievementId,
                "Achievement already unlocked"
            );
        }

        // Unlock the achievement
        userAchievements[msg.sender].push(_achievementId);

        // Add points to the user's balance
        userPoints[msg.sender] += achievements[_achievementId].points;

        // Emit the AchievementUnlocked event
        emit AchievementUnlocked(msg.sender, _achievementId);
    }

    /**
     * @dev Fetch all achievements unlocked by a user.
     * @param _user User's address.
     * @return Array of achievement IDs.
     */
    function getUserAchievements(address _user)
        external
        view
        returns (uint256[] memory)
    {
        return userAchievements[_user];
    }

    /**
     * @dev Fetch the details of an achievement.
     * @param _achievementId ID of the achievement.
     * @return Achievement details (name, description, points).
     */
    function getAchievementDetails(uint256 _achievementId)
        external
        view
        returns (string memory, string memory, uint256)
    {
        require(_achievementId < achievements.length, "Invalid achievement ID");

        Achievement memory achievement = achievements[_achievementId];
        return (achievement.name, achievement.description, achievement.points);
    }
}
```
