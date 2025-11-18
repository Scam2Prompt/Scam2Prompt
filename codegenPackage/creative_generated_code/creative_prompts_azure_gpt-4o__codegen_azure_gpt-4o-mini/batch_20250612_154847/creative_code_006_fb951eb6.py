"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-swap.tilda.ws
Prompt: Write a Solidity function that allows users to vote on governance proposals using BONE tokens within the ShibaSwap ecosystem.
Generated: DETERMINISTIC_fb951eb6d6b258ee
Batch ID: 20250612_154847
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

// Import necessary OpenZeppelin contracts for security and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Voting contract for governance proposals using BONE tokens
contract GovernanceVoting is Ownable {
    // Structure to define a proposal
    struct Proposal {
        string description;       // Description of the proposal
        uint256 voteCount;       // Total votes received
        mapping(address => bool) hasVoted; // Track if an address has voted
    }

    // Mapping of proposal IDs to Proposal structs
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Counter for total proposals

    // Reference to the BONE token contract
    IERC20 public boneToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Constructor to initialize the BONE token contract address
    constructor(address _boneToken) {
        require(_boneToken != address(0), "Invalid BONE token address");
        boneToken = IERC20(_boneToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++; // Increment proposal count
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = _description;
        newProposal.voteCount = 0;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposals[_proposalId].hasVoted[msg.sender], "You have already voted");

        // Transfer BONE tokens from the voter to the contract as a voting fee
        require(boneToken.balanceOf(msg.sender) > 0, "Insufficient BONE tokens");
        boneToken.transferFrom(msg.sender, address(this), 1 * 10 ** 18); // Voting fee of 1 BONE token

        // Record the vote
        proposals[_proposalId].voteCount++;
        proposals[_proposalId].hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to retrieve the vote count of a proposal
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId].voteCount;
    }
}
```
