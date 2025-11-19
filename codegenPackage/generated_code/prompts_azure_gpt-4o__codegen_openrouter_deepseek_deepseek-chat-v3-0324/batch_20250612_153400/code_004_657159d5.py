"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Write a smart contract in Solidity or Rust for staking EGLD and enabling governance voting on MultiversX proposals.
Generated: DETERMINISTIC_657159d58e8df4f1
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EGLDStakingGovernance is Ownable, ReentrancyGuard {
    IERC20 public egldToken;
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 deadline;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) public stakes;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    
    uint256 public totalStaked;
    uint256 public proposalCount;
    uint256 public constant MIN_STAKE = 1 ether;
    uint256 public constant VOTING_PERIOD = 7 days;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(address indexed voter, uint256 proposalId, bool support);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _egldToken) {
        egldToken = IERC20(_egldToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE, "Amount below minimum stake");
        require(egldToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];
        
        require(egldToken.transfer(msg.sender, userStake.amount), "Transfer failed");
        emit Unstaked(msg.sender, userStake.amount);
    }
    
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            deadline: block.timestamp + VOTING_PERIOD,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, description);
    }
    
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[msg.sender][proposalId], "Already voted");
        require(stakes[msg.sender].amount > 0, "No stake to vote");
        
        hasVoted[msg.sender][proposalId] = true;
        
        if (support) {
            proposal.votesFor += stakes[msg.sender].amount;
        } else {
            proposal.votesAgainst += stakes[msg.sender].amount;
        }
        
        emit Voted(msg.sender, proposalId, support);
    }
    
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        proposal.executed = true;
        
        emit ProposalExecuted(proposalId);
    }
    
    function getVotingPower(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
    
    function getProposal(uint256 proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 deadline,
        uint256 votesFor,
        uint256 votesAgainst,
        bool executed
    ) {
        Proposal memory proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.deadline,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.executed
        );
    }
}
```
