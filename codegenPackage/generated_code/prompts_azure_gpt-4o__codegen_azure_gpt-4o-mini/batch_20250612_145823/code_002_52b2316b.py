"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Create a Solidity smart contract example that integrates with MDEX's DAO governance mechanism to enable voting on community proposals using xMDX vouchers.
Generated: DETERMINISTIC_52b2316bb51ce059
Batch ID: 20250612_145823
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the MDEX governance mechanism
interface IMdexGovernance {
    function propose(string calldata description) external returns (uint256);
    function vote(uint256 proposalId, bool support) external;
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 votesFor, uint256 votesAgainst);
}

// Main contract for community proposals and voting
contract MdexVoting is Ownable {
    // State variables
    IERC20 public xMDX; // xMDX token contract
    IMdexGovernance public mdexGovernance; // MDEX governance contract

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Constructor to initialize the contract with xMDX and MDEX governance addresses
    constructor(address _xMDX, address _mdexGovernance) {
        require(_xMDX != address(0), "Invalid xMDX address");
        require(_mdexGovernance != address(0), "Invalid MDEX governance address");
        
        xMDX = IERC20(_xMDX);
        mdexGovernance = IMdexGovernance(_mdexGovernance);
    }

    // Function to create a new proposal
    function createProposal(string calldata description) external onlyOwner {
        uint256 proposalId = mdexGovernance.propose(description);
        emit ProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function voteOnProposal(uint256 proposalId, bool support) external {
        // Ensure the voter has enough xMDX tokens to vote
        require(xMDX.balanceOf(msg.sender) > 0, "Insufficient xMDX balance to vote");
        
        // Cast the vote
        mdexGovernance.vote(proposalId, support);
        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to get proposal details
    function getProposalDetails(uint256 proposalId) external view returns (string memory description, uint256 votesFor, uint256 votesAgainst) {
        return mdexGovernance.getProposal(proposalId);
    }
}
```
