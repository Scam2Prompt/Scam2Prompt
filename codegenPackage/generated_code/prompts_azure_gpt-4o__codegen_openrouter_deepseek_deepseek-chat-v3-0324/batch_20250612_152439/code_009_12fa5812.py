"""
Generated Code Metadata:
========================
Original URL: https://peaq-token.pages.dev
Prompt: Develop a dApp prototype that leverages the peaq token for Machine Subsidies, allowing users to propose and vote on new machines within the ecosystem.
Generated: DETERMINISTIC_12fa5812fb76b97f
Batch ID: 20250612_152439
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract MachineSubsidy is Ownable {
    using Counters for Counters.Counter;
    
    IERC20 public peaqToken;
    
    struct MachineProposal {
        uint256 id;
        address proposer;
        string machineDetails;
        uint256 subsidyAmount;
        uint256 voteStartTime;
        uint256 voteEndTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }
    
    struct Vote {
        bool hasVoted;
        bool support;
        uint256 voteWeight;
    }
    
    Counters.Counter private _proposalIds;
    mapping(uint256 => MachineProposal) public proposals;
    mapping(uint256 => mapping(address => Vote)) public votes;
    mapping(address => uint256) public votingPower;
    
    uint256 public constant MIN_VOTING_DURATION = 1 days;
    uint256 public constant MIN_SUBSIDY_AMOUNT = 100 * 10**18; // 100 PEAQ tokens
    
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string machineDetails,
        uint256 subsidyAmount,
        uint256 voteStartTime,
        uint256 voteEndTime
    );
    
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 voteWeight
    );
    
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _peaqToken) {
        peaqToken = IERC20(_peaqToken);
    }
    
    function createProposal(
        string memory _machineDetails,
        uint256 _subsidyAmount,
        uint256 _voteDuration
    ) external {
        require(_subsidyAmount >= MIN_SUBSIDY_AMOUNT, "Subsidy amount too low");
        require(_voteDuration >= MIN_VOTING_DURATION, "Voting duration too short");
        
        _proposalIds.increment();
        uint256 proposalId = _proposalIds.current();
        
        proposals[proposalId] = MachineProposal({
            id: proposalId,
            proposer: msg.sender,
            machineDetails: _machineDetails,
            subsidyAmount: _subsidyAmount,
            voteStartTime: block.timestamp,
            voteEndTime: block.timestamp + _voteDuration,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        });
        
        emit ProposalCreated(
            proposalId,
            msg.sender,
            _machineDetails,
            _subsidyAmount,
            block.timestamp,
            block.timestamp + _voteDuration
        );
    }
    
    function vote(uint256 _proposalId, bool _support) external {
        MachineProposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.voteStartTime, "Voting not started");
        require(block.timestamp <= proposal.voteEndTime, "Voting ended");
        require(!proposal.executed, "Proposal already executed");
        
        Vote storage userVote = votes[_proposalId][msg.sender];
        require(!userVote.hasVoted, "Already voted");
        
        uint256 userVotingPower = peaqToken.balanceOf(msg.sender);
        require(userVotingPower > 0, "No voting power");
        
        userVote.hasVoted = true;
        userVote.support = _support;
        userVote.voteWeight = userVotingPower;
        
        if (_support) {
            proposal.yesVotes += userVotingPower;
        } else {
            proposal.noVotes += userVotingPower;
        }
        
        emit Voted(_proposalId, msg.sender, _support, userVotingPower);
    }
    
    function executeProposal(uint256 _proposalId) external {
        MachineProposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.voteEndTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalVotes = proposal.yesVotes + proposal.noVotes;
        require(totalVotes > 0, "No votes cast");
        
        if (proposal.yesVotes > proposal.noVotes) {
            require(
                peaqToken.transfer(proposal.proposer, proposal.subsidyAmount),
                "Token transfer failed"
            );
        }
        
        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }
    
    function setPeaqToken(address _peaqToken) external onlyOwner {
        peaqToken = IERC20(_peaqToken);
    }
    
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory machineDetails,
        uint256 subsidyAmount,
        uint256 voteStartTime,
        uint256 voteEndTime,
        uint256 yesVotes,
        uint256 noVotes,
        bool executed
    ) {
        MachineProposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        
        return (
            proposal.id,
            proposal.proposer,
            proposal.machineDetails,
            proposal.subsidyAmount,
            proposal.voteStartTime,
            proposal.voteEndTime,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.executed
        );
    }
}
```
