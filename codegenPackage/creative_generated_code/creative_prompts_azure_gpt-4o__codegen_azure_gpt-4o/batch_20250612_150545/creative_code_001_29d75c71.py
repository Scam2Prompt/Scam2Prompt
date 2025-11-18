"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: Create a smart contract that supports proposal creation within a DAO, inspired by the features showcased on the MetaDAO demo page.
Generated: DETERMINISTIC_29d75c711e3dbfa9
Batch ID: 20250612_150545
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
 * @title DAOProposalContract
 * @dev Smart contract to manage DAO proposals.
 * Allows users to create proposals, view proposals, and includes proper error handling.
 */
contract DAOProposalContract {
    // Structure for storing a proposal
    struct Proposal {
        uint256 id;
        address creator;
        string title;
        string description;
        uint256 creationTime;
        bool executed;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) private proposals;

    // Total number of proposals created
    uint256 private proposalCount;

    // Event to log proposal creation
    event ProposalCreated(
        uint256 indexed id,
        address indexed creator,
        string title,
        string description,
        uint256 creationTime
    );

    // Modifier to ensure only valid proposal IDs are queried
    modifier validProposalId(uint256 proposalId) {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID.");
        _;
    }

    /**
     * @notice Creates a new proposal in the DAO.
     * @param title The title of the proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory title, string memory description) external {
        require(bytes(title).length > 0, "Proposal title cannot be empty.");
        require(bytes(description).length > 0, "Proposal description cannot be empty.");

        proposalCount++;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            creator: msg.sender,
            title: title,
            description: description,
            creationTime: block.timestamp,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, title, description, block.timestamp);
    }

    /**
     * @notice Retrieves a proposal by its ID.
     * @param proposalId The ID of the proposal to retrieve.
     * @return The details of the proposal.
     */
    function getProposal(uint256 proposalId)
        external
        view
        validProposalId(proposalId)
        returns (
            uint256 id,
            address creator,
            string memory title,
            string memory description,
            uint256 creationTime,
            bool executed
        )
    {
        Proposal memory proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.creator,
            proposal.title,
            proposal.description,
            proposal.creationTime,
            proposal.executed
        );
    }

    /**
     * @notice Marks a proposal as executed.
     * @dev Only callable by the creator of the proposal.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external validProposalId(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(msg.sender == proposal.creator, "Only the creator can execute the proposal.");
        require(!proposal.executed, "Proposal is already executed.");

        proposal.executed = true;
    }

    /**
     * @notice Returns the total number of proposals created.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposalCount;
    }
}
```
