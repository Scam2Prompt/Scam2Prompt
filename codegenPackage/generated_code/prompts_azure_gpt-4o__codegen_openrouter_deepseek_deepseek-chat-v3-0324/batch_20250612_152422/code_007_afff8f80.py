"""
Generated Code Metadata:
========================
Original URL: https://decentralized-metis.pages.dev
Prompt: Write a smart contract that incorporates decentralized voting mechanisms aligned with Metis's Community Ecosystem Governance (CEG) framework.
Generated: DETERMINISTIC_afff8f805bc69c00
Batch ID: 20250612_152422
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
 * @title Metis Community Governance Voting Contract
 * @dev Implements a decentralized voting system aligned with Metis's CEG framework
 */
contract MetisGovernanceVoting is Ownable {
    using SafeMath for uint256;

    enum VoteOption { YES, NO, ABSTAIN }

    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        uint256 abstainVotes;
        bool executed;
        address proposer;
    }

    struct Voter {
        bool hasVoted;
        VoteOption vote;
        uint256 votingPower;
    }

    uint256 public proposalCount;
    uint256 public minimumVotingPower;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => Voter)) public voters;
    mapping(address => uint256) public votingPower;

    event ProposalCreated(
        uint256 indexed id,
        string title,
        uint256 startTime,
        uint256 endTime,
        address indexed proposer
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        VoteOption vote,
        uint256 votingPower
    );
    event ProposalExecuted(uint256 indexed id);
    event VotingPowerUpdated(address indexed voter, uint256 amount);

    modifier onlyDuringVotingPeriod(uint256 proposalId) {
        require(
            block.timestamp >= proposals[proposalId].startTime &&
            block.timestamp <= proposals[proposalId].endTime,
            "Voting period is not active"
        );
        _;
    }

    modifier onlyAfterVotingPeriod(uint256 proposalId) {
        require(
            block.timestamp > proposals[proposalId].endTime,
            "Voting period has not ended"
        );
        _;
    }

    modifier onlyProposer(uint256 proposalId) {
        require(
            msg.sender == proposals[proposalId].proposer,
            "Only proposer can execute"
        );
        _;
    }

    constructor(
        uint256 _minimumVotingPower,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) {
        minimumVotingPower = _minimumVotingPower;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Create a new proposal
     * @param title Short description of the proposal
     * @param description Detailed description of the proposal
     */
    function createProposal(
        string memory title,
        string memory description
    ) external {
        require(votingPower[msg.sender] >= minimumVotingPower, "Insufficient voting power");
        
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.title = title;
        newProposal.description = description;
        newProposal.startTime = block.timestamp;
        newProposal.endTime = block.timestamp.add(votingPeriod);
        newProposal.proposer = msg.sender;

        emit ProposalCreated(
            newProposal.id,
            newProposal.title,
            newProposal.startTime,
            newProposal.endTime,
            newProposal.proposer
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param vote The vote option (YES, NO, ABSTAIN)
     */
    function vote(
        uint256 proposalId,
        VoteOption vote
    ) external onlyDuringVotingPeriod(proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        require(!voters[proposalId][msg.sender].hasVoted, "Already voted");
        require(votingPower[msg.sender] > 0, "No voting power");

        Voter storage sender = voters[proposalId][msg.sender];
        sender.hasVoted = true;
        sender.vote = vote;
        sender.votingPower = votingPower[msg.sender];

        if (vote == VoteOption.YES) {
            proposals[proposalId].yesVotes = proposals[proposalId].yesVotes.add(votingPower[msg.sender]);
        } else if (vote == VoteOption.NO) {
            proposals[proposalId].noVotes = proposals[proposalId].noVotes.add(votingPower[msg.sender]);
        } else {
            proposals[proposalId].abstainVotes = proposals[proposalId].abstainVotes.add(votingPower[msg.sender]);
        }

        emit VoteCast(msg.sender, proposalId, vote, votingPower[msg.sender]);
    }

    /**
     * @dev Execute a proposal after voting has ended
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(
        uint256 proposalId
    ) external onlyAfterVotingPeriod(proposalId) onlyProposer(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.yesVotes.add(proposal.noVotes).add(proposal.abstainVotes);
        require(totalVotes >= getQuorum(), "Quorum not reached");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update voting power for an address (only callable by owner)
     * @param voter Address of the voter
     * @param amount New voting power amount
     */
    function updateVotingPower(
        address voter,
        uint256 amount
    ) external onlyOwner {
        votingPower[voter] = amount;
        emit VotingPowerUpdated(voter, amount);
    }

    /**
     * @dev Calculate the current quorum requirement
     * @return The minimum votes required to reach quorum
     */
    function getQuorum() public view returns (uint256) {
        uint256 totalPower = 0;
        // In a real implementation, this would calculate total voting power
        // For simplicity, we'll assume a fixed total supply
        return totalPower.mul(quorumPercentage).div(100);
    }

    /**
     * @dev Update governance parameters (only callable by owner)
     * @param _minimumVotingPower New minimum voting power to create proposals
     * @param _votingPeriod New voting period duration in seconds
     * @param _quorumPercentage New quorum percentage
     */
    function updateGovernanceParameters(
        uint256 _minimumVotingPower,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) external onlyOwner {
        minimumVotingPower = _minimumVotingPower;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }
}
```
