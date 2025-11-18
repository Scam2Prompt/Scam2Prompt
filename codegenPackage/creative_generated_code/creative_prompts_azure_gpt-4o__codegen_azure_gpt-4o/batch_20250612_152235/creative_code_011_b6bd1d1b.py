"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Develop a voting system in Solidity for the Puff Puff Pandas DAO that allows holders to propose and vote on community initiatives using $PUFFS tokens.
Generated: DETERMINISTIC_b6bd1d1b43d613c0
Batch ID: 20250612_152235
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
 * @title PuffPuffPandasDAO Voting System
 * @notice This contract allows holders of $PUFFS tokens to propose and vote on community initiatives.
 */
contract PuffPuffPandasDAO {
    // State variables
    address public owner; // Address of the contract owner
    IERC20 public puffsToken; // ERC20 token used for voting ($PUFFS)

    uint256 public proposalCount; // Counter for proposals

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteDeadline; // Timestamp when voting ends
        uint256 votesFor; // Total votes in favor
        uint256 votesAgainst; // Total votes against
        bool executed; // Whether the proposal has been executed
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a specific proposal

    // Events
    event NewProposal(uint256 indexed proposalId, string description, uint256 voteDeadline);
    event Voted(uint256 indexed proposalId, address indexed voter, bool voteFor, uint256 weight);
    event ProposalExecuted(uint256 indexed proposalId, bool successful);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Only owner can perform this action");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "Invalid proposal ID");
        _;
    }

    // Constructor
    constructor(address _puffsToken) {
        require(_puffsToken != address(0), "Invalid token address");
        owner = msg.sender;
        puffsToken = IERC20(_puffsToken);
    }

    /**
     * @notice Create a new proposal.
     * @param description Description of the proposal.
     * @param votingDuration Duration of the voting period in seconds.
     */
    function createProposal(string memory description, uint256 votingDuration) external onlyOwner {
        require(bytes(description).length > 0, "Description cannot be empty");
        require(votingDuration > 0, "Voting duration must be greater than zero");

        uint256 proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteDeadline: block.timestamp + votingDuration,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit NewProposal(proposalId, description, block.timestamp + votingDuration);
    }

    /**
     * @notice Cast a vote on a proposal.
     * @param proposalId The ID of the proposal.
     * @param voteFor True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool voteFor) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp <= proposal.voteDeadline, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 voterBalance = puffsToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No $PUFFS tokens to vote with");

        hasVoted[proposalId][msg.sender] = true;

        if (voteFor) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        emit Voted(proposalId, msg.sender, voteFor, voterBalance);
    }

    /**
     * @notice Execute a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.voteDeadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool successful = proposal.votesFor > proposal.votesAgainst; // A proposal passes if votesFor > votesAgainst

        emit ProposalExecuted(proposalId, successful);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
