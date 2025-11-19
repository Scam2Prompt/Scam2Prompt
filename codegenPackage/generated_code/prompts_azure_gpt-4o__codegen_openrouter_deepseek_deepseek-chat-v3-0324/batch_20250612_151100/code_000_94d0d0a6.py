"""
Generated Code Metadata:
========================
Original URL: https://testtt-ba0.pages.dev
Prompt: Write a smart contract in Solidity for managing WOOL tokens, including functionality for governance voting and token transfers, as described in the Wolf Game ecosystem.
Generated: DETERMINISTIC_94d0d0a6e5aab099
Batch ID: 20250612_151100
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WOOL is ERC20, ERC20Snapshot, Ownable {
    using SafeMath for uint256;

    // Governance variables
    struct Proposal {
        uint256 id;
        string description;
        uint256 deadline;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) voters;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public votingPeriod = 3 days;
    uint256 public minimumQuorum = 1000 * 10**18; // 1000 WOOL required for quorum

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 deadline);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);
    event ProposalExecuted(uint256 indexed proposalId);
    event VotingPeriodUpdated(uint256 newVotingPeriod);
    event MinimumQuorumUpdated(uint256 newMinimumQuorum);

    constructor() ERC20("WOOL", "WOOL") {
        _mint(msg.sender, 100000000 * 10**18); // 100M initial supply
    }

    // Token functions
    function snapshot() public onlyOwner {
        _snapshot();
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    // Governance functions
    function createProposal(string memory _description) public onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.deadline = block.timestamp.add(votingPeriod);
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description, newProposal.deadline);
    }

    function vote(uint256 _proposalId, bool _support) public {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!proposal.voters[msg.sender], "Already voted");
        require(balanceOf(msg.sender) > 0, "No voting power");

        uint256 votingPower = balanceOf(msg.sender);
        proposal.voters[msg.sender] = true;

        if (_support) {
            proposal.votesFor = proposal.votesFor.add(votingPower);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(votingPower);
        }

        emit VoteCast(msg.sender, _proposalId, _support);
    }

    function executeProposal(uint256 _proposalId) public onlyOwner {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.votesFor.add(proposal.votesAgainst);
        require(totalVotes >= minimumQuorum, "Quorum not reached");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function setVotingPeriod(uint256 _newVotingPeriod) public onlyOwner {
        require(_newVotingPeriod > 0, "Voting period must be positive");
        votingPeriod = _newVotingPeriod;
        emit VotingPeriodUpdated(_newVotingPeriod);
    }

    function setMinimumQuorum(uint256 _newMinimumQuorum) public onlyOwner {
        require(_newMinimumQuorum > 0, "Quorum must be positive");
        minimumQuorum = _newMinimumQuorum;
        emit MinimumQuorumUpdated(_newMinimumQuorum);
    }

    // Override required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
