"""
Generated Code Metadata:
========================
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate code for setting up a DAO (Decentralized Autonomous Organization) for NFT holders, similar to the "Cats World" roadmap phase 2.
Generated: DETERMINISTIC_dff6dd56dfb223c0
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract NFTDAO is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;
    
    IERC721 public nftContract;
    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;
    uint256 public quorumPercentage = 10; // 10% of total NFT holders required
    
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }
    
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    EnumerableSet.AddressSet private nftHolders;
    
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 voteEnd);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }
    
    modifier onlyNFTHolder() {
        require(nftContract.balanceOf(msg.sender) > 0, "Not an NFT holder");
        _;
    }
    
    function createProposal(string memory _description) external onlyNFTHolder {
        uint256 voteEnd = block.timestamp + votingPeriod;
        proposalCount++;
        
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            description: _description,
            voteEnd: voteEnd,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, msg.sender, _description, voteEnd);
    }
    
    function vote(uint256 _proposalId, bool _support) external onlyNFTHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        
        uint256 votingPower = nftContract.balanceOf(msg.sender);
        
        if (_support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }
        
        hasVoted[_proposalId][msg.sender] = true;
        emit VoteCast(msg.sender, _proposalId, _support, votingPower);
    }
    
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting not ended");
        require(!proposal.executed, "Already executed");
        
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 totalHolders = nftContract.totalSupply();
        uint256 quorum = (totalHolders * quorumPercentage) / 100;
        
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");
        
        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }
    
    function updateVotingPeriod(uint256 _newVotingPeriod) external onlyOwner {
        require(_newVotingPeriod >= 1 days && _newVotingPeriod <= 14 days, "Invalid voting period");
        votingPeriod = _newVotingPeriod;
    }
    
    function updateQuorumPercentage(uint256 _newQuorumPercentage) external onlyOwner {
        require(_newQuorumPercentage > 0 && _newQuorumPercentage <= 100, "Invalid quorum percentage");
        quorumPercentage = _newQuorumPercentage;
    }
    
    function isNFTHolder(address _address) public view returns (bool) {
        return nftContract.balanceOf(_address) > 0;
    }
    
    function getProposal(uint256 _proposalId) public view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 voteEnd,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.voteEnd,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }
}
```
