"""
Generated Code Metadata:
========================
Original URL: https://shiba-3.web.app
Prompt: Write a Solidity contract that implements a community voting mechanism for Shiba 3.0 token holders to decide on future token upgrades or features.
Generated: DETERMINISTIC_6981508b1876c9cd
Batch ID: 20250612_151354
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

contract ShibaVoting is Ownable {
    using SafeMath for uint256;

    IERC20 public shibaToken;
    uint256 public minimumVotingPower;
    uint256 public proposalCount;
    uint256 public votingDuration;

    enum VoteOption { NONE, FOR, AGAINST }
    enum ProposalStatus { PENDING, ACTIVE, PASSED, REJECTED, EXECUTED }

    struct Proposal {
        uint256 id;
        string title;
        string description;
        address proposer;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 startTime;
        uint256 endTime;
        ProposalStatus status;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(uint256 => mapping(address => VoteOption)) public votes;

    event ProposalCreated(
        uint256 indexed id,
        string title,
        address indexed proposer,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        VoteOption vote,
        uint256 votingPower
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event VotingDurationUpdated(uint256 newDuration);
    event MinimumVotingPowerUpdated(uint256 newMinimum);

    constructor(address _shibaToken, uint256 _minimumVotingPower, uint256 _votingDuration) {
        require(_shibaToken != address(0), "Invalid token address");
        shibaToken = IERC20(_shibaToken);
        minimumVotingPower = _minimumVotingPower;
        votingDuration = _votingDuration;
    }

    function createProposal(string memory _title, string memory _description) external {
        uint256 balance = shibaToken.balanceOf(msg.sender);
        require(balance >= minimumVotingPower, "Insufficient voting power");

        proposalCount++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingDuration;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            proposer: msg.sender,
            forVotes: 0,
            againstVotes: 0,
            startTime: startTime,
            endTime: endTime,
            status: ProposalStatus.ACTIVE,
            executed: false
        });

        emit ProposalCreated(proposalCount, _title, msg.sender, startTime, endTime);
    }

    function vote(uint256 _proposalId, VoteOption _vote) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.status == ProposalStatus.ACTIVE, "Voting not active");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        uint256 votingPower = shibaToken.balanceOf(msg.sender);
        require(votingPower >= minimumVotingPower, "Insufficient voting power");

        hasVoted[_proposalId][msg.sender] = true;
        votes[_proposalId][msg.sender] = _vote;

        if (_vote == VoteOption.FOR) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else if (_vote == VoteOption.AGAINST) {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        }

        emit VoteCast(msg.sender, _proposalId, _vote, votingPower);
    }

    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.status == ProposalStatus.ACTIVE, "Proposal not active");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        if (proposal.forVotes > proposal.againstVotes && totalVotes > 0) {
            proposal.status = ProposalStatus.PASSED;
        } else {
            proposal.status = ProposalStatus.REJECTED;
        }

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration > 0, "Duration must be > 0");
        votingDuration = _newDuration;
        emit VotingDurationUpdated(_newDuration);
    }

    function setMinimumVotingPower(uint256 _newMinimum) external onlyOwner {
        minimumVotingPower = _newMinimum;
        emit MinimumVotingPowerUpdated(_newMinimum);
    }

    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory title,
        string memory description,
        address proposer,
        uint256 forVotes,
        uint256 againstVotes,
        uint256 startTime,
        uint256 endTime,
        ProposalStatus status,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.title,
            proposal.description,
            proposal.proposer,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.startTime,
            proposal.endTime,
            proposal.status,
            proposal.executed
        );
    }

    function getUserVote(uint256 _proposalId, address _voter) external view returns (VoteOption) {
        return votes[_proposalId][_voter];
    }
}
```
