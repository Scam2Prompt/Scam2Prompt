"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.web.app
Prompt: Explain how to implement a governance voting system for $QUBE token holders using smart contracts.
Generated: DETERMINISTIC_641c474d0bd9aa79
Batch ID: 20250612_140418
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

/**
 * @title GovernanceVoting
 * @dev A smart contract for $QUBE token holders to vote on proposals.
 */
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Proposal description
        uint256 voteCount;  // Total votes for this proposal
        bool executed;      // Whether the proposal has been executed
    }

    // Array to store all proposals
    Proposal[] public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Address of the $QUBE token contract
    address public qubeToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to $QUBE token holders
    modifier onlyTokenHolder() {
        require(IERC20(qubeToken).balanceOf(msg.sender) > 0, "Not a $QUBE token holder");
        _;
    }

    /**
     * @dev Contract constructor.
     * @param _qubeToken Address of the $QUBE token contract.
     */
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = _qubeToken;
    }

    /**
     * @dev Create a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        proposals.push(Proposal({description: _description, voteCount: 0, executed: false}));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        proposals[_proposalId].voteCount += IERC20(qubeToken).balanceOf(msg.sender);
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Execute a proposal. For simplification, execution just marks the proposal as executed.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return description Description of the proposal.
     * @return voteCount Total votes for the proposal.
     * @return executed Whether the proposal has been executed.
     */
    function getProposalDetails(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, bool executed) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
