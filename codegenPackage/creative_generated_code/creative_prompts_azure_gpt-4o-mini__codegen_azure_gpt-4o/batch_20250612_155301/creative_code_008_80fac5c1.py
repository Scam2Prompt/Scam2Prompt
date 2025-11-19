"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Describe how to build a decentralized autonomous organization (DAO) on Ethereum and provide a sample code structure.
Generated: DETERMINISTIC_80fac5c158e3fc82
Batch ID: 20250612_155301
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

/**
 * @title Decentralized Autonomous Organization (DAO)
 * @notice A simple DAO smart contract that allows members to propose and vote on actions.
 * @dev This contract is simplified to demonstrate the structure and functionality of a DAO.
 */
contract DAO {
    // Struct representing a single proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes in favor
        bool executed; // Whether the proposal has been executed
        uint256 deadline; // Deadline for voting
    }

    // List of all proposals
    Proposal[] public proposals;

    // Mapping to track which address is a member
    mapping(address => bool) public members;

    // Mapping to track whether a member has voted on a given proposal
    mapping(uint256 => mapping(address => bool)) public votes;

    // Owner of the DAO contract
    address public owner;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @notice Modifier to restrict access to DAO members
     */
    modifier onlyMembers() {
        require(members[msg.sender], "Access restricted to DAO members");
        _;
    }

    /**
     * @notice Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    /**
     * @notice Constructor to initialize the DAO
     */
    constructor() {
        owner = msg.sender; // Set contract deployer as owner
        members[owner] = true; // Owner is the first member
    }

    /**
     * @notice Function to add a new member
     * @param _member Address of the new member
     */
    function addMember(address _member) external onlyOwner {
        require(!members[_member], "Address is already a member");
        members[_member] = true;
    }

    /**
     * @notice Function to create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of the voting period in seconds
     */
    function createProposal(string memory _description, uint256 _duration) external onlyMembers {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            executed: false,
            deadline: block.timestamp + _duration
        }));
        emit ProposalCreated(proposals.length - 1, _description, block.timestamp + _duration);
    }

    /**
     * @notice Function to vote on a proposal
     * @param _proposalId ID of the proposal
     */
    function vote(uint256 _proposalId) external onlyMembers {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!votes[_proposalId][msg.sender], "Member has already voted on this proposal");

        proposal.voteCount += 1; // Increase vote count
        votes[_proposalId][msg.sender] = true; // Mark voting as done
        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @notice Function to execute a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) external onlyMembers {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(block.timestamp >= proposal.deadline, "Voting period has not yet ended");

        // Simplified execution logic, only mark the proposal as executed
        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }
}
```
