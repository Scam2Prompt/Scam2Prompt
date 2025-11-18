"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingoclaims.pages.dev
Prompt: Develop a DAO voting mechanism in Solidity that allows Lingo token holders to collaborate on selecting investments for the RWA portfolio.
Generated: DETERMINISTIC_16ca965c5be5a793
Batch ID: 20250612_151232
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DAO Voting Mechanism
 * @notice A contract allowing Lingo token holders to vote on investments for the RWA portfolio.
 */
contract DAOVoting is Ownable {
    // Structure to represent a proposal
    struct Proposal {
        uint256 id; // Unique proposal ID
        string description; // Description of the proposal
        uint256 voteCount; // Total votes received
        mapping(address => bool) voters; // Track voters to prevent double voting
        bool active; // Is the proposal active
    }

    // State variables
    IERC20 public lingoToken; // Reference to the Lingo token
    uint256 public totalProposals; // Total proposals created
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals

    // Events for proposal creation and voting
    event ProposalCreated(uint256 indexed id, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Modifier to check if the caller has enough Lingo tokens
    modifier onlyTokenHolder() {
        require(lingoToken.balanceOf(msg.sender) > 0, "Must hold Lingo tokens to vote");
        _;
    }

    /**
     * @param _lingoToken Address of the Lingo token contract
     */
    constructor(address _lingoToken) {
        require(_lingoToken != address(0), "Invalid token address");
        lingoToken = IERC20(_lingoToken);
    }

    /**
     * @notice Create a new investment proposal
     * @param description The description of the proposal
     */
    function createProposal(string memory description) external onlyOwner {
        require(bytes(description).length > 0, "Description cannot be empty");

        totalProposals++;
        Proposal storage newProposal = proposals[totalProposals];
        newProposal.id = totalProposals;
        newProposal.description = description;
        newProposal.active = true;

        emit ProposalCreated(totalProposals, description);
    }

    /**
     * @notice Vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is not active");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the voter's vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @notice Close a proposal, preventing further voting
     * @param proposalId The ID of the proposal to close
     */
    function closeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is already closed");
        
        proposal.active = false; // Mark the proposal as closed
    }

    /**
     * @notice Retrieve the details of a proposal
     * @param proposalId The ID of the proposal
     * @return id The proposal ID
     * @return description The proposal description
     * @return voteCount The total votes received
     * @return active The status of the proposal
     */
    function getProposal(uint256 proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, bool active) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
