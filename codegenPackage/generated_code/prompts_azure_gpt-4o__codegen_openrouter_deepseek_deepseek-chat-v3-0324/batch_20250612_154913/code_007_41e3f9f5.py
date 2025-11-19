"""
Generated Code Metadata:
========================
Original URL: https://pabshq.com
Prompt: Develop a smart contract in Solidity for a voting system where $PABS token holders can vote on community-driven initiatives, aligning with the "Community Driven" ethos of Pabs HQ.
Generated: DETERMINISTIC_41e3f9f537cef397
Batch ID: 20250612_154913
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

contract PabsVoting is Ownable {
    IERC20 public pabsToken;

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
    uint256 public votingDuration = 3 days;

    event ProposalCreated(uint256 indexed id, string description, uint256 voteEnd);
    event Voted(uint256 indexed proposalId, address indexed voter, bool vote);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _pabsToken) {
        pabsToken = IERC20(_pabsToken);
    }

    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteEnd = block.timestamp + votingDuration;
        newProposal.yesVotes = 0;
        newProposal.noVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description, newProposal.voteEnd);
    }

    function vote(uint256 _proposalId, bool _vote) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period has ended");
        require(!proposal.voters[msg.sender], "Already voted");
        require(pabsToken.balanceOf(msg.sender) > 0, "No PABS tokens");

        uint256 voteWeight = pabsToken.balanceOf(msg.sender);
        
        if (_vote) {
            proposal.yesVotes += voteWeight;
        } else {
            proposal.noVotes += voteWeight;
        }

        proposal.voters[msg.sender] = true;
        emit Voted(_proposalId, msg.sender, _vote);
    }

    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting still ongoing");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingDuration(uint256 _duration) external onlyOwner {
        require(_duration >= 1 days, "Duration too short");
        votingDuration = _duration;
    }

    function getProposalVotes(uint256 _proposalId) external view returns (uint256 yes, uint256 no) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.yesVotes, proposal.noVotes);
    }

    function hasVoted(uint256 _proposalId, address _voter) external view returns (bool) {
        return proposals[_proposalId].voters[_voter];
    }
}
```
