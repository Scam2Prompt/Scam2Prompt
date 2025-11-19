"""
Generated Code Metadata:
========================
Original URL: https://www-venus.com
Prompt: Design a community-driven governance system for a DeFi project using the Venus Protocol's governance token (XVS) as a reference, ensuring transparency and user empowerment.
Generated: DETERMINISTIC_594482ced050197b
Batch ID: 20250622_212746
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

/**
 * @title Venus Governance Contract
 * @dev A community-driven governance system for DeFi projects
 */
contract VenusGovernance is Ownable {
    using SafeMath for uint256;

    // Governance token interface
    IERC20 public xvsToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Minimum voting power required to create a proposal (1% of total supply)
    uint256 public proposalThreshold;

    // Voting period in blocks (approximately 3 days)
    uint256 public votingPeriod = 172800;

    // Proposals array
    Proposal[] public proposals;

    // Events
    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor
     * @param _xvsToken Address of the XVS token contract
     */
    constructor(address _xvsToken) {
        require(_xvsToken != address(0), "Invalid token address");
        xvsToken = IERC20(_xvsToken);
        
        // Set proposal threshold to 1% of total supply
        uint256 totalSupply = xvsToken.totalSupply();
        proposalThreshold = totalSupply.div(100);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        uint256 votingPower = xvsToken.balanceOf(msg.sender);
        require(votingPower >= proposalThreshold, "Insufficient voting power");
        require(bytes(description).length > 0, "Empty description");

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(votingPeriod);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposals.length - 1;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.createTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(newProposal.id, msg.sender, description, startTime, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True if voting for, false if voting against
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 votingPower = xvsToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.voters[msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @dev Execute a proposal if it has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);

        // Here you would implement the actual proposal execution logic
        // For example: call external contracts, change parameters, etc.
    }

    /**
     * @dev Get the number of proposals
     * @return Number of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id, proposer, description, createTime, endTime, forVotes, againstVotes, executed
     */
    function getProposal(uint256 proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 createTime,
        uint256 endTime,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.createTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }

    /**
     * @dev Check if a user has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address of the voter
     * @return True if the user has voted
     */
    function hasVoted(uint256 proposalId, address voter) external view returns (bool) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        return proposals[proposalId].voters[voter];
    }

    /**
     * @dev Update voting period (only owner)
     * @param newVotingPeriod New voting period in blocks
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(newVotingPeriod > 0, "Invalid voting period");
        votingPeriod = newVotingPeriod;
    }
}
```
