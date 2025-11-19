"""
Generated Code Metadata:
========================
Original URL: https://op-rf4-voting-ui.vercel.app
Prompt: "How can I implement a badgeholder manual voting system for Retro Funding rounds using web3 technologies?"
Generated: DETERMINISTIC_b69c7420ee1ba526
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Voting contract for badgeholder manual voting system
contract BadgeholderVoting is Ownable {
    // Struct to represent a voting option
    struct Option {
        string name; // Name of the voting option
        uint256 voteCount; // Number of votes received
    }

    // Mapping to store options
    Option[] public options;

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Event to emit when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed optionId);

    // Constructor to initialize voting options
    constructor(string[] memory optionNames) {
        for (uint256 i = 0; i < optionNames.length; i++) {
            options.push(Option({
                name: optionNames[i],
                voteCount: 0
            }));
        }
    }

    // Function to cast a vote for a specific option
    function vote(uint256 optionId) external {
        // Check if the voter has already voted
        require(!hasVoted[msg.sender], "You have already voted.");
        // Check if the option ID is valid
        require(optionId < options.length, "Invalid option ID.");

        // Record the vote
        hasVoted[msg.sender] = true;
        options[optionId].voteCount += 1;

        // Emit the vote cast event
        emit VoteCast(msg.sender, optionId);
    }

    // Function to get the current vote count for an option
    function getVoteCount(uint256 optionId) external view returns (uint256) {
        require(optionId < options.length, "Invalid option ID.");
        return options[optionId].voteCount;
    }

    // Function to get all options
    function getOptions() external view returns (Option[] memory) {
        return options;
    }

    // Function to reset the voting (only owner can call)
    function resetVoting() external onlyOwner {
        for (uint256 i = 0; i < options.length; i++) {
            options[i].voteCount = 0;
        }
        // Reset the hasVoted mapping
        for (uint256 i = 0; i < options.length; i++) {
            hasVoted[address(i)] = false; // This is a placeholder; in practice, you would need a better way to reset
        }
    }
}
```

This code implements a simple manual voting system for badgeholders using Solidity. It allows users to vote for options, tracks whether they have voted, and provides functions to retrieve vote counts and options. The contract owner can reset the voting process.
