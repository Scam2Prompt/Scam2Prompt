"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Write a Solidity-based DAO smart contract that aligns with Quecko's Web3 development expertise and includes governance mechanisms.
Generated: DETERMINISTIC_579a2a2e8da10530
Batch ID: 20250612_154029
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
 * @title QueckoDAO
 * @dev A decentralized autonomous organization with governance mechanisms
 */
contract QueckoDAO is Ownable {
    using SafeMath for uint256;

    // Token contract interface
    IERC20 public governanceToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Minimum voting delay in blocks
    uint256 public constant MIN_VOTING_DELAY = 1;
    // Minimum voting period in blocks
    uint256 public constant MIN_VOTING_PERIOD = 5760; // ~24 hours in blocks (assuming 15s block time)
    // Proposal threshold in tokens
    uint256 public proposalThreshold;
    // Quorum required for proposal execution
    uint256 public quorumPercentage;

    // Proposals mapping
    mapping(uint256 => Proposal) public proposals;
    // Total proposals count
    uint256 public proposalCount;

    // Events
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
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event ThresholdUpdated(uint256 newThreshold);
    event QuorumUpdated(uint256 newQuorum);

    /**
     * @dev Constructor
     * @param _token Address of the governance token
     * @param _threshold Minimum tokens required to create a proposal
     * @param _quorum Minimum percentage of votes required for quorum
     */
    constructor(
        address _token,
        uint256 _threshold,
        uint256 _quorum
    ) {
        require(_token != address(0), "Invalid token address");
        require(_quorum <= 100, "Quorum must be <= 100");

        governanceToken = IERC20(_token);
        proposalThreshold = _threshold;
        quorumPercentage = _quorum;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     * @param votingDelay Delay before voting starts in blocks
     * @param votingPeriod Duration of voting in blocks
     */
    function propose(
        string memory description,
        uint256 votingDelay,
        uint256 votingPeriod
    ) external returns (uint256) {
        require(
            governanceToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient tokens to propose"
        );
        require(
            votingDelay >= MIN_VOTING_DELAY,
            "Voting delay too low"
        );
        require(
            votingPeriod >= MIN_VOTING_PERIOD,
            "Voting period too low"
        );
        require(
            bytes(description).length > 0,
            "Empty description"
        );

        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.voteStart = block.number.add(votingDelay);
        newProposal.voteEnd = newProposal.voteStart.add(votingPeriod);
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            newProposal.voteStart,
            newProposal.voteEnd
        );

        return proposalId;
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function castVote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.number >= proposal.voteStart,
            "Voting not started"
        );
        require(
            block.number <= proposal.voteEnd,
            "Voting ended"
        );
        require(
            !proposal.voters[msg.sender],
            "Already voted"
        );

        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        proposal.voters[msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    /**
     * @dev Execute a proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.number > proposal.voteEnd,
            "Voting not ended"
        );
        require(
            !proposal.executed,
            "Already executed"
        );

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 quorum = totalVotes.mul(quorumPercentage).div(100);
        require(
            totalVotes >= quorum,
            "Quorum not reached"
        );
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal rejected"
        );

        proposal.executed = true;

        // Here you would implement the proposal execution logic
        // For example: call external contracts, transfer funds, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update proposal threshold (onlyOwner)
     * @param newThreshold New threshold value
     */
    function updateThreshold(uint256 newThreshold) external onlyOwner {
        proposalThreshold = newThreshold;
        emit ThresholdUpdated(newThreshold);
    }

    /**
     * @dev Update quorum percentage (onlyOwner)
     * @param newQuorum New quorum percentage (0-100)
     */
    function updateQuorum(uint256 newQuorum) external onlyOwner {
        require(newQuorum <= 100, "Quorum must be <= 100");
        quorumPercentage = newQuorum;
        emit QuorumUpdated(newQuorum);
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id, proposer, description, voteStart, voteEnd, forVotes, againstVotes, executed
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            string memory description,
            uint256 voteStart,
            uint256 voteEnd,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
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

    /**
     * @dev Check if an address has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address to check
     * @return True if voted, false otherwise
     */
    function hasVoted(uint256 proposalId, address voter)
        external
        view
        returns (bool)
    {
        return proposals[proposalId].voters[voter];
    }
}
```
