"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: Provide an example of a governance voting smart contract in Solidity that allows LOOKS token holders to propose and vote on platform changes, similar to LooksRare's governance model.
Generated: DETERMINISTIC_3080ed88a3a3e9c2
Batch ID: 20250612_145121
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

// Import the OpenZeppelin ERC20 contract interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Governance Voting Smart Contract
contract Governance {
    // Token used for governance
    IERC20 public immutable looksToken;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        mapping(address => bool) voted;
    }

    // Events to emit when proposals are created and votes are cast
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);

    // State variables
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;

    // Constructor to set the LOOKS token address
    constructor(address _looksToken) {
        require(_looksToken != address(0), "Invalid token address");
        looksToken = IERC20(_looksToken);
    }

    // Function to create a new proposal
    function createProposal(string calldata _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than 0");
        require(looksToken.balanceOf(msg.sender) > 0, "Only LOOKS token holders can create proposals");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0; // Initialize votes to 0
        newProposal.endTime = block.timestamp + _duration;

        emit ProposalCreated(proposalCount, _description, newProposal.endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is still open for voting
        require(proposal.id > 0 && proposal.id <= proposalCount, "Invalid proposal ID");
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voted[msg.sender], "You have already voted");

        // Record the vote
        proposal.voted[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the current proposal details
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id > 0 && proposal.id <= proposalCount, "Invalid proposal ID");

        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
