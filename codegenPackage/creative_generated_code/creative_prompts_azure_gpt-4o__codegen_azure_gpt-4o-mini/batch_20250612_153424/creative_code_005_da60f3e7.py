"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterrfinance.github.io
Prompt: Develop a governance token smart contract in Solidity that includes voting rights and proposal functionalities, similar to the governance features described in Orbiter Finance.
Generated: DETERMINISTIC_da60f3e798774054
Batch ID: 20250612_153424
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// GovernanceToken contract implements an ERC20 token with governance features
contract GovernanceToken is ERC20, Ownable {
    using Counters for Counters.Counter;

    // Proposal structure to hold proposal details
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Total votes for the proposal
        mapping(address => bool) voted; // Track if an address has voted
    }

    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    uint256 public votingEndTime; // End time for the voting period
    uint256 public constant VOTING_DURATION = 1 weeks; // Duration of voting period

    // Events for logging
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the token
    constructor() ERC20("GovernanceToken", "GT") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to the deployer
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalIdCounter.increment(); // Increment proposal ID counter
        uint256 newProposalId = proposalIdCounter.current(); // Get new proposal ID

        // Create the new proposal and initialize its fields
        Proposal storage newProposal = proposals[newProposalId];
        newProposal.id = newProposalId;
        newProposal.description = _description;
        newProposal.voteCount = 0;

        votingEndTime = block.timestamp + VOTING_DURATION; // Set voting end time

        emit ProposalCreated(newProposalId, _description); // Emit event
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(block.timestamp < votingEndTime, "Voting period has ended"); // Check if voting is still open
        require(balanceOf(msg.sender) > 0, "Must hold tokens to vote"); // Ensure voter holds tokens
        Proposal storage proposal = proposals[_proposalId]; // Reference to proposal

        require(!proposal.voted[msg.sender], "You have already voted"); // Prevent double voting

        proposal.voted[msg.sender] = true; // Mark voter as having voted
        proposal.voteCount++; // Increment the proposal's vote count

        emit Voted(_proposalId, msg.sender); // Emit voting event
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount); // Return proposal details
    }

    // Function to check if the voting period is still active
    function isVotingActive() external view returns (bool) {
        return block.timestamp < votingEndTime; // Return true if voting is active
    }
}
```
