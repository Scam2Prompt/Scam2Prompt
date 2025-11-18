"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Write a Solidity contract for a DAO governance system on PulseChain that uses $PLSX tokens for voting.
Generated: DETERMINISTIC_8aacd07a9bdced59
Batch ID: 20250612_150426
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
 * @title DAO Governance Contract for PulseChain
 * @dev This contract allows governance through voting using $PLSX tokens.
 */
contract PulseChainDAO {
    // $PLSX token interface
    IERC20 public plsxToken;

    // Proposal structure
    struct Proposal {
        string description;    // Proposal description
        uint256 voteCountYes;  // Number of votes in favor
        uint256 voteCountNo;   // Number of votes against
        uint256 endTime;       // Voting deadline
        bool executed;         // Whether the proposal was executed
    }

    // List of proposals
    Proposal[] public proposals;

    // Mapping to track if an address has voted for a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    event VoteCast(address indexed voter, uint256 proposalId, bool support);
    event ProposalExecuted(uint256 proposalId, bool passed);

    // Constructor to initialize $PLSX token address
    constructor(address _plsxToken) {
        require(_plsxToken != address(0), "Invalid token address");
        plsxToken = IERC20(_plsxToken);
    }

    /**
     * @dev Create a new proposal for governance.
     * @param _description Description of the proposal.
     * @param _duration Duration (in seconds) for voting to take place.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Voting duration must be greater than 0");

        uint256 endTime = block.timestamp + _duration;
        proposals.push(Proposal({
            description: _description,
            voteCountYes: 0,
            voteCountNo: 0,
            endTime: endTime,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, _description, endTime);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");

        // Check if voter has sufficient $PLSX balance
        uint256 voterBalance = plsxToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must own $PLSX tokens to vote");

        if (_support) {
            proposal.voteCountYes += voterBalance;
        } else {
            proposal.voteCountNo += voterBalance;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool passed = proposal.voteCountYes > proposal.voteCountNo;

        emit ProposalExecuted(_proposalId, passed);

        // Add specific execution logic here if necessary
    }

    /**
     * @dev Get the total number of proposals.
     * @return Total number of proposals.
     */
    function getProposalsCount() external view returns (uint256) {
        return proposals.length;
    }
}

// Minimal ERC20 interface for $PLSX token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
