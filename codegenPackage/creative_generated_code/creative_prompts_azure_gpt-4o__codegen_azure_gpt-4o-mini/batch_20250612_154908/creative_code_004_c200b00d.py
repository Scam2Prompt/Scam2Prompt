"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-blockchain-webapp.vercel.app
Prompt: Create a voting mechanism for governance proposals on the Uniswap platform using Ethereum smart contracts.
Generated: DETERMINISTIC_c200b00d793987bd
Batch ID: 20250612_154908
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

// Import OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title Governance Voting Contract
/// @notice This contract allows users to create and vote on governance proposals
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        mapping(address => bool) hasVoted;
    }

    // State variables
    IERC20 public votingToken; // Token used for voting
    Proposal[] public proposals; // Array of proposals
    uint256 public proposalCount; // Total number of proposals
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the contract with a voting token and duration
    constructor(IERC20 _votingToken, uint256 _votingDuration) {
        votingToken = _votingToken;
        votingDuration = _votingDuration;
    }

    /// @notice Create a new proposal
    /// @param _description The description of the proposal
    function createProposal(string memory _description) external {
        // Increment proposal count
        proposalCount++;
        
        // Create a new proposal
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.endTime = block.timestamp + votingDuration;

        emit ProposalCreated(newProposal.id, _description, newProposal.endTime);
    }

    /// @notice Vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    /// @param _amount The amount of tokens to vote with
    function vote(uint256 _proposalId, uint256 _amount) external {
        // Check if the proposal ID is valid
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID.");
        
        // Retrieve the proposal
        Proposal storage proposal = proposals[_proposalId - 1];

        // Check if voting period is still open
        require(block.timestamp < proposal.endTime, "Voting has ended.");

        // Check if the voter has already voted
        require(!proposal.hasVoted[msg.sender], "You have already voted.");

        // Transfer tokens from the voter to this contract
        require(votingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed.");

        // Update the proposal with the vote
        proposal.voteCount += _amount;
        proposal.hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Get the details of a proposal
    /// @param _proposalId The ID of the proposal
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The total vote count for the proposal
    /// @return endTime The end time of the voting period
    function getProposal(uint256 _proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, uint256 endTime) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId - 1];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
