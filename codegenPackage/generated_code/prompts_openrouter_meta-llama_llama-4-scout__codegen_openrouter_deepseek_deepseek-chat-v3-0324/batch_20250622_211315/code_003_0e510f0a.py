"""
Generated Code Metadata:
========================
Original URL: https://88bitkan.com
Prompt: Design a tokenomics structure for a new DeFi project that incorporates equal voting power and proposal creation features, inspired by World Liberty Financial's $WLFI token.
Generated: DETERMINISTIC_0e510f0af24c9d2c
Batch ID: 20250622_211315
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title WLFIToken
 * @dev A tokenomics structure for a DeFi project with equal voting power and proposal creation features.
 * Inspired by World Liberty Financial's $WLFI token.
 */
contract WLFIToken is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 createdAt;
        bool executed;
    }

    // Voting power per token holder (1 token = 1 vote)
    uint256 public constant VOTING_POWER_PER_TOKEN = 1;

    // Minimum tokens required to create a proposal
    uint256 public minProposalThreshold;

    // List of all proposals
    Proposal[] public proposals;

    // Track which addresses have voted for which proposals
    mapping(uint256 => EnumerableSet.AddressSet) private _voters;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Constructor initializes the token with initial supply and sets the minimum proposal threshold.
     * @param initialSupply The initial token supply.
     * @param _minProposalThreshold Minimum tokens required to create a proposal.
     */
    constructor(
        uint256 initialSupply,
        uint256 _minProposalThreshold
    ) ERC20("World Liberty Financial", "WLFI") {
        _mint(msg.sender, initialSupply);
        minProposalThreshold = _minProposalThreshold;
    }

    /**
     * @dev Creates a new proposal.
     * @param description Description of the proposal.
     */
    function createProposal(string memory description) external {
        require(balanceOf(msg.sender) >= minProposalThreshold, "Insufficient tokens to create proposal");
        
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            proposer: msg.sender,
            description: description,
            voteCount: 0,
            createdAt: block.timestamp,
            executed: false
        }));

        emit ProposalCreated(proposalId, msg.sender, description);
    }

    /**
     * @dev Votes for a proposal.
     * @param proposalId ID of the proposal to vote for.
     * @param votes Number of votes to cast (must be <= sender's balance).
     */
    function vote(uint256 proposalId, uint256 votes) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[proposalId].executed, "Proposal already executed");
        require(balanceOf(msg.sender) >= votes, "Insufficient voting power");
        require(!_voters[proposalId].contains(msg.sender), "Already voted for this proposal");

        _voters[proposalId].add(msg.sender);
        proposals[proposalId].voteCount += votes;

        emit Voted(proposalId, msg.sender, votes);
    }

    /**
     * @dev Executes a proposal if it has enough votes.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[proposalId].executed, "Proposal already executed");
        
        Proposal storage proposal = proposals[proposalId];
        uint256 totalSupply = totalSupply();
        uint256 requiredVotes = totalSupply / 2; // Simple majority (50%+1)

        require(proposal.voteCount >= requiredVotes, "Insufficient votes to execute");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Updates the minimum proposal threshold.
     * @param newThreshold New minimum threshold value.
     */
    function updateProposalThreshold(uint256 newThreshold) external onlyOwner {
        minProposalThreshold = newThreshold;
    }

    /**
     * @dev Returns the list of all proposals.
     */
    function getAllProposals() external view returns (Proposal[] memory) {
        return proposals;
    }

    /**
     * @dev Returns the voters for a specific proposal.
     * @param proposalId ID of the proposal.
     */
    function getVoters(uint256 proposalId) external view returns (address[] memory) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        return _voters[proposalId].values();
    }
}
```
