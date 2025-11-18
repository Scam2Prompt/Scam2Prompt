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
 * @title MemeAthleteLeaderboard
 * @dev A smart contract for tracking the leaderboard of meme athletes.
 * The contract ensures data integrity and transparency on the blockchain.
 */
contract MemeAthleteLeaderboard {
    struct Athlete {
        string name;          // Name of the athlete
        uint256 score;       // Score of the athlete
        uint256 rank;        // Rank of the athlete based on score
    }

    // Mapping to store athletes by their address
    mapping(address => Athlete) private athletes;
    // Array to keep track of all athlete addresses for leaderboard
    address[] private athleteAddresses;

    // Event emitted when a new athlete is added or updated
    event AthleteUpdated(address indexed athleteAddress, string name, uint256 score, uint256 rank);

    /**
     * @dev Add or update an athlete's score in the leaderboard.
     * @param _name Name of the athlete.
     * @param _score Score of the athlete, must be non-negative.
     */
    function updateAthlete(string memory _name, uint256 _score) public {
        require(bytes(_name).length > 0, "Athlete name cannot be empty.");
        require(_score >= 0, "Score must be non-negative.");

        if (athletes[msg.sender].score == 0) {
            // New athlete
            athleteAddresses.push(msg.sender);
        }

        // Update athlete's score and name
        athletes[msg.sender].name = _name;
        athletes[msg.sender].score = _score;

        // Re-rank the leaderboard
        updateRanks();

        emit AthleteUpdated(msg.sender, _name, _score, athletes[msg.sender].rank);
    }

    /**
     * @dev Internal function to update ranks based on scores.
     */
    function updateRanks() internal {
        // Sort athletes by score and update ranks
        for (uint256 i = 0; i < athleteAddresses.length; i++) {
            for (uint256 j = i + 1; j < athleteAddresses.length; j++) {
                if (athletes[athleteAddresses[i]].score < athletes[athleteAddresses[j]].score) {
                    address temp = athleteAddresses[i];
                    athleteAddresses[i] = athleteAddresses[j];
                    athleteAddresses[j] = temp;
                }
            }
        }

        // Assign ranks based on sorted order
        for (uint256 i = 0; i < athleteAddresses.length; i++) {
            athletes[athleteAddresses[i]].rank = i + 1;
        }
    }

    /**
     * @dev Retrieve athlete data by address.
     * @param _athleteAddress Address of the athlete.
     * @return name Name of the athlete.
     * @return score Score of the athlete.
     * @return rank Rank of the athlete.
     */
    function getAthlete(address _athleteAddress) public view returns (string memory name, uint256 score, uint256 rank) {
        require(_athleteAddress != address(0), "Invalid address.");
        Athlete memory athlete = athletes[_athleteAddress];
        return (athlete.name, athlete.score, athlete.rank);
    }

    /**
     * @dev Retrieve the leaderboard as an array of athlete addresses sorted by their scores.
     * @return address[] List of athlete addresses in leaderboard order.
     */
    function getLeaderboard() public view returns (address[] memory) {
        return athleteAddresses;
    }

    /**
     * @dev Get total number of athletes in the leaderboard.
     * @return uint256 Number of athletes.
     */
    function getTotalAthletes() public view returns (uint256) {
        return athleteAddresses.length;
    }
}
```
