"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundaktion.org
Prompt: Develop a governance voting system for a DAO that allows ONDO token holders to shape the future of DeFi protocols like Flux Finance.
Generated: DETERMINISTIC_26aeb0069ac91fc0
Batch ID: 20250612_154842
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
 * @title DAO Governance Voting System
 * @dev This contract allows ONDO token holders to participate in governance voting.
 * Each token holder can propose and vote on various DeFi protocol decisions.
 */

contract DAOGovernance {
    // State variables
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        address proposer;
        bool executed;
        mapping(address => bool) voters;
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public proposalCount; // Total number of proposals
    address public tokenAddress; // Address of the ONDO token contract
    uint256 public votingDuration; // Duration for voting in seconds

    event ProposalCreated(uint256 id, string description, address proposer);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the caller has the ONDO tokens
    modifier onlyTokenHolders() {
        require(IERC20(tokenAddress).balanceOf(msg.sender) > 0, "You must hold ONDO tokens to vote.");
        _;
    }

    // Constructor to initialize the token address and voting duration
    constructor(address _tokenAddress, uint256 _votingDuration) {
        tokenAddress = _tokenAddress;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyTokenHolders {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.proposer = msg.sender;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, description, msg.sender);
    }

    /**
     * @dev Vote for a proposal.
     * @param proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external onlyTokenHolders {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.voters[msg.sender], "You have already voted for this proposal.");
        require(proposal.id > 0 && proposal.id <= proposalCount, "Invalid proposal ID.");

        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if enough votes are received.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id > 0 && proposal.id <= proposalCount, "Invalid proposal ID.");
        require(!proposal.executed, "Proposal has already been executed.");

        // Assuming here that a proposal is successful if it receives more than 50% of the votes
        uint256 totalVotes = IERC20(tokenAddress).totalSupply();
        require(proposal.voteCount > totalVotes / 2, "Not enough votes to execute proposal.");

        // Execute proposal logic here (e.g. fund allocation, contract changes, etc.)

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}

/**
 * @title ERC20 Interface
 * @dev Minimal interface for the ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}
```
