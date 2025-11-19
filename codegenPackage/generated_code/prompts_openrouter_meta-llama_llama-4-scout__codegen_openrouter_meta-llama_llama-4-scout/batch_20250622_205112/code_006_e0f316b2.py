"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Design a DAO structure for a community-driven web3 project, allowing users to govern themselves and make key decisions about the project's direction.
Generated: DETERMINISTIC_e0f316b2fcc06833
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Governance DAO
 * @author [Your Name]
 * @notice Decentralized Autonomous Organization (DAO) for community-driven governance
 */
contract GovernanceDAO is AccessControl {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Mapping of proposal IDs to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user votes
    mapping(uint256 => mapping(address => bool)) public votes;

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
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        address[] voters;
    }

    // Role for proposers
    bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");

    // Role for voters
    bytes32 public constant VOTER_ROLE = keccak256("VOTER_ROLE");

    // Total voting power
    uint256 public totalVotingPower;

    // Token used for voting power
    IERC20 public token;

    /**
     * @dev Initializes the GovernanceDAO contract
     * @param _token Address of the token used for voting power
     */
    constructor(IERC20 _token) {
        // Set token used for voting power
        token = _token;

        // Set proposer and voter roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(PROPOSER_ROLE, msg.sender);
        _grantRole(VOTER_ROLE, msg.sender);
    }

    /**
     * @dev Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public onlyRole(PROPOSER_ROLE) {
        // Create a new proposal
        Proposal memory proposal;
        proposal.id = uint256(keccak256(abi.encodePacked(_description, block.timestamp)));
        proposal.description = _description;
        proposals[proposal.id] = proposal;

        // Emit event
        emit NewProposal(proposal.id, _description);
    }

    /**
     * @dev Casts a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Vote (true for yes, false for no)
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        // Check if user has voting power
        require(votingPower[msg.sender] > 0, "User has no voting power");

        // Check if proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if user has not already voted
        require(!votes[_proposalId][msg.sender], "User has already voted");

        // Update user's vote
        votes[_proposalId][msg.sender] = _vote;

        // Update proposal votes
        if (_vote) {
            proposals[_proposalId].yesVotes += votingPower[msg.sender];
        } else {
            proposals[_proposalId].noVotes += votingPower[msg.sender];
        }

        // Add voter to proposal
        proposals[_proposalId].voters.push(msg.sender);

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Executes a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        // Check if proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if proposal has not been executed
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Check if proposal has sufficient yes votes
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal did not pass");

        // Execute proposal
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Sets the voting power of a user
     * @param _user Address of the user
     * @param _power Voting power of the user
     */
    function setVotingPower(address _user, uint256 _power) public onlyRole(DEFAULT_ADMIN_ROLE) {
        // Update user's voting power
        votingPower[_user] = _power;

        // Update total voting power
        totalVotingPower += _power;
    }

    /**
     * @dev Grants a role to a user
     * @param _user Address of the user
     * @param _role Role to grant
     */
    function grantRole(bytes32 _role, address _user) public override onlyRole(DEFAULT_ADMIN_ROLE) {
        _grantRole(_role, _user);
    }

    /**
     * @dev Revokes a role from a user
     * @param _user Address of the user
     * @param _role Role to revoke
     */
    function revokeRole(bytes32 _role, address _user) public override onlyRole(DEFAULT_ADMIN_ROLE) {
        _revokeRole(_role, _user);
    }
}
```
