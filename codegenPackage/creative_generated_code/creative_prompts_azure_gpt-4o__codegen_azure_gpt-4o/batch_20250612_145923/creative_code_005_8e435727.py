"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Create a governance system in Solidity for a blockchain marketplace, enabling token holders to propose and vote on platform changes, similar to Pushd's decentralized governance model.
Generated: DETERMINISTIC_8e43572783a9e1ff
Batch ID: 20250612_145923
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
 * @title GovernanceSystem
 * @dev A decentralized governance system for a blockchain marketplace that allows token holders to propose and vote on platform changes.
 */
contract GovernanceSystem {
    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description; // Short description of the proposal
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline; // Deadline for voting
        bool executed; // Whether the proposal has been executed
        address proposer; // Address of the proposer
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Governance token contract reference
    IERC20 public governanceToken;

    // Minimum token balance required to create a proposal
    uint256 public proposalThreshold;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Events
    event ProposalCreated(uint256 id, string description, address proposer, uint256 deadline);
    event ProposalVoted(uint256 id, address voter, bool support);
    event ProposalExecuted(uint256 id, bool success);

    /**
     * @dev Constructor to initialize the governance system.
     * @param _governanceToken Address of the governance token contract.
     * @param _proposalThreshold Minimum token balance required to create a proposal.
     * @param _votingDuration Voting duration in seconds.
     */
    constructor(
        address _governanceToken,
        uint256 _proposalThreshold,
        uint256 _votingDuration
    ) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_proposalThreshold > 0, "Proposal threshold must be greater than zero");
        require(_votingDuration > 0, "Voting duration must be greater than zero");

        governanceToken = IERC20(_governanceToken);
        proposalThreshold = _proposalThreshold;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(
            governanceToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient token balance to create proposal"
        );

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalCount, _description, msg.sender, block.timestamp + votingDuration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function voteOnProposal(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has expired");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");
        require(governanceToken.balanceOf(msg.sender) > 0, "Insufficient token balance to vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit ProposalVoted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal if it has passed.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period is not yet over");
        require(!proposal.executed, "Proposal already executed");

        // Proposal passes if votesFor > votesAgainst
        bool success = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(_proposalId, success);
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
