"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Create a Solidity contract for decentralized governance of NFT cities in the EarthMeta metaverse, allowing users to vote on economic policies.
Generated: DETERMINISTIC_e9f4599f9a752700
Batch ID: 20250612_151219
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

// Importing OpenZeppelin's Ownable and SafeMath libraries for security and ease of use
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the ERC721 NFT standard, assuming NFT cities are ERC721 tokens
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function totalSupply() external view returns (uint256);
}

// Contract for decentralized governance of NFT cities
contract NFTCityGovernance is Ownable {
    using SafeMath for uint256;

    // Structure to define a proposal
    struct Proposal {
        string description;                     // Description of the proposal
        uint256 voteCountFor;                  // Count of votes for the proposal
        uint256 voteCountAgainst;              // Count of votes against the proposal
        mapping(address => bool) hasVoted;     // Track if an address has voted
        bool executed;                         // Status to check if proposal is executed
    }

    IERC721 public nftCityContract;           // The ERC721 contract of the NFT cities
    Proposal[] public proposals;                // Array to hold all proposals
    uint256 public votingEndTime;              // End time for voting on proposals

    // Event to emit when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    
    // Event to emit when a vote is cast
    event Voted(uint256 proposalId, address voter, bool support);
    
    // Event to emit when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Constructor to set the NFT city contract address
    constructor(address _nftCityContract) {
        nftCityContract = IERC721(_nftCityContract);
    }

    // Modifier to check if the voting period is active
    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        uint256 proposalId = proposals.length; // Get the proposal ID
        proposals.push(Proposal(description, 0, 0, false)); // Create new proposal

        emit ProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external votingActive {
        Proposal storage proposal = proposals[proposalId]; // Reference to the proposal

        // Ensure the voter is a city owner
        require(nftCityContract.ownerOf(proposalId) == msg.sender, "You do not own a voting NFT");
        require(!proposal.hasVoted[msg.sender], "You have already voted"); // Ensure they haven't voted

        // Record the vote
        proposal.hasVoted[msg.sender] = true;

        // Update vote counts based on support or opposition
        if (support) {
            proposal.voteCountFor = proposal.voteCountFor.add(1);
        } else {
            proposal.voteCountAgainst = proposal.voteCountAgainst.add(1);
        }

        emit Voted(proposalId, msg.sender, support);
    }

    // Function to end voting and execute the proposal if the conditions are met
    function endVoting(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId]; // Reference to the proposal
        require(block.timestamp >= votingEndTime, "Voting is still active"); // Ensure period is over
        require(!proposal.executed, "Proposal already executed"); // Check if already executed

        // Logic to execute the proposal based on votes
        if (proposal.voteCountFor > proposal.voteCountAgainst) {
            // Execute the proposal's actions here
            // Example: update economic policies (not implemented)
            proposal.executed = true; // Mark as executed
            emit ProposalExecuted(proposalId);
        }
    }

    // Function to set voting duration
    function setVotingDuration(uint256 duration) external onlyOwner {
        votingEndTime = block.timestamp.add(duration);
    }
}
```
