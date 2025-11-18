"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Create a Solidity contract that implements governance functionality for QUBE token holders, allowing them to propose and vote on platform decisions, as described in InQubeta's governance model.
Generated: DETERMINISTIC_cbce3912a3367d3a
Batch ID: 20250612_153400
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

/// @title Governance Contract for QUBE Token Holders
/// @notice This contract allows QUBE token holders to propose and vote on platform decisions
contract QubeGovernance is Ownable {
    IERC20 public qubeToken; // Reference to the QUBE token contract

    struct Proposal {
        uint256 id; // Unique identifier for each proposal
        address proposer; // Address of the proposer
        string description; // Description of the proposal
        uint256 voteCount; // Total votes for the proposal
        uint256 endTime; // When the voting ends
        mapping(address => bool) hasVoted; // Tracks if an address has voted
    }

    Proposal[] public proposals; // Array to store all proposals
    uint256 public proposalCount; // Count of proposals created

    event ProposalCreated(uint256 id, address indexed proposer, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);

    /// @param _qubeToken Address of the QUBE token contract
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
    }

    /// @notice Create a new proposal
    /// @param _description Description of the proposal
    /// @param _duration Duration of the voting period in seconds
    function createProposal(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero");

        proposalCount++;
        uint256 endTime = block.timestamp + _duration;

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.endTime = endTime;

        emit ProposalCreated(proposalCount, msg.sender, _description, endTime);
    }

    /// @notice Cast a vote on a proposal
    /// @param _proposalId ID of the proposal to vote on
    /// @param _support True to support the proposal, false to oppose
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Ensure the voter has enough QUBE tokens to vote (min 1 token)
        require(qubeToken.balanceOf(msg.sender) > 0, "You must hold QUBE tokens to vote");

        proposal.hasVoted[msg.sender] = true;
        if (_support) {
            proposal.voteCount++;
        }

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Get proposal details
    /// @param _proposalId ID of the proposal
    /// @return details of the proposal
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId - 1];
    }

    /// @notice Get the total number of proposals
    /// @return The total number of proposals
    function totalProposals() external view returns (uint256) {
        return proposalCount;
    }
}
```
