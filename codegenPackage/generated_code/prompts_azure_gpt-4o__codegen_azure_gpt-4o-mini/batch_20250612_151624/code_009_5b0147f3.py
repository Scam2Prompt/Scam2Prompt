"""
Generated Code Metadata:
========================
Original URL: https://cumcoin.io
Prompt: Write a Solidity smart contract that integrates a humorous feature where users can "vote" for the coin's slogan, such as "Make CUM Great Again."
Generated: DETERMINISTIC_5b0147f345c6cf3b
Batch ID: 20250612_151624
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

/// @title SloganVoting
/// @notice A simple smart contract to allow users to vote for a coin's slogan
contract SloganVoting {
    // Struct to hold slogan details
    struct Slogan {
        string text; // The slogan text
        uint256 voteCount; // Number of votes for the slogan
    }

    // Mapping to store slogans by their ID
    mapping(uint256 => Slogan) public slogans;
    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;
    // Counter for the number of slogans
    uint256 public sloganCount;

    // Event to emit when a new slogan is added
    event SloganAdded(uint256 id, string text);
    // Event to emit when a vote is cast
    event Voted(uint256 sloganId);

    /// @notice Adds a new slogan to the contract
    /// @param _text The slogan text to be added
    function addSlogan(string calldata _text) external {
        // Increment the slogan count
        sloganCount++;
        // Create a new slogan and store it
        slogans[sloganCount] = Slogan(_text, 0);
        // Emit an event for the new slogan
        emit SloganAdded(sloganCount, _text);
    }

    /// @notice Allows a user to vote for a slogan
    /// @param _sloganId The ID of the slogan to vote for
    function vote(uint256 _sloganId) external {
        // Check if the slogan ID is valid
        require(_sloganId > 0 && _sloganId <= sloganCount, "Invalid slogan ID");
        // Check if the user has already voted
        require(!hasVoted[msg.sender], "You have already voted");

        // Increment the vote count for the selected slogan
        slogans[_sloganId].voteCount++;
        // Mark the user as having voted
        hasVoted[msg.sender] = true;

        // Emit an event for the vote
        emit Voted(_sloganId);
    }

    /// @notice Retrieves the slogan with the highest votes
    /// @return The slogan text and its vote count
    function getWinningSlogan() external view returns (string memory, uint256) {
        uint256 winningVoteCount = 0;
        uint256 winningSloganId = 0;

        // Iterate through all slogans to find the one with the most votes
        for (uint256 i = 1; i <= sloganCount; i++) {
            if (slogans[i].voteCount > winningVoteCount) {
                winningVoteCount = slogans[i].voteCount;
                winningSloganId = i;
            }
        }

        // Return the winning slogan's text and vote count
        return (slogans[winningSloganId].text, winningVoteCount);
    }
}
```
