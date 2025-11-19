"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a code example for creating a Decentralized Autonomous Organization (DAO) on Ethereum, highlighting its unique governance token features.
Generated: DETERMINISTIC_9a1dbfbaa93e1cdf
Batch ID: 20250612_163647
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DAO contract that includes governance token features
contract GovernanceToken is ERC20, Ownable {
    // Mapping to track the voting power of each address
    mapping(address => uint256) public votingPower;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    
    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Struct to represent a proposal
    struct Proposal {
        string description;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        bool executed;
    }

    // Array to store proposals
    Proposal[] public proposals;

    // Constructor to initialize the token
    constructor() ERC20("GovernanceToken", "GT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    // Function to cast a vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(!proposals[proposalId].executed, "Proposal already executed");

        // Update voting power based on the token balance
        uint256 power = balanceOf(msg.sender);
        require(power > 0, "No voting power");

        if (support) {
            proposals[proposalId].voteCountFor += power;
        } else {
            proposals[proposalId].voteCountAgainst += power;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(!proposals[proposalId].executed, "Proposal already executed");

        // Check if the proposal has enough votes to pass (simple majority)
        require(proposals[proposalId].voteCountFor > proposals[proposalId].voteCountAgainst, "Not enough votes in favor");

        // Mark the proposal as executed
        proposals[proposalId].executed = true;

        // Logic to execute the proposal can be added here
        // For example, transferring funds or changing contract state
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
