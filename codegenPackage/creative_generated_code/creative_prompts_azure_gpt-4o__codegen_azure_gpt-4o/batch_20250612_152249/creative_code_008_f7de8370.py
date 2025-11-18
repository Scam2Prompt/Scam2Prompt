"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytradefinance.com
Prompt: Create a Solidity-based governance contract for the SHE Protocol, allowing $SHE token holders to vote on ecosystem development proposals.
Generated: DETERMINISTIC_f7de83701afc1066
Batch ID: 20250612_152249
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
 * @title SHEProtocolGovernance
 * @dev A governance contract for the SHE Protocol that allows $SHE token holders
 * to create and vote on proposals regarding ecosystem development.
 */
contract SHEProtocolGovernance {
    // Represents a proposal in the governance system
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // A brief description of the proposal
        uint256 voteCountYes; // Number of "Yes" votes
        uint256 voteCountNo; // Number of "No" votes
        bool executed; // Whether the proposal has been executed
        uint256 deadline; // Voting deadline for the proposal
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Total number of proposals created
    uint256 public proposalCount;

    // Address of the $SHE token contract
    IERC20 public sheToken;

    // Minimum number of tokens required to create a proposal
    uint256 public minTokensToPropose;

    // Minimum number of tokens required to vote
    uint256 public minTokensToVote;

    // Events
    event ProposalCreated(uint256 id, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter, bool vote);
    event ProposalExecuted(uint256 id, bool approved);

    // Constructor
    constructor(
        address _sheTokenAddress,
        uint256 _minTokensToPropose,
        uint256 _minTokensToVote
    ) {
        require(_sheTokenAddress != address(0), "Invalid token address");
        sheToken = IERC20(_sheTokenAddress);
        minTokensToPropose = _minTokensToPropose;
        minTokensToVote = _minTokensToVote;
    }

    /**
     * @dev Creates a new proposal. Caller must hold at least `minTokensToPropose` tokens.
     * @param _description A brief description of the proposal.
     * @param _duration Duration (in seconds) for which voting on the proposal will remain open.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(sheToken.balanceOf(msg.sender) >= minTokensToPropose, "Insufficient tokens to create proposal");
        require(_duration > 0, "Invalid duration");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCountYes: 0,
            voteCountNo: 0,
            executed: false,
            deadline: block.timestamp + _duration
        });

        emit ProposalCreated(proposalCount, _description, block.timestamp + _duration);
    }

    /**
     * @dev Casts a vote on a proposal. Caller must hold at least `minTokensToVote`.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True for "Yes", False for "No".
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        require(sheToken.balanceOf(msg.sender) >= minTokensToVote, "Insufficient tokens to vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.voteCountYes++;
        } else {
            proposal.voteCountNo++;
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal after the voting deadline has passed.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool approved = proposal.voteCountYes > proposal.voteCountNo;

        emit ProposalExecuted(_proposalId, approved);

        // Logic for executing the proposal can be added here if needed
    }
}

// Minimal interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
