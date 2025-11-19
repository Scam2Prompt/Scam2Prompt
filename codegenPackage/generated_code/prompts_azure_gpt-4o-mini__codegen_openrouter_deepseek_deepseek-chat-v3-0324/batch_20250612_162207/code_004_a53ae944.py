"""
Generated Code Metadata:
========================
Original URL: https://chaindigital.pages.dev
Prompt: Provide an example of how to implement a DAO voting mechanism in a smart contract, inspired by the Popcorn DAO mentioned on the Chain Digital webpage.
Generated: DETERMINISTIC_a53ae944d5208b79
Batch ID: 20250612_162207
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title DAOVoting
 * @dev A smart contract for DAO voting mechanism where token holders can propose and vote on proposals
 */
contract DAOVoting is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public votingToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _members;

    uint256 public constant MIN_VOTING_DURATION = 1 days;
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 * 10**18; // 1000 tokens

    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        string description,
        uint256 voteStart,
        uint256 voteEnd
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 weight
    );
    event ProposalExecuted(uint256 indexed proposalId);

    modifier onlyMember() {
        require(_members.contains(msg.sender), "DAOVoting: caller is not a member");
        _;
    }

    /**
     * @dev Constructor
     * @param _votingToken Address of the ERC20 token used for voting
     */
    constructor(address _votingToken) {
        votingToken = IERC20(_votingToken);
    }

    /**
     * @dev Add a member to the DAO
     * @param member Address to add as member
     */
    function addMember(address member) external onlyOwner {
        _members.add(member);
    }

    /**
     * @dev Remove a member from the DAO
     * @param member Address to remove from members
     */
    function removeMember(address member) external onlyOwner {
        _members.remove(member);
    }

    /**
     * @dev Check if address is a member
     * @param member Address to check
     * @return bool True if member
     */
    function isMember(address member) external view returns (bool) {
        return _members.contains(member);
    }

    /**
     * @dev Create a new proposal
     * @param description String description of the proposal
     * @param duration Duration of voting period in seconds
     */
    function propose(string memory description, uint256 duration) external onlyMember {
        require(
            votingToken.balanceOf(msg.sender) >= MIN_PROPOSAL_THRESHOLD,
            "DAOVoting: proposer doesn't have enough tokens"
        );
        require(
            duration >= MIN_VOTING_DURATION,
            "DAOVoting: voting duration too short"
        );

        proposalCount++;
        uint256 voteStart = block.timestamp;
        uint256 voteEnd = voteStart + duration;

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.voteStart = voteStart;
        newProposal.voteEnd = voteEnd;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, msg.sender, description, voteStart, voteEnd);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes vote, false for no vote
     */
    function vote(uint256 proposalId, bool support) external onlyMember {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "DAOVoting: proposal doesn't exist");
        require(block.timestamp >= proposal.voteStart, "DAOVoting: voting not started");
        require(block.timestamp <= proposal.voteEnd, "DAOVoting: voting ended");
        require(!proposal.hasVoted[msg.sender], "DAOVoting: already voted");

        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower > 0, "DAOVoting: no voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @dev Execute a proposal if voting passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyMember {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "DAOVoting: proposal doesn't exist");
        require(block.timestamp > proposal.voteEnd, "DAOVoting: voting not ended");
        require(!proposal.executed, "DAOVoting: proposal already executed");
        require(
            proposal.forVotes > proposal.againstVotes,
            "DAOVoting: proposal didn't pass"
        );

        proposal.executed = true;

        // Here you would implement the actual proposal execution logic
        // For example: call another contract, transfer funds, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id Proposal ID
     * @return proposer Proposer address
     * @return description Proposal description
     * @return voteStart Voting start timestamp
     * @return voteEnd Voting end timestamp
     * @return forVotes Total votes for
     * @return againstVotes Total votes against
     * @return executed Execution status
     */
    function getProposal(uint256 proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 voteStart,
        uint256 voteEnd,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "DAOVoting: proposal doesn't exist");

        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.voteStart,
            proposal.voteEnd,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }
}
```
