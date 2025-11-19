"""
Generated Code Metadata:
========================
Original URL: https://chaingpt-app.pages.dev
Prompt: Generate a Solidity smart contract for a DAO governance system using ChainGPT's Smart Contract Generator.
Generated: DETERMINISTIC_b4f11c2db643b05e
Batch ID: 20250612_154642
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DAO Governance System
 * @author [Your Name]
 * @notice This contract provides a basic governance system for a DAO.
 */
contract DAOGovernance {
    // Using SafeMath for uint256
    using SafeMath for uint256;

    // Mapping of members and their voting power
    mapping(address => uint256) public members;

    // Mapping of proposals and their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of votes cast by members
    mapping(uint256 => mapping(address => Vote)) public votes;

    // Proposal counters
    uint256 public proposalCount;
    uint256 public votingPeriod;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed proposer, string description);

    // Event emitted when a member votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Struct to represent a vote
    struct Vote {
        bool support;
        bool isValid;
    }

    /**
     * @notice Constructor for the DAOGovernance contract
     * @param _votingPeriod The duration of the voting period in blocks
     */
    constructor(uint256 _votingPeriod) public {
        votingPeriod = _votingPeriod;
    }

    /**
     * @notice Add a new member to the DAO
     * @param _member The address of the new member
     * @param _votingPower The voting power of the new member
     */
    function addMember(address _member, uint256 _votingPower) public onlyOwner {
        members[_member] = _votingPower;
    }

    /**
     * @notice Create a new proposal
     * @param _description The description of the proposal
     */
    function createProposal(string memory _description) public {
        require(members[msg.sender] > 0, "Only members can create proposals");

        Proposal memory proposal;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.startBlock = block.number;
        proposal.endBlock = block.number.add(votingPeriod);
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposalCount++;
        proposals[proposalCount] = proposal;

        emit NewProposal(proposalCount, msg.sender, _description);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param _proposalId The ID of the proposal
     * @param _support Whether to support the proposal
     */
    function castVote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].startBlock > 0, "Proposal does not exist");
        require(proposals[_proposalId].endBlock > block.number, "Voting period has ended");
        require(votes[_proposalId][msg.sender].isValid == false, "Already voted");

        Proposal storage proposal = proposals[_proposalId];
        if (_support) {
            proposal.yesVotes = proposal.yesVotes.add(members[msg.sender]);
        } else {
            proposal.noVotes = proposal.noVotes.add(members[msg.sender]);
        }

        votes[_proposalId][msg.sender] = Vote(_support, true);

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId The ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].endBlock < block.number, "Voting period has not ended");
        require(proposals[_proposalId].executed == false, "Proposal already executed");

        Proposal storage proposal = proposals[_proposalId];
        if (proposal.yesVotes > proposal.noVotes) {
            // Execute the proposal
            proposal.executed = true;

            emit ProposalExecuted(_proposalId);
        }
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
