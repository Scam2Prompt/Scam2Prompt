"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Provide an example of a decentralized governance model for the HEHE ecosystem, including voting mechanisms for $HEHE token holders.
Generated: DETERMINISTIC_9e1114f86c9c4853
Batch ID: 20250612_153517
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

// Import necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Governance contract for the HEHE ecosystem
contract HEHEGovernance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public token; // ERC20 token used for governance voting
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter, uint256 voteCount);

    // Modifier to check if the voting period has ended
    modifier onlyDuringVoting(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].endTime, "Voting period has ended.");
        _;
    }

    // Constructor to initialize the contract with the token address
    constructor(address tokenAddress) {
        token = IERC20(tokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.endTime = block.timestamp + duration;

        emit ProposalCreated(newProposal.id, description, newProposal.endTime);
    }

    // Function for $HEHE token holders to vote on a proposal
    function vote(uint256 proposalId, uint256 voteAmount) external onlyDuringVoting(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted on this proposal.");
        
        // Transfer tokens from the voter to the contract
        require(token.transferFrom(msg.sender, address(this), voteAmount), "Token transfer failed.");

        // Update the proposal's vote count and mark the voter
        proposal.voteCount += voteAmount;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender, voteAmount);
    }

    // Function to retrieve the vote count of a proposal
    function getVoteCount(uint256 proposalId) external view returns (uint256) {
        return proposals[proposalId].voteCount;
    }

    // Function to withdraw tokens after end of voting period (only owner)
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw.");
        require(token.transfer(msg.sender, balance), "Token withdrawal failed.");
    }
}
```
