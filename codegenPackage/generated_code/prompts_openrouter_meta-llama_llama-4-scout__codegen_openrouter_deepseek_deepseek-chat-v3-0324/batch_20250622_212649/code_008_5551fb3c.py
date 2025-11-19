"""
Generated Code Metadata:
========================
Original URL: https://doubleton.pages.dev
Prompt: Propose a use case for TON's on-chain governance program and suggest how to implement it.
Generated: DETERMINISTIC_5551fb3cae1e1b58
Batch ID: 20250622_212649
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TONGovernance
 * @dev A smart contract for decentralized governance on TON blockchain
 * allowing token holders to propose and vote on protocol changes.
 */
contract TONGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public tonToken;
    uint256 public proposalCount;
    uint256 public votingPeriod; // in blocks
    uint256 public quorumPercentage; // minimum % of total supply required
    uint256 public thresholdPercentage; // minimum % of votes required to pass

    enum ProposalState { Pending, Active, Passed, Failed }

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        ProposalState state;
        mapping(address => bool) hasVoted;
    }

    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId, ProposalState outcome);

    /**
     * @dev Initialize governance contract
     * @param _tonToken Address of TON token contract
     * @param _votingPeriod Duration of voting period in blocks
     * @param _quorumPercentage Minimum participation percentage
     * @param _thresholdPercentage Minimum approval percentage
     */
    constructor(
        address _tonToken,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _thresholdPercentage
    ) {
        require(_tonToken != address(0), "Invalid token address");
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        require(_thresholdPercentage <= 100, "Threshold must be <= 100");

        tonToken = IERC20(_tonToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        thresholdPercentage = _thresholdPercentage;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of proposed change
     */
    function propose(string memory description) external {
        uint256 balance = tonToken.balanceOf(msg.sender);
        require(balance > 0, "No token balance");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.startBlock = block.number;
        newProposal.endBlock = block.number.add(votingPeriod);
        newProposal.state = ProposalState.Active;

        emit ProposalCreated(
            newProposal.id,
            msg.sender,
            description,
            newProposal.startBlock,
            newProposal.endBlock
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of proposal to vote on
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.Active, "Voting not active");
        require(block.number <= proposal.endBlock, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 balance = tonToken.balanceOf(msg.sender);
        require(balance > 0, "No token balance");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(balance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(balance);
        }

        emit VoteCast(msg.sender, proposalId, support, balance);
    }

    /**
     * @dev Execute a proposal after voting period ends
     * @param proposalId ID of proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.Active, "Proposal not active");
        require(block.number > proposal.endBlock, "Voting period not ended");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 totalSupply = tonToken.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);

        if (totalVotes < quorum) {
            proposal.state = ProposalState.Failed;
            emit ProposalExecuted(proposalId, ProposalState.Failed);
            return;
        }

        uint256 approvalPercentage = proposal.forVotes.mul(100).div(totalVotes);
        if (approvalPercentage >= thresholdPercentage) {
            proposal.state = ProposalState.Passed;
            emit ProposalExecuted(proposalId, ProposalState.Passed);
        } else {
            proposal.state = ProposalState.Failed;
            emit ProposalExecuted(proposalId, ProposalState.Failed);
        }
    }

    /**
     * @dev Update governance parameters (onlyOwner)
     */
    function updateParameters(
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _thresholdPercentage
    ) external onlyOwner {
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        require(_thresholdPercentage <= 100, "Threshold must be <= 100");

        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        thresholdPercentage = _thresholdPercentage;
    }
}
```
