"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a smart contract code in Solidity to facilitate Ethereum governance token evolution, specifically for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_ee37388f331fd019
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GovernanceToken is an ERC20 token that allows for governance in a DeFi application
contract GovernanceToken is ERC20, Ownable {
    // Mapping to track the voting power of each address
    mapping(address => uint256) public votingPower;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    
    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 proposalId, bool support);

    // Struct to represent a proposal
    struct Proposal {
        string description;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        uint256 endTime;
        bool executed;
    }

    // Array to store proposals
    Proposal[] public proposals;

    // Modifier to check if the proposal is still active
    modifier onlyActiveProposal(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(block.timestamp < proposals[proposalId].endTime, "Proposal voting has ended");
        _;
    }

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("GovernanceToken", "GT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 endTime = block.timestamp + duration;
        proposals.push(Proposal({
            description: description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            endTime: endTime,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to cast a vote on a proposal
    function vote(uint256 proposalId, bool support) external onlyActiveProposal(proposalId) {
        require(votingPower[msg.sender] > 0, "No voting power");

        if (support) {
            proposals[proposalId].voteCountFor += votingPower[msg.sender];
        } else {
            proposals[proposalId].voteCountAgainst += votingPower[msg.sender];
        }

        emit VoteCast(msg.sender, proposalId, support);
    }

    // Function to execute a proposal if it has passed
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(block.timestamp >= proposals[proposalId].endTime, "Proposal voting is still active");
        require(!proposals[proposalId].executed, "Proposal already executed");

        // Check if the proposal has enough votes to pass
        if (proposals[proposalId].voteCountFor > proposals[proposalId].voteCountAgainst) {
            // Logic for executing the proposal can be added here
        }

        proposals[proposalId].executed = true;
    }

    // Function to update voting power for an address
    function updateVotingPower(address account, uint256 power) external onlyOwner {
        votingPower[account] = power;
    }
}
```
