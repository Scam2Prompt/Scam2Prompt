"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Write a script in Solidity to implement governance voting functionality for $QUBE token holders, allowing them to propose and vote on platform decisions.
Generated: DETERMINISTIC_b728a7d4e680d827
Batch ID: 20250612_152620
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
 * @title Qube Governance Voting
 * @author Expert Programmer
 * @notice A contract for $QUBE token holders to propose and vote on platform decisions.
 */
contract QubeGovernance {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline;   // Voting deadline (timestamp)
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // $QUBE token contract interface
    IERC20 public qubeToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);

    // Event emitted when a vote is cast
    event VoteCasted(uint256 proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId, bool passed);

    /**
     * @dev Sets the $QUBE token contract address.
     * @param _qubeToken Address of the $QUBE token contract.
     */
    constructor(address _qubeToken) {
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Modifier to ensure the caller has $QUBE tokens.
     */
    modifier onlyTokenHolder() {
        require(qubeToken.balanceOf(msg.sender) > 0, "Only $QUBE token holders can call this function.");
        _;
    }

    /**
     * @dev Allows token holders to create a new proposal.
     * @param _description The description of the proposal.
     * @param _votingDuration The duration (in seconds) for voting.
     */
    function createProposal(string memory _description, uint256 _votingDuration) external onlyTokenHolder {
        require(_votingDuration > 0, "Voting duration must be greater than zero.");

        // Increment proposal count and create a new proposal
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, proposals[proposalCount].deadline);
    }

    /**
     * @dev Allows token holders to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support True if voting in favor, false if voting against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and voting is still open
        require(proposal.deadline != 0, "Proposal does not exist.");
        require(block.timestamp < proposal.deadline, "Voting period has ended.");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        // Record vote
        hasVoted[_proposalId][msg.sender] = true;

        // Increase vote counts based on vote type
        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCasted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Allows the creator to execute the proposal after the voting deadline.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure proposal exists and voting has ended
        require(proposal.deadline != 0, "Proposal does not exist.");
        require(block.timestamp >= proposal.deadline, "Voting period has not ended.");
        require(!proposal.executed, "Proposal has already been executed.");

        // Determine if the proposal passed
        bool passed = proposal.votesFor > proposal.votesAgainst;

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, passed);

        // Additional logic for executing passed proposals can be implemented here
    }
}

// Interface for ERC20 token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
