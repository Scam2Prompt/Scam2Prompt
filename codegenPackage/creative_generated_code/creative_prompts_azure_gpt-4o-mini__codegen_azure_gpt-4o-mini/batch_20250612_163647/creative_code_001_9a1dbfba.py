"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Generate a code example for creating a Decentralized Autonomous Organization (DAO) on Ethereum, highlighting its unique governance token features.
Generated: DETERMINISTIC_9a1dbfbaa93e1cdf
Batch ID: 20250612_163647
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

// Importing OpenZeppelin contracts for ERC20 token and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// DAO contract to manage governance through a unique token
contract DAOToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Variables to hold the minimum voting period and quorum
    uint256 public minVotingPeriod;
    uint256 public quorumPercentage;

    // Structure to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votingEnds;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Mapping to track proposals by ID
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Mapping to track votes of each address
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);

    // Constructor to initialize the token properties
    constructor(uint256 initialSupply, uint256 _minVotingPeriod, uint256 _quorumPercentage)
        ERC20("DAO Governance Token", "DGT")
    {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
        minVotingPeriod = _minVotingPeriod;
        quorumPercentage = _quorumPercentage;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            votingEnds: block.timestamp.add(minVotingPeriod),
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        // Validate that the proposal exists
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        // Ensure the voting period has not ended
        require(block.timestamp < proposals[proposalId].votingEnds, "Voting has ended");
        // Prevent double voting
        require(!hasVoted[proposalId][msg.sender], "Already voted on this proposal");

        // Register the vote
        hasVoted[proposalId][msg.sender] = true;
        if (support) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }
        
        emit Voted(proposalId, msg.sender, support);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 proposalId) external {
        // Validate that the proposal exists
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        // Ensure the voting period has ended
        require(block.timestamp >= proposals[proposalId].votingEnds, "Voting still active");
        // Ensure the proposal has not been executed yet
        require(!proposals[proposalId].executed, "Proposal already executed");

        // Ensure quorum is met
        uint256 totalVotes = proposals[proposalId].votesFor.add(proposals[proposalId].votesAgainst);
        uint256 quorum = totalSupply().mul(quorumPercentage).div(100);
        require(totalVotes >= quorum, "Quorum not met");

        // Execute proposal logic (Placeholder for actual actions)
        proposals[proposalId].executed = true;
        // Emit event for execution (if any actions are performed)
    }
}
```
