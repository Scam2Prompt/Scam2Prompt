"""
Generated Code Metadata:
========================
Original URL: https://magahatvip.pages.dev
Prompt: Write a Solidity smart contract for a meme token inspired by MAGA ($MAGA) with features like 0% tax and community-driven governance.
Generated: DETERMINISTIC_53a5745b12863ef6
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract MAGAToken is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Community governance variables
    EnumerableSet.AddressSet private _governanceMembers;
    uint256 public proposalCount;
    uint256 public quorumPercentage = 10; // 10% of total supply required for quorum
    uint256 public votingPeriod = 3 days;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        address proposer;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    event ProposalCreated(uint256 indexed proposalId, address indexed proposer);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);
    event ProposalExecuted(uint256 indexed proposalId);
    event GovernanceMemberAdded(address indexed member);
    event GovernanceMemberRemoved(address indexed member);

    constructor() ERC20("MAGA Token", "MAGA") {
        _mint(msg.sender, 1000000000 * 10 ** decimals()); // 1 billion tokens
    }

    // Governance functions
    function addGovernanceMember(address member) external onlyOwner {
        require(!_governanceMembers.contains(member), "Already a governance member");
        _governanceMembers.add(member);
        emit GovernanceMemberAdded(member);
    }

    function removeGovernanceMember(address member) external onlyOwner {
        require(_governanceMembers.contains(member), "Not a governance member");
        _governanceMembers.remove(member);
        emit GovernanceMemberRemoved(member);
    }

    function isGovernanceMember(address member) public view returns (bool) {
        return _governanceMembers.contains(member);
    }

    function getGovernanceMembers() public view returns (address[] memory) {
        return _governanceMembers.values();
    }

    function createProposal(string memory description) external {
        require(isGovernanceMember(msg.sender), "Only governance members can create proposals");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteStart: block.timestamp,
            voteEnd: block.timestamp + votingPeriod,
            forVotes: 0,
            againstVotes: 0,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalCount, msg.sender);
    }

    function vote(uint256 proposalId, bool support) external {
        require(isGovernanceMember(msg.sender), "Only governance members can vote");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(block.timestamp >= proposals[proposalId].voteStart, "Voting not started");
        require(block.timestamp <= proposals[proposalId].voteEnd, "Voting ended");
        
        hasVoted[proposalId][msg.sender] = true;
        
        if (support) {
            proposals[proposalId].forVotes += balanceOf(msg.sender);
        } else {
            proposals[proposalId].againstVotes += balanceOf(msg.sender);
        }

        emit VoteCast(msg.sender, proposalId, support);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(block.timestamp > proposal.voteEnd, "Voting not ended");
        
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 quorum = (totalSupply() * quorumPercentage) / 100;
        
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Override transfer functions to ensure 0% tax
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
