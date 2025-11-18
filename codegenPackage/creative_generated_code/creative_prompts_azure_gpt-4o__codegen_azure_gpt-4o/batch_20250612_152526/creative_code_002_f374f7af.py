"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Create a governance voting system for a decentralized application using the Community Ecosystem Governance (CEG) framework on Metis. Include code that integrates with Metis's decentralized voting features.
Generated: DETERMINISTIC_f374f7af1c8345ea
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

// Importing necessary libraries and interfaces from Metis
import "@metis-network/core/contracts/interfaces/IGovernance.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GovernanceVotingSystem
 * @dev A decentralized governance voting system using the Metis Community Ecosystem Governance (CEG) framework.
 */
contract GovernanceVotingSystem is Ownable {
    using Counters for Counters.Counter;

    // State variables
    IGovernance public governanceContract; // Address of the Metis governance contract
    Counters.Counter private proposalIdCounter; // Counter for unique proposal IDs
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteStartTime;
        uint256 voteEndTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to its details
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Track if an address has voted on a proposal

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 voteStartTime, uint256 voteEndTime);
    event VoteCast(uint256 indexed proposalId, address voter, bool vote);
    event ProposalExecuted(uint256 indexed proposalId, bool passed);

    /**
     * @dev Constructor to set the governance contract address.
     * @param _governanceContract Address of the Metis governance contract.
     */
    constructor(address _governanceContract) {
        require(_governanceContract != address(0), "Invalid governance contract address");
        governanceContract = IGovernance(_governanceContract);
    }

    /**
     * @dev Create a new proposal for governance voting.
     * @param _description Description of the proposal.
     * @param _voteDuration Duration (in seconds) for voting to remain open.
     */
    function createProposal(string memory _description, uint256 _voteDuration) external onlyOwner {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_voteDuration > 0, "Vote duration must be greater than zero");

        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        Proposal memory newProposal = Proposal({
            id: newProposalId,
            description: _description,
            voteStartTime: block.timestamp,
            voteEndTime: block.timestamp + _voteDuration,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        });

        proposals[newProposalId] = newProposal;

        emit ProposalCreated(newProposalId, _description, newProposal.voteStartTime, newProposal.voteEndTime);
    }

    /**
     * @dev Cast a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote True for 'yes', false for 'no'.
     */
    function castVote(uint256 _proposalId, bool _vote) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.voteStartTime, "Voting has not started yet");
        require(block.timestamp <= proposal.voteEndTime, "Voting has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the vote
        if (_vote) {
            proposal.yesVotes += 1;
        } else {
            proposal.noVotes += 1;
        }
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.voteEndTime, "Voting period has not ended yet");
        require(!proposal.executed, "Proposal has already been executed");

        bool passed = proposal.yesVotes > proposal.noVotes;
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, passed);

        // Integrate execution logic with Metis governance if required
        // Example: Call governance methods to apply state changes
        if (passed) {
            // Add logic to execute governance action if the proposal passes
        }
    }

    /**
     * @dev Get details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
