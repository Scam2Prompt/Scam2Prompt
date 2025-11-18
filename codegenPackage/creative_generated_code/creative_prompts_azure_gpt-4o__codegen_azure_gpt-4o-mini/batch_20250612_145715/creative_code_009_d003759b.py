"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Write a Solidity contract that incorporates Deadpool Inu's ethos by allowing token holders to vote on humorous community proposals, such as meme contests or pop culture collaborations.
Generated: DETERMINISTIC_d003759b651571ff
Batch ID: 20250612_145715
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

// @title Deadpool Inu Community Voting Contract
// @dev This contract allows token holders to vote on humorous community proposals.
contract DeadpoolInuVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a community proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool active;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    // Mapping to keep track of votes per address
    mapping(address => mapping(uint256 => bool)) public votes;
    
    // Counter for proposal IDs
    Counters.Counter private proposalIdCounter;
    // ERC20 token used for voting
    IERC20 public votingToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    // Event emitted when a vote is cast
    event Voted(address voter, uint256 proposalId);

    // Constructor to initialize the voting token
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    // @dev Function to create a new proposal
    // @param _description Description of the proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();
        
        proposals[newProposalId] = Proposal({
            id: newProposalId,
            description: _description,
            voteCount: 0,
            active: true
        });

        emit ProposalCreated(newProposalId, _description);
    }

    // @dev Function to vote for a proposal
    // @param _proposalId ID of the proposal to vote for
    function vote(uint256 _proposalId) external {
        // Check if the proposal exists and is active
        require(proposals[_proposalId].active, "Proposal is not active");
        require(!votes[msg.sender][_proposalId], "You have already voted for this proposal");
        
        // Ensure the voter has enough tokens to vote (1 token = 1 vote)
        require(votingToken.balanceOf(msg.sender) > 0, "You must hold tokens to vote");

        // Record the vote
        votes[msg.sender][_proposalId] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(msg.sender, _proposalId);
    }

    // @dev Function to close a proposal
    // @param _proposalId ID of the proposal to close
    function closeProposal(uint256 _proposalId) external onlyOwner {
        require(proposals[_proposalId].active, "Proposal is already closed");
        proposals[_proposalId].active = false;
    }

    // @dev Function to get details of a proposal
    // @param _proposalId ID of the proposal
    // @return id, description, voteCount, active status
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, bool) {
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
