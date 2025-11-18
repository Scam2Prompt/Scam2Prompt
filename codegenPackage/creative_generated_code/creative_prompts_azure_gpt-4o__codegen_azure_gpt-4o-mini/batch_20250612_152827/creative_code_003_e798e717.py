"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poohclaim.pages.dev
Prompt: Create a Solidity smart contract that integrates with the $POOH DAO to allow holders to vote on proposals using their token balance.
Generated: DETERMINISTIC_e798e7172d1cc777
Batch ID: 20250612_152827
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
 * @title POOHDAO
 * @dev Smart contract for managing proposals and voting using $POOH tokens
 */
contract POOHDAO is Ownable {
    // Token interface
    IERC20 public poohToken;

    // Proposal structure
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        mapping(address => bool) voted; // Track if an address has voted
        bool isActive;      // Status of the proposal
    }

    // Array to hold proposals
    Proposal[] public proposals;

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Constructor to initialize the contract with the POOH token address
     * @param _poohToken Address of the $POOH token contract
     */
    constructor(address _poohToken) {
        require(_poohToken != address(0), "Invalid token address");
        poohToken = IERC20(_poohToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.isActive = true;

        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId The id of the proposal to vote on
     */
    function vote(uint256 _proposalId) external {
        // Ensure the proposal exists and is active
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is not active");
        require(!proposal.voted[msg.sender], "You have already voted");

        // Get the balance of $POOH tokens for the voter
        uint256 balance = poohToken.balanceOf(msg.sender);
        require(balance > 0, "You must hold $POOH tokens to vote");

        // Count the vote
        proposal.voteCount += balance;
        proposal.voted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Close a proposal, marking it as inactive
     * @param _proposalId The id of the proposal to close
     */
    function closeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is already inactive");
        
        proposal.isActive = false;
    }

    /**
     * @dev Get the details of a proposal
     * @param _proposalId The id of the proposal to retrieve
     * @return description The description of the proposal
     * @return voteCount The total votes received for this proposal
     * @return isActive The active status of the proposal
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, bool isActive) {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.isActive);
    }
}
```
