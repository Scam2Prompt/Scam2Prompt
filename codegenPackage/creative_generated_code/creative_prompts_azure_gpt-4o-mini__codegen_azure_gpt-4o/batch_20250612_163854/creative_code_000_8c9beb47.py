"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for my project?
Generated: DETERMINISTIC_8c9beb47c5aadce2
Batch ID: 20250612_163854
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

/**
 * @title AgoraOnChainGovernance
 * @notice This contract implements on-chain governance using the Agora platform's principles.
 * @dev This is a simplified example. For production use, customize as per your project's requirements.
 */
contract AgoraOnChainGovernance {
    // State variables
    uint256 public proposalCount; // Counter to track total proposals
    address public admin; // Address of the contract administrator

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;            // Unique ID for the proposal
        string description;    // Text describing the proposal
        uint256 voteCountYes;  // Number of votes in favor
        uint256 voteCountNo;   // Number of votes against
        bool executed;         // Whether the proposal has been executed
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter, bool voteYes);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the contract
    constructor() {
        admin = msg.sender; // Set the deployer as the admin
    }

    /**
     * @dev Function to create a new proposal.
     * @param description The text description of the proposal.
     */
    function createProposal(string memory description) external onlyAdmin {
        proposalCount++; // Increment proposal counter
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCountYes: 0,
            voteCountNo: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param voteYes True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool voteYes) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        require(!hasVoted[proposalId][msg.sender], "You have already voted");

        hasVoted[proposalId][msg.sender] = true; // Mark the voter as having voted

        if (voteYes) {
            proposal.voteCountYes++; // Increment 'yes' votes
        } else {
            proposal.voteCountNo++; // Increment 'no' votes
        }

        emit Voted(proposalId, msg.sender, voteYes);
    }

    /**
     * @dev Function to execute a proposal.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyAdmin {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");
        require(
            proposal.voteCountYes > proposal.voteCountNo,
            "Proposal did not pass"
        );

        proposal.executed = true; // Mark the proposal as executed
        emit ProposalExecuted(proposalId);

        // Add logic for executing the proposal action here (e.g., transferring funds, updating data, etc.)
    }

    /**
     * @dev Function to retrieve details of a specific proposal.
     * @param proposalId The ID of the proposal to retrieve.
     * @return Proposal Details of the specified proposal.
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            string memory description,
            uint256 voteCountYes,
            uint256 voteCountNo,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        return (
            proposal.id,
            proposal.description,
            proposal.voteCountYes,
            proposal.voteCountNo,
            proposal.executed
        );
    }
}
```
