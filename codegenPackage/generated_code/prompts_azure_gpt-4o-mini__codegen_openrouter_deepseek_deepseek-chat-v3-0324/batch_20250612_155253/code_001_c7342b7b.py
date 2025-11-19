"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Write a code snippet that allows members to stake cryptocurrency in a POC-DAO and vote on commitment levels.
Generated: DETERMINISTIC_c7342b7b77178006
Batch ID: 20250612_155253
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

contract POCDAO is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    
    struct Commitment {
        uint256 amount;
        uint256 level;
        uint256 voteWeight;
    }
    
    struct Proposal {
        string description;
        uint256[] commitmentLevels;
        uint256[] votes;
        uint256 endTime;
        bool executed;
    }
    
    mapping(address => Commitment) public commitments;
    mapping(address => uint256) public lastStakeTime;
    Proposal[] public proposals;
    
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant MAX_COMMITMENT_LEVEL = 3;
    
    event Staked(address indexed user, uint256 amount, uint256 commitmentLevel);
    event Unstaked(address indexed user, uint256 amount);
    event ProposalCreated(uint256 proposalId, string description, uint256[] commitmentLevels);
    event Voted(address indexed user, uint256 proposalId, uint256 commitmentLevel);
    event ProposalExecuted(uint256 proposalId);
    
    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }
    
    function stake(uint256 _amount, uint256 _commitmentLevel) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_commitmentLevel > 0 && _commitmentLevel <= MAX_COMMITMENT_LEVEL, "Invalid commitment level");
        
        commitments[msg.sender].amount += _amount;
        commitments[msg.sender].level = _commitmentLevel;
        commitments[msg.sender].voteWeight = _amount * _commitmentLevel;
        lastStakeTime[msg.sender] = block.timestamp;
        
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );
        
        emit Staked(msg.sender, _amount, _commitmentLevel);
    }
    
    function unstake() external nonReentrant {
        require(commitments[msg.sender].amount > 0, "No stake to withdraw");
        require(
            block.timestamp >= lastStakeTime[msg.sender] + MIN_STAKE_DURATION,
            "Minimum stake duration not met"
        );
        
        uint256 amount = commitments[msg.sender].amount;
        delete commitments[msg.sender];
        
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        
        emit Unstaked(msg.sender, amount);
    }
    
    function createProposal(
        string memory _description,
        uint256[] memory _commitmentLevels,
        uint256 _duration
    ) external onlyOwner {
        require(_commitmentLevels.length > 0, "No commitment levels provided");
        for (uint256 i = 0; i < _commitmentLevels.length; i++) {
            require(
                _commitmentLevels[i] > 0 && _commitmentLevels[i] <= MAX_COMMITMENT_LEVEL,
                "Invalid commitment level"
            );
        }
        
        proposals.push(Proposal({
            description: _description,
            commitmentLevels: _commitmentLevels,
            votes: new uint256[](_commitmentLevels.length),
            endTime: block.timestamp + _duration,
            executed: false
        }));
        
        emit ProposalCreated(proposals.length - 1, _description, _commitmentLevels);
    }
    
    function vote(uint256 _proposalId, uint256 _commitmentLevelIndex) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp < proposal.endTime, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");
        require(
            _commitmentLevelIndex < proposal.commitmentLevels.length,
            "Invalid commitment level index"
        );
        
        Commitment storage userCommitment = commitments[msg.sender];
        require(userCommitment.amount > 0, "No stake to vote with");
        
        proposal.votes[_commitmentLevelIndex] += userCommitment.voteWeight;
        
        emit Voted(msg.sender, _proposalId, proposal.commitmentLevels[_commitmentLevelIndex]);
    }
    
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        proposal.executed = true;
        
        emit ProposalExecuted(_proposalId);
    }
    
    function getWinningCommitmentLevel(uint256 _proposalId) external view returns (uint256) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        uint256 maxVotes = 0;
        uint256 winningIndex = 0;
        
        for (uint256 i = 0; i < proposal.votes.length; i++) {
            if (proposal.votes[i] > maxVotes) {
                maxVotes = proposal.votes[i];
                winningIndex = i;
            }
        }
        
        return proposal.commitmentLevels[winningIndex];
    }
}
```
