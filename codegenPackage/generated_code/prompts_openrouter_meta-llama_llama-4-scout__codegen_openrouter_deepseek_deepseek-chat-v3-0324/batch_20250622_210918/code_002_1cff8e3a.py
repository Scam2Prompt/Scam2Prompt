"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Generate a smart contract code for a tokenized venture capital platform, incorporating features such as token exposure, private angel network access, and enhanced DAO staking and voting rights.
Generated: DETERMINISTIC_1cff8e3a6d9a7a39
Batch ID: 20250622_210918
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract VentureCapitalToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Token exposure tiers
    enum Tier { BASIC, PREMIUM, VIP }
    
    // Mapping of addresses to their tier
    mapping(address => Tier) public tiers;
    
    // Mapping of addresses to staked amounts
    mapping(address => uint256) public stakedBalances;
    
    // Mapping of addresses to voting power
    mapping(address => uint256) public votingPower;
    
    // Mapping of addresses to private network access
    mapping(address => bool) private privateNetworkAccess;
    
    // Total staked tokens
    uint256 public totalStaked;
    
    // Minimum stake duration (in seconds)
    uint256 public constant MIN_STAKE_DURATION = 30 days;
    
    // Last stake time for each address
    mapping(address => uint256) public lastStakeTime;
    
    // DAO proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
    }
    
    // List of all proposals
    Proposal[] public proposals;
    
    // Mapping of voter to proposal to whether they've voted
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    
    // Events
    event TierUpdated(address indexed user, Tier tier);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event PrivateNetworkAccessGranted(address indexed user);
    event PrivateNetworkAccessRevoked(address indexed user);
    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(address indexed voter, uint256 proposalId, uint256 votes);
    event ProposalExecuted(uint256 indexed id);
    
    constructor() ERC20("VentureCapitalToken", "VCT") {
        _mint(msg.sender, 100000000 * 10 ** decimals());
    }
    
    // Set tier for a user (only owner)
    function setTier(address user, Tier tier) external onlyOwner {
        tiers[user] = tier;
        emit TierUpdated(user, tier);
    }
    
    // Stake tokens to gain voting power
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        // Voting power increases with stake amount and tier
        uint256 multiplier = 1;
        if (tiers[msg.sender] == Tier.PREMIUM) {
            multiplier = 2;
        } else if (tiers[msg.sender] == Tier.VIP) {
            multiplier = 3;
        }
        
        votingPower[msg.sender] = votingPower[msg.sender].add(amount.mul(multiplier));
        lastStakeTime[msg.sender] = block.timestamp;
        
        emit Staked(msg.sender, amount);
    }
    
    // Unstake tokens after minimum duration
    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        require(block.timestamp >= lastStakeTime[msg.sender] + MIN_STAKE_DURATION, "Minimum stake duration not met");
        
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        // Reduce voting power proportionally
        uint256 multiplier = 1;
        if (tiers[msg.sender] == Tier.PREMIUM) {
            multiplier = 2;
        } else if (tiers[msg.sender] == Tier.VIP) {
            multiplier = 3;
        }
        
        votingPower[msg.sender] = votingPower[msg.sender].sub(amount.mul(multiplier));
        
        _transfer(address(this), msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
    
    // Grant private network access (only owner)
    function grantPrivateAccess(address user) external onlyOwner {
        privateNetworkAccess[user] = true;
        emit PrivateNetworkAccessGranted(user);
    }
    
    // Revoke private network access (only owner)
    function revokePrivateAccess(address user) external onlyOwner {
        privateNetworkAccess[user] = false;
        emit PrivateNetworkAccessRevoked(user);
    }
    
    // Check private network access
    function hasPrivateAccess(address user) external view returns (bool) {
        return privateNetworkAccess[user];
    }
    
    // Create a new DAO proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 proposalId = proposals.length;
        uint256 deadline = block.timestamp.add(duration);
        
        proposals.push(Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            deadline: deadline,
            executed: false
        }));
        
        emit ProposalCreated(proposalId, description, deadline);
    }
    
    // Vote on a proposal
    function vote(uint256 proposalId) external whenNotPaused {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[msg.sender][proposalId], "Already voted");
        require(votingPower[msg.sender] > 0, "No voting power");
        
        hasVoted[msg.sender][proposalId] = true;
        proposal.voteCount = proposal.voteCount.add(votingPower[msg.sender]);
        
        emit Voted(msg.sender, proposalId, votingPower[msg.sender]);
    }
    
    // Execute a proposal if voting passed
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        // Simple majority voting threshold (can be customized)
        if (proposal.voteCount > totalStaked.div(2)) {
            proposal.executed = true;
            emit ProposalExecuted(proposalId);
        }
    }
    
    // Pause contract in case of emergency
    function pause() external onlyOwner {
        _pause();
    }
    
    // Unpause contract
    function unpause() external onlyOwner {
        _unpause();
    }
    
    // Override transfer to prevent transfers while paused
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
