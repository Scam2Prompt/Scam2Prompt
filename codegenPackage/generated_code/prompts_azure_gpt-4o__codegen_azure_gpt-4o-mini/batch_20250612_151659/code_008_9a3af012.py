"""
Generated Code Metadata:
========================
Original URL: https://clashofdragonz-mint.com
Prompt: Develop a DAO-based voting system in Solidity that allows NFT holders to decide on the metaverse platform (e.g., Sandbox, Decentraland) for relocating a Play-to-Earn game.
Generated: DETERMINISTIC_9a3af01264abe1e1
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Voting contract for NFT holders to decide on a metaverse platform
contract VotingSystem is Ownable {
    // Struct to hold voting options
    struct Option {
        string name; // Name of the metaverse platform
        uint256 voteCount; // Number of votes received
    }

    // Mapping to track options
    mapping(uint256 => Option) public options;
    uint256 public optionsCount; // Total number of options

    // Mapping to track if an NFT holder has voted
    mapping(address => bool) public hasVoted;

    // Event to emit when a vote is cast
    event VoteCast(address indexed voter, uint256 optionId);

    // Modifier to check if the caller is an NFT holder
    modifier onlyNFTHolder(address nftContract, uint256 tokenId) {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Not the NFT holder");
        _;
    }

    // Constructor to initialize the voting options
    constructor(string[] memory optionNames) {
        require(optionNames.length > 0, "At least one option required");
        for (uint256 i = 0; i < optionNames.length; i++) {
            options[i] = Option({
                name: optionNames[i],
                voteCount: 0
            });
        }
        optionsCount = optionNames.length;
    }

    // Function to cast a vote
    function vote(uint256 optionId, address nftContract, uint256 tokenId) 
        external 
        onlyNFTHolder(nftContract, tokenId) 
    {
        require(!hasVoted[msg.sender], "You have already voted");
        require(optionId < optionsCount, "Invalid option ID");

        // Record the vote
        options[optionId].voteCount += 1;
        hasVoted[msg.sender] = true;

        emit VoteCast(msg.sender, optionId);
    }

    // Function to get the current vote count for an option
    function getVoteCount(uint256 optionId) external view returns (uint256) {
        require(optionId < optionsCount, "Invalid option ID");
        return options[optionId].voteCount;
    }

    // Function to get the name of an option
    function getOptionName(uint256 optionId) external view returns (string memory) {
        require(optionId < optionsCount, "Invalid option ID");
        return options[optionId].name;
    }

    // Function to check if an address has voted
    function hasVotedStatus(address voter) external view returns (bool) {
        return hasVoted[voter];
    }
}
```
