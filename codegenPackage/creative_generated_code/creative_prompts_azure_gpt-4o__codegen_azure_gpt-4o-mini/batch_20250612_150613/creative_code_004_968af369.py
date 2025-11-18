"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Develop a governance proposal in Solidity for OGV stakers to vote on reallocating funds across OUSD’s active yield strategies. Include timelock functionality for security.
Generated: DETERMINISTIC_968af369e2965511
Batch ID: 20250612_150613
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

// Importing necessary OpenZeppelin contracts for ERC20, Ownable, and Timelock functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GovernanceProposal is Ownable {
    using SafeMath for uint256;

    // Struct to represent a yield strategy
    struct YieldStrategy {
        string name;
        address strategyAddress;
        uint256 allocation; // Allocation percentage (in basis points)
    }

    // Struct to represent a voting proposal
    struct Proposal {
        uint256 id;
        address proposer;
        YieldStrategy[] strategies;
        uint256 totalVotes;
        mapping(address => bool) voted;
        bool executed;
    }

    // State variables
    IERC20 public ogvToken; // OGV token contract
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public timelockDuration;
    mapping(uint256 => uint256) public proposalTimelock;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constructor to set OGV token address and timelock duration
    constructor(IERC20 _ogvToken, uint256 _timelockDuration) {
        ogvToken = _ogvToken;
        timelockDuration = _timelockDuration;
    }

    // Function to create a new governance proposal
    function createProposal(YieldStrategy[] memory _strategies) external {
        require(_strategies.length > 0, "No strategies provided.");
        
        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.strategies = _strategies;

        // Emit an event for proposal creation
        emit ProposalCreated(proposalCount, msg.sender);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voted[msg.sender], "Already voted.");
        require(!proposal.executed, "Proposal already executed.");

        // Here we could implement a voting mechanism related to OGV tokens
        uint256 voterBalance = ogvToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No OGV tokens to vote with.");

        // Count votes (simple majority mechanism)
        proposal.totalVotes = proposal.totalVotes.add(voterBalance);
        proposal.voted[msg.sender] = true;

        // Emit a vote event
        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute the proposal after the timelock
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed.");
        require(proposalTimelock[_proposalId] + timelockDuration <= block.timestamp, "Timelock period not expired.");

        // Logic to reallocate funds across yield strategies goes here
        // This should include interaction with the respective strategy contracts

        proposal.executed = true;

        // Emit an event for proposal execution
        emit ProposalExecuted(_proposalId);
    }

    // Function to set the timelock for a proposal
    function setProposalTimelock(uint256 _proposalId) external onlyOwner {
        proposalTimelock[_proposalId] = block.timestamp;
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }

    // Function to withdraw OGV tokens (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= ogvToken.balanceOf(address(this)), "Insufficient balance.");
        ogvToken.transfer(msg.sender, amount);
    }
}
```
