"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaindigital.pages.dev
Prompt: Provide an example of how to implement a DAO voting mechanism in a smart contract, inspired by the Popcorn DAO mentioned on the Chain Digital webpage.
Generated: DETERMINISTIC_a53ae944d5208b79
Batch ID: 20250612_162207
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
 * @title DAO Voting Mechanism
 * @dev A simple voting mechanism for a DAO. Members can propose actions and vote on them.
 */
contract DAOVoting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Proposal description
        uint256 voteCount; // Number of votes received
        bool executed; // Proposal execution status
    }

    // List of proposals
    Proposal[] public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Address of the DAO owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Modifier to ensure a valid proposal index
    modifier validProposalIndex(uint256 proposalIndex) {
        require(proposalIndex < proposals.length, "Invalid proposal index.");
        _;
    }

    // Event to log the creation of a new proposal
    event ProposalCreated(uint256 indexed proposalIndex, string description);

    // Event to log a vote
    event Voted(uint256 indexed proposalIndex, address indexed voter);

    // Event to log proposal execution
    event ProposalExecuted(uint256 indexed proposalIndex, string description);

    /**
     * @dev Contract constructor to set the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalIndex Index of the proposal to vote on.
     */
    function vote(uint256 _proposalIndex) external validProposalIndex(_proposalIndex) {
        require(!hasVoted[_proposalIndex][msg.sender], "You have already voted on this proposal.");
        require(!proposals[_proposalIndex].executed, "Proposal has already been executed.");

        proposals[_proposalIndex].voteCount++;
        hasVoted[_proposalIndex][msg.sender] = true;

        emit Voted(_proposalIndex, msg.sender);
    }

    /**
     * @dev Function to execute a proposal if it reaches the required votes.
     * @param _proposalIndex Index of the proposal to execute.
     */
    function executeProposal(uint256 _proposalIndex) external onlyOwner validProposalIndex(_proposalIndex) {
        require(!proposals[_proposalIndex].executed, "Proposal has already been executed.");
        require(proposals[_proposalIndex].voteCount > 0, "Proposal must have at least one vote to be executed.");

        proposals[_proposalIndex].executed = true;

        // Proposal execution logic can be added here (e.g., transferring funds, updating state, etc.)
        emit ProposalExecuted(_proposalIndex, proposals[_proposalIndex].description);
    }

    /**
     * @dev Function to get the total number of proposals.
     * @return Total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Function to get details of a proposal.
     * @param _proposalIndex Index of the proposal.
     * @return Description, vote count, and execution status of the proposal.
     */
    function getProposalDetails(uint256 _proposalIndex) 
        external 
        view 
        validProposalIndex(_proposalIndex) 
        returns (string memory, uint256, bool) 
    {
        Proposal memory proposal = proposals[_proposalIndex];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
