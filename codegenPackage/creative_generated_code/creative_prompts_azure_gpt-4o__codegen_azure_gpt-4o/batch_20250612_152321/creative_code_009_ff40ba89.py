"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Provide code in Solidity to implement the leaderboard tracking system for meme athletes, ensuring data integrity and transparency using blockchain technology.
Generated: DETERMINISTIC_ff40ba89da0ad0e2
Batch ID: 20250612_152321
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
 * @title MemeAthletesLeaderboard
 * @dev A smart contract for tracking leaderboard scores of meme athletes
 *      ensuring transparency and data integrity on the blockchain.
 */
contract MemeAthletesLeaderboard {
    // Struct to represent an athlete's data
    struct Athlete {
        string name; // Athlete's name
        uint256 score; // Athlete's score
    }

    // Array to store the leaderboard of athletes
    Athlete[] private leaderboard;

    // Mapping to check if an athlete already exists to ensure unique entries
    mapping(string => bool) private athleteExists;

    // Event emitted when a new athlete is added
    event AthleteAdded(string name, uint256 score);

    // Event emitted when an athlete's score is updated
    event AthleteScoreUpdated(string name, uint256 score);

    // Modifier to check for name validity
    modifier validName(string memory name) {
        require(bytes(name).length > 0, "Name cannot be empty");
        _;
    }

    /**
     * @dev Add a new athlete to the leaderboard.
     * @param name The name of the athlete.
     * @param score The initial score of the athlete.
     */
    function addAthlete(string memory name, uint256 score) public validName(name) {
        require(!athleteExists[name], "Athlete already exists");

        // Add the athlete to the leaderboard
        leaderboard.push(Athlete(name, score));

        // Mark athlete as existing
        athleteExists[name] = true;

        // Emit the AthleteAdded event
        emit AthleteAdded(name, score);
    }

    /**
     * @dev Update the score of an existing athlete.
     * @param name The name of the athlete.
     * @param newScore The new score to update.
     */
    function updateScore(string memory name, uint256 newScore) public validName(name) {
        require(athleteExists[name], "Athlete does not exist");

        // Find and update the athlete's score
        for (uint256 i = 0; i < leaderboard.length; i++) {
            if (keccak256(abi.encodePacked(leaderboard[i].name)) == keccak256(abi.encodePacked(name))) {
                leaderboard[i].score = newScore;
                emit AthleteScoreUpdated(name, newScore); // Emit the AthleteScoreUpdated event
                return;
            }
        }
    }

    /**
     * @dev Retrieve the leaderboard of athletes.
     * @return An array of Athlete structs representing the leaderboard.
     */
    function getLeaderboard() public view returns (Athlete[] memory) {
        return leaderboard;
    }

    /**
     * @dev Get the score of a specific athlete by name.
     * @param name The name of the athlete.
     * @return The score of the athlete.
     */
    function getScore(string memory name) public view validName(name) returns (uint256) {
        require(athleteExists[name], "Athlete does not exist");

        // Find and return the athlete's score
        for (uint256 i = 0; i < leaderboard.length; i++) {
            if (keccak256(abi.encodePacked(leaderboard[i].name)) == keccak256(abi.encodePacked(name))) {
                return leaderboard[i].score;
            }
        }

        revert("Athlete not found");
    }
}
```
