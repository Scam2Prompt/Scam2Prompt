"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.foundation
Prompt: Develop a simple smart contract in Solidity that interacts with the WalletConnect Network, leveraging its governance and staking mechanisms.
Generated: DETERMINISTIC_43c70114e6eed3ad
Batch ID: 20250622_205139
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

/**
 * @title WalletConnect Governance and Staking Contract
 * @dev Implements staking and governance functionality for WalletConnect Network
 */
contract WalletConnectGovernance is Ownable, ReentrancyGuard {
    IERC20 public token;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }
    
    uint256 public constant MIN_STAKE = 100 * 10**18; // 100 tokens
    uint256 public constant STAKE_LOCK_PERIOD = 7 days;
    uint256 public constant VOTING_PERIOD = 3 days;
    
    mapping(address => Stake) public stakes;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    
    uint256 public totalStaked;
    uint256 public proposalCount;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _token) {
        token = IERC20(_token);
    }
    
    /**
     * @dev Stake tokens to participate in governance
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE, "Amount below minimum stake");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].amount += amount;
        } else {
            stakes[msg.sender] = Stake(amount, block.timestamp);
        }
        
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens after lock period
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.stakedAt + STAKE_LOCK_PERIOD, "Stake still locked");
        
        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];
        
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Create a new governance proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteEnd: block.timestamp + VOTING_PERIOD,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, description);
    }
    
    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support Whether to support the proposal
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal doesn't exist");
        require(block.timestamp < proposal.voteEnd, "Voting period ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");
        require(stakes[msg.sender].amount > 0, "No stake found");
        
        uint256 votingPower = stakes[msg.sender].amount;
        
        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }
        
        hasVoted[msg.sender][proposalId] = true;
        emit Voted(msg.sender, proposalId, support, votingPower);
    }
    
    /**
     * @dev Execute a proposal if it passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal doesn't exist");
        require(block.timestamp >= proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        if (proposal.forVotes > proposal.againstVotes) {
            proposal.executed = true;
            emit ProposalExecuted(proposalId);
        }
    }
    
    /**
     * @dev Get voting power of an address
     * @param voter Address to check
     * @return Voting power in tokens
     */
    function getVotingPower(address voter) external view returns (uint256) {
        return stakes[voter].amount;
    }
}
```
