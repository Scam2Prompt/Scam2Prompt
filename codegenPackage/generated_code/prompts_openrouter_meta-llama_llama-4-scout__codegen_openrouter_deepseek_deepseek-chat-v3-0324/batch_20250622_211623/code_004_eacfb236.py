"""
Generated Code Metadata:
========================
Original URL: https://light-chain-ai.pages.dev
Prompt: "Generate a smart contract code (in Solidity or similar) that implements a simple decentralized governance system using Lightchain AI’s PoI consensus and AIVM."
Generated: DETERMINISTIC_eacfb236a6bfe208
Batch ID: 20250622_211623
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Decentralized Governance Contract
 * @dev Implements a simple governance system using Lightchain AI's PoI consensus and AIVM.
 */
contract Governance is Ownable {
    using SafeMath for uint256;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) voters;
    }

    // Voting token interface (to be replaced with actual token contract)
    interface IVotingToken {
        function balanceOf(address account) external view returns (uint256);
        function getPriorVotes(address account, uint256 blockNumber) external view returns (uint256);
    }

    IVotingToken public votingToken;
    uint256 public proposalCount;
    uint256 public minimumQuorum; // Minimum votes required for proposal to pass
    uint256 public debatingPeriodDuration; // Default debating period in blocks

    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 createTime,
        uint256 duration
    );

    event VoteCast(
        address voter,
        uint256 proposalId,
        bool support,
        uint256 votes
    );

    event ProposalExecuted(
        uint256 id,
        bool result
    );

    /**
     * @dev Constructor
     * @param _votingToken Address of the voting token contract
     * @param _minimumQuorum Minimum votes required for proposal to pass
     * @param _debatingPeriodDuration Default debating period in blocks
     */
    constructor(
        address _votingToken,
        uint256 _minimumQuorum,
        uint256 _debatingPeriodDuration
    ) {
        require(_votingToken != address(0), "Invalid token address");
        votingToken = IVotingToken(_votingToken);
        minimumQuorum = _minimumQuorum;
        debatingPeriodDuration = _debatingPeriodDuration;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     * @param duration Duration of the voting period (in blocks)
     */
    function propose(string memory description, uint256 duration) public {
        require(bytes(description).length > 0, "Empty description");
        require(duration > 0, "Duration must be positive");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.createTime = block.number;
        newProposal.duration = duration;
        newProposal.votesFor = 0;
        newProposal.votesAgainst = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            newProposal.proposer,
            newProposal.description,
            newProposal.createTime,
            newProposal.duration
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal
     */
    function vote(uint256 proposalId, bool support) public {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.number < proposal.createTime.add(proposal.duration), "Voting period ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 votes = votingToken.getPriorVotes(msg.sender, proposal.createTime);
        require(votes > 0, "No voting power");

        proposal.voters[msg.sender] = true;

        if (support) {
            proposal.votesFor = proposal.votesFor.add(votes);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(votes);
        }

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @dev Execute a proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) public {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.number >= proposal.createTime.add(proposal.duration), "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.votesFor.add(proposal.votesAgainst);
        require(totalVotes >= minimumQuorum, "Quorum not reached");

        bool result = proposal.votesFor > proposal.votesAgainst;
        proposal.executed = true;

        // Here you would implement the actual proposal execution logic
        // For demonstration, we're just emitting an event
        emit ProposalExecuted(proposalId, result);
    }

    /**
     * @dev Update minimum quorum (only callable by owner)
     * @param newQuorum New minimum quorum value
     */
    function updateMinimumQuorum(uint256 newQuorum) public onlyOwner {
        require(newQuorum > 0, "Quorum must be positive");
        minimumQuorum = newQuorum;
    }

    /**
     * @dev Update debating period duration (only callable by owner)
     * @param newDuration New debating period duration
     */
    function updateDebatingPeriodDuration(uint256 newDuration) public onlyOwner {
        require(newDuration > 0, "Duration must be positive");
        debatingPeriodDuration = newDuration;
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id, proposer, description, createTime, duration, votesFor, votesAgainst, executed
     */
    function getProposal(uint256 proposalId) public view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 createTime,
        uint256 duration,
        uint256 votesFor,
        uint256 votesAgainst,
        bool executed
    ) {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.createTime,
            proposal.duration,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.executed
        );
    }

    /**
     * @dev Check if an address has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address to check
     * @return True if the address has voted
     */
    function hasVoted(uint256 proposalId, address voter) public view returns (bool) {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        return proposals[proposalId].voters[voter];
    }
}
```
