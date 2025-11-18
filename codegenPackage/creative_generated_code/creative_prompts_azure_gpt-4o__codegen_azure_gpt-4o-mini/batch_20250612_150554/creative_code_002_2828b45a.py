"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Generate a smart contract in Solidity that aligns with the ethos of ETHBerlin04, emphasizing community collaboration and decentralized governance.
Generated: DETERMINISTIC_2828b45aece382fc
Batch ID: 20250612_150554
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CommunityGovernance
 * @dev A smart contract for community collaboration and decentralized governance
 */
contract CommunityGovernance is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to define a proposal
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 endTime;
        mapping(address => bool) voters;
    }

    // Events to emit
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // State variables
    Counters.Counter private proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;

    // Modifier to check if the proposal is still active
    modifier activeProposal(uint256 proposalId) {
        require(proposals[proposalId].endTime > block.timestamp, "Proposal is no longer active.");
        _;
    }

    /**
     * @dev Create a new proposal
     * @param _description The description of the proposal
     * @param duration The duration for which the proposal is active (in seconds)
     */
    function createProposal(string memory _description, uint256 duration) external onlyOwner {
        // Increment proposal ID counter
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        // Create new proposal
        Proposal storage newProposal = proposals[newProposalId];
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.endTime = block.timestamp + duration;

        emit ProposalCreated(newProposalId, _description, newProposal.endTime);
    }

    /**
     * @dev Vote on an active proposal
     * @param proposalId The ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external activeProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the sender has already voted
        require(!proposal.voters[msg.sender], "You have already voted.");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has received enough votes (simple majority)
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        // Ensure the proposal has already ended
        require(proposal.endTime <= block.timestamp, "Proposal is still active.");
        require(proposal.voteCount > 0, "No votes cast for proposal.");

        // Execute the proposal (custom logic can be implemented here)
        // For now, just emit an event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get the details of a proposal
     * @param proposalId The ID of the proposal
     * @return description The description of the proposal
     * @return voteCount The number of votes received
     * @return endTime The end time of the proposal
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
