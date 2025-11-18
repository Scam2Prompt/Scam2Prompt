"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Write a smart contract to implement a decentralized autonomous organization (DAO) structure for projects seeking funding, similar to the Merit Circle example on Fjord Foundry.
Generated: DETERMINISTIC_0cc1dc3333494340
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Decentralized Autonomous Organization (DAO) Smart Contract
 * @dev This contract allows projects to create proposals for funding, which can be voted on by token holders.
 */
contract DAO is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed creator);
    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    struct Proposal {
        string description;
        address creator;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        uint256 endTime;
        bool executed;
    }

    // Array of proposals
    Proposal[] public proposals;
    // Mapping of addresses to their voting status on proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    // Token used for voting
    IERC20 public token;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Constructor to set the token used for voting and the voting duration
    constructor(IERC20 _token, uint256 _votingDuration) {
        token = _token;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Creates a new funding proposal
     * @param _description The description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            description: _description,
            creator: msg.sender,
            voteCountFor: 0,
            voteCountAgainst: 0,
            endTime: block.timestamp + votingDuration,
            executed: false
        }));
        emit ProposalCreated(proposalId, _description, msg.sender);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     * @param support A boolean indicating if the vote is for (true) or against (false)
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "DAO: Proposal does not exist");
        require(!hasVoted[proposalId][msg.sender], "DAO: You have already voted on this proposal");
        require(block.timestamp < proposals[proposalId].endTime, "DAO: Voting has ended");

        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "DAO: You must hold tokens to vote");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposals[proposalId].voteCountFor += voterBalance;
        } else {
            proposals[proposalId].voteCountAgainst += voterBalance;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Executes the proposal if it has passed
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "DAO: Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "DAO: Voting is still ongoing");
        require(!proposal.executed, "DAO: Proposal has already been executed");

        if (proposal.voteCountFor > proposal.voteCountAgainst) {
            // Execute the proposal logic here (funding, etc.)
            // Example: transfer funds to the project (implementation omitted)
        }

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Retrieve the number of proposals
     * @return The total number of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Retrieve details of a specific proposal
     * @param proposalId The ID of the proposal to retrieve
     * @return The proposal details
     */
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        require(proposalId < proposals.length, "DAO: Proposal does not exist");
        return proposals[proposalId];
    }
}
```
