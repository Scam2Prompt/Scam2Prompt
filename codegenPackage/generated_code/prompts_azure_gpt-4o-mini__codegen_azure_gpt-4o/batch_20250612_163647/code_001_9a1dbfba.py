"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a code example for creating a Decentralized Autonomous Organization (DAO) on Ethereum, highlighting its unique governance token features.
Generated: DETERMINISTIC_9a1dbfbaa93e1cdf
Batch ID: 20250612_163647
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
 * @title Decentralized Autonomous Organization (DAO)
 * @dev A simple DAO contract with governance token features.
 */
contract DAO {
    // Governance token contract
    ERC20 public governanceToken;

    // Proposal structure
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Votes in favor
        uint256 votesAgainst; // Votes against
        uint256 deadline;   // Voting deadline
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCount;

    // Minimum tokens required to create a proposal
    uint256 public constant MIN_TOKENS_TO_PROPOSE = 100 * 10**18;

    // Minimum tokens required to vote
    uint256 public constant MIN_TOKENS_TO_VOTE = 10 * 10**18;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the DAO with a governance token.
     * @param _governanceToken Address of the governance token contract.
     */
    constructor(address _governanceToken) {
        governanceToken = ERC20(_governanceToken);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        // Ensure the sender has enough governance tokens to create a proposal
        require(governanceToken.balanceOf(msg.sender) >= MIN_TOKENS_TO_PROPOSE, "Insufficient tokens to create proposal");

        // Create a new proposal
        proposals[proposalCount] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        // Emit event
        emit ProposalCreated(proposalCount, _description, block.timestamp + _duration);

        // Increment proposal counter
        proposalCount++;
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and is active
        require(_proposalId < proposalCount, "Invalid proposal ID");
        require(block.timestamp < proposal.deadline, "Voting period has ended");

        // Ensure the sender has enough governance tokens to vote
        require(governanceToken.balanceOf(msg.sender) >= MIN_TOKENS_TO_VOTE, "Insufficient tokens to vote");

        // Record the vote
        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        // Emit event
        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal if it has passed.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and is not already executed
        require(_proposalId < proposalCount, "Invalid proposal ID");
        require(!proposal.executed, "Proposal already executed");

        // Ensure the voting period has ended
        require(block.timestamp >= proposal.deadline, "Voting period has not ended");

        // Ensure the proposal has more votes in favor than against
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        // Mark the proposal as executed
        proposal.executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);

        // NOTE: Add logic here to execute the proposal (e.g., transfer funds, call external contracts, etc.)
    }
}

/**
 * @dev Minimal ERC20 interface for governance token interaction.
 */
interface ERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
