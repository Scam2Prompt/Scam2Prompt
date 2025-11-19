"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Design a staking and voting system for a DAO, ensuring that users with a minimum of 100,000 $MBDAO tokens have access to VIP features, including deal flow and DD reports.
Generated: DETERMINISTIC_a12bede595b2e973
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MBDAOGovernance is Ownable, ReentrancyGuard {
    IERC20 public mbdaoToken;
    uint256 public constant MIN_STAKE_FOR_VIP = 100_000 * 10**18; // 100,000 MBDAO tokens (assuming 18 decimals)
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) public stakes;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public votes;
    mapping(address => bool) public vipMembers;
    
    uint256 public proposalCount;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 startTime, uint256 endTime);
    event Voted(address indexed voter, uint256 indexed proposalId, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    event VIPStatusChanged(address indexed user, bool isVIP);
    
    constructor(address _mbdaoToken) {
        mbdaoToken = IERC20(_mbdaoToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(mbdaoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += amount;
        
        _updateVIPStatus(msg.sender);
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(mbdaoToken.transfer(msg.sender, amount), "Transfer failed");
        
        _updateVIPStatus(msg.sender);
        emit Unstaked(msg.sender, amount);
    }
    
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + duration;
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, description, startTime, endTime);
    }
    
    function vote(uint256 proposalId) external {
        require(stakes[msg.sender].amount > 0, "No staked tokens");
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        require(block.timestamp >= proposals[proposalId].startTime, "Voting not started");
        require(block.timestamp <= proposals[proposalId].endTime, "Voting ended");
        require(!votes[msg.sender][proposalId], "Already voted");
        
        votes[msg.sender][proposalId] = true;
        proposals[proposalId].voteCount += stakes[msg.sender].amount;
        
        emit Voted(msg.sender, proposalId, stakes[msg.sender].amount);
    }
    
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        require(block.timestamp > proposals[proposalId].endTime, "Voting not ended");
        require(!proposals[proposalId].executed, "Proposal already executed");
        
        proposals[proposalId].executed = true;
        emit ProposalExecuted(proposalId);
    }
    
    function _updateVIPStatus(address user) private {
        bool newStatus = stakes[user].amount >= MIN_STAKE_FOR_VIP;
        if (vipMembers[user] != newStatus) {
            vipMembers[user] = newStatus;
            emit VIPStatusChanged(user, newStatus);
        }
    }
    
    function accessVIPFeatures() external view returns (bool) {
        return vipMembers[msg.sender];
    }
    
    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
    
    function getProposal(uint256 proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteCount,
        uint256 startTime,
        uint256 endTime,
        bool executed
    ) {
        Proposal memory proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.voteCount,
            proposal.startTime,
            proposal.endTime,
            proposal.executed
        );
    }
}
```
