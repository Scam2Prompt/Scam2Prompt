"""
Generated Code Metadata:
========================
Original URL: https://lightchain.live-apps.com
Prompt: What are the steps to integrate decentralized governance features in a smart contract using Lightchain AI's framework?
Generated: DETERMINISTIC_e35ba299fcb0a884
Batch ID: 20250612_155944
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

/**
 * @title Decentralized Governance Smart Contract
 * @dev This contract integrates decentralized governance features using Lightchain AI's framework.
 *      It allows token holders to propose and vote on changes to the contract.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DecentralizedGovernance {
    // Governance proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // State variables
    address public admin; // Contract admin
    IERC20 public governanceToken; // Governance token contract
    uint256 public proposalCount; // Counter for proposals
    uint256 public votingDuration; // Duration for voting (in seconds)
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    // Events
    event ProposalCreated(uint256 id, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 id, bool success);

    /**
     * @dev Constructor to initialize the contract.
     * @param _governanceToken Address of the governance token contract.
     * @param _votingDuration Duration for voting (in seconds).
     */
    constructor(address _governanceToken, uint256 _votingDuration) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_votingDuration > 0, "Voting duration must be greater than zero");

        admin = msg.sender;
        governanceToken = IERC20(_governanceToken);
        votingDuration = _votingDuration;
    }

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyAdmin {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, proposals[proposalId].deadline);
    }

    /**
     * @dev Function to cast a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");
        require(governanceToken.balanceOf(msg.sender) > 0, "You must hold governance tokens to vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyAdmin {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(_proposalId, success);

        // Add logic to implement the proposal if successful
        // Example: if (success) { performAction(); }
    }

    /**
     * @dev Function to update the voting duration.
     * @param _newDuration New voting duration (in seconds).
     */
    function updateVotingDuration(uint256 _newDuration) external onlyAdmin {
        require(_newDuration > 0, "Voting duration must be greater than zero");
        votingDuration = _newDuration;
    }
}
```
