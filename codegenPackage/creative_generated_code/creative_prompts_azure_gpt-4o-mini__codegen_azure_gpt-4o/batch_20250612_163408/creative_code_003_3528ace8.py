"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drift-2kl.pages.dev
Prompt: Develop a smart contract that allows users to participate in the governance of the Drift ecosystem by holding $DRIFT tokens.
Generated: DETERMINISTIC_3528ace896fc3c33
Batch ID: 20250612_163408
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
 * @title DriftGovernance
 * @dev This contract allows users holding $DRIFT tokens to participate in governance decisions
 *      for the Drift ecosystem.
 */

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract DriftGovernance {
    IERC20 public driftToken;

    // Struct representing a single proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCounter;

    // Mapping of proposal ID to voter addresses to ensure one vote per proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 deadline);

    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    /**
     * @dev Constructor to initialize the governance contract with the $DRIFT token address.
     * @param _driftToken Address of the $DRIFT token contract.
     */
    constructor(address _driftToken) {
        require(_driftToken != address(0), "Drift token address cannot be zero");
        driftToken = IERC20(_driftToken);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Duration (in seconds) for which voting will be open.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Proposal duration must be greater than zero");

        uint256 proposalId = proposalCounter++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, proposals[proposalId].deadline);
    }

    /**
     * @dev Cast a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, False to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");
        require(driftToken.balanceOf(msg.sender) > 0, "You must hold $DRIFT tokens to vote");

        // Record the vote
        hasVoted[_proposalId][msg.sender] = true;
        if (_support) {
            proposal.votesFor += driftToken.balanceOf(msg.sender);
        } else {
            proposal.votesAgainst += driftToken.balanceOf(msg.sender);
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period has not ended yet");
        require(!proposal.executed, "Proposal has already been executed");

        // Execute action based on the outcome of the vote
        proposal.executed = true;

        bool success;
        if (proposal.votesFor > proposal.votesAgainst) {
            success = true; // Placeholder for actual action execution logic
        } else {
            success = false; // Proposal rejected
        }

        emit ProposalExecuted(_proposalId, success);
    }
}
```
