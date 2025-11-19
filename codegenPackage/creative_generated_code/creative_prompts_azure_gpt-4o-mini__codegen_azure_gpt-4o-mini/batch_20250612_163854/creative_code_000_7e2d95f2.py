"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for proposal management?
Generated: DETERMINISTIC_7e2d95f2fc2b056f
Batch ID: 20250612_163854
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

// Import interfaces for ERC20 token and governance
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Governance contract for managing proposals
contract Governance is Ownable {
    // Struct to define a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Total votes for this proposal
        mapping(address => bool) hasVoted; // Track if an address has voted
    }

    // State variables
    IERC20 public token; // ERC20 token used for voting
    Proposal[] public proposals; // List of proposals
    uint256 public proposalCount; // Count of proposals created

    // Events for logging
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the governance contract with the token
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = _description;
        
        emit ProposalCreated(newProposal.id, newProposal.description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Transfer tokens to authorize the vote
        require(token.transferFrom(msg.sender, address(this), 1), "Token transfer failed");
        
        proposal.voteCount++;
        proposal.hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        
        return (proposal.id, proposal.description, proposal.voteCount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Cannot withdraw to zero address");
        require(_amount <= token.balanceOf(address(this)), "Insufficient balance");
        
        token.transfer(_to, _amount);
    }
}
```
