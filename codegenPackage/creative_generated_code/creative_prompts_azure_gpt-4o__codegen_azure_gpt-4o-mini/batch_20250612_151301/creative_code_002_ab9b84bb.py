"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofinance-claim.pages.dev
Prompt: Generate code to create a governance voting system for a DAO, using ONDO tokens as the governance token, and include functionality for community-led decision-making.
Generated: DETERMINISTIC_ab9b84bbf43b86fb
Batch ID: 20250612_151301
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// GovernanceVoting contract allows ONDO token holders to submit and vote on proposals
contract GovernanceVoting is Ownable {
    using SafeMath for uint256;

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        mapping(address => bool) voted;
        bool executed;
    }

    // State variables
    IERC20 public governanceToken; // Reference to the ONDO token contract
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal id to Proposal

    // Events
    event ProposalCreated(uint256 id, address proposer, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor
    constructor(address _governanceToken) {
        governanceToken = IERC20(_governanceToken);
    }

    // Modifier to check if the caller is a token holder
    modifier onlyTokenHolder() {
        require(governanceToken.balanceOf(msg.sender) > 0, "Must hold ONDO tokens to vote");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyTokenHolder {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, msg.sender, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        require(!proposal.voted[msg.sender], "Already voted on this proposal");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.voted[msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(governanceToken.balanceOf(msg.sender));

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it meets the criteria
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > (governanceToken.totalSupply() / 2), "Not enough votes to execute");

        proposal.executed = true;

        // Execute logic for the proposal (to be defined based on the proposal's description)
        // Example: Could interact with other contracts or perform specific changes

        emit ProposalExecuted(_proposalId);
    }

    // Function to retrieve proposal details
    function getProposal(uint256 _proposalId) external view returns (uint256, address, string memory, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.proposer, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
