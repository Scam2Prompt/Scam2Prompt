"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: "Propose a community-driven DAO governance model for Lingo, enabling token holders to participate in decision-making processes for the RWA investment portfolio."
Generated: DETERMINISTIC_ab6271421b3d4932
Batch ID: 20250622_211405
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LingoDAO
 * @dev A decentralized autonomous organization (DAO) governance model for Lingo
 * enabling token holders to participate in decision-making for RWA investments.
 */
contract LingoDAO is Ownable {
    using SafeMath for uint256;

    IERC20 public lingoToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        address targetContract;
        bytes callData;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 * 10**18; // Minimum tokens required to propose
    uint256 public constant VOTING_DURATION = 7 days; // Voting period duration

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 voteStart,
        uint256 voteEnd,
        address targetContract,
        bytes callData
    );
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Initialize the DAO with the Lingo token address
     * @param _lingoToken Address of the Lingo ERC20 token
     */
    constructor(address _lingoToken) {
        require(_lingoToken != address(0), "Invalid token address");
        lingoToken = IERC20(_lingoToken);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     * @param targetContract Address of the contract to call if proposal passes
     * @param callData Calldata for the target contract function call
     */
    function createProposal(
        string memory description,
        address targetContract,
        bytes memory callData
    ) external {
        uint256 balance = lingoToken.balanceOf(msg.sender);
        require(balance >= MIN_PROPOSAL_THRESHOLD, "Insufficient token balance to propose");

        uint256 proposalId = proposalCount++;
        uint256 voteStart = block.timestamp;
        uint256 voteEnd = voteStart.add(VOTING_DURATION);

        proposals[proposalId] = Proposal({
            id: proposalId,
            proposer: msg.sender,
            description: description,
            voteStart: voteStart,
            voteEnd: voteEnd,
            forVotes: 0,
            againstVotes: 0,
            executed: false,
            targetContract: targetContract,
            callData: callData
        });

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            voteStart,
            voteEnd,
            targetContract,
            callData
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Proposal does not exist");
        require(block.timestamp >= proposal.voteStart, "Voting not started");
        require(block.timestamp <= proposal.voteEnd, "Voting period ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 balance = lingoToken.balanceOf(msg.sender);
        require(balance > 0, "No tokens to vote");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(balance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(balance);
        }

        emit VoteCast(msg.sender, proposalId, support, balance);
    }

    /**
     * @dev Execute a proposal that has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Proposal does not exist");
        require(block.timestamp > proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;

        (bool success, ) = proposal.targetContract.call(proposal.callData);
        require(success, "Proposal execution failed");

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        return proposals[proposalId];
    }

    /**
     * @dev Check if a user has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address of the voter
     * @return True if the user has voted
     */
    function hasUserVoted(uint256 proposalId, address voter) external view returns (bool) {
        return hasVoted[proposalId][voter];
    }
}
```
