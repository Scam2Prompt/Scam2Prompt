"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Develop a community-driven governance model for Across Protocol using decentralized decision-making mechanisms, and discuss the benefits and challenges of such an approach.
Generated: DETERMINISTIC_eb45dd7531371891
Batch ID: 20250622_211853
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AcrossProtocolGovernance
 * @dev A decentralized governance contract for Across Protocol allowing token holders to propose and vote on changes.
 */
contract AcrossProtocolGovernance is Ownable {
    using SafeMath for uint256;

    // Struct to represent a governance proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // The governance token contract
    IERC20 public governanceToken;

    // Minimum votes required to create a proposal (1% of total supply)
    uint256 public proposalThreshold;

    // Minimum duration for a proposal to be active (in seconds)
    uint256 public minimumDuration;

    // Array of all proposals
    Proposal[] public proposals;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 createTime,
        uint256 duration
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Constructor to initialize the governance contract
     * @param _governanceToken Address of the governance token contract
     */
    constructor(address _governanceToken) {
        require(
            _governanceToken != address(0),
            "Governance token address cannot be zero"
        );
        governanceToken = IERC20(_governanceToken);
        
        // Set initial thresholds
        proposalThreshold = governanceToken.totalSupply().div(100); // 1% of total supply
        minimumDuration = 3 days;
    }

    /**
     * @dev Create a new governance proposal
     * @param description Description of the proposal
     * @param duration Duration for voting period (must be >= minimumDuration)
     */
    function createProposal(string memory description, uint256 duration) external {
        require(
            governanceToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient token balance to create proposal"
        );
        require(
            duration >= minimumDuration,
            "Proposal duration too short"
        );
        require(
            bytes(description).length > 0,
            "Proposal description cannot be empty"
        );

        uint256 proposalId = proposals.length;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.createTime = block.timestamp;
        newProposal.duration = duration;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            block.timestamp,
            duration
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support True if voting in support, false if voting against
     */
    function vote(uint256 proposalId, bool support) external {
        require(
            proposalId < proposals.length,
            "Invalid proposal ID"
        );
        Proposal storage proposal = proposals[proposalId];
        require(
            block.timestamp < proposal.createTime.add(proposal.duration),
            "Voting period has ended"
        );
        require(
            !proposal.hasVoted[msg.sender],
            "Already voted on this proposal"
        );

        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(
            voterBalance > 0,
            "No governance tokens to vote with"
        );

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    /**
     * @dev Execute a proposal if it has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(
            proposalId < proposals.length,
            "Invalid proposal ID"
        );
        Proposal storage proposal = proposals[proposalId];
        require(
            block.timestamp >= proposal.createTime.add(proposal.duration),
            "Voting period has not ended"
        );
        require(
            !proposal.executed,
            "Proposal already executed"
        );
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal did not pass"
        );

        proposal.executed = true;
        emit ProposalExecuted(proposalId);

        // Here you would implement the actual proposal execution logic
        // For example: call external contracts, change protocol parameters, etc.
    }

    /**
     * @dev Update the proposal threshold (only callable by owner)
     * @param newThreshold New proposal threshold value
     */
    function setProposalThreshold(uint256 newThreshold) external onlyOwner {
        require(
            newThreshold <= governanceToken.totalSupply(),
            "Threshold cannot exceed total supply"
        );
        proposalThreshold = newThreshold;
    }

    /**
     * @dev Update the minimum proposal duration (only callable by owner)
     * @param newDuration New minimum duration in seconds
     */
    function setMinimumDuration(uint256 newDuration) external onlyOwner {
        require(
            newDuration >= 1 days,
            "Duration too short"
        );
        minimumDuration = newDuration;
    }

    /**
     * @dev Get the total number of proposals
     * @return uint256 Count of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id, proposer, description, createTime, duration, forVotes, againstVotes, executed
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            string memory description,
            uint256 createTime,
            uint256 duration,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed
        )
    {
        require(
            proposalId < proposals.length,
            "Invalid proposal ID"
        );
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.createTime,
            proposal.duration,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }
}
```
