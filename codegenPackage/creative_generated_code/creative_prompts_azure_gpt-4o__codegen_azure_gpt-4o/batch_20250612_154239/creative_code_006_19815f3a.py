"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a Solidity implementation for decentralized governance that allows Bulldogito Coin holders to propose and vote on asset management strategies using their voting power.
Generated: DETERMINISTIC_19815f3a3d0e94e1
Batch ID: 20250612_154239
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
 * @title Bulldogito Governance Contract
 * @dev Implements a decentralized governance system for Bulldogito Coin holders.
 * Bulldogito Coin holders can propose and vote on asset management strategies.
 */
contract BulldogitoGovernance {
    // Data structure for a proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the asset management strategy
        uint256 voteCountYes; // Count of "Yes" votes
        uint256 voteCountNo; // Count of "No" votes
        uint256 deadline; // Expiration time of the proposal
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    // Mapping of proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track voting status of users for each proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Bulldogito Coin contract address (ERC20)
    IERC20 public bulldogitoCoin;

    // Minimum number of Bulldogito Coins required to create a proposal
    uint256 public proposalThreshold;

    // Duration for which a proposal is active
    uint256 public proposalDuration;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Events
    event ProposalCreated(uint256 id, string description, address proposer, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool voteYes);
    event ProposalExecuted(uint256 id, bool success);

    /**
     * @dev Constructor to initialize the contract.
     * @param _bulldogitoCoin Address of the Bulldogito Coin ERC20 contract.
     * @param _proposalThreshold Minimum number of coins required to create a proposal.
     * @param _proposalDuration Duration (in seconds) for which a proposal is active.
     */
    constructor(
        address _bulldogitoCoin,
        uint256 _proposalThreshold,
        uint256 _proposalDuration
    ) {
        bulldogitoCoin = IERC20(_bulldogitoCoin);
        proposalThreshold = _proposalThreshold;
        proposalDuration = _proposalDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the asset management strategy.
     */
    function createProposal(string memory description) external {
        require(
            bulldogitoCoin.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient Bulldogito Coin balance to create proposal"
        );

        uint256 proposalId = ++proposalCounter; // Generate a new proposal ID
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteCountYes: 0,
            voteCountNo: 0,
            deadline: block.timestamp + proposalDuration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalId, description, msg.sender, proposals[proposalId].deadline);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param voteYes True if voting "Yes", false for "No".
     */
    function vote(uint256 proposalId, bool voteYes) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");
        require(
            bulldogitoCoin.balanceOf(msg.sender) > 0,
            "You must hold Bulldogito Coin to vote"
        );

        // Record the vote
        hasVoted[proposalId][msg.sender] = true;

        if (voteYes) {
            proposal.voteCountYes += bulldogitoCoin.balanceOf(msg.sender);
        } else {
            proposal.voteCountNo += bulldogitoCoin.balanceOf(msg.sender);
        }

        emit Voted(proposalId, msg.sender, voteYes);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period is not over");
        require(!proposal.executed, "Proposal has already been executed");

        // Check if the proposal passed
        bool success = proposal.voteCountYes > proposal.voteCountNo;

        // Mark the proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(proposalId, success);

        // Additional logic for executing the proposal can be added here (e.g., interacting with other contracts).
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
