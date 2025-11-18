"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth2-0.pages.dev
Prompt: Write a Solidity smart contract to implement a decentralized voting system for ETH2.0 token holders to decide on future missions or roadmap milestones.
Generated: DETERMINISTIC_933a14863c323e8e
Batch ID: 20250612_153517
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

/**
 * @title Decentralized Voting System
 * @dev This contract allows ETH2.0 token holders to vote on future missions or roadmap milestones.
 */
contract VotingSystem is Ownable {
    IERC20 public token; // The ERC20 token (ETH2.0 token)
    
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        bool exists;        // Flag to check if the proposal exists
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(address => mapping(uint256 => bool)) public voters; // Track if an address has voted for a proposal
    uint256 public proposalCount; // Total count of proposals

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(address indexed voter, uint256 proposalId);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress The address of the ERC20 token.
     */
    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            exists: true
        });
        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        // Check if the proposal exists
        require(proposals[_proposalId].exists, "Proposal does not exist");
        // Check if the voter has already voted on this proposal
        require(!voters[msg.sender][_proposalId], "You have already voted on this proposal");
        
        // Transfer 1 token from the voter to the contract for voting
        require(token.transferFrom(msg.sender, address(this), 1), "Token transfer failed");

        // Record the vote
        voters[msg.sender][_proposalId] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(msg.sender, _proposalId);
    }

    /**
     * @dev Function to get the details of a specific proposal.
     * @param _proposalId The ID of the proposal to fetch.
     * @return The description and vote count of the proposal.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return (proposals[_proposalId].description, proposals[_proposalId].voteCount);
    }
}
```
