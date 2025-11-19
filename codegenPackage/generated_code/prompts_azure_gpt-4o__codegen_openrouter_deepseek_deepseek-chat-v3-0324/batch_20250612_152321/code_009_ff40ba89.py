"""
Generated Code Metadata:
========================
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Provide code in Solidity to implement the leaderboard tracking system for meme athletes, ensuring data integrity and transparency using blockchain technology.
Generated: DETERMINISTIC_ff40ba89da0ad0e2
Batch ID: 20250612_152321
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
 * @title MemeAthleteLeaderboard
 * @dev A smart contract for tracking meme athlete scores on the blockchain
 */
contract MemeAthleteLeaderboard {
    // Struct to store athlete information
    struct Athlete {
        string name;
        uint256 score;
        uint256 lastUpdated;
        address updatedBy;
    }

    // Mapping from athlete ID to Athlete struct
    mapping(uint256 => Athlete) public athletes;

    // Array to store all athlete IDs for enumeration
    uint256[] public athleteIds;

    // Event emitted when an athlete's score is updated
    event ScoreUpdated(
        uint256 indexed athleteId,
        string name,
        uint256 newScore,
        uint256 timestamp,
        address updatedBy
    );

    // Event emitted when a new athlete is added
    event AthleteAdded(
        uint256 indexed athleteId,
        string name,
        uint256 initialScore,
        uint256 timestamp,
        address addedBy
    );

    // Modifier to check if the athlete exists
    modifier athleteExists(uint256 athleteId) {
        require(bytes(athletes[athleteId].name).length != 0, "Athlete does not exist");
        _;
    }

    /**
     * @dev Add a new athlete to the leaderboard
     * @param athleteId The unique identifier for the athlete
     * @param name The name of the athlete
     * @param initialScore The initial score for the athlete
     */
    function addAthlete(
        uint256 athleteId,
        string memory name,
        uint256 initialScore
    ) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(athletes[athleteId].name).length == 0, "Athlete already exists");

        athletes[athleteId] = Athlete({
            name: name,
            score: initialScore,
            lastUpdated: block.timestamp,
            updatedBy: msg.sender
        });

        athleteIds.push(athleteId);

        emit AthleteAdded(
            athleteId,
            name,
            initialScore,
            block.timestamp,
            msg.sender
        );
    }

    /**
     * @dev Update an athlete's score
     * @param athleteId The ID of the athlete to update
     * @param newScore The new score to set
     */
    function updateScore(uint256 athleteId, uint256 newScore)
        external
        athleteExists(athleteId)
    {
        Athlete storage athlete = athletes[athleteId];
        athlete.score = newScore;
        athlete.lastUpdated = block.timestamp;
        athlete.updatedBy = msg.sender;

        emit ScoreUpdated(
            athleteId,
            athlete.name,
            newScore,
            block.timestamp,
            msg.sender
        );
    }

    /**
     * @dev Get an athlete's details
     * @param athleteId The ID of the athlete to retrieve
     * @return name The athlete's name
     * @return score The athlete's current score
     * @return lastUpdated Timestamp of last update
     * @return updatedBy Address that last updated the score
     */
    function getAthlete(uint256 athleteId)
        external
        view
        athleteExists(athleteId)
        returns (
            string memory name,
            uint256 score,
            uint256 lastUpdated,
            address updatedBy
        )
    {
        Athlete memory athlete = athletes[athleteId];
        return (
            athlete.name,
            athlete.score,
            athlete.lastUpdated,
            athlete.updatedBy
        );
    }

    /**
     * @dev Get all athlete IDs
     * @return Array of all athlete IDs
     */
    function getAllAthleteIds() external view returns (uint256[] memory) {
        return athleteIds;
    }

    /**
     * @dev Get the top N athletes by score
     * @param count The number of top athletes to return
     * @return topAthletes Array of athlete IDs sorted by score (descending)
     */
    function getTopAthletes(uint256 count) external view returns (uint256[] memory) {
        require(count > 0, "Count must be greater than 0");
        
        uint256[] memory ids = new uint256[](athleteIds.length);
        uint256[] memory scores = new uint256[](athleteIds.length);
        
        // Copy athlete IDs and scores to memory arrays
        for (uint256 i = 0; i < athleteIds.length; i++) {
            ids[i] = athleteIds[i];
            scores[i] = athletes[athleteIds[i]].score;
        }
        
        // Sort the arrays in descending order of score
        for (uint256 i = 0; i < scores.length; i++) {
            for (uint256 j = i + 1; j < scores.length; j++) {
                if (scores[i] < scores[j]) {
                    (scores[i], scores[j]) = (scores[j], scores[i]);
                    (ids[i], ids[j]) = (ids[j], ids[i]);
                }
            }
        }
        
        // Prepare the result array with the top N athletes
        uint256 resultCount = count > ids.length ? ids.length : count;
        uint256[] memory result = new uint256[](resultCount);
        
        for (uint256 i = 0; i < resultCount; i++) {
            result[i] = ids[i];
        }
        
        return result;
    }
}
```
