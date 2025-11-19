"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applecoin-49f.pages.dev
Prompt: Create a Solidity smart contract that incorporates the principles of community ownership and decentralization mentioned in the Silly Dragon project.
Generated: DETERMINISTIC_d51275d633038d1d
Batch ID: 20250612_155846
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
 * @title SillyDragonCommunity
 * @dev This contract establishes community ownership and decentralization principles.
 * Ownership is distributed among token holders, and decisions are made via voting mechanisms.
 */
contract SillyDragonCommunity {
    // Events
    event ProposalCreated(uint256 proposalId, string description, address proposer);
    event VoteCast(uint256 proposalId, address voter, uint256 weight, bool support);
    event ProposalExecuted(uint256 proposalId);

    // Token-related variables
    mapping(address => uint256) public tokenBalance;
    uint256 public totalSupply;

    // Governance-related variables
    struct Proposal {
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        uint256 endTime;
    }
    Proposal[] public proposals;

    // Ownership distribution variables
    mapping(address => bool) public communityMembers;
    uint256 public communityMemberCount;

    // Modifiers
    modifier onlyCommunityMember() {
        require(communityMembers[msg.sender], "Not a community member");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        _;
    }

    // Constructor
    constructor() {
        // Add contract deployer as the first community member
        communityMembers[msg.sender] = true;
        communityMemberCount = 1;
    }

    /**
     * @dev Mint tokens and distribute ownership in the community.
     * @param recipient The address to receive the tokens.
     * @param amount The number of tokens to mint.
     */
    function mintTokens(address recipient, uint256 amount) external onlyCommunityMember {
        require(amount > 0, "Amount must be greater than zero");

        tokenBalance[recipient] += amount;
        totalSupply += amount;

        // Add recipient to community members if not already
        if (!communityMembers[recipient]) {
            communityMembers[recipient] = true;
            communityMemberCount++;
        }
    }

    /**
     * @dev Create a proposal for community voting.
     * @param description A short description of the proposal.
     * @param duration The duration (in seconds) the proposal is open for voting.
     */
    function createProposal(string calldata description, uint256 duration) external onlyCommunityMember {
        require(duration > 0, "Duration must be greater than zero");

        Proposal memory newProposal = Proposal({
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            endTime: block.timestamp + duration
        });

        proposals.push(newProposal);

        emit ProposalCreated(proposals.length - 1, description, msg.sender);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True if supporting the proposal, false otherwise.
     */
    function vote(uint256 proposalId, bool support) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(tokenBalance[msg.sender] > 0, "Insufficient token balance to vote");

        uint256 votingWeight = tokenBalance[msg.sender];

        if (support) {
            proposal.votesFor += votingWeight;
        } else {
            proposal.votesAgainst += votingWeight;
        }

        emit VoteCast(proposalId, msg.sender, votingWeight, support);
    }

    /**
     * @dev Execute a proposal if it has passed.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyCommunityMember proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period is not yet over");
        require(!proposal.executed, "Proposal already executed");

        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Check if an address is a community member.
     * @param account The address to check.
     * @return True if the address is a community member, false otherwise.
     */
    function isCommunityMember(address account) external view returns (bool) {
        return communityMembers[account];
    }
}
```
