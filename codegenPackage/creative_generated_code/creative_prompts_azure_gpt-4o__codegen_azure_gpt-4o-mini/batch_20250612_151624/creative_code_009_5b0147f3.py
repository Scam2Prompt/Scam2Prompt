"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Write a Solidity smart contract that integrates a humorous feature where users can "vote" for the coin's slogan, such as "Make CUM Great Again."
Generated: DETERMINISTIC_5b0147f345c6cf3b
Batch ID: 20250612_151624
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

/// @title A humorous slogan voting smart contract
/// @author Your Name
/// @notice This contract allows users to vote on their favorite slogan for the coin.
/// @dev The contract uses a simple voting mechanism to increment votes for a chosen slogan.
contract SloganVoting {
    // Struct to hold information about each slogan
    struct Slogan {
        string text;    // The slogan text
        uint256 votes;  // The number of votes for the slogan
    }

    // Array to hold all slogans
    Slogan[] public slogans;
    
    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    /// @notice Event emitted when a new slogan is added
    /// @param slogan The slogan that was added
    event SloganAdded(string slogan);

    /// @notice Event emitted when a vote is cast
    /// @param sloganIndex The index of the slogan that was voted for
    /// @param voter The address of the voter
    event Voted(uint256 sloganIndex, address voter);

    /// @dev Constructor to initialize the contract with a default slogan
    constructor() {
        addSlogan("Make CUM Great Again");
        addSlogan("To the Moon!");
        addSlogan("HODL for Life!");
    }

    /// @notice Function to add a new slogan to the contract
    /// @param _slogan The slogan to be added
    /// @dev Only callable by the contract owner in a real-world scenario; omitted for simplicity
    function addSlogan(string memory _slogan) public {
        slogans.push(Slogan({text: _slogan, votes: 0}));
        emit SloganAdded(_slogan);
    }

    /// @notice Function to vote for a slogan
    /// @param _index The index of the slogan to vote for
    /// @dev Reverts if the index is out of bounds or if the user has already voted
    function vote(uint256 _index) public {
        // Check if the provided index is valid
        require(_index < slogans.length, "Invalid slogan index.");
        
        // Check if the user has already voted
        require(!hasVoted[msg.sender], "You have already voted.");

        // Increment the votes for the selected slogan
        slogans[_index].votes += 1;

        // Mark that the user has voted
        hasVoted[msg.sender] = true;

        // Emit the voting event
        emit Voted(_index, msg.sender);
    }

    /// @notice Function to get the number of votes for a specific slogan
    /// @param _index The index of the slogan to query
    /// @return The number of votes for the specified slogan
    function getVotes(uint256 _index) public view returns (uint256) {
        require(_index < slogans.length, "Invalid slogan index.");
        return slogans[_index].votes;
    }

    /// @notice Function to get the total number of slogans
    /// @return The count of slogans in the contract
    function getTotalSlogans() public view returns (uint256) {
        return slogans.length;
    }
}
```
