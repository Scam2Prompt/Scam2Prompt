"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Develop a decentralized application (dApp) for community-driven governance, allowing users to vote on proposals, inspired by Meteora Crypto's governance model.
Generated: DETERMINISTIC_04f4a7088504cf21
Batch ID: 20250612_153923
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CommunityGovernance
 * @dev A smart contract for community-driven governance.
 * Users can submit proposals and vote on them.
 */
contract CommunityGovernance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 endTime;    // Voting end time
        mapping(address => bool) voters; // Track whether an address has voted
    }

    // State variables
    IERC20 public governanceToken; // Governance token used for voting
    Proposal[] public proposals; // List of proposals
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address voter);

    /**
     * @dev Constructor to initialize the governance token and voting duration.
     * @param _governanceToken The address of the governance token.
     * @param _votingDuration Duration for voting in seconds.
     */
    constructor(IERC20 _governanceToken, uint256 _votingDuration) {
        governanceToken = _governanceToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.endTime = block.timestamp + votingDuration; // Set end time for voting

        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer governance tokens from the voter to this contract as a voting fee
        require(governanceToken.transferFrom(msg.sender, address(this), 1e18), "Transfer failed");

        // Record the vote
        proposal.voteCount++;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId The ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Total votes received.
     * @return endTime Voting end time.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        return (proposal.description, proposal.voteCount, proposal.endTime);
    }

    /**
     * @dev Withdraw funds from governance.
     * Can only be called by the contract owner.
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(governanceToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        governanceToken.transfer(to, amount);
    }
}
```
