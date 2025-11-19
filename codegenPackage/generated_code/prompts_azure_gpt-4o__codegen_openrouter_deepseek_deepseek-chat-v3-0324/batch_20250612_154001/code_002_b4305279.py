"""
Generated Code Metadata:
========================
Original URL: https://88bitkan.com
Prompt: Generate Solidity code for creating a smart contract that allows $WLFI token holders to propose and vote on changes to a decentralized finance platform.
Generated: DETERMINISTIC_b4305279fbc81447
Batch ID: 20250612_154001
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

contract WLFIGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public wlfiToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public votingDelay = 1 days;
    uint256 public votingPeriod = 3 days;
    uint256 public proposalThreshold = 1000 * 10**18; // 1000 WLFI tokens

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    constructor(address _wlfiToken) {
        wlfiToken = IERC20(_wlfiToken);
    }

    function propose(string memory _description) external {
        require(
            wlfiToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient WLFI balance to propose"
        );

        uint256 startTime = block.timestamp.add(votingDelay);
        uint256 endTime = startTime.add(votingPeriod);

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            newProposal.proposer,
            newProposal.description,
            newProposal.startTime,
            newProposal.endTime
        );
    }

    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Invalid proposal ID");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 voterBalance = wlfiToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No WLFI tokens to vote");

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
        require(proposal.id == _proposalId, "Invalid proposal ID");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal did not pass"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingDelay(uint256 _votingDelay) external onlyOwner {
        votingDelay = _votingDelay;
    }

    function setVotingPeriod(uint256 _votingPeriod) external onlyOwner {
        votingPeriod = _votingPeriod;
    }

    function setProposalThreshold(uint256 _proposalThreshold) external onlyOwner {
        proposalThreshold = _proposalThreshold;
    }
}
```
