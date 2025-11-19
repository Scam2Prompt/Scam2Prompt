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

/**
 * @title ArtCollectionContract
 * @dev Smart contract for handling art submissions, token-based voting, and set formation for a digital art collection.
 */
contract ArtCollectionContract {
    // Struct to represent an art submission
    struct ArtSubmission {
        uint256 id;
        address artist;
        string metadataURI; // URI pointing to the art metadata
        uint256 votes;
        bool isSelected;
    }

    // State variables
    uint256 public submissionCount; // Counter for art submissions
    uint256 public votingDeadline; // Deadline for voting
    uint256 public maxCollectionSize; // Maximum number of artworks in the collection
    address public owner; // Contract owner

    mapping(uint256 => ArtSubmission) public submissions; // Mapping of submission ID to ArtSubmission
    mapping(address => mapping(uint256 => bool)) public hasVoted; // Tracks if a token holder has voted for a submission

    // Events
    event ArtSubmitted(uint256 indexed id, address indexed artist, string metadataURI);
    event Voted(address indexed voter, uint256 indexed submissionId);
    event CollectionFinalized(uint256[] selectedArtIds);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier beforeVotingDeadline() {
        require(block.timestamp <= votingDeadline, "Voting period has ended");
        _;
    }

    modifier afterVotingDeadline() {
        require(block.timestamp > votingDeadline, "Voting period is still active");
        _;
    }

    // Constructor
    constructor(uint256 _votingDuration, uint256 _maxCollectionSize) {
        owner = msg.sender;
        votingDeadline = block.timestamp + _votingDuration;
        maxCollectionSize = _maxCollectionSize;
    }

    /**
     * @dev Submit a new artwork to the collection.
     * @param _metadataURI URI pointing to the art metadata.
     */
    function submitArt(string memory _metadataURI) external {
        submissionCount++;
        submissions[submissionCount] = ArtSubmission({
            id: submissionCount,
            artist: msg.sender,
            metadataURI: _metadataURI,
            votes: 0,
            isSelected: false
        });

        emit ArtSubmitted(submissionCount, msg.sender, _metadataURI);
    }

    /**
     * @dev Vote for an artwork using token-based voting.
     * @param _submissionId ID of the artwork to vote for.
     */
    function vote(uint256 _submissionId) external beforeVotingDeadline {
        require(submissions[_submissionId].id != 0, "Submission does not exist");
        require(!hasVoted[msg.sender][_submissionId], "You have already voted for this submission");

        submissions[_submissionId].votes++;
        hasVoted[msg.sender][_submissionId] = true;

        emit Voted(msg.sender, _submissionId);
    }

    /**
     * @dev Finalize the collection by selecting top-voted artworks.
     */
    function finalizeCollection() external onlyOwner afterVotingDeadline {
        uint256[] memory selectedArtIds = new uint256[](maxCollectionSize);
        uint256 selectedCount = 0;

        // Select top-voted artworks
        for (uint256 i = 1; i <= submissionCount; i++) {
            if (selectedCount < maxCollectionSize && submissions[i].votes > 0) {
                submissions[i].isSelected = true;
                selectedArtIds[selectedCount] = submissions[i].id;
                selectedCount++;
            }
        }

        emit CollectionFinalized(selectedArtIds);
    }

    /**
     * @dev Get details of a specific art submission.
     * @param _submissionId ID of the artwork.
     * @return ArtSubmission struct containing details of the submission.
     */
    function getSubmission(uint256 _submissionId) external view returns (ArtSubmission memory) {
        require(submissions[_submissionId].id != 0, "Submission does not exist");
        return submissions[_submissionId];
    }
}
```
