"""
Generated Code Metadata:
========================
Original URL: https://agora-next-8n06xjzv6-voteagora.vercel.app
Prompt: "Design a basic implementation of an on-chain governance system inspired by Agora’s features."
Generated: DETERMINISTIC_7dd518f0b6d0269a
Batch ID: 20250622_204951
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
 * @title OnChainGovernance
 * @dev A basic implementation of an on-chain governance system inspired by Agora
 */
contract OnChainGovernance {
    // Structs
    struct Proposal {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => bool) public members;
    address public owner;
    uint256 public minimumVotesForQuorum;
    uint256 public votingDuration;

    // Events
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string title,
        string description,
        uint256 duration
    );
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only members can perform this action");
        _;
    }

    modifier activeProposal(uint256 proposalId) {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.createTime + proposal.duration, "Voting period has ended");
        _;
    }

    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    constructor(uint256 _minimumVotesForQuorum, uint256 _votingDuration) {
        owner = msg.sender;
        members[msg.sender] = true;
        minimumVotesForQuorum = _minimumVotesForQuorum;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Add a new member to the governance system
     * @param _member Address of the new member
     */
    function addMember(address _member) external onlyOwner {
        require(!members[_member], "Address is already a member");
        members[_member] = true;
        emit MemberAdded(_member);
    }

    /**
     * @dev Remove a member from the governance system
     * @param _member Address of the member to remove
     */
    function removeMember(address _member) external onlyOwner {
        require(members[_member], "Address is not a member");
        members[_member] = false;
        emit MemberRemoved(_member);
    }

    /**
     * @dev Create a new proposal
     * @param _title Title of the proposal
     * @param _description Description of the proposal
     */
    function createProposal(
        string memory _title,
        string memory _description
    ) external onlyMember {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.title = _title;
        newProposal.description = _description;
        newProposal.createTime = block.timestamp;
        newProposal.duration = votingDuration;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            _title,
            _description,
            votingDuration
        );
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _support Boolean indicating support (true) or opposition (false)
     */
    function vote(
        uint256 _proposalId,
        bool _support
    ) external onlyMember activeProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voters[msg.sender] = true;

        if (_support) {
            proposal.forVotes += 1;
        } else {
            proposal.againstVotes += 1;
        }

        emit Voted(_proposalId, msg.sender, _support, 1);
    }

    /**
     * @dev Execute a proposal if it meets quorum and has majority support
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(
        uint256 _proposalId
    ) external onlyMember notExecuted(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(
            block.timestamp >= proposal.createTime + proposal.duration,
            "Voting period has not ended"
        );

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        require(
            totalVotes >= minimumVotesForQuorum,
            "Quorum not reached"
        );
        require(
            proposal.forVotes > proposal.againstVotes,
            "Majority support not reached"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Update the minimum votes required for quorum
     * @param _newQuorum New quorum value
     */
    function updateQuorum(uint256 _newQuorum) external onlyOwner {
        minimumVotesForQuorum = _newQuorum;
    }

    /**
     * @dev Update the default voting duration
     * @param _newDuration New duration in seconds
     */
    function updateVotingDuration(uint256 _newDuration) external onlyOwner {
        votingDuration = _newDuration;
    }
}
```
