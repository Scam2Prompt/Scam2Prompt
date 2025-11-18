"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Write a Solidity-based DAO smart contract that aligns with Quecko's Web3 development expertise and includes governance mechanisms.
Generated: DETERMINISTIC_579a2a2e8da10530
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title DAO Contract
 * @dev A decentralized autonomous organization (DAO) contract with basic governance mechanisms.
 * @author Quecko
 */
contract SimpleDAO {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Votes in favor of the proposal
        uint256 votesAgainst; // Votes against the proposal
        uint256 deadline;   // Voting deadline (timestamp)
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track voter participation per proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Role management
    address public chairperson;
    mapping(address => bool) public members;

    // Proposal counter
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId, bool success);

    // Modifier to restrict access to members only
    modifier onlyMembers() {
        require(members[msg.sender], "Access restricted to DAO members");
        _;
    }

    // Modifier to restrict access to the chairperson only
    modifier onlyChairperson() {
        require(msg.sender == chairperson, "Access restricted to chairperson");
        _;
    }

    /**
     * @dev Constructor to initialize the DAO
     * @param _chairperson Address of the chairperson
     */
    constructor(address _chairperson) {
        require(_chairperson != address(0), "Chairperson address cannot be zero");
        chairperson = _chairperson;
        members[_chairperson] = true; // Chairperson is automatically added as member
    }

    /**
     * @dev Function to add a new member to the DAO
     * @param _member Address of the new member
     */
    function addMember(address _member) external onlyChairperson {
        require(_member != address(0), "Member address cannot be zero");
        require(!members[_member], "Address is already a member");
        members[_member] = true;
    }

    /**
     * @dev Function to create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration (in seconds) for voting to remain open
     */
    function createProposal(string memory _description, uint256 _duration) external onlyMembers {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Voting duration must be greater than zero");

        uint256 proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, block.timestamp + _duration);
    }

    /**
     * @dev Function to cast a vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _support Boolean indicating vote support (true = for, false = against)
     */
    function vote(uint256 _proposalId, bool _support) external onlyMembers {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal if voting has ended
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyMembers {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Simple rule: proposal passes if votesFor > votesAgainst
        bool success = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Function to remove a member from the DAO
     * @param _member Address of the member to remove
     */
    function removeMember(address _member) external onlyChairperson {
        require(_member != address(0), "Member address cannot be zero");
        require(members[_member], "Address is not a member");
        members[_member] = false;
    }
}
```
