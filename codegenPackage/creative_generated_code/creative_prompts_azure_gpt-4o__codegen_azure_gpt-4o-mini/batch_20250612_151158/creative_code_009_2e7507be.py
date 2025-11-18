"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Create a blockchain-based voting system for the Bobo community to propose and decide on new meme designs or roadmap updates, leveraging the decentralized ethos described on the Bobo the Bear website.
Generated: DETERMINISTIC_2e7507be74e3189f
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin libraries for safe math and access control
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Voting contract allows community members to propose and vote on new meme designs or roadmap updates
contract BoboVoting is Ownable {
    using SafeMath for uint256;

    // Struct representing a voting proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the proposal
        uint256 voteCount; // Total votes received
        mapping(address => bool) voters; // Track who has voted
        bool active; // Active status of the proposal
    }

    // Mapping to keep track of proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Counter for proposal IDs

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 id, string description);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address indexed voter);

    // Modifier to check if a proposal is active
    modifier onlyActiveProposal(uint256 proposalId) {
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory description) public onlyOwner {
        proposalCount = proposalCount.add(1); // Increment proposal count
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.active = true; // Set as active

        emit ProposalCreated(proposalCount, description); // Emit event
    }

    // Function to vote for a proposal
    function vote(uint256 proposalId) public onlyActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(1); // Increment vote count

        emit Voted(proposalId, msg.sender); // Emit event
    }

    // Function to close a proposal
    function closeProposal(uint256 proposalId) public onlyOwner onlyActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        proposal.active = false; // Deactivate the proposal
    }

    // Function to get proposal details
    function getProposal(uint256 proposalId) public view returns (uint256, string memory, uint256, bool) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
