"""
Generated Code Metadata:
========================
Original URL: https://allocation-optimismdao.app
Prompt: Write a smart contract for a DAO that optimizes resource allocation using the Optimism protocol.
Generated: DETERMINISTIC_9d65556884c146d2
Batch ID: 20250622_205156
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// DAO contract for resource allocation using the Optimism protocol
contract ResourceAllocationDAO {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public token; // Token used for voting and resource allocation
    uint256 public totalVotes; // Total votes cast
    uint256 public proposalCount; // Number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    mapping(address => uint256) public votes; // Votes per address

    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Proposal ID
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes for the proposal
        bool executed; // Status of proposal execution
    }

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _token) {
        owner = msg.sender; // Set the contract deployer as the owner
        token = IERC20(_token); // Set the token address
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++; // Increment proposal count
        proposals[proposalCount] = Proposal(proposalCount, _description, 0, false); // Create new proposal
        emit ProposalCreated(proposalCount, _description); // Emit event
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(votes[msg.sender] == 0, "Already voted"); // Ensure the voter hasn't voted yet

        // Transfer tokens from voter to the contract as a vote
        token.transferFrom(msg.sender, address(this), 1);
        proposals[_proposalId].voteCount++; // Increment vote count for the proposal
        votes[msg.sender] = _proposalId; // Record the voter's choice

        emit Voted(_proposalId, msg.sender); // Emit event
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed"); // Ensure proposal hasn't been executed

        // Check if the proposal has enough votes (simple majority)
        require(proposal.voteCount > totalVotes / 2, "Not enough votes to execute");

        // Execute the proposal logic here (e.g., resource allocation)
        // ...

        proposal.executed = true; // Mark proposal as executed
        emit ProposalExecuted(_proposalId); // Emit event
    }

    // Function to withdraw tokens from the contract (only by owner)
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_amount <= token.balanceOf(address(this)), "Insufficient balance");
        token.transfer(_to, _amount); // Transfer tokens to the specified address
    }

    // Function to get the current vote count for a proposal
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId].voteCount; // Return the vote count
    }
}
```
