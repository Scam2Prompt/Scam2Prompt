"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Provide an example of a smart contract that integrates with Agora for managing voting on Optimism proposals.
Generated: DETERMINISTIC_f9465da2ad56bb80
Batch ID: 20250612_163854
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
 * @title OptimismVotingContract
 * @dev A smart contract for managing voting on Optimism proposals using Agora integration.
 */
contract OptimismVotingContract {
    // Address of the Agora contract
    address public agoraContract;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool exists;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, address indexed voter);

    /**
     * @dev Constructor to initialize the Agora contract address.
     * @param _agoraContract Address of the Agora contract.
     */
    constructor(address _agoraContract) {
        require(_agoraContract != address(0), "Invalid Agora contract address");
        agoraContract = _agoraContract;
    }

    /**
     * @dev Function to create a new proposal.
     * @param proposalId Unique ID of the proposal.
     * @param description Description of the proposal.
     */
    function createProposal(uint256 proposalId, string memory description) external {
        require(!proposals[proposalId].exists, "Proposal ID already exists");

        // Create a new proposal
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Function to cast a vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function castVote(uint256 proposalId) external {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        // Mark the sender as having voted
        hasVoted[proposalId][msg.sender] = true;

        // Increment the vote count for the proposal
        proposals[proposalId].voteCount++;

        emit VoteCast(proposalId, msg.sender);
    }

    /**
     * @dev Function to get the details of a proposal.
     * @param proposalId ID of the proposal to retrieve.
     * @return description Description of the proposal.
     * @return voteCount Number of votes the proposal has received.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount) {
        require(proposals[proposalId].exists, "Proposal does not exist");

        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    /**
     * @dev Function to check if an address has voted on a proposal.
     * @param proposalId ID of the proposal.
     * @param voter Address of the voter.
     * @return True if the voter has voted, false otherwise.
     */
    function hasVotedOnProposal(uint256 proposalId, address voter) external view returns (bool) {
        return hasVoted[proposalId][voter];
    }
}
```
