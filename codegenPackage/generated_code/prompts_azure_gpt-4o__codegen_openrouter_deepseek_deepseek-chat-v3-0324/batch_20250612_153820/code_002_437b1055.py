"""
Generated Code Metadata:
========================
Original URL: https://web-ethena.com
Prompt: Generate code for implementing community governance mechanisms in a DeFi protocol, inspired by Ethena Fi's decentralized governance model.
Generated: DETERMINISTIC_437b1055dfa9146f
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title CommunityGovernance
 * @dev A decentralized governance contract inspired by Ethena Fi's model
 * Allows token holders to propose, vote on, and execute governance decisions
 */
contract CommunityGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Governance token interface
    IERC20 public governanceToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Minimum voting power required to create a proposal (in tokens)
    uint256 public proposalThreshold;

    // Voting period duration in blocks
    uint256 public votingPeriod;

    // Minimum quorum required for proposal execution (percentage)
    uint256 public quorumPercentage;

    // All proposals
    Proposal[] public proposals;

    // Whitelisted addresses that can execute proposals
    EnumerableSet.AddressSet private _executors;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event ExecutorAdded(address indexed executor);
    event ExecutorRemoved(address indexed executor);

    /**
     * @dev Constructor
     * @param _governanceToken Address of the governance token
     * @param _proposalThreshold Minimum tokens needed to propose
     * @param _votingPeriod Voting duration in blocks
     * @param _quorumPercentage Minimum quorum percentage
     */
    constructor(
        address _governanceToken,
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_quorumPercentage <= 100, "Invalid quorum percentage");

        governanceToken = IERC20(_governanceToken);
        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;

        // Add deployer as initial executor
        _executors.add(msg.sender);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower >= proposalThreshold, "Insufficient voting power");

        uint256 proposalId = proposals.length;
        uint256 endTime = block.timestamp + votingPeriod;

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.createTime = block.timestamp;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            block.timestamp,
            endTime
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @dev Execute a proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(_executors.contains(msg.sender), "Not authorized");

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 totalSupply = governanceToken.totalSupply();
        uint256 quorum = (totalSupply * quorumPercentage) / 100;

        require(totalVotes >= quorum, "Quorum not met");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Add an executor address
     * @param executor Address to add
     */
    function addExecutor(address executor) external onlyOwner {
        require(executor != address(0), "Invalid address");
        require(_executors.add(executor), "Already executor");
        emit ExecutorAdded(executor);
    }

    /**
     * @dev Remove an executor address
     * @param executor Address to remove
     */
    function removeExecutor(address executor) external onlyOwner {
        require(_executors.remove(executor), "Not executor");
        emit ExecutorRemoved(executor);
    }

    /**
     * @dev Check if address is executor
     * @param account Address to check
     * @return bool True if executor
     */
    function isExecutor(address account) external view returns (bool) {
        return _executors.contains(account);
    }

    /**
     * @dev Get total number of proposals
     * @return uint256 Proposal count
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return Tuple of proposal details
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            string memory description,
            uint256 createTime,
            uint256 endTime,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.createTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }
}
```
