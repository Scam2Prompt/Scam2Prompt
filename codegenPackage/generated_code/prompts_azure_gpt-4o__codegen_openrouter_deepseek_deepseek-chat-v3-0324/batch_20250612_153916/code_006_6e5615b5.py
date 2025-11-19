"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: Develop a smart contract that incorporates Spark's audited Savings USDS protocol to distribute rewards transparently based on Sky's community-driven governance.
Generated: DETERMINISTIC_6e5615b5ce63ecb6
Batch ID: 20250612_153916
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

interface ISavingsUSDS {
    function distributeRewards(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

contract SkyRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    ISavingsUSDS public savingsContract;
    
    // Governance parameters
    uint256 public rewardDistributionInterval = 7 days;
    uint256 public lastDistributionTime;
    uint256 public minDistributionAmount;
    
    // Community governance
    address[] public governanceMembers;
    mapping(address => bool) public isGovernanceMember;
    uint256 public quorumThreshold = 50; // 50% of members must approve
    
    // Proposal tracking
    struct Proposal {
        uint256 id;
        uint256 amount;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }
    
    Proposal[] public proposals;
    uint256 public proposalCount;
    
    event RewardDistributed(uint256 amount, uint256 timestamp);
    event ProposalCreated(uint256 id, uint256 amount, uint256 endTime);
    event VoteCast(address voter, uint256 proposalId, bool support);
    event ProposalExecuted(uint256 id, uint256 amount);
    
    constructor(
        address _rewardToken,
        address _savingsContract,
        uint256 _minDistributionAmount,
        address[] memory _initialGovernance
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_savingsContract != address(0), "Invalid savings contract address");
        
        rewardToken = IERC20(_rewardToken);
        savingsContract = ISavingsUSDS(_savingsContract);
        minDistributionAmount = _minDistributionAmount;
        
        for (uint256 i = 0; i < _initialGovernance.length; i++) {
            _addGovernanceMember(_initialGovernance[i]);
        }
    }
    
    modifier onlyGovernance() {
        require(isGovernanceMember[msg.sender], "Caller is not a governance member");
        _;
    }
    
    function _addGovernanceMember(address member) internal {
        require(member != address(0), "Invalid member address");
        if (!isGovernanceMember[member]) {
            isGovernanceMember[member] = true;
            governanceMembers.push(member);
        }
    }
    
    function addGovernanceMember(address member) external onlyOwner {
        _addGovernanceMember(member);
    }
    
    function removeGovernanceMember(address member) external onlyOwner {
        require(isGovernanceMember[member], "Not a governance member");
        isGovernanceMember[member] = false;
        
        for (uint256 i = 0; i < governanceMembers.length; i++) {
            if (governanceMembers[i] == member) {
                governanceMembers[i] = governanceMembers[governanceMembers.length - 1];
                governanceMembers.pop();
                break;
            }
        }
    }
    
    function createProposal(uint256 amount, uint256 votingDuration) external onlyGovernance {
        require(amount >= minDistributionAmount, "Amount below minimum");
        require(votingDuration >= 1 days && votingDuration <= 14 days, "Invalid voting duration");
        
        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.amount = amount;
        newProposal.endTime = block.timestamp + votingDuration;
        
        emit ProposalCreated(proposalId, amount, newProposal.endTime);
    }
    
    function vote(uint256 proposalId, bool support) external onlyGovernance {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");
        
        proposal.hasVoted[msg.sender] = true;
        if (support) {
            proposal.yesVotes++;
        } else {
            proposal.noVotes++;
        }
        
        emit VoteCast(msg.sender, proposalId, support);
    }
    
    function executeProposal(uint256 proposalId) external nonReentrant {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalVotes = proposal.yesVotes + proposal.noVotes;
        uint256 quorum = (totalVotes * 100) / governanceMembers.length;
        
        require(quorum >= quorumThreshold, "Quorum not reached");
        require(proposal.yesVotes > proposal.noVotes, "Proposal not approved");
        
        uint256 amount = proposal.amount;
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient reward tokens");
        
        proposal.executed = true;
        rewardToken.approve(address(savingsContract), amount);
        savingsContract.distributeRewards(amount);
        
        lastDistributionTime = block.timestamp;
        emit ProposalExecuted(proposalId, amount);
        emit RewardDistributed(amount, block.timestamp);
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(rewardToken), "Cannot withdraw reward token");
        IERC20(token).transfer(owner(), amount);
    }
    
    function setDistributionInterval(uint256 newInterval) external onlyOwner {
        require(newInterval >= 1 days, "Interval too short");
        rewardDistributionInterval = newInterval;
    }
    
    function setMinDistributionAmount(uint256 newAmount) external onlyOwner {
        minDistributionAmount = newAmount;
    }
    
    function setQuorumThreshold(uint256 newThreshold) external onlyOwner {
        require(newThreshold > 0 && newThreshold <= 100, "Invalid threshold");
        quorumThreshold = newThreshold;
    }
    
    function getGovernanceMembers() external view returns (address[] memory) {
        return governanceMembers;
    }
    
    function getProposalVotes(uint256 proposalId) external view returns (uint256 yes, uint256 no) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.yesVotes, proposal.noVotes);
    }
}
```
