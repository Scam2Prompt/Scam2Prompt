"""
Generated Code Metadata:
========================
Original URL: https://shibaswap.mypixieset.com
Prompt: Propose a new feature for ShibaSwap's Doggy DAO, utilizing BONE tokens for governance and voting on protocol changes.
Generated: DETERMINISTIC_2c89730109d83b84
Batch ID: 20250622_212541
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

contract DoggyDAO is Ownable, ReentrancyGuard {
    IERC20 public boneToken;
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }
    
    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;
    uint256 public quorumPercentage = 10; // 10% of total BONE supply required
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    event ProposalCreated(uint256 indexed id, string description, uint256 voteEnd);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed id);
    
    constructor(address _boneToken) {
        require(_boneToken != address(0), "Invalid BONE token address");
        boneToken = IERC20(_boneToken);
    }
    
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteEnd: block.timestamp + votingPeriod,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, _description, block.timestamp + votingPeriod);
    }
    
    function vote(uint256 _proposalId, bool _support) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp <= proposal.voteEnd, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        
        uint256 voterBalance = boneToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No BONE tokens to vote with");
        
        hasVoted[_proposalId][msg.sender] = true;
        
        if (_support) {
            proposal.yesVotes += voterBalance;
        } else {
            proposal.noVotes += voterBalance;
        }
        
        emit Voted(_proposalId, msg.sender, _support, voterBalance);
    }
    
    function executeProposal(uint256 _proposalId) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalBoneSupply = boneToken.totalSupply();
        uint256 quorum = (totalBoneSupply * quorumPercentage) / 100;
        uint256 totalVotes = proposal.yesVotes + proposal.noVotes;
        
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.yesVotes > proposal.noVotes, "Proposal did not pass");
        
        proposal.executed = true;
        
        emit ProposalExecuted(_proposalId);
    }
    
    function setVotingPeriod(uint256 _newPeriod) external onlyOwner {
        require(_newPeriod > 0, "Period must be > 0");
        votingPeriod = _newPeriod;
    }
    
    function setQuorumPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Invalid percentage");
        quorumPercentage = _newPercentage;
    }
}
```
