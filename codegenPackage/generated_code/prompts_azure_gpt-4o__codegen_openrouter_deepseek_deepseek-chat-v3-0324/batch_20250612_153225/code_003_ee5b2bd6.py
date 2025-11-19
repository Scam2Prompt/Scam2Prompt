"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.pages.dev
Prompt: Write Solidity code for a smart contract that implements the governance features of the $QUBE token, allowing token holders to propose and vote on platform changes.
Generated: DETERMINISTIC_ee5b2bd6d15f0322
Batch ID: 20250612_153225
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QubeGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public qubeToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Minimum quorum required for proposal to pass (percentage)
    uint256 public constant MIN_QUORUM = 10;
    // Minimum voting period in blocks
    uint256 public constant MIN_VOTING_PERIOD = 5760; // ~24 hours at 15s/block
    // Minimum tokens required to create a proposal
    uint256 public proposalThreshold;
    // Total supply snapshot for quorum calculations
    uint256 public totalSupplySnapshot;

    // Array of all proposals
    Proposal[] public proposals;
    // Current proposal count
    uint256 public proposalCount;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _qubeToken, uint256 _proposalThreshold) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
        proposalThreshold = _proposalThreshold;
    }

    /**
     * @notice Create a new proposal
     * @param _description Description of the proposal
     * @param _votingPeriod Duration of voting period in blocks
     */
    function propose(string memory _description, uint256 _votingPeriod) external {
        uint256 balance = qubeToken.balanceOf(msg.sender);
        require(balance >= proposalThreshold, "Insufficient tokens to propose");
        require(_votingPeriod >= MIN_VOTING_PERIOD, "Voting period too short");
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Take snapshot of total supply for quorum calculations
        totalSupplySnapshot = qubeToken.totalSupply();

        uint256 proposalId = proposalCount;
        uint256 startTime = block.number;
        uint256 endTime = startTime.add(_votingPeriod);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        proposalCount++;

        emit ProposalCreated(proposalId, msg.sender, _description, startTime, endTime);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True if voting for, false if voting against
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        require(block.number >= proposal.startTime, "Voting not started");
        require(block.number <= proposal.endTime, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 balance = qubeToken.balanceOf(msg.sender);
        require(balance > 0, "No tokens to vote");

        proposal.hasVoted[msg.sender] = true;

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(balance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(balance);
        }

        emit VoteCast(msg.sender, _proposalId, _support, balance);
    }

    /**
     * @notice Execute a proposal if it has passed
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        require(block.number > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 quorum = totalVotes.mul(100).div(totalSupplySnapshot);

        require(quorum >= MIN_QUORUM, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Update the proposal threshold
     * @param _newThreshold New threshold amount
     */
    function setProposalThreshold(uint256 _newThreshold) external onlyOwner {
        proposalThreshold = _newThreshold;
    }

    /**
     * @notice Get proposal details
     * @param _proposalId ID of the proposal
     * @return id Proposal ID
     * @return proposer Proposal creator
     * @return description Proposal description
     * @return startTime Voting start time
     * @return endTime Voting end time
     * @return forVotes Votes in favor
     * @return againstVotes Votes against
     * @return executed Execution status
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 startTime,
        uint256 endTime,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.startTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }

    /**
     * @notice Check if an address has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address of the voter
     * @return True if the address has voted
     */
    function hasVoted(uint256 _proposalId, address _voter) external view returns (bool) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        return proposals[_proposalId].hasVoted[_voter];
    }
}
```
