"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ambassadors.org
Prompt: Write a smart contract that rewards creativity and shares power in a decentralized ecosystem, inspired by Starknet Foundation's mission.
Generated: DETERMINISTIC_ced92b0aaa23149b
Batch ID: 20250612_150342
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

/// @title CreativityRewardContract
/// @notice A smart contract to reward creative contributions in a decentralized ecosystem
/// @dev This contract allows users to submit creative ideas and get rewarded based on community votes

contract CreativityRewardContract {
    struct Idea {
        string description;
        address creator;
        uint256 votes;
        bool exists;
    }

    // Mapping from idea ID to Idea object
    mapping(uint256 => Idea) public ideas;
    // Mapping to track votes by address
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    // Total number of ideas submitted
    uint256 public ideaCount;

    // Event emitted when a new idea is submitted
    event IdeaSubmitted(uint256 indexed ideaId, string description, address indexed creator);
    // Event emitted when an idea is voted on
    event IdeaVoted(uint256 indexed ideaId, address indexed voter);

    /// @notice Submit a new creative idea
    /// @param _description A short description of the creative idea
    /// @dev Requires a non-empty description
    function submitIdea(string calldata _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        ideaCount++;
        ideas[ideaCount] = Idea({
            description: _description,
            creator: msg.sender,
            votes: 0,
            exists: true
        });

        emit IdeaSubmitted(ideaCount, _description, msg.sender);
    }

    /// @notice Vote for a creative idea
    /// @param _ideaId The ID of the idea to vote for
    /// @dev Requires the idea to exist and the voter to not have voted before
    function voteForIdea(uint256 _ideaId) external {
        require(ideas[_ideaId].exists, "Idea does not exist");
        require(!hasVoted[msg.sender][_ideaId], "You have already voted for this idea");

        ideas[_ideaId].votes++;
        hasVoted[msg.sender][_ideaId] = true;

        emit IdeaVoted(_ideaId, msg.sender);
    }

    /// @notice Get the details of an idea
    /// @param _ideaId The ID of the idea
    /// @return description The description of the idea
    /// @return creator The address of the idea creator
    /// @return votes The number of votes the idea has received
    function getIdea(uint256 _ideaId) external view returns (string memory description, address creator, uint256 votes) {
        require(ideas[_ideaId].exists, "Idea does not exist");

        Idea memory idea = ideas[_ideaId];
        return (idea.description, idea.creator, idea.votes);
    }

    /// @notice Get the total number of ideas submitted
    /// @return The total number of ideas
    function totalIdeas() external view returns (uint256) {
        return ideaCount;
    }
}
```
