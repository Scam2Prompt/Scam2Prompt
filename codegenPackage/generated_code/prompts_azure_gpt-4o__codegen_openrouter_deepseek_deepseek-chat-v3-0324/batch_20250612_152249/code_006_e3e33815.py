"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Create a governance smart contract for BGT token management on Berachain, including functionality for bribes and voting.
Generated: DETERMINISTIC_e3e33815c97298b3
Batch ID: 20250612_152249
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

contract BGTGovernance is Ownable, ReentrancyGuard {
    IERC20 public bgtToken;
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) voters;
    }
    
    struct Bribe {
        address token;
        uint256 amount;
        bool claimed;
    }
    
    uint256 public proposalCount;
    uint256 public constant VOTING_PERIOD = 3 days;
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 * 10**18; // 1000 BGT
    
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => Bribe) public bribes;
    mapping(address => uint256) public lockedTokens;
    mapping(address => uint256) public unlockTime;
    
    event ProposalCreated(uint256 indexed id, string description, uint256 voteEnd);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed id, bool result);
    event BribeDeposited(uint256 indexed proposalId, address token, uint256 amount);
    event BribeClaimed(uint256 indexed proposalId, address claimer, uint256 amount);
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed user, uint256 amount);
    
    constructor(address _bgtToken) {
        bgtToken = IERC20(_bgtToken);
    }
    
    modifier onlyDuringVoting(uint256 proposalId) {
        require(proposals[proposalId].voteEnd > block.timestamp, "Voting period ended");
        _;
    }
    
    modifier onlyAfterVoting(uint256 proposalId) {
        require(proposals[proposalId].voteEnd <= block.timestamp, "Voting ongoing");
        _;
    }
    
    modifier onlyProposalNotExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }
    
    function createProposal(string memory description) external {
        uint256 balance = bgtToken.balanceOf(msg.sender);
        require(balance >= MIN_PROPOSAL_THRESHOLD, "Insufficient BGT for proposal");
        
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.voteEnd = block.timestamp + VOTING_PERIOD;
        
        emit ProposalCreated(proposalCount, description, newProposal.voteEnd);
    }
    
    function vote(uint256 proposalId, bool support) external onlyDuringVoting(proposalId) nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voters[msg.sender], "Already voted");
        
        uint256 voteWeight = bgtToken.balanceOf(msg.sender);
        require(voteWeight > 0, "No BGT to vote with");
        
        if (support) {
            proposal.votesFor += voteWeight;
        } else {
            proposal.votesAgainst += voteWeight;
        }
        
        proposal.voters[msg.sender] = true;
        emit Voted(proposalId, msg.sender, support, voteWeight);
    }
    
    function executeProposal(uint256 proposalId) external onlyAfterVoting(proposalId) onlyProposalNotExecuted(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        proposal.executed = true;
        
        bool result = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(proposalId, result);
    }
    
    function depositBribe(uint256 proposalId, address token, uint256 amount) external {
        require(proposals[proposalId].id != 0, "Invalid proposal");
        require(proposals[proposalId].voteEnd > block.timestamp, "Voting ended");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        bribes[proposalId] = Bribe(token, amount, false);
        
        emit BribeDeposited(proposalId, token, amount);
    }
    
    function claimBribe(uint256 proposalId) external nonReentrant {
        require(proposals[proposalId].executed, "Proposal not executed");
        require(proposals[proposalId].votesFor > proposals[proposalId].votesAgainst, "Proposal failed");
        require(proposals[proposalId].voters[msg.sender], "Did not vote for winning proposal");
        require(!bribes[proposalId].claimed, "Bribe already claimed");
        
        Bribe storage bribe = bribes[proposalId];
        bribe.claimed = true;
        
        IERC20(bribe.token).transfer(msg.sender, bribe.amount);
        emit BribeClaimed(proposalId, msg.sender, bribe.amount);
    }
    
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Cannot lock 0 tokens");
        require(bgtToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        lockedTokens[msg.sender] += amount;
        unlockTime[msg.sender] = block.timestamp + lockDuration;
        
        emit TokensLocked(msg.sender, amount, unlockTime[msg.sender]);
    }
    
    function unlockTokens() external nonReentrant {
        require(block.timestamp >= unlockTime[msg.sender], "Tokens still locked");
        require(lockedTokens[msg.sender] > 0, "No locked tokens");
        
        uint256 amount = lockedTokens[msg.sender];
        lockedTokens[msg.sender] = 0;
        
        require(bgtToken.transfer(msg.sender, amount), "Transfer failed");
        emit TokensUnlocked(msg.sender, amount);
    }
    
    function emergencyWithdraw(address token) external onlyOwner {
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
