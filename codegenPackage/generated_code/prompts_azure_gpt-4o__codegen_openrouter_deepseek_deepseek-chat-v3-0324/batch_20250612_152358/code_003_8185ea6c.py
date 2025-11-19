"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Create a decentralized voting system in Solidity that aligns with the governance model described for Global Miracle Coin, using the LYCAN Chain infrastructure.
Generated: DETERMINISTIC_8185ea6ca9798b5c
Batch ID: 20250612_152358
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

/**
 * @title Global Miracle Coin Voting System
 * @dev A decentralized voting system for GMC governance on LYCAN Chain
 */
contract GMCVoting is Ownable {
    // Voting token interface
    IERC20 public votingToken;

    // Struct to store proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEndTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Minimum voting duration (1 day)
    uint256 public constant MIN_VOTING_DURATION = 1 days;

    // Minimum quorum percentage (5%)
    uint256 public constant MIN_QUORUM = 5;

    // Proposals mapping
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 voteEndTime
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Constructor
     * @param _votingToken Address of the GMC token used for voting
     */
    constructor(address _votingToken) {
        require(_votingToken != address(0), "Invalid token address");
        votingToken = IERC20(_votingToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _votingDuration Duration of voting period in seconds
     */
    function createProposal(string memory _description, uint256 _votingDuration) external onlyOwner {
        require(_votingDuration >= MIN_VOTING_DURATION, "Voting duration too short");
        require(bytes(_description).length > 0, "Description cannot be empty");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteEndTime = block.timestamp + _votingDuration;

        emit ProposalCreated(proposalCount, _description, newProposal.voteEndTime);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True for yes, false for no
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp <= proposal.voteEndTime, "Voting period has ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");
        
        uint256 voterBalance = votingToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting tokens");

        proposal.hasVoted[msg.sender] = true;
        
        if (_support) {
            proposal.yesVotes += voterBalance;
        } else {
            proposal.noVotes += voterBalance;
        }

        emit VoteCast(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Execute a proposal if quorum is reached and majority votes yes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.voteEndTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalVotes = proposal.yesVotes + proposal.noVotes;
        uint256 totalSupply = votingToken.totalSupply();
        uint256 quorum = (totalVotes * 100) / totalSupply;
        
        require(quorum >= MIN_QUORUM, "Quorum not reached");
        require(proposal.yesVotes > proposal.noVotes, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Check if a voter has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address of the voter
     * @return True if the voter has voted
     */
    function hasVoted(uint256 _proposalId, address _voter) public view returns (bool) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId].hasVoted[_voter];
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return id, description, voteEndTime, yesVotes, noVotes, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteEndTime,
        uint256 yesVotes,
        uint256 noVotes,
        bool executed
    ) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.voteEndTime,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.executed
        );
    }
}
```
