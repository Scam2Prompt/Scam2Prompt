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
pragma solidity ^0.8.18;

/**
 * @title MetaLeaguesDAO
 * @dev A decentralized autonomous organization (DAO) contract for NFT leasing decisions and fund allocation governance.
 */
contract MetaLeaguesDAO {
    // Struct to represent a proposal
    struct Proposal {
        string description;         // Description of the proposal
        uint256 voteCountYes;       // Count of 'Yes' votes
        uint256 voteCountNo;        // Count of 'No' votes
        uint256 creationTime;       // Timestamp when the proposal was created
        bool executed;              // Flag to indicate if proposal has been executed
    }

    // Mapping to store proposals by proposal ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a given proposal
    mapping(uint256 => mapping(address => bool)) public votes;

    // Proposal counter
    uint256 public proposalCount;

    // Duration within which voting is allowed (e.g., 7 days)
    uint256 public votingDuration = 7 days;

    // Address of the DAO administrator
    address public admin;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 creationTime);
    event Voted(uint256 proposalId, address voter, bool vote);
    event ProposalExecuted(uint256 proposalId, string description, bool success);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    // Modifier to ensure proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    // Modifier to ensure voting is active for a proposal
    modifier votingActive(uint256 proposalId) {
        require(
            block.timestamp <= proposals[proposalId].creationTime + votingDuration,
            "Voting period has ended"
        );
        _;
    }

    // Constructor to initialize the DAO admin
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Create a new proposal.
     * @param _description A brief description of the proposal.
     */
    function createProposal(string calldata _description) external onlyAdmin {
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCountYes: 0,
            voteCountNo: 0,
            creationTime: block.timestamp,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, block.timestamp);
        proposalCount++;
    }

    /**
     * @dev Cast a vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _vote True for 'Yes', False for 'No'.
     */
    function vote(uint256 _proposalId, bool _vote)
        external
        proposalExists(_proposalId)
        votingActive(_proposalId)
    {
        require(!votes[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the vote
        votes[_proposalId][msg.sender] = true;

        // Update vote counts
        if (_vote) {
            proposals[_proposalId].voteCountYes++;
        } else {
            proposals[_proposalId].voteCountNo++;
        }

        emit Voted(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(
            block.timestamp > proposal.creationTime + votingDuration,
            "Voting period has not ended"
        );
        require(!proposal.executed, "Proposal has already been executed");

        // Mark the proposal as executed
        proposal.executed = true;

        // Determine the outcome and execute accordingly (placeholder logic)
        bool success = false;
        if (proposal.voteCountYes > proposal.voteCountNo) {
            // Logic for successful proposal execution (e.g., fund allocation)
            success = true;
        }

        emit ProposalExecuted(_proposalId, proposal.description, success);
    }

    /**
     * @dev Change the admin of the contract.
     * @param _newAdmin The address of the new admin.
     */
    function changeAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "New admin cannot be the zero address");
        admin = _newAdmin;
    }

    /**
     * @dev Change the voting duration.
     * @param _newDuration The new voting duration in seconds.
     */
    function setVotingDuration(uint256 _newDuration) external onlyAdmin {
        require(_newDuration > 0, "Voting duration must be greater than zero");
        votingDuration = _newDuration;
    }
}
```
