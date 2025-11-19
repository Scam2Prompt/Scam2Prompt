"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Create a Solidity smart contract example that integrates with MDEX's DAO governance mechanism to enable voting on community proposals using xMDX vouchers.
Generated: DETERMINISTIC_52b2316bb51ce059
Batch ID: 20250612_145823
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IxMDX {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract MDEXGovernance is Ownable, ReentrancyGuard {
    IxMDX public xMDXToken;

    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        address proposer;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;
    uint256 public proposalThreshold;

    event ProposalCreated(
        uint256 indexed id,
        string title,
        string description,
        uint256 endTime,
        address proposer
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _xMDXToken, uint256 _proposalThreshold) {
        xMDXToken = IxMDX(_xMDXToken);
        proposalThreshold = _proposalThreshold;
    }

    function createProposal(
        string memory _title,
        string memory _description
    ) external {
        uint256 xMDXBalance = xMDXToken.balanceOf(msg.sender);
        require(xMDXBalance >= proposalThreshold, "Insufficient xMDX balance");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            createTime: block.timestamp,
            endTime: block.timestamp + votingPeriod,
            forVotes: 0,
            againstVotes: 0,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(
            proposalCount,
            _title,
            _description,
            block.timestamp + votingPeriod,
            msg.sender
        );
    }

    function vote(uint256 _proposalId, bool _support) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp <= proposal.endTime, "Voting period ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        
        uint256 voterBalance = xMDXToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No xMDX balance");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.forVotes += voterBalance;
        } else {
            proposal.againstVotes += voterBalance;
        }

        emit VoteCast(msg.sender, _proposalId, _support, voterBalance);
    }

    function executeProposal(uint256 _proposalId) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        proposal.executed = true;
        
        emit ProposalExecuted(_proposalId);
    }

    function setVotingPeriod(uint256 _newVotingPeriod) external onlyOwner {
        require(_newVotingPeriod > 0, "Invalid voting period");
        votingPeriod = _newVotingPeriod;
    }

    function setProposalThreshold(uint256 _newThreshold) external onlyOwner {
        proposalThreshold = _newThreshold;
    }

    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory title,
        string memory description,
        uint256 createTime,
        uint256 endTime,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed,
        address proposer
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.title,
            proposal.description,
            proposal.createTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed,
            proposal.proposer
        );
    }
}
```
