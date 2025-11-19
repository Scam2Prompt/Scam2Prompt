"""
Generated Code Metadata:
========================
Original URL: https://ghsttoken.co
Prompt: Design a basic smart contract on Ethereum that utilizes GHST tokens for governance voting, similar to the AavegotchiDAO.
Generated: DETERMINISTIC_0b6abc9a49793ca5
Batch ID: 20250622_212139
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

contract GHSTGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public ghstToken;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    Proposal[] public proposals;
    uint256 public proposalCount;
    uint256 public minimumVotingPower;
    uint256 public votingDuration;

    event ProposalCreated(uint256 id, string description, uint256 startTime, uint256 endTime);
    event VoteCast(address indexed voter, uint256 proposalId, uint256 votes);
    event ProposalExecuted(uint256 id);

    constructor(address _ghstTokenAddress, uint256 _minimumVotingPower, uint256 _votingDuration) {
        ghstToken = IERC20(_ghstTokenAddress);
        minimumVotingPower = _minimumVotingPower;
        votingDuration = _votingDuration;
    }

    function createProposal(string memory _description) public onlyOwner {
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(votingDuration);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        proposalCount++;

        emit ProposalCreated(newProposal.id, _description, startTime, endTime);
    }

    function vote(uint256 _proposalId) public {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.voters[msg.sender], "Already voted");
        
        uint256 votingPower = ghstToken.balanceOf(msg.sender);
        require(votingPower >= minimumVotingPower, "Insufficient voting power");

        proposal.voteCount = proposal.voteCount.add(votingPower);
        proposal.voters[msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId, votingPower);
    }

    function executeProposal(uint256 _proposalId) public onlyOwner {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes cast");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    function setMinimumVotingPower(uint256 _minimumVotingPower) public onlyOwner {
        minimumVotingPower = _minimumVotingPower;
    }

    function setVotingDuration(uint256 _votingDuration) public onlyOwner {
        votingDuration = _votingDuration;
    }

    function getProposalCount() public view returns (uint256) {
        return proposalCount;
    }

    function hasVoted(uint256 _proposalId, address _voter) public view returns (bool) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        return proposals[_proposalId].voters[_voter];
    }
}
```
