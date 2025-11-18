"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shinoberryinu.pages.dev
Prompt: Generate Solidity code for a governance voting system that aligns with Shinoberry Inu's mission of community-driven decision-making. Include functionality for token holders to vote on proposals using $SHINO tokens.
Generated: DETERMINISTIC_2ff82e99ca5cc212
Batch ID: 20250612_145711
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
 * @title Shinoberry Inu Governance Voting System
 * @dev This contract enables $SHINO token holders to create and vote on proposals.
 * It ensures a community-driven decision-making process for governance.
 */
contract ShinoberryGovernance {
    // Event to emit when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, address creator, uint256 deadline);

    // Event to emit when a vote is cast
    event VoteCasted(address voter, uint256 proposalId, uint256 weight, bool support);

    // Event to emit when a proposal is finalized
    event ProposalFinalized(uint256 proposalId, bool passed);

    // Struct representing a proposal
    struct Proposal {
        string description; // Proposal description
        address creator;    // Address of proposal creator
        uint256 deadline;   // Voting deadline (block timestamp)
        uint256 votesFor;   // Total votes in support
        uint256 votesAgainst;  // Total votes against
        bool finalized;     // Whether the proposal is finalized
    }

    Proposal[] public proposals; // Array of all proposals
    address public tokenAddress; // ERC20 $SHINO token contract address
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Track votes per proposal

    // Modifier to ensure a function is executed only after a proposal's expiration
    modifier onlyAfterDeadline(uint256 proposalId) {
        require(block.timestamp > proposals[proposalId].deadline, "Voting is still ongoing");
        _;
    }

    // Modifier to ensure a function is executed only before a proposal's expiration
    modifier onlyBeforeDeadline(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].deadline, "Voting has ended");
        _;
    }

    // Constructor to initialize the governance contract
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Creates a new proposal for governance voting.
     * @param _description The description of the proposal.
     * @param _duration The duration (in seconds) for the voting period.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Duration must be greater than 0");

        uint256 proposalId = proposals.length;

        proposals.push(Proposal({
            description: _description,
            creator: msg.sender,
            deadline: block.timestamp + _duration,
            votesFor: 0,
            votesAgainst: 0,
            finalized: false
        }));

        emit ProposalCreated(proposalId, _description, msg.sender, block.timestamp + _duration);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support Whether the vote is in support (true) or against (false).
     */
    function vote(uint256 proposalId, bool support) external onlyBeforeDeadline(proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];
        uint256 voterBalance = IERC20(tokenAddress).balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold $SHINO tokens to vote");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        emit VoteCasted(msg.sender, proposalId, voterBalance, support);
    }

    /**
     * @dev Finalizes a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal to finalize.
     */
    function finalizeProposal(uint256 proposalId) external onlyAfterDeadline(proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.finalized, "Proposal has already been finalized");

        proposal.finalized = true;
        bool passed = proposal.votesFor > proposal.votesAgainst;

        emit ProposalFinalized(proposalId, passed);
    }

    /**
     * @dev Gets the details of a proposal.
     * @param proposalId The ID of the proposal to fetch.
     * @return description The description of the proposal.
     * @return creator The creator of the proposal.
     * @return deadline The voting deadline.
     * @return votesFor Total votes in support.
     * @return votesAgainst Total votes against.
     * @return finalized Whether the proposal is finalized.
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            string memory description,
            address creator,
            uint256 deadline,
            uint256 votesFor,
            uint256 votesAgainst,
            bool finalized
        )
    {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.description,
            proposal.creator,
            proposal.deadline,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.finalized
        );
    }
}

/**
 * @dev Minimal interface for ERC20 token interactions.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
