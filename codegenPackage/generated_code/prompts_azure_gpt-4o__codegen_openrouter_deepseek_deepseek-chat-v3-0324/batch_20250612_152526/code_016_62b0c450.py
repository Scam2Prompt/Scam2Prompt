"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: Write a Solidity contract to integrate Metis's EcoNodes for decentralized decision-making and governance in a blockchain project.
Generated: DETERMINISTIC_62b0c45010348e05
Batch ID: 20250612_152526
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

import "@metis.io/contracts/EcoNodes/EcoNodesInterface.sol";

/**
 * @title GovernanceContract
 * @dev A contract for decentralized decision-making using Metis EcoNodes
 */
contract GovernanceContract {
    // EcoNodes interface instance
    EcoNodesInterface public ecoNodes;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Counter for proposals
    uint256 public proposalCount;

    // Minimum voting duration (in seconds)
    uint256 public constant MIN_VOTING_DURATION = 86400; // 1 day

    // Events
    event ProposalCreated(uint256 indexed id, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Constructor
     * @param _ecoNodesAddress Address of the EcoNodes contract
     */
    constructor(address _ecoNodesAddress) {
        require(_ecoNodesAddress != address(0), "Invalid EcoNodes address");
        ecoNodes = EcoNodesInterface(_ecoNodesAddress);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _votingDuration Duration of voting period in seconds
     */
    function createProposal(string memory _description, uint256 _votingDuration) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_votingDuration >= MIN_VOTING_DURATION, "Voting duration too short");

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + _votingDuration;

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;

        emit ProposalCreated(proposalCount, _description, startTime, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support Whether the voter supports the proposal
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!proposal.voters[msg.sender], "Already voted");
        
        // Check if voter is a valid EcoNode
        require(ecoNodes.isEcoNode(msg.sender), "Only EcoNodes can vote");

        proposal.voters[msg.sender] = true;
        if (_support) {
            proposal.voteCount++;
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalEcoNodes = ecoNodes.getTotalEcoNodes();
        require(proposal.voteCount > totalEcoNodes / 2, "Majority not reached");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: call other contracts, change state, etc.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Check if an address has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address of the voter
     * @return bool Whether the address has voted
     */
    function hasVoted(uint256 _proposalId, address _voter) public view returns (bool) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId].voters[_voter];
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return id, description, voteCount, startTime, endTime, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteCount,
        uint256 startTime,
        uint256 endTime,
        bool executed
    ) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.voteCount,
            proposal.startTime,
            proposal.endTime,
            proposal.executed
        );
    }
}
```
