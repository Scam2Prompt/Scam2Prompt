"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shinoberryinu.pages.dev
Prompt: Generate Solidity code for a governance voting system that aligns with Shinoberry Inu's mission of community-driven decision-making. Include functionality for token holders to vote on proposals using $SHINO tokens.
Generated: DETERMINISTIC_2ff82e99ca5cc212
Batch ID: 20250612_145711
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

// GovernanceVoting contract to enable community-driven decision-making
contract GovernanceVoting is Ownable {
    using Counters for Counters.Counter;

    // Structure to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount; // Total votes for the proposal
        uint256 endTime; // Timestamp when voting ends
        bool exists; // Check if proposal exists
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Token used for voting
    IERC20 public shinoToken;
    // Counter for proposal IDs
    Counters.Counter private _proposalIdCounter;

    // Constructor to initialize the contract with the SHINO token address
    constructor(address _shinoToken) {
        require(_shinoToken != address(0), "Invalid token address");
        shinoToken = IERC20(_shinoToken);
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        require(bytes(description).length > 0, "Proposal description required");
        require(duration > 0, "Duration must be greater than 0");

        // Increment proposal ID
        uint256 proposalId = _proposalIdCounter.current();
        _proposalIdCounter.increment();

        // Create new proposal
        proposals[proposalId] = Proposal({
            description: description,
            voteCount: 0,
            endTime: block.timestamp + duration,
            exists: true
        });

        emit ProposalCreated(proposalId, description, proposals[proposalId].endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        // Check if proposal exists and is still active
        require(proposal.exists, "Proposal does not exist");
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted");

        // Transfer $SHINO tokens from voter to contract as a voting mechanism
        uint256 tokenBalance = shinoToken.balanceOf(msg.sender);
        require(tokenBalance > 0, "Insufficient SHINO tokens to vote");

        // Mark the voter as having voted for this proposal
        hasVoted[proposalId][msg.sender] = true;

        // Increment the vote count for the proposal
        proposal.voteCount += tokenBalance;

        // Emit voted event
        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.exists, "Proposal does not exist");

        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
