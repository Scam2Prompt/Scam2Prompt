"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Create a decentralized governance system in Solidity for a platform like Pushd, allowing token holders to vote on proposals and changes to platform features and policies.
Generated: DETERMINISTIC_4f89dc68c55b8563
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Governance contract allowing token holders to create and vote on proposals
contract Governance is Ownable {
    using Counters for Counters.Counter;

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;
    // Mapping to keep track of whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    // Counter for proposal IDs
    Counters.Counter private proposalIdCounter;
    // Token used for governance voting
    IERC20 public governanceToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the proposal is still active
    modifier onlyActiveProposal(uint256 _proposalId) {
        require(block.timestamp < proposals[_proposalId].endTime, "Proposal has ended");
        _;
    }

    // Modifier to check if the proposal has been executed
    modifier onlyNonExecutedProposal(uint256 _proposalId) {
        require(!proposals[_proposalId].executed, "Proposal already executed");
        _;
    }

    // Modifier to check if caller is a token holder
    modifier onlyTokenHolder() {
        require(governanceToken.balanceOf(msg.sender) > 0, "Only token holders can vote");
        _;
    }

    // Constructor to initialize governance token
    constructor(IERC20 _governanceToken) {
        governanceToken = _governanceToken;
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero");

        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();
        proposals[newProposalId] = Proposal({
            id: newProposalId,
            creator: msg.sender,
            description: _description,
            voteCount: 0,
            endTime: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(newProposalId, _description, block.timestamp + _duration);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external onlyTokenHolder onlyActiveProposal(_proposalId) onlyNonExecutedProposal(_proposalId) {
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        hasVoted[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount += governanceToken.balanceOf(msg.sender);

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has ended
    function executeProposal(uint256 _proposalId) external onlyNonExecutedProposal(_proposalId) {
        require(block.timestamp >= proposals[_proposalId].endTime, "Proposal has not ended yet");

        proposals[_proposalId].executed = true;
        // Placeholder for execution logic (e.g., changing platform features)
        // add your feature execution logic here

        emit ProposalExecuted(_proposalId);
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
