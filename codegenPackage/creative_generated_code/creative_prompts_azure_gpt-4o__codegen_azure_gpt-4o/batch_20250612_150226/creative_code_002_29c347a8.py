"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Generate code to integrate a voting system into a decentralized governance model for a blockchain platform like Pushd, allowing token holders to propose and vote on changes to platform features and policies.
Generated: DETERMINISTIC_29c347a88b600116
Batch ID: 20250612_150226
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
 * @title Decentralized Governance Voting System
 * @notice This contract allows token holders to propose and vote on changes to platform features and policies.
 */
contract GovernanceVoting {
    // Struct representing a proposal
    struct Proposal {
        uint256 id; // Proposal ID
        string description; // Description of the proposal
        address proposer; // Address of the proposer
        uint256 yesVotes; // Count of "Yes" votes
        uint256 noVotes; // Count of "No" votes
        uint256 deadline; // Voting deadline (timestamp)
        bool executed; // Whether the proposal has been executed
    }

    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks whether an address has voted on a proposal
    address public tokenContract; // Address of the token contract

    // Events
    event ProposalCreated(uint256 id, string description, address proposer, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool vote);
    event ProposalExecuted(uint256 id, bool success);

    modifier onlyTokenHolders() {
        require(IERC20(tokenContract).balanceOf(msg.sender) > 0, "Only token holders can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract address.
     * @param _tokenContract Address of the token contract.
     */
    constructor(address _tokenContract) {
        tokenContract = _tokenContract;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyTokenHolders {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Voting duration must be greater than zero");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            proposer: msg.sender,
            yesVotes: 0,
            noVotes: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, msg.sender, block.timestamp + _duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _vote True for "Yes", false for "No".
     */
    function vote(uint256 _proposalId, bool _vote) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        hasVoted[_proposalId][msg.sender] = true;
        if (_vote) {
            proposal.yesVotes++;
        } else {
            proposal.noVotes++;
        }

        emit Voted(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        // Determine the outcome of the vote
        bool success = proposal.yesVotes > proposal.noVotes;

        emit ProposalExecuted(_proposalId, success);

        // Note: In practice, platform changes would be implemented here based on the proposal outcome.
    }
}

/**
 * @title ERC20 Interface
 * @notice Minimal ERC20 interface used to check token balances.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
