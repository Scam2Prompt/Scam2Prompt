"""
Generated Code Metadata:
========================
Original URL: https://openweb-3ua.pages.dev
Prompt: Generate a smart contract code snippet for handling art submissions, token voting, and set formation for a digital art collection, inspired by Opepen's "Permanent Collection" model.
Generated: DETERMINISTIC_c5063693885a1a0e
Batch ID: 20250622_210856
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for managing art submissions and voting for a digital art collection
contract DigitalArtCollection is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent an art submission
    struct ArtSubmission {
        uint256 id;
        address artist;
        string metadataURI; // URI pointing to the art metadata
        uint256 voteCount;
        bool exists;
    }

    // Mapping from submission ID to ArtSubmission
    mapping(uint256 => ArtSubmission) public submissions;
    // Counter for generating unique submission IDs
    Counters.Counter private submissionIdCounter;
    // Array to hold all submission IDs for iteration
    uint256[] public submissionIds;

    // Event emitted when a new art submission is created
    event ArtSubmitted(uint256 indexed submissionId, address indexed artist, string metadataURI);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed submissionId, address indexed voter);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("DigitalArtCollection", "DAC") {}

    // Function to submit new art
    function submitArt(string memory _metadataURI) external {
        // Increment the submission ID counter
        submissionIdCounter.increment();
        uint256 newSubmissionId = submissionIdCounter.current();

        // Create a new art submission
        submissions[newSubmissionId] = ArtSubmission({
            id: newSubmissionId,
            artist: msg.sender,
            metadataURI: _metadataURI,
            voteCount: 0,
            exists: true
        });

        // Add the new submission ID to the array
        submissionIds.push(newSubmissionId);

        // Emit the ArtSubmitted event
        emit ArtSubmitted(newSubmissionId, msg.sender, _metadataURI);
    }

    // Function to vote for an art submission
    function vote(uint256 _submissionId) external {
        // Ensure the submission exists
        require(submissions[_submissionId].exists, "Submission does not exist");

        // Increment the vote count for the submission
        submissions[_submissionId].voteCount++;

        // Emit the Voted event
        emit Voted(_submissionId, msg.sender);
    }

    // Function to get submission details
    function getSubmission(uint256 _submissionId) external view returns (ArtSubmission memory) {
        // Ensure the submission exists
        require(submissions[_submissionId].exists, "Submission does not exist");
        return submissions[_submissionId];
    }

    // Function to get all submission IDs
    function getAllSubmissions() external view returns (uint256[] memory) {
        return submissionIds;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
