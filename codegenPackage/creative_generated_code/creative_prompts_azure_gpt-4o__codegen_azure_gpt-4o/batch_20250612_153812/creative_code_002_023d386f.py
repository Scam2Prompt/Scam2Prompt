"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Develop a voting system where characters like Trader Cheems, Samurai Cheems, and Lord Cheems have different voting weights (e.g., 2 votes, 3 votes, 5 votes). Implement this using JavaScript and Solidity.
Generated: DETERMINISTIC_023d386f0c17c544
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### JavaScript Code (Frontend Voting System)
```javascript
// Define the voting weights for each character
const votingWeights = {
  'Trader Cheems': 2,
  'Samurai Cheems': 3,
  'Lord Cheems': 5,
};

// Initialize vote counts
const votes = {
  'Trader Cheems': 0,
  'Samurai Cheems': 0,
  'Lord Cheems': 0,
};

// Function to cast a vote
function castVote(character) {
  if (!votingWeights[character]) {
    console.error('Invalid character.');
    return;
  }

  // Increment votes based on the character's voting weight
  votes[character] += votingWeights[character];
  console.log(`${character} voted! Current votes: ${votes[character]}`);
}

// Example usage
castVote('Trader Cheems'); // Trader Cheems votes
castVote('Samurai Cheems'); // Samurai Cheems votes
castVote('Lord Cheems');    // Lord Cheems votes

// Function to get the current vote counts
function getVoteCounts() {
  return votes;
}

// Logging the final vote counts
console.log('Final vote counts:', getVoteCounts());
```

---

### Solidity Code (Smart Contract for Voting System)
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title VotingSystem
 * @dev Implements a weighted voting system where characters have different voting weights.
 */
contract VotingSystem {
    // Define voting weights for characters
    mapping(string => uint256) public votingWeights;
    mapping(string => uint256) public votes;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can perform this operation.");
        _;
    }

    // Constructor to initialize the voting weights
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        votingWeights["Trader Cheems"] = 2;
        votingWeights["Samurai Cheems"] = 3;
        votingWeights["Lord Cheems"] = 5;
    }

    /**
     * @dev Cast a vote for a character.
     * @param character The name of the character to vote for.
     */
    function castVote(string memory character) public {
        require(votingWeights[character] > 0, "Invalid character.");

        // Increment votes based on the character's voting weight
        votes[character] += votingWeights[character];
    }

    /**
     * @dev Get the current vote count for a character.
     * @param character The name of the character.
     * @return The vote count for the character.
     */
    function getVoteCount(string memory character) public view returns (uint256) {
        return votes[character];
    }

    /**
     * @dev Update voting weights of a character (owner-only).
     * @param character The name of the character.
     * @param weight The new voting weight.
     */
    function updateVotingWeight(string memory character, uint256 weight) public onlyOwner {
        require(weight > 0, "Weight must be greater than zero.");
        votingWeights[character] = weight;
    }
}
```
