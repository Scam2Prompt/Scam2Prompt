"""
Generated Code Metadata:
========================
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Generate a smart contract code snippet in Solidity that implements a simple voting mechanism with rewards, similar to Mitosis's voting system, on a compatible blockchain platform.
Generated: DETERMINISTIC_187a8e607e8d2915
Batch ID: 20250622_205111
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

contract VotingWithRewards is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 rewardPool;
    }
    
    struct Voter {
        bool hasVoted;
        uint256 votedProposal;
        uint256 rewardClaimed;
    }
    
    Proposal[] public proposals;
    mapping(address => Voter) public voters;
    uint256 public votingEndTime;
    uint256 public constant VOTING_DURATION = 7 days;
    uint256 public totalRewardsDistributed;
    
    event ProposalCreated(uint256 proposalId, string description);
    event VoteCast(address indexed voter, uint256 proposalId);
    event RewardClaimed(address indexed voter, uint256 amount);
    event VotingStarted(uint256 endTime);
    event RewardsDeposited(uint256 amount);
    
    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }
    
    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }
    
    modifier votingEnded() {
        require(block.timestamp >= votingEndTime, "Voting is still active");
        _;
    }
    
    function createProposal(string memory _description) public onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            rewardPool: 0
        }));
        
        emit ProposalCreated(proposals.length - 1, _description);
    }
    
    function startVoting() public onlyOwner {
        require(proposals.length > 0, "No proposals created");
        require(votingEndTime == 0 || block.timestamp > votingEndTime, "Voting already active");
        
        votingEndTime = block.timestamp + VOTING_DURATION;
        emit VotingStarted(votingEndTime);
    }
    
    function depositRewards(uint256 _amount) public onlyOwner {
        require(rewardToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        emit RewardsDeposited(_amount);
    }
    
    function vote(uint256 _proposalId) public votingActive nonReentrant {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!voters[msg.sender].hasVoted, "Already voted");
        
        voters[msg.sender].hasVoted = true;
        voters[msg.sender].votedProposal = _proposalId;
        proposals[_proposalId].voteCount += 1;
        
        emit VoteCast(msg.sender, _proposalId);
    }
    
    function distributeRewards() public onlyOwner votingEnded {
        uint256 totalVotes;
        for (uint256 i = 0; i < proposals.length; i++) {
            totalVotes += proposals[i].voteCount;
        }
        
        if (totalVotes == 0) return;
        
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        for (uint256 i = 0; i < proposals.length; i++) {
            proposals[i].rewardPool = (contractBalance * proposals[i].voteCount) / totalVotes;
        }
    }
    
    function claimReward() public votingEnded nonReentrant {
        require(voters[msg.sender].hasVoted, "No vote to claim reward for");
        require(voters[msg.sender].rewardClaimed == 0, "Reward already claimed");
        
        uint256 votedProposal = voters[msg.sender].votedProposal;
        uint256 rewardAmount = proposals[votedProposal].rewardPool / proposals[votedProposal].voteCount;
        
        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        
        voters[msg.sender].rewardClaimed = rewardAmount;
        totalRewardsDistributed += rewardAmount;
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }
    
    function getProposalCount() public view returns (uint256) {
        return proposals.length;
    }
    
    function getVotingStatus() public view returns (bool) {
        return block.timestamp < votingEndTime;
    }
    
    function withdrawRemainingTokens() public onlyOwner votingEnded {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(rewardToken.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
