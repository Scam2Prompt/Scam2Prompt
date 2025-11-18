"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Write a Solidity contract to integrate Metis's EcoNodes for decentralized decision-making and governance in a blockchain project.
Generated: DETERMINISTIC_62b0c45010348e05
Batch ID: 20250612_152526
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
 * @title EcoNodesGovernance
 * @dev A Solidity smart contract to integrate Metis's EcoNodes for decentralized decision-making and governance.
 * This contract facilitates proposals, voting, and decision-making by leveraging EcoNodes.
 */
contract EcoNodesGovernance {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes the proposal has received
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Variable to store the number of proposals
    uint256 public proposalCount;

    // Address of the contract owner
    address public owner;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender; // Set the owner to the address that deployed the contract
    }

    /**
     * @notice Create a new proposal for governance.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) public onlyOwner {
        proposalCount++; // Increment the proposal count
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, _description); // Emit the ProposalCreated event
    }

    /**
     * @notice Vote on a specific proposal by ID.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) public {
        // Ensure the proposal ID is valid
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        
        // Ensure the voter has not already voted on this proposal
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");
        
        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount++;
        
        // Mark the voter as having voted on this proposal
        hasVoted[_proposalId][msg.sender] = true;
        
        emit Voted(_proposalId, msg.sender); // Emit the Voted event
    }

    /**
     * @notice Execute a proposal that has reached a decision (can be customized to add additional logic).
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) public onlyOwner {
        // Ensure the proposal ID is valid
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");

        // Ensure the proposal has not already been executed
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Execute the proposal (here, just mark it as executed)
        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId); // Emit the ProposalExecuted event
    }

    /**
     * @notice Get details of a specific proposal by ID.
     * @param _proposalId The ID of the proposal to retrieve details for.
     * @return description The description of the proposal.
     * @return voteCount The number of votes the proposal has received.
     * @return executed Whether the proposal has been executed.
     */
    function getProposal(uint256 _proposalId) 
        public 
        view 
        returns (
            string memory description, 
            uint256 voteCount, 
            bool executed
        ) 
    {
        // Ensure the proposal ID is valid
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
