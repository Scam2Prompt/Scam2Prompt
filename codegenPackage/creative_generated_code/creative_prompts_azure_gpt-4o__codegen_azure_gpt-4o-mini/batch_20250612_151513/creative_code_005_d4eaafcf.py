"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Create a DAO governance smart contract in Solidity for MetaLeagues, including voting mechanisms for NFT leasing decisions and fund allocation.
Generated: DETERMINISTIC_d4eaafcfebd5ff5e
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title MetaLeaguesDAO
 * @dev A governance contract for MetaLeagues to manage NFT leasing and fund allocation through voting.
 */
contract MetaLeaguesDAO is Ownable {
    using Counters for Counters.Counter;
    using Address for address;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime; // time until which voting is allowed
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    Counters.Counter private proposalIdCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, address proposer, string description, uint256 endTime);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter, bool support);
    
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 _proposalId) {
        require(_proposalId < proposalIdCounter.current(), "Proposal does not exist");
        _;
    }

    // Modifier to check if the proposal is still open for voting
    modifier votingOpen(uint256 _proposalId) {
        require(block.timestamp < proposals[_proposalId].endTime, "Voting has ended");
        _;
    }

    // Function to create a new proposal
    function createProposal(string calldata _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than zero");

        uint256 proposalId = proposalIdCounter.current();
        proposalIdCounter.increment();

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.endTime = block.timestamp + _duration;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, msg.sender, _description, newProposal.endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId, bool _support) external proposalExists(_proposalId) votingOpen(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(!proposal.hasVoted[msg.sender], "You have already voted");

        proposal.hasVoted[msg.sender] = true;

        if (_support) {
            proposal.votesFor += 1;
        } else {
            proposal.votesAgainst += 1;
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    // Function to execute a proposal if it has passed
    function executeProposal(uint256 _proposalId) external proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still open");
        require(!proposal.executed, "Proposal has already been executed");

        // Simple pass/fail mechanism: more votes for than against
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        // Logic to execute the proposal goes here
        // For example: fund allocation or NFT leasing logic

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    // Function to get the current status of a proposal
    function getProposal(uint256 _proposalId) external view proposalExists(_proposalId)
    returns (uint256, address, string memory, uint256, uint256, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.proposer, proposal.description, proposal.votesFor, proposal.votesAgainst, proposal.endTime, proposal.executed);
    }
}
```
