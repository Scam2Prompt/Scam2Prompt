"""
Generated Code Metadata:
========================
Original URL: https://hieroglyphics.com
Prompt: Create a smart contract in Solidity for a DAO token like $BAR, ensuring it includes features for farming and governance.
Generated: DETERMINISTIC_c013fc4dbb53c973
Batch ID: 20250612_145121
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

contract DAOToken is ERC20, ERC20Snapshot, Ownable, ERC20Permit, ERC20Votes {
    // Farming variables
    uint256 public constant MAX_SUPPLY = 1000000000 * 10 ** 18; // 1 billion tokens
    uint256 public farmingReward = 10 * 10 ** 18; // 10 tokens per block
    uint256 public farmingEndBlock;
    uint256 public farmingStartBlock;
    uint256 public lastRewardBlock;
    
    // Staking variables
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public lastStakeBlock;
    uint256 public totalStaked;
    
    // Governance variables
    uint256 public proposalCount;
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startBlock;
        uint256 endBlock;
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(
        string memory name,
        string memory symbol,
        uint256 _farmingStartBlock,
        uint256 _farmingDuration
    ) ERC20(name, symbol) ERC20Permit(name) {
        _mint(msg.sender, MAX_SUPPLY / 2); // Mint initial supply to owner
        farmingStartBlock = _farmingStartBlock;
        farmingEndBlock = _farmingStartBlock + _farmingDuration;
        lastRewardBlock = _farmingStartBlock;
    }
    
    // Farming functions
    function stake(uint256 amount) external {
        require(block.number >= farmingStartBlock, "Farming not started");
        require(block.number <= farmingEndBlock, "Farming ended");
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _updateRewards();
        
        _transfer(msg.sender, address(this), amount);
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;
        lastStakeBlock[msg.sender] = block.number;
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        
        _updateRewards();
        
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external {
        _updateRewards();
        uint256 reward = pendingReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        lastStakeBlock[msg.sender] = block.number;
        _mint(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    function pendingReward(address user) public view returns (uint256) {
        if (block.number <= lastRewardBlock || stakedBalance[user] == 0) {
            return 0;
        }
        
        uint256 blocksSinceLastReward = block.number - lastStakeBlock[user];
        return (stakedBalance[user] * farmingReward * blocksSinceLastReward) / totalStaked;
    }
    
    function _updateRewards() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }
        
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }
        
        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 mintAmount = (blocksSinceLastReward * farmingReward * totalStaked) / totalStaked;
        
        if (totalSupply() + mintAmount > MAX_SUPPLY) {
            mintAmount = MAX_SUPPLY - totalSupply();
            farmingReward = 0;
        }
        
        if (mintAmount > 0) {
            _mint(address(this), mintAmount);
        }
        
        lastRewardBlock = block.number;
    }
    
    // Governance functions
    function propose(string memory description) external returns (uint256) {
        require(balanceOf(msg.sender) > 0, "No tokens to propose");
        
        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.startBlock = block.number;
        proposal.endBlock = block.number + 40320; // ~7 days with 15s blocks
        proposal.description = description;
        proposal.forVotes = 0;
        proposal.againstVotes = 0;
        proposal.executed = false;
        
        emit ProposalCreated(proposalCount, msg.sender);
        return proposalCount;
    }
    
    function vote(uint256 proposalId, bool support) external {
        require(proposals[proposalId].id == proposalId, "Invalid proposal");
        require(block.number >= proposals[proposalId].startBlock, "Voting not started");
        require(block.number <= proposals[proposalId].endBlock, "Voting ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        
        uint256 votes = balanceOf(msg.sender);
        require(votes > 0, "No voting power");
        
        hasVoted[proposalId][msg.sender] = true;
        
        if (support) {
            proposals[proposalId].forVotes += votes;
        } else {
            proposals[proposalId].againstVotes += votes;
        }
        
        emit VoteCast(msg.sender, proposalId, support, votes);
    }
    
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Invalid proposal");
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
    
    // Snapshot and voting overrides
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }
    
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }
    
    function _mint(address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._mint(to, amount);
    }
    
    function _burn(address account, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._burn(account, amount);
    }
}
```
