"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stekecoredao.org
Prompt: Generate a code snippet to enable decentralized voting using CoreDAO’s governance model, allowing users to cast votes based on their staked CORE tokens.
Generated: DETERMINISTIC_d621c0770297676b
Batch ID: 20250612_154651
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

// Interface for the governance contract
interface IGovernance {
    function propose(string calldata description) external returns (uint256);
    function vote(uint256 proposalId, bool support) external;
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 yesVotes, uint256 noVotes, bool executed);
}

// CoreDAO Voting Contract
contract CoreDAOVoting is Ownable, IGovernance {
    struct Proposal {
        string description;           // Description of the proposal
        uint256 yesVotes;            // Total votes in favor
        uint256 noVotes;             // Total votes against
        mapping(address => bool) voted; // Track if an address has voted
        bool executed;               // Status of proposal execution
    }

    IERC20 public coreToken;            // Reference to the CORE token
    uint256 public proposalCount;       // Number of proposals created
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constructor to set the CORE token address
    constructor(address _coreToken) {
        require(_coreToken != address(0), "Invalid token address");
        coreToken = IERC20(_coreToken);
    }

    // Create a new proposal
    function propose(string calldata description) external override onlyOwner returns (uint256) {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = description;
        emit ProposalCreated(proposalCount, description);
        return proposalCount;
    }

    // Cast a vote on a proposal
    function vote(uint256 proposalId, bool support) external override {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voted[msg.sender], "Already voted");

        // Check the user's stake in CORE tokens
        uint256 stake = coreToken.balanceOf(msg.sender);
        require(stake > 0, "Must stake CORE tokens to vote");

        // Record the vote and update the vote counts
        proposal.voted[msg.sender] = true;
        if (support) {
            proposal.yesVotes += stake;
        } else {
            proposal.noVotes += stake;
        }
        emit Voted(proposalId, msg.sender, support);
    }

    // Retrieve details of a proposal
    function getProposal(uint256 proposalId) external view override returns (string memory description, uint256 yesVotes, uint256 noVotes, bool executed) {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.yesVotes, proposal.noVotes, proposal.executed);
    }

    // Execute a proposal if passed
    function executeProposal(uint256 proposalId) external {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        // Simple threshold for proposal passing: yesVotes must be greater than noVotes
        require(proposal.yesVotes > proposal.noVotes, "Proposal not passed");

        // Execute the proposal logic (placeholder for actual execution)
        // ...

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}
```
