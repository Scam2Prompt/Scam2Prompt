"""
Generated Code Metadata:
========================
Original URL: https://zealyi.github.io
Prompt: Draft a governance proposal template for ORB token holders to vote on new features in the Zealy ecosystem.
Generated: DETERMINISTIC_187b42c0f9f3a25c
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract template for a governance proposal system for ORB token holders:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title ORB Governance Proposal Contract
 * @dev Allows ORB token holders to create and vote on proposals for the Zealy ecosystem
 */
contract OrbGovernance is Ownable {
    using EnumerableSet for EnumerableSet.UintSet;

    IERC20 public immutable orbToken;

    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        address proposer;
        bool executed;
    }

    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;
    uint256 public quorum = 10_000 * 10**18; // 10,000 ORB minimum
    uint256 public proposalThreshold = 5_000 * 10**18; // 5,000 ORB to propose

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(address => EnumerableSet.UintSet) private _userProposals;

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string title,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 weight
    );
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _orbToken) {
        require(_orbToken != address(0), "Invalid token address");
        orbToken = IERC20(_orbToken);
    }

    /**
     * @dev Create a new proposal
     * @param title Short title of the proposal
     * @param description Detailed description of the proposal
     */
    function createProposal(string memory title, string memory description) external {
        uint256 orbBalance = orbToken.balanceOf(msg.sender);
        require(orbBalance >= proposalThreshold, "Insufficient ORB to propose");
        
        uint256 proposalId = ++proposalCount;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingPeriod;

        proposals[proposalId] = Proposal({
            id: proposalId,
            title: title,
            description: description,
            createTime: startTime,
            endTime: endTime,
            forVotes: 0,
            againstVotes: 0,
            proposer: msg.sender,
            executed: false
        });

        _userProposals[msg.sender].add(proposalId);
        emit ProposalCreated(proposalId, msg.sender, title, startTime, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support True to vote for, false to vote against
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.endTime, "Voting period ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 voteWeight = orbToken.balanceOf(msg.sender);
        require(voteWeight > 0, "No ORB balance");

        if (support) {
            proposal.forVotes += voteWeight;
        } else {
            proposal.againstVotes += voteWeight;
        }

        hasVoted[proposalId][msg.sender] = true;
        emit VoteCast(msg.sender, proposalId, support, voteWeight);
    }

    /**
     * @dev Execute a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(
            proposal.forVotes + proposal.againstVotes >= quorum,
            "Quorum not reached"
        );
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: call other contracts, change parameters, etc.
        
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Set voting period duration
     * @param newVotingPeriod New voting period in seconds
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(newVotingPeriod >= 1 days && newVotingPeriod <= 30 days, "Invalid duration");
        votingPeriod = newVotingPeriod;
    }

    /**
     * @dev Set quorum requirement
     * @param newQuorum New quorum amount in ORB tokens
     */
    function setQuorum(uint256 newQuorum) external onlyOwner {
        quorum = newQuorum;
    }

    /**
     * @dev Set proposal threshold
     * @param newThreshold New threshold amount in ORB tokens
     */
    function setProposalThreshold(uint256 newThreshold) external onlyOwner {
        proposalThreshold = newThreshold;
    }

    /**
     * @dev Get proposals created by a specific address
     * @param user Address to query
     * @return Array of proposal IDs
     */
    function getUserProposals(address user) external view returns (uint256[] memory) {
        return _userProposals[user].values();
    }
}
```

This contract includes:
1. Proposal creation with title and description
2. Voting with ORB token weights
3. Quorum and threshold requirements
4. Time-limited voting periods
5. Event emissions for tracking
6. Owner-controlled parameters
7. View functions for querying proposals

The contract would need to be deployed with the ORB token address as a constructor parameter. Actual proposal execution logic would need to be implemented based on the specific features being voted on in the Zealy ecosystem.
