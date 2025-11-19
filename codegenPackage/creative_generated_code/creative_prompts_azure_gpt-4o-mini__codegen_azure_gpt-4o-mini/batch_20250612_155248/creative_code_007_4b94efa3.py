"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invest-destreams.web.app
Prompt: Generate a code snippet for a voting mechanism that allows token holders to propose changes in a decentralized streaming platform like DeeStream.
Generated: DETERMINISTIC_4b94efa38f461fb4
Batch ID: 20250612_155248
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
 * @title VotingMechanism
 * @dev A contract to manage proposals and voting for token holders in a decentralized streaming platform.
 */
contract VotingMechanism is Ownable {
    // Structure to define a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Total votes cast in favor
        uint256 endTime; // End time for voting
        mapping(address => bool) hasVoted; // Tracks if an address has voted
    }

    // State variables
    IERC20 public token; // Reference to the ERC20 token
    Proposal[] public proposals; // Array of proposals
    uint256 public proposalCount; // Counter for proposals

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token contract used for voting.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param duration Duration in seconds for how long the proposal is open for voting.
     */
    function createProposal(string memory _description, uint256 duration) external onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(duration > 0, "Duration must be greater than zero");

        proposalCount++;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.endTime = block.timestamp + duration;

        emit ProposalCreated(newProposal.id, newProposal.description, newProposal.endTime);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId - 1];
        require(!proposal.hasVoted[msg.sender], "You have already voted");
        require(block.timestamp < proposal.endTime, "Voting has ended");

        // Transfer 1 token as a vote (assumes 1 vote per token holder)
        require(token.transferFrom(msg.sender, address(this), 1), "Token transfer failed");

        proposal.voteCount++;
        proposal.hasVoted[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Get details of a proposal.
     * @param proposalId ID of the proposal.
     * @return id, description, voteCount, endTime
     */
    function getProposal(uint256 proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, uint256 endTime) {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId - 1];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.endTime);
    }

    /**
     * @dev Withdraw tokens from the contract (for the owner).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
