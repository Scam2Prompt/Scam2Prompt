"""
Generated Code Metadata:
========================
Original URL: https://shibuswap.github.io
Prompt: Explain how to use ShibaSwap's governance token, BONE, to propose and vote on protocol changes, and provide an example of a voting transaction using Ethereum smart contracts.
Generated: DETERMINISTIC_3fdd68de3c3de6bf
Batch ID: 20250612_142640
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title ShibaSwap Governance Contract
 * @dev Allows BONE token holders to propose and vote on protocol changes
 */
contract ShibaSwapGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public immutable boneToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _whitelistedTokens;

    uint256 public constant MIN_PROPOSAL_BALANCE = 1000 * 10**18; // 1000 BONE required to propose
    uint256 public constant VOTING_PERIOD = 17280; // ~3 days in blocks (assuming 15s block time)
    uint256 public constant QUORUM_PERCENTAGE = 4; // 4% of total supply required

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _boneToken) {
        require(_boneToken != address(0), "Invalid BONE token address");
        boneToken = IERC20(_boneToken);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        require(boneToken.balanceOf(msg.sender) >= MIN_PROPOSAL_BALANCE, "Insufficient BONE balance");
        
        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.startBlock = block.number;
        newProposal.endBlock = block.number + VOTING_PERIOD;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            newProposal.startBlock,
            newProposal.endBlock
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True if voting for, false if voting against
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 voterBalance = boneToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No BONE balance");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes += voterBalance;
        } else {
            proposal.againstVotes += voterBalance;
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    /**
     * @dev Execute a proposal if quorum is reached and majority is for
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalSupply = boneToken.totalSupply();
        uint256 quorum = (totalSupply * QUORUM_PERCENTAGE) / 100;
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;

        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Majority not for");

        proposal.executed = true;

        // Here you would implement the actual changes based on the proposal
        // For example: update parameters, call other contracts, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Check if a proposal has passed
     * @param proposalId ID of the proposal
     * @return bool True if proposal passed
     */
    function proposalPassed(uint256 proposalId) external view returns (bool) {
        Proposal storage proposal = proposals[proposalId];
        if (block.number <= proposal.endBlock) return false;
        if (proposal.executed) return true;

        uint256 totalSupply = boneToken.totalSupply();
        uint256 quorum = (totalSupply * QUORUM_PERCENTAGE) / 100;
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;

        return totalVotes >= quorum && proposal.forVotes > proposal.againstVotes;
    }
}

// Example of how to interact with the contract
contract GovernanceInteractionExample {
    ShibaSwapGovernance public governance;

    constructor(address _governance) {
        governance = ShibaSwapGovernance(_governance);
    }

    /**
     * @dev Example function to create a proposal
     * @param description Description of the proposal
     */
    function createProposalExample(string memory description) external {
        governance.propose(description);
    }

    /**
     * @dev Example function to vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True if voting for, false if voting against
     */
    function voteExample(uint256 proposalId, bool support) external {
        governance.vote(proposalId, support);
    }

    /**
     * @dev Example function to execute a passed proposal
     * @param proposalId ID of the proposal
     */
    function executeProposalExample(uint256 proposalId) external {
        governance.executeProposal(proposalId);
    }
}
```
