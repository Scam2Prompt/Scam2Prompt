"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Write a Solidity contract that incorporates Deadpool Inu's ethos by allowing token holders to vote on humorous community proposals, such as meme contests or pop culture collaborations.
Generated: DETERMINISTIC_d003759b651571ff
Batch ID: 20250612_145715
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

/// @title Deadpool Inu Community Voting Contract
/// @notice This contract allows token holders to vote on humorous proposals
/// such as meme contests or pop culture collaborations.
/// @dev Designed to align with Deadpool Inu's ethos of fun and community engagement.
contract DeadpoolInuVoting {
    // -------------------------------
    // Structs
    // -------------------------------
    
    struct Proposal {
        string description; // Description of the community proposal
        uint256 voteCount;  // Total number of votes the proposal has received
        bool active;        // Whether the proposal is open for voting
    }

    // -------------------------------
    // State Variables
    // -------------------------------
    
    address public owner; // Contract owner
    Proposal[] public proposals; // Array of proposals
    mapping(uint256 => mapping(address => bool)) public votes; // Tracks if a user has voted on a proposal

    // -------------------------------
    // Events
    // -------------------------------
    
    event ProposalCreated(uint256 proposalId, string description);
    event VoteCast(address voter, uint256 proposalId);
    event ProposalClosed(uint256 proposalId);

    // -------------------------------
    // Modifiers
    // -------------------------------
    
    /// @notice Restricts a function to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /// @notice Restricts a function to only active proposals
    modifier onlyActiveProposal(uint256 proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    // -------------------------------
    // Constructor
    // -------------------------------
    
    /// @notice Initializes the contract's owner
    constructor() {
        owner = msg.sender;
    }

    // -------------------------------
    // Functions
    // -------------------------------

    /// @notice Allows the owner to create a new proposal
    /// @param _description The description of the proposal
    function createProposal(string calldata _description) external onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            active: true
        }));

        emit ProposalCreated(proposals.length - 1, _description);
    }

    /// @notice Allows a token holder to vote on an active proposal
    /// @param proposalId The ID of the proposal to vote on
    function vote(uint256 proposalId) external onlyActiveProposal(proposalId) {
        require(!votes[proposalId][msg.sender], "You have already voted on this proposal");

        // Record the user's vote
        votes[proposalId][msg.sender] = true;

        // Increment the proposal's vote count
        proposals[proposalId].voteCount += 1;

        emit VoteCast(msg.sender, proposalId);
    }

    /// @notice Allows the owner to close voting on a proposal
    /// @param proposalId The ID of the proposal to close
    function closeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(proposals[proposalId].active, "Proposal is already closed");

        // Mark the proposal as inactive
        proposals[proposalId].active = false;

        emit ProposalClosed(proposalId);
    }

    /// @notice Retrieves proposal details
    /// @param proposalId The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The vote count of the proposal
    /// @return active Whether the proposal is active
    function getProposal(uint256 proposalId) 
        external 
        view 
        returns (string memory description, uint256 voteCount, bool active) 
    {
        require(proposalId < proposals.length, "Invalid proposal ID");

        Proposal memory p = proposals[proposalId];
        return (p.description, p.voteCount, p.active);
    }

    /// @notice Returns the total number of proposals
    /// @return The number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
