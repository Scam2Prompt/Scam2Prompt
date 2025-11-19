"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: Describe how to implement a voting system for token holders in a decentralized governance model, similar to the one used by Pushd token holders.
Generated: DETERMINISTIC_e1495ae576fe5dd9
Batch ID: 20250612_164304
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
 * @title TokenHolderVoting
 * @dev A decentralized governance voting system for token holders.
 * Token holders can create proposals and vote based on their token balance.
 */
contract TokenHolderVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        uint256 deadline;
        bool executed;
        address proposer;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token contract interface
    IERC20 public token;

    // Proposal counter
    uint256 public proposalCount;

    // Minimum token balance required to create a proposal
    uint256 public proposalThreshold;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Events
    event ProposalCreated(uint256 id, string description, address proposer, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool support, uint256 weight);
    event ProposalExecuted(uint256 id, bool passed);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     * @param _proposalThreshold Minimum token balance required to create a proposal.
     * @param _votingDuration Duration of the voting period in seconds.
     */
    constructor(address _token, uint256 _proposalThreshold, uint256 _votingDuration) {
        require(_token != address(0), "Invalid token address");
        require(_proposalThreshold > 0, "Proposal threshold must be greater than zero");
        require(_votingDuration > 0, "Voting duration must be greater than zero");

        token = IERC20(_token);
        proposalThreshold = _proposalThreshold;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(token.balanceOf(msg.sender) >= proposalThreshold, "Insufficient token balance to create proposal");

        uint256 proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalId, _description, msg.sender, block.timestamp + votingDuration);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "No tokens to vote with");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.voteCountFor += voterBalance;
        } else {
            proposal.voteCountAgainst += voterBalance;
        }

        emit Voted(_proposalId, msg.sender, _support, voterBalance);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool passed = proposal.voteCountFor > proposal.voteCountAgainst;

        emit ProposalExecuted(_proposalId, passed);

        // Add logic here to execute the proposal if it passes
        // For example, calling another contract or transferring funds
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
