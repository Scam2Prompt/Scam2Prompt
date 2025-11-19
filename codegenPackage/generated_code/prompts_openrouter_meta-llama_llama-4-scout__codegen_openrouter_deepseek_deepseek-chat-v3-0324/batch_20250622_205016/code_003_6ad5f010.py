"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Design a basic DeFi use case using Baby Grok tokens, including staking and governance features, and provide a high-level architecture for the implementation.
Generated: DETERMINISTIC_6ad5f01094407ff3
Batch ID: 20250622_205016
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BabyGrokToken
 * @dev ERC20 token with governance and staking capabilities
 */
contract BabyGrokToken is ERC20, ERC20Votes, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant STAKING_REWARD_RATE = 10; // 10% annual reward
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor() ERC20("Baby Grok", "BGROK") ERC20Permit("Baby Grok") {
        _mint(msg.sender, MAX_SUPPLY);
    }
    
    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }
        
        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp
        });
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        claimReward();
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Claim staking rewards
     */
    function claimReward() public nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            stakes[msg.sender].stakedAt = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }
    
    /**
     * @dev Calculate staking rewards for a user
     * @param user Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - stakeInfo.stakedAt;
        reward = (stakeInfo.amount * STAKING_REWARD_RATE * stakingDuration) / (100 * 365 days);
    }
    
    // The following functions are overrides required by Solidity.
    function _afterTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._afterTokenTransfer(from, to, amount);
    }
    
    function _mint(address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._mint(to, amount);
    }
    
    function _burn(address account, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._burn(account, amount);
    }
}

/**
 * @title BabyGrokGovernance
 * @dev Governance contract for BabyGrok ecosystem
 */
contract BabyGrokGovernance {
    BabyGrokToken public token;
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }
    
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    event ProposalCreated(uint256 id, string description);
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 id);
    
    constructor(address _token) {
        token = BabyGrokToken(_token);
    }
    
    /**
     * @dev Create a new governance proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        proposals.push(Proposal({
            id: proposals.length,
            description: description,
            voteEnd: block.timestamp + 7 days,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }
    
    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        
        uint256 votes = token.getPastVotes(msg.sender, proposal.voteEnd - 1);
        require(votes > 0, "No voting power");
        
        hasVoted[proposalId][msg.sender] = true;
        
        if (support) {
            proposal.forVotes += votes;
        } else {
            proposal.againstVotes += votes;
        }
        
        emit VoteCast(msg.sender, proposalId, support, votes);
    }
    
    /**
     * @dev Execute a proposal if it has passed
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}
```
