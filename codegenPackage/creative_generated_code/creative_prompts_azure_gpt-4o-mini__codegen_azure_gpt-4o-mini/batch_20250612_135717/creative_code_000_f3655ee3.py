"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: How can I implement an NFT claim feature for a voting system similar to the one described on the Shibuya website?
Generated: DETERMINISTIC_f3655ee319c77fe3
Batch ID: 20250612_135717
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract VotingWithNFT is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a voting option
    struct VoteOption {
        string name;
        uint256 voteCount;
    }

    // Mapping from NFT token ID to whether the token has claimed their vote
    mapping(uint256 => bool) public hasClaimedVote;

    // Array of voting options
    VoteOption[] public voteOptions;

    // Event for when a vote is cast
    event VoteCast(uint256 indexed optionIndex, address indexed voter);

    // Counter for tracking current option index
    Counters.Counter private optionCounter;

    // The NFT contract that governs the ownership of NFTs
    IERC721 public nftContract;

    // Constructor to initialize the NFT contract and voting options
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }

    // Function to add voting options
    function addVoteOption(string memory optionName) external onlyOwner {
        require(bytes(optionName).length > 0, "Option name cannot be empty");
        voteOptions.push(VoteOption(optionName, 0));
        optionCounter.increment();
    }

    // Function to claim a vote using the NFT token ID
    function claimVote(uint256 tokenId, uint256 optionIndex) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Ensure the token has not already claimed its vote
        require(!hasClaimedVote[tokenId], "Vote already claimed for this NFT");
        
        // Ensure the option index is valid
        require(optionIndex < optionCounter.current(), "Invalid option index");

        // Mark the token as having claimed their vote
        hasClaimedVote[tokenId] = true;

        // Increment the vote count for the selected option
        voteOptions[optionIndex].voteCount++;

        // Emit the vote cast event
        emit VoteCast(optionIndex, msg.sender);
    }

    // Function to get the total number of options
    function getVoteOptionCount() external view returns (uint256) {
        return optionCounter.current();
    }

    // Function to get details of a specific vote option
    function getVoteOption(uint256 optionIndex) external view returns (string memory name, uint256 voteCount) {
        require(optionIndex < optionCounter.current(), "Invalid option index");
        VoteOption memory option = voteOptions[optionIndex];
        return (option.name, option.voteCount);
    }
}
```
