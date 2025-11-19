"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Illustrate how to implement a voting mechanism for token holders in the Pushd decentralized governance system using Solidity.
Generated: DETERMINISTIC_b0099c2517e784cf
Batch ID: 20250612_163659
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
 * @title PushdTokenGovernance
 * @dev A contract for decentralized governance voting by token holders in the Pushd system.
 */
contract PushdTokenGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 voteCountFor; // Number of votes in favor
        uint256 voteCountAgainst; // Number of votes against
        uint256 creationTime; // Timestamp of proposal creation
        bool executed; // Whether the proposal has been executed
    }

    // Mapping from proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping from proposal ID to voter address to prevent double voting
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Address of the token contract (ERC20 compatible)
    address public tokenContract;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 id,
        string description,
        uint256 creationTime
    );

    // Event emitted when a vote is cast
    event VoteCast(
        uint256 proposalId,
        address voter,
        bool voteFor
    );

    // Event emitted when a proposal is executed
    event ProposalExecuted(
        uint256 proposalId,
        bool passed
    );

    /**
     * @dev Constructor to initialize the governance contract.
     * @param _tokenContract Address of the token contract used for voting.
     */
    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string calldata _description) external {
        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            creationTime: block.timestamp,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _description, block.timestamp);
    }

    /**
     * @dev Casts a vote for or against a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _voteFor True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _voteFor) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        // Check token balance of the voter
        uint256 voterBalance = IERC20(tokenContract).balanceOf(msg.sender);
        require(voterBalance > 0, "Insufficient token balance to vote");

        // Register the vote
        if (_voteFor) {
            proposal.voteCountFor += voterBalance;
        } else {
            proposal.voteCountAgainst += voterBalance;
        }

        hasVoted[_proposalId][msg.sender] = true;
        emit VoteCast(_proposalId, msg.sender, _voteFor);
    }

    /**
     * @dev Executes a proposal to determine its outcome.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");

        // Determine the outcome
        bool passed = proposal.voteCountFor > proposal.voteCountAgainst;
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, passed);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
