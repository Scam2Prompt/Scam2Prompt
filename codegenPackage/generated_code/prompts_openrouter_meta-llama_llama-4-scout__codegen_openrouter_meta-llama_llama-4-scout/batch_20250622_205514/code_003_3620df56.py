"""
Generated Code Metadata:
========================
Original URL: https://restore-tenon.pages.dev
Prompt: "Design a decentralized governance system for a DeFi protocol, incorporating blockchain aspects and decentralized decision-making processes."
Generated: DETERMINISTIC_3620df5642fb09a0
Batch ID: 20250622_205514
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Decentralized Governance System for DeFi Protocol
 * @author [Your Name]
 * @notice This contract implements a decentralized governance system for a DeFi protocol.
 */
contract DecentralizedGovernanceSystem {
    // Mapping of proposals to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of users to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of users to their voting history
    mapping(address => mapping(uint256 => bool)) public votingHistory;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votingStart;
        uint256 votingEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Access control roles
    bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");
    bytes32 public constant VOTER_ROLE = keccak256("VOTER_ROLE");

    // Enumerable set of proposers
    using EnumerableSet for EnumerableSet.AddressSet;
    EnumerableSet.AddressSet private proposers;

    // Enumerable set of voters
    using EnumerableSet for EnumerableSet.AddressSet;
    EnumerableSet.AddressSet private voters;

    // Token used for voting power
    ERC20 public token;

    /**
     * @notice Initializes the decentralized governance system
     * @param _token Address of the token used for voting power
     */
    constructor(ERC20 _token) {
        token = _token;

        // Initialize access control roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(PROPOSER_ROLE, msg.sender);
        _grantRole(VOTER_ROLE, msg.sender);
    }

    /**
     * @notice Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public onlyRole(PROPOSER_ROLE) {
        uint256 proposalId = uint256(keccak256(abi.encodePacked(_description))) % (2**256);

        // Initialize proposal details
        Proposal memory proposal;
        proposal.id = proposalId;
        proposal.description = _description;
        proposal.votingStart = block.timestamp;
        proposal.votingEnd = block.timestamp + 30 days;
        proposal.executed = false;

        // Store proposal details
        proposals[proposalId] = proposal;

        // Emit event
        emit NewProposal(proposalId, _description);
    }

    /**
     * @notice Votes on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Vote (true for yes, false for no)
     */
    function vote(uint256 _proposalId, bool _vote) public {
        // Check if user has voting power
        require(votingPower[msg.sender] > 0, "User has no voting power");

        // Check if user has not voted before
        require(!votingHistory[msg.sender][_proposalId], "User has already voted");

        // Update voting history
        votingHistory[msg.sender][_proposalId] = true;

        // Update proposal votes
        if (_vote) {
            proposals[_proposalId].yesVotes += votingPower[msg.sender];
        } else {
            proposals[_proposalId].noVotes += votingPower[msg.sender];
        }

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @notice Executes a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        // Check if proposal has ended
        require(proposals[_proposalId].votingEnd < block.timestamp, "Proposal has not ended");

        // Check if proposal has not been executed
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Check if proposal has been approved
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal has not been approved");

        // Mark proposal as executed
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Grants voting power to a user
     * @param _user Address of the user
     * @param _amount Amount of voting power
     */
    function grantVotingPower(address _user, uint256 _amount) public onlyRole(DEFAULT_ADMIN_ROLE) {
        votingPower[_user] += _amount;
    }

    /**
     * @notice Revokes voting power from a user
     * @param _user Address of the user
     * @param _amount Amount of voting power
     */
    function revokeVotingPower(address _user, uint256 _amount) public onlyRole(DEFAULT_ADMIN_ROLE) {
        require(votingPower[_user] >= _amount, "Insufficient voting power");
        votingPower[_user] -= _amount;
    }

    /**
     * @notice Adds a proposer
     * @param _proposer Address of the proposer
     */
    function addProposer(address _proposer) public onlyRole(DEFAULT_ADMIN_ROLE) {
        proposers.add(_proposer);
        _grantRole(PROPOSER_ROLE, _proposer);
    }

    /**
     * @notice Removes a proposer
     * @param _proposer Address of the proposer
     */
    function removeProposer(address _proposer) public onlyRole(DEFAULT_ADMIN_ROLE) {
        proposers.remove(_proposer);
        _revokeRole(PROPOSER_ROLE, _proposer);
    }

    /**
     * @notice Adds a voter
     * @param _voter Address of the voter
     */
    function addVoter(address _voter) public onlyRole(DEFAULT_ADMIN_ROLE) {
        voters.add(_voter);
        _grantRole(VOTER_ROLE, _voter);
    }

    /**
     * @notice Removes a voter
     * @param _voter Address of the voter
     */
    function removeVoter(address _voter) public onlyRole(DEFAULT_ADMIN_ROLE) {
        voters.remove(_voter);
        _revokeRole(VOTER_ROLE, _voter);
    }
}
```
