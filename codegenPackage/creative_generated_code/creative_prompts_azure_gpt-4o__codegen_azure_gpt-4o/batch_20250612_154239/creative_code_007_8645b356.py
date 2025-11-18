"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Provide an example of a smart contract that implements a decentralized voting system for $FLOCK token holders, ensuring rewards are distributed based on participation.
Generated: DETERMINISTIC_8645b35674b4221a
Batch ID: 20250612_154239
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
 * @title Decentralized Voting System for $FLOCK Token Holders
 * @dev Implements a voting system where $FLOCK token holders can vote on proposals
 *      and receive rewards based on their participation.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract FlockVoting {
    IERC20 public flockToken; // $FLOCK Token contract instance
    address public owner;     // Contract owner
    uint256 public totalProposals; // Total number of proposals

    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals; // Proposal storage
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter, bool voteFor);
    event ProposalExecuted(uint256 id, bool passed);
    event RewardDistributed(address voter, uint256 rewardAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "Invalid proposal ID");
        _;
    }

    constructor(address _flockToken) {
        owner = msg.sender;
        flockToken = IERC20(_flockToken);
    }

    /**
     * @dev Creates a new proposal for voting.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        totalProposals++;
        proposals[totalProposals] = Proposal({
            id: totalProposals,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(totalProposals, description);
    }

    /**
     * @dev Allows $FLOCK token holders to vote on a proposal.
     * @param proposalId The ID of the proposal.
     * @param voteFor True to vote in favor, False to vote against.
     */
    function vote(uint256 proposalId, bool voteFor) external validProposal(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");
        require(flockToken.balanceOf(msg.sender) > 0, "You must hold $FLOCK tokens to vote");

        Proposal storage proposal = proposals[proposalId];

        if (voteFor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, voteFor);

        // Distribute reward for voting
        uint256 rewardAmount = 10 * 10**18; // Example reward of 10 tokens
        if (flockToken.transfer(msg.sender, rewardAmount)) {
            emit RewardDistributed(msg.sender, rewardAmount);
        }
    }

    /**
     * @dev Executes a proposal and marks it as completed.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool passed = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(proposalId, passed);
    }
}
```
