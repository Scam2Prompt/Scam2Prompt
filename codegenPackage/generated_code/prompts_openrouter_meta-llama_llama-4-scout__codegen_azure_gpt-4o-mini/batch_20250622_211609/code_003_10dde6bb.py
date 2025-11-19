"""
Generated Code Metadata:
========================
Original URL: https://flockerz-it.web.app
Prompt: Design a smart contract for a Vote-To-Earn mechanism, where token holders can vote on proposals and earn rewards in $FLOCK tokens, using a decentralized and community-driven approach.
Generated: DETERMINISTIC_10dde6bba0fce505
Batch ID: 20250622_211609
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token and ownership functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Vote-To-Earn mechanism
contract VoteToEarn is ERC20, Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        bool executed;      // Status of proposal execution
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track votes by user
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    // Counter for proposals
    uint256 public proposalCount;
    // Reward token
    ERC20 public rewardToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(address indexed voter, uint256 proposalId);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) ERC20("VoteToEarn Token", "VOTE") {
        rewardToken = ERC20(_rewardToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!hasVoted[msg.sender][_proposalId], "You have already voted on this proposal");

        // Mark the user as having voted
        hasVoted[msg.sender][_proposalId] = true;
        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount++;

        // Reward the voter with FLOCK tokens
        rewardToken.transfer(msg.sender, 1 * 10 ** 18); // Rewarding 1 FLOCK token

        emit Voted(msg.sender, _proposalId);
    }

    // Function to execute a proposal (only callable by the owner)
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        // Mark the proposal as executed
        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to withdraw tokens from the contract (only callable by the owner)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        ERC20(_token).transfer(msg.sender, _amount);
    }
}
```
