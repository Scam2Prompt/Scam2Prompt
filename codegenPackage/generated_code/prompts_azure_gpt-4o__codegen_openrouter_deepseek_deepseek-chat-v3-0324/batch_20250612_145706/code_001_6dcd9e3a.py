"""
Generated Code Metadata:
========================
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism using Agora's on-chain governance system, ensuring compatibility with RetroPGF principles.
Generated: DETERMINISTIC_6dcd9e3a755b2ec2
Batch ID: 20250612_145706
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
 * @title RetroPGFVoting
 * @dev A voting contract implementing Agora's on-chain governance with RetroPGF principles
 */
contract RetroPGFVoting is Ownable {
    using SafeMath for uint256;

    // Voting token interface
    IERC20 public votingToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 creationTime;
        uint256 votingEndTime;
        uint256 totalVotes;
        bool executed;
        mapping(address => uint256) votes;
    }

    // Array of all proposals
    Proposal[] public proposals;

    // Minimum voting duration (in seconds)
    uint256 public minVotingDuration;

    // Minimum proposal threshold (token amount)
    uint256 public proposalThreshold;

    // Voting quorum percentage (e.g., 20 for 20%)
    uint256 public quorumPercentage;

    // Events
    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        string description,
        uint256 votingEndTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        uint256 amount
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event VotingSettingsUpdated(
        uint256 minVotingDuration,
        uint256 proposalThreshold,
        uint256 quorumPercentage
    );

    /**
     * @dev Constructor
     * @param _votingToken Address of the voting token contract
     * @param _minVotingDuration Minimum voting duration in seconds
     * @param _proposalThreshold Minimum tokens required to create a proposal
     * @param _quorumPercentage Minimum percentage of total supply required for quorum
     */
    constructor(
        address _votingToken,
        uint256 _minVotingDuration,
        uint256 _proposalThreshold,
        uint256 _quorumPercentage
    ) {
        require(_votingToken != address(0), "Invalid token address");
        require(_minVotingDuration > 0, "Duration must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");

        votingToken = IERC20(_votingToken);
        minVotingDuration = _minVotingDuration;
        proposalThreshold = _proposalThreshold;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     * @param duration Voting duration in seconds (must be >= minVotingDuration)
     */
    function createProposal(string memory description, uint256 duration) external {
        require(
            votingToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient tokens to propose"
        );
        require(bytes(description).length > 0, "Description cannot be empty");
        require(duration >= minVotingDuration, "Duration too short");

        uint256 proposalId = proposals.length;
        uint256 votingEndTime = block.timestamp.add(duration);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.creationTime = block.timestamp;
        newProposal.votingEndTime = votingEndTime;
        newProposal.totalVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, msg.sender, description, votingEndTime);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param amount Amount of tokens to vote with
     */
    function vote(uint256 proposalId, uint256 amount) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.votingEndTime, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");
        require(amount > 0, "Vote amount must be > 0");

        uint256 balance = votingToken.balanceOf(msg.sender);
        require(balance >= amount, "Insufficient token balance");

        // Check if voter has already voted and update their vote
        if (proposal.votes[msg.sender] > 0) {
            proposal.totalVotes = proposal.totalVotes.sub(proposal.votes[msg.sender]);
        }

        proposal.votes[msg.sender] = amount;
        proposal.totalVotes = proposal.totalVotes.add(amount);

        emit VoteCast(msg.sender, proposalId, amount);
    }

    /**
     * @dev Execute a proposal if quorum is met and voting period has ended
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.votingEndTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalSupply = votingToken.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);
        require(proposal.totalVotes >= quorum, "Quorum not met");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);

        // Here you would implement the actual proposal execution logic
        // based on your specific requirements
    }

    /**
     * @dev Update voting settings (only owner)
     * @param _minVotingDuration New minimum voting duration
     * @param _proposalThreshold New proposal threshold
     * @param _quorumPercentage New quorum percentage
     */
    function updateVotingSettings(
        uint256 _minVotingDuration,
        uint256 _proposalThreshold,
        uint256 _quorumPercentage
    ) external onlyOwner {
        require(_minVotingDuration > 0, "Duration must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");

        minVotingDuration = _minVotingDuration;
        proposalThreshold = _proposalThreshold;
        quorumPercentage = _quorumPercentage;

        emit VotingSettingsUpdated(
            _minVotingDuration,
            _proposalThreshold,
            _quorumPercentage
        );
    }

    /**
     * @dev Get vote count for a specific voter on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address of the voter
     * @return Amount of votes cast by the voter
     */
    function getVotes(uint256 proposalId, address voter) external view returns (uint256) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        return proposals[proposalId].votes[voter];
    }

    /**
     * @dev Check if a proposal has reached quorum
     * @param proposalId ID of the proposal
     * @return True if quorum is met, false otherwise
     */
    function hasQuorum(uint256 proposalId) external view returns (bool) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        uint256 totalSupply = votingToken.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);
        return proposal.totalVotes >= quorum;
    }
}
```
