"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Create a Solidity smart contract for a decentralized autonomous organization (DAO) with voting functionality, following the guidelines from Ethereum.org.
Generated: DETERMINISTIC_44ed0d4944475425
Batch ID: 20250612_151948
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

/**
 * @title Decentralized Autonomous Organization (DAO) with Voting
 * @dev Implements a DAO where members can propose and vote on proposals
 */
contract DAO {
    // Structs
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
        address proposer;
    }

    // State variables
    mapping(address => bool) public members;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public votes;
    uint256 public proposalCount;
    uint256 public minimumVotesRequired;
    uint256 public votingPeriod;

    // Events
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed proposer);
    event VoteCast(address indexed voter, uint256 indexed proposalId);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifiers
    modifier onlyMember() {
        require(members[msg.sender], "Only members can call this function");
        _;
    }

    modifier onlyValidProposal(uint256 _proposalId) {
        require(_proposalId <= proposalCount && _proposalId > 0, "Invalid proposal ID");
        _;
    }

    modifier onlyActiveProposal(uint256 _proposalId) {
        require(block.timestamp <= proposals[_proposalId].deadline, "Voting period has ended");
        _;
    }

    modifier onlyAfterVoting(uint256 _proposalId) {
        require(block.timestamp > proposals[_proposalId].deadline, "Voting period is still active");
        _;
    }

    modifier onlyNotExecuted(uint256 _proposalId) {
        require(!proposals[_proposalId].executed, "Proposal already executed");
        _;
    }

    /**
     * @dev Constructor initializes the DAO with initial parameters
     * @param _minimumVotesRequired Minimum votes required for a proposal to pass
     * @param _votingPeriod Duration of voting period in seconds
     */
    constructor(uint256 _minimumVotesRequired, uint256 _votingPeriod) {
        minimumVotesRequired = _minimumVotesRequired;
        votingPeriod = _votingPeriod;
        // Add the deployer as the first member
        members[msg.sender] = true;
        emit MemberAdded(msg.sender);
    }

    /**
     * @dev Add a new member to the DAO
     * @param _member Address of the new member
     */
    function addMember(address _member) external onlyMember {
        require(!members[_member], "Address is already a member");
        members[_member] = true;
        emit MemberAdded(_member);
    }

    /**
     * @dev Remove a member from the DAO
     * @param _member Address of the member to remove
     */
    function removeMember(address _member) external onlyMember {
        require(members[_member], "Address is not a member");
        members[_member] = false;
        emit MemberRemoved(_member);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyMember {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            deadline: block.timestamp + votingPeriod,
            executed: false,
            proposer: msg.sender
        });
        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external onlyMember onlyValidProposal(_proposalId) onlyActiveProposal(_proposalId) {
        require(!votes[msg.sender][_proposalId], "Already voted on this proposal");
        
        votes[msg.sender][_proposalId] = true;
        proposals[_proposalId].voteCount++;
        
        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) 
        external 
        onlyMember 
        onlyValidProposal(_proposalId) 
        onlyAfterVoting(_proposalId) 
        onlyNotExecuted(_proposalId) 
    {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.voteCount >= minimumVotesRequired, "Not enough votes to execute");
        
        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
        
        // Here you would implement the actual proposal execution logic
        // For example: transfer funds, change DAO parameters, etc.
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 _proposalId) 
        external 
        view 
        onlyValidProposal(_proposalId) 
        returns (Proposal memory) 
    {
        return proposals[_proposalId];
    }
}
```
