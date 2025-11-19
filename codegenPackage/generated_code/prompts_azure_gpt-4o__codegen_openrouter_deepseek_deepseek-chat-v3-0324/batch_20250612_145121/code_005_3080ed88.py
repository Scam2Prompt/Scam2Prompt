"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: Provide an example of a governance voting smart contract in Solidity that allows LOOKS token holders to propose and vote on platform changes, similar to LooksRare's governance model.
Generated: DETERMINISTIC_3080ed88a3a3e9c2
Batch ID: 20250612_145121
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

contract LooksGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public looksToken;

    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        string description;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    uint256 public votingDelay = 1;
    uint256 public votingPeriod = 17280; // ~3 days in blocks (assuming 15s block time)
    uint256 public proposalThreshold = 100000 * 10**18; // 100k LOOKS required to propose

    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(
        uint256 id,
        address proposer,
        uint256 startBlock,
        uint256 endBlock,
        string description
    );
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    constructor(address _looksToken) {
        looksToken = IERC20(_looksToken);
    }

    function propose(string memory _description) external returns (uint256) {
        require(
            looksToken.balanceOf(msg.sender) >= proposalThreshold,
            "LooksGovernance::propose: proposer votes below proposal threshold"
        );

        uint256 startBlock = block.number.add(votingDelay);
        uint256 endBlock = startBlock.add(votingPeriod);

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.startBlock = startBlock;
        newProposal.endBlock = endBlock;
        newProposal.description = _description;

        emit ProposalCreated(
            newProposal.id,
            msg.sender,
            startBlock,
            endBlock,
            _description
        );

        return newProposal.id;
    }

    function vote(uint256 _proposalId, bool _support) external {
        require(
            proposals[_proposalId].startBlock <= block.number,
            "LooksGovernance::vote: voting not started"
        );
        require(
            proposals[_proposalId].endBlock >= block.number,
            "LooksGovernance::vote: voting already ended"
        );
        require(
            !proposals[_proposalId].hasVoted[msg.sender],
            "LooksGovernance::vote: already voted"
        );

        uint256 votes = looksToken.balanceOf(msg.sender);
        require(votes > 0, "LooksGovernance::vote: no votes");

        Proposal storage proposal = proposals[_proposalId];
        proposal.hasVoted[msg.sender] = true;

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(votes);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votes);
        }

        emit VoteCast(msg.sender, _proposalId, _support, votes);
    }

    function executeProposal(uint256 _proposalId) external {
        require(
            proposals[_proposalId].endBlock < block.number,
            "LooksGovernance::executeProposal: voting not ended"
        );
        require(
            !proposals[_proposalId].executed,
            "LooksGovernance::executeProposal: already executed"
        );

        Proposal storage proposal = proposals[_proposalId];
        require(
            proposal.forVotes > proposal.againstVotes,
            "LooksGovernance::executeProposal: proposal failed"
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

    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            uint256 startBlock,
            uint256 endBlock,
            uint256 forVotes,
            uint256 againstVotes,
            string memory description,
            bool executed
        )
    {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.startBlock,
            proposal.endBlock,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.description,
            proposal.executed
        );
    }
}
```
