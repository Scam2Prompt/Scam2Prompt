"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: Write a Solidity-based governance proposal submission system for stakeflarre, allowing FLR token holders to vote on active proposals using the stakeflarre Portal.
Generated: DETERMINISTIC_34299311f2f92b92
Batch ID: 20250612_155037
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

contract StakeFlareGovernance is Ownable {
    // Structure to hold proposal information
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for this proposal
        uint256 endTime;    // End time for voting
        mapping(address => bool) voters; // Track if an address has voted
        bool active;        // Is the proposal active
    }

    IERC20 public flrToken; // Reference to FLR token contract
    Proposal[] public proposals; // Array of proposals

    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if the proposal is active
    modifier onlyActiveProposal(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(proposals[proposalId].active, "Proposal is not active");
        require(block.timestamp < proposals[proposalId].endTime, "Voting has ended");
        _;
    }

    // Constructor to initialize the contract with the FLR token address
    constructor(address _flrTokenAddress) {
        require(_flrTokenAddress != address(0), "Invalid token address");
        flrToken = IERC20(_flrTokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be greater than zero");
        uint256 endTime = block.timestamp + duration;

        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.endTime = endTime;
        newProposal.active = true;

        emit ProposalCreated(proposals.length - 1, description, endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external onlyActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer FLR tokens to vote (1 token = 1 vote)
        require(flrToken.transferFrom(msg.sender, address(this), 1), "Token transfer failed");

        // Update voting status and count
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to finalize a proposal after voting ends
    function finalizeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(block.timestamp >= proposals[proposalId].endTime, "Voting is still active");

        proposals[proposalId].active = false;
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(flrToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        flrToken.transfer(msg.sender, amount);
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
