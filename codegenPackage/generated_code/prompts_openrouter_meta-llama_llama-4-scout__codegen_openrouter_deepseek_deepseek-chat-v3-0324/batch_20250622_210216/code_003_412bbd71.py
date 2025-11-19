"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Develop a simple smart contract in Solidity to manage the governance functionality of $QUBE tokens, allowing holders to propose and vote on platform decisions.
Generated: DETERMINISTIC_412bbd717bcc6742
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QubeGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public qubeToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public votingDelay;
    uint256 public votingPeriod;

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    constructor(address _qubeToken, uint256 _votingDelay, uint256 _votingPeriod) {
        qubeToken = IERC20(_qubeToken);
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
    }

    function propose(string memory _description) external returns (uint256) {
        require(qubeToken.balanceOf(msg.sender) > 0, "Must hold QUBE tokens to propose");
        
        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.createTime = block.timestamp.add(votingDelay);
        newProposal.endTime = newProposal.createTime.add(votingPeriod);
        newProposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            _description,
            newProposal.createTime,
            newProposal.endTime
        );
        return proposalId;
    }

    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.createTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");
        
        uint256 voterBalance = qubeToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;
        if (_support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, _proposalId, _support, voterBalance);
    }

    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingDelay(uint256 _votingDelay) external onlyOwner {
        votingDelay = _votingDelay;
    }

    function setVotingPeriod(uint256 _votingPeriod) external onlyOwner {
        votingPeriod = _votingPeriod;
    }
}
```
