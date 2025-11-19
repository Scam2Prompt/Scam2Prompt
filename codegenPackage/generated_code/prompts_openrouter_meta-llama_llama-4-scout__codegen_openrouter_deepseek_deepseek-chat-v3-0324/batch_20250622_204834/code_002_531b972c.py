"""
Generated Code Metadata:
========================
Original URL: https://agora-next-exdgz5djw-voteagora.vercel.app
Prompt: Generate a proposal voting system using Agora's on-chain governance features.
Generated: DETERMINISTIC_531b972ca7da9479
Batch ID: 20250622_204834
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ProposalVotingSystem is Ownable {
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    IERC20 public votingToken;
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => uint256)) public votes;
    mapping(address => uint256) public voterStakes;

    event ProposalCreated(uint256 indexed id, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 amount);
    event ProposalExecuted(uint256 indexed id);
    event VotingPeriodUpdated(uint256 newPeriod);
    event QuorumUpdated(uint256 newQuorum);

    constructor(address _votingToken, uint256 _votingPeriod, uint256 _quorumPercentage) {
        require(_votingToken != address(0), "Invalid token address");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        
        votingToken = IERC20(_votingToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }

    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingPeriod;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, startTime, endTime);
    }

    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be > 0");
        require(votingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        voterStakes[msg.sender] += _amount;
    }

    function unstakeTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be > 0");
        require(voterStakes[msg.sender] >= _amount, "Insufficient stake");

        voterStakes[msg.sender] -= _amount;
        require(votingToken.transfer(msg.sender, _amount), "Transfer failed");
    }

    function vote(uint256 _proposalId, uint256 _amount) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.executed, "Proposal already executed");
        require(_amount > 0, "Amount must be > 0");
        require(voterStakes[msg.sender] >= _amount, "Insufficient stake");

        votes[_proposalId][msg.sender] += _amount;
        proposal.voteCount += _amount;
        
        emit Voted(_proposalId, msg.sender, _amount);
    }

    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalSupply = votingToken.totalSupply();
        uint256 quorum = (totalSupply * quorumPercentage) / 100;
        require(proposal.voteCount >= quorum, "Quorum not reached");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingPeriod(uint256 _newPeriod) external onlyOwner {
        require(_newPeriod > 0, "Period must be > 0");
        votingPeriod = _newPeriod;
        emit VotingPeriodUpdated(_newPeriod);
    }

    function setQuorumPercentage(uint256 _newQuorum) external onlyOwner {
        require(_newQuorum <= 100, "Quorum must be <= 100");
        quorumPercentage = _newQuorum;
        emit QuorumUpdated(_newQuorum);
    }

    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteCount,
        uint256 startTime,
        uint256 endTime,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];
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
