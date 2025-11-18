"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turbos-coin.com
Prompt: Write a Solidity function to implement a decentralized voting system for Turbo Token holders to propose and vote on community-driven initiatives.
Generated: DETERMINISTIC_6c6b847ff028d256
Batch ID: 20250612_153854
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
 * @title TurboTokenVoting
 * @dev A decentralized voting system for Turbo Token holders to propose and vote on initiatives.
 */
contract TurboTokenVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description; // Text describing the proposal
        uint256 voteCount;  // Total votes received by the proposal
        address proposer;   // Address of the proposer
        bool exists;        // Check if the proposal exists
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted for a specific proposal
    // proposalId => voterAddress => hasVoted
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Turbo Token contract address
    IERC20 public turboToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed id, string description, address indexed proposer);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId);

    // Counter for proposal IDs
    uint256 private proposalIdCounter;

    /**
     * @dev Modifier to ensure the sender holds Turbo Tokens.
     */
    modifier onlyTokenHolder() {
        require(turboToken.balanceOf(msg.sender) > 0, "You must hold Turbo Tokens to participate.");
        _;
    }

    /**
     * @dev Constructor to set the Turbo Token contract address.
     * @param _turboToken Address of the Turbo Token contract.
     */
    constructor(address _turboToken) {
        require(_turboToken != address(0), "Invalid Turbo Token contract address.");
        turboToken = IERC20(_turboToken);
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        require(bytes(_description).length > 0, "Proposal description cannot be empty.");

        // Increment the proposal ID counter
        proposalIdCounter++;

        // Create a new proposal
        proposals[proposalIdCounter] = Proposal({
            id: proposalIdCounter,
            description: _description,
            voteCount: 0,
            proposer: msg.sender,
            exists: true
        });

        emit ProposalCreated(proposalIdCounter, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        // Ensure the proposal exists
        require(proposals[_proposalId].exists, "Proposal does not exist.");

        // Ensure the voter has not already voted on this proposal
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        // Cast the vote
        proposals[_proposalId].voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Function to get details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return id Proposal ID.
     * @return description Proposal description.
     * @return voteCount Total votes received.
     * @return proposer Address of the proposer.
     * @return exists Boolean indicating if the proposal exists.
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            string memory description,
            uint256 voteCount,
            address proposer,
            bool exists
        )
    {
        // Ensure the proposal exists
        require(proposals[_proposalId].exists, "Proposal does not exist.");

        Proposal memory proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.voteCount,
            proposal.proposer,
            proposal.exists
        );
    }
}

// Interface for the Turbo Token contract
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
