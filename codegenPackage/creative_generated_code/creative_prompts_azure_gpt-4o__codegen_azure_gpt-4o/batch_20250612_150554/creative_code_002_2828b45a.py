"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Generate a smart contract in Solidity that aligns with the ethos of ETHBerlin04, emphasizing community collaboration and decentralized governance.
Generated: DETERMINISTIC_2828b45aece382fc
Batch ID: 20250612_150554
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
 * @title ETHBerlin04CommunityGovernance
 * @dev A smart contract designed to emphasize community collaboration and decentralized governance.
 * Community members can propose initiatives, vote, and execute proposals based on majority quorum.
 */
contract ETHBerlin04CommunityGovernance {
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        uint256 deadline;
        bool executed;
    }

    uint256 public proposalCount; // Tracks the number of proposals
    uint256 public votingDuration = 7 days; // Voting duration for proposals
    uint256 public quorumPercentage = 50; // Minimum percentage of votes required to pass a proposal

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal details
    mapping(uint256 => mapping(address => bool)) public votes; // Tracks votes by proposal ID and voter address

    event ProposalCreated(uint256 indexed id, string description, address indexed proposer, uint256 deadline);
    event VoteCast(uint256 indexed id, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed id, bool success);

    modifier onlyValidProposal(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");
        _;
    }

    /**
     * @dev Allows a community member to create a new proposal.
     * @param description A short description of the proposal.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            proposer: msg.sender,
            voteCountFor: 0,
            voteCountAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalId, description, msg.sender, proposals[proposalId].deadline);
    }

    /**
     * @dev Allows a community member to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function voteOnProposal(uint256 proposalId, bool support)
        external
        onlyValidProposal(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.deadline, "Voting period is over");
        require(!votes[proposalId][msg.sender], "You have already voted on this proposal");

        votes[proposalId][msg.sender] = true;

        if (support) {
            proposal.voteCountFor++;
        } else {
            proposal.voteCountAgainst++;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Allows the proposer or any community member to execute a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId)
        external
        onlyValidProposal(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.deadline, "Voting period is not over");
        require(!proposal.executed, "Proposal has already been executed");

        uint256 totalVotes = proposal.voteCountFor + proposal.voteCountAgainst;
        uint256 requiredQuorum = (totalVotes * quorumPercentage) / 100;

        bool success = proposal.voteCountFor >= requiredQuorum;
        require(success, "Proposal did not reach quorum or majority support");

        proposal.executed = true;

        emit ProposalExecuted(proposalId, success);
    }
}
```
