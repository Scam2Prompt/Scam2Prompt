"""
Generated Code Metadata:
========================
Original URL: https://shinoberryinu.pages.dev
Prompt: Generate Solidity code for a governance voting system that aligns with Shinoberry Inu's mission of community-driven decision-making. Include functionality for token holders to vote on proposals using $SHINO tokens.
Generated: DETERMINISTIC_2ff82e99ca5cc212
Batch ID: 20250612_145711
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

contract ShinoberryGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public shinoToken;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public votingPeriod = 3 days;
    uint256 public quorumPercentage = 10; // 10% of total supply required

    event ProposalCreated(uint256 indexed id, string description, uint256 voteEnd);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed id);

    constructor(address _shinoToken) {
        shinoToken = IERC20(_shinoToken);
    }

    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.description = _description;
        proposal.voteEnd = block.timestamp + votingPeriod;
        proposal.executed = false;

        emit ProposalCreated(proposalCount, _description, proposal.voteEnd);
    }

    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period has ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 voterBalance = shinoToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        proposal.voters[msg.sender] = true;

        if (_support) {
            proposal.yesVotes = proposal.yesVotes.add(voterBalance);
        } else {
            proposal.noVotes = proposal.noVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, _proposalId, _support, voterBalance);
    }

    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.yesVotes.add(proposal.noVotes);
        uint256 totalSupply = shinoToken.totalSupply();
        require(totalVotes >= totalSupply.mul(quorumPercentage).div(100), "Quorum not reached");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    function setVotingPeriod(uint256 _newPeriod) external onlyOwner {
        require(_newPeriod >= 1 days && _newPeriod <= 14 days, "Invalid voting period");
        votingPeriod = _newPeriod;
    }

    function setQuorumPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Invalid quorum percentage");
        quorumPercentage = _newPercentage;
    }

    function getProposalVotes(uint256 _proposalId) external view returns (uint256 yesVotes, uint256 noVotes) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.yesVotes, proposal.noVotes);
    }
}
```
