"""
Generated Code Metadata:
========================
Original URL: https://dypius-xyz.pages.dev
Prompt: Create a governance voting smart contract that allows DYP token holders to propose and vote on ecosystem changes, such as adding pools or burning tokens.
Generated: DETERMINISTIC_00ac092295a46ce7
Batch ID: 20250612_153527
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

contract Governance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public immutable dypToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _whitelistedPools;

    uint256 public constant MIN_VOTING_DURATION = 1 days;
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 10000 * 10**18; // 10,000 DYP
    uint256 public constant QUORUM_THRESHOLD = 100000 * 10**18; // 100,000 DYP

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
    event PoolAdded(address indexed pool);
    event PoolRemoved(address indexed pool);
    event TokensBurned(uint256 amount);

    constructor(address _dypToken) {
        require(_dypToken != address(0), "Invalid DYP token address");
        dypToken = IERC20(_dypToken);
    }

    modifier onlyWhitelistedPool() {
        require(_whitelistedPools.contains(msg.sender), "Not whitelisted pool");
        _;
    }

    function propose(string memory description, uint256 duration) external {
        require(duration >= MIN_VOTING_DURATION, "Duration too short");
        uint256 balance = dypToken.balanceOf(msg.sender);
        require(balance >= MIN_PROPOSAL_THRESHOLD, "Insufficient DYP balance");

        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.description = description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp + duration;
        proposal.forVotes = 0;
        proposal.againstVotes = 0;
        proposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            description,
            proposal.startTime,
            proposal.endTime
        );
    }

    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Invalid proposal ID");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 balance = dypToken.balanceOf(msg.sender);
        require(balance > 0, "No DYP tokens");

        proposal.hasVoted[msg.sender] = true;
        if (support) {
            proposal.forVotes += balance;
        } else {
            proposal.againstVotes += balance;
        }

        emit VoteCast(msg.sender, proposalId, support, balance);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Invalid proposal ID");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(
            proposal.forVotes + proposal.againstVotes >= QUORUM_THRESHOLD,
            "Quorum not reached"
        );
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    function addPool(address pool) external onlyOwner {
        require(pool != address(0), "Invalid pool address");
        require(_whitelistedPools.add(pool), "Pool already whitelisted");
        emit PoolAdded(pool);
    }

    function removePool(address pool) external onlyOwner {
        require(_whitelistedPools.remove(pool), "Pool not whitelisted");
        emit PoolRemoved(pool);
    }

    function burnTokens(uint256 amount) external onlyWhitelistedPool {
        require(amount > 0, "Amount must be positive");
        require(
            dypToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        dypToken.transfer(address(0xdead), amount);
        emit TokensBurned(amount);
    }

    function isPoolWhitelisted(address pool) external view returns (bool) {
        return _whitelistedPools.contains(pool);
    }

    function getWhitelistedPools() external view returns (address[] memory) {
        return _whitelistedPools.values();
    }

    function getVotingPower(address voter) external view returns (uint256) {
        return dypToken.balanceOf(voter);
    }
}
```
