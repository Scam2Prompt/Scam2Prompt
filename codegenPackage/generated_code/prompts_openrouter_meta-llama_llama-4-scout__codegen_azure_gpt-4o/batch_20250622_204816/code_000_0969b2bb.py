"""
Generated Code Metadata:
========================
Original URL: https://kelpdao-protocol.xyz
Prompt: "Write a smart contract for a basic DAO protocol."
Generated: DETERMINISTIC_0969b2bb57eb5843
Batch ID: 20250622_204816
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
 * @title DAOContract
 * @dev A basic DAO protocol allowing members to propose and vote on decisions.
 */
contract DAOContract {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping to track members of the DAO
    mapping(address => bool) public members;

    // Array to store all proposals
    Proposal[] public proposals;

    // Mapping to track votes for each proposal
    mapping(uint256 => mapping(address => bool)) public votes;

    // Address of the contract owner
    address public owner;

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to DAO members
    modifier onlyMember() {
        require(members[msg.sender], "Not a DAO member");
        _;
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the DAO contract.
     * @param _members Initial list of DAO members.
     */
    constructor(address[] memory _members) {
        owner = msg.sender;
        for (uint256 i = 0; i < _members.length; i++) {
            members[_members[i]] = true;
        }
    }

    /**
     * @dev Add a new member to the DAO.
     * @param _member Address of the new member.
     */
    function addMember(address _member) external onlyOwner {
        require(!members[_member], "Already a member");
        members[_member] = true;
    }

    /**
     * @dev Remove a member from the DAO.
     * @param _member Address of the member to remove.
     */
    function removeMember(address _member) external onlyOwner {
        require(members[_member], "Not a member");
        members[_member] = false;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyMember {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyMember {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!votes[_proposalId][msg.sender], "Already voted");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        votes[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount += 1;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has enough votes.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyMember {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[_proposalId].executed, "Proposal already executed");
        require(proposals[_proposalId].voteCount > (getMemberCount() / 2), "Not enough votes");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get the total number of members in the DAO.
     * @return The number of members.
     */
    function getMemberCount() public view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < proposals.length; i++) {
            if (members[address(uint160(i))]) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Get the total number of proposals.
     * @return The number of proposals.
     */
    function getProposalCount() public view returns (uint256) {
        return proposals.length;
    }
}
```
