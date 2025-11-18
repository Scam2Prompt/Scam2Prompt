"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Write a Solidity contract to implement a governance system for $ETFS token holders, including voting rights on platform updates, as described in ETFSwap's tokenomics.
Generated: DETERMINISTIC_47b149896837fb63
Batch ID: 20250612_153401
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

contract ETFSGovernance {
    // Token holder structure
    struct Member {
        uint256 votingPower; // Voting power of the member
        bool isMember;       // Whether address is a member
    }

    // Proposal structure
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Count of votes for the proposal
        mapping(address => bool) voted; // Track if an address has voted
        bool executed; // Status of proposal execution
    }

    // State variables
    mapping(address => Member) public members; // Mapping of members
    Proposal[] public proposals; // Array of proposals
    address public admin; // Admin address
    uint256 public proposalCount; // Counter for proposals

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(address voter, uint256 proposalId);
    event ProposalExecuted(uint256 proposalId);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier onlyMembers() {
        require(members[msg.sender].isMember, "Only members can vote");
        _;
    }

    constructor() {
        admin = msg.sender; // Set the deployer as the admin
    }

    // Function to add a new member
    function addMember(address _member, uint256 _votingPower) external onlyAdmin {
        require(!members[_member].isMember, "Member already exists");
        members[_member] = Member({
            votingPower: _votingPower,
            isMember: true
        });
    }

    // Function to create a new proposal
    function createProposal(string calldata _description) external onlyMembers {
        proposalCount++;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;

        emit ProposalCreated(newProposal.id, newProposal.description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external onlyMembers {
        require(_proposalId > 0 && _proposalId <= proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        require(!proposal.voted[msg.sender], "Already voted on this proposal");

        proposal.voted[msg.sender] = true;
        proposal.voteCount += members[msg.sender].votingPower;

        emit Voted(msg.sender, _proposalId);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external onlyAdmin {
        require(_proposalId > 0 && _proposalId <= proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        require(!proposal.executed, "Proposal already executed");

        // Placeholder for actual implementation of proposal execution
        // require(proposal.voteCount > requiredVotes, "Not enough votes");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    // Function to remove a member
    function removeMember(address _member) external onlyAdmin {
        require(members[_member].isMember, "Member does not exist");
        delete members[_member];
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, bool) {
        require(_proposalId > 0 && _proposalId <= proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId - 1];
        
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
