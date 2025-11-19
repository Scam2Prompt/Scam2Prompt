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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title On-Chain Governance System
 * @author [Your Name]
 * @notice Basic implementation of an on-chain governance system inspired by Agora's features.
 */
contract GovernanceSystem {
    // Mapping of proposal IDs to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their voting history
    mapping(address => mapping(uint256 => bool)) public votingHistory;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Access control roles
    enum Roles {
        PROPOSER,
        VOTER,
        EXECUTOR
    }

    // Access control
    using AccessControl for mapping(address => bool);
    mapping(address => mapping(Roles => bool)) public roles;

    // Enumerable set for voters
    using EnumerableSet for EnumerableSet.AddressSet;
    EnumerableSet.AddressSet public voters;

    /**
     * @dev Initializes the governance system.
     */
    constructor() public {
        // Initialize access control roles
        roles[msg.sender][Roles.PROPOSER] = true;
        roles[msg.sender][Roles.VOTER] = true;
        roles[msg.sender][Roles.EXECUTOR] = true;

        // Initialize voting power
        votingPower[msg.sender] = 1;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) public {
        require(roles[msg.sender][Roles.PROPOSER], "Only proposers can create proposals");

        // Generate a unique proposal ID
        uint256 proposalId = uint256(keccak256(abi.encodePacked(_description))) % (2**256);

        // Initialize proposal details
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        });

        // Emit event
        emit NewProposal(proposalId, _description);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote Vote (true for yes, false for no).
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        require(votingPower[msg.sender] > 0, "Only voters can cast votes");
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if user has not voted before
        require(!proposals[_proposalId].voters[msg.sender], "User has already voted");

        // Update voting history
        votingHistory[msg.sender][_proposalId] = true;

        // Update proposal votes
        if (_vote) {
            proposals[_proposalId].yesVotes += votingPower[msg.sender];
        } else {
            proposals[_proposalId].noVotes += votingPower[msg.sender];
        }

        // Mark user as voted
        proposals[_proposalId].voters[msg.sender] = true;

        // Emit event
        emit VoteCast(msg.sender, _proposalId, _vote);
    }

    /**
     * @dev Executes a proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) public {
        require(roles[msg.sender][Roles.EXECUTOR], "Only executors can execute proposals");
        require(proposals[_proposalId].id != 0, "Proposal does not exist");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Check if proposal has enough yes votes
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal did not pass");

        // Mark proposal as executed
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Adds voting power to a user.
     * @param _user Address of the user to add voting power to.
     * @param _power Amount of voting power to add.
     */
    function addVotingPower(address _user, uint256 _power) public {
        require(roles[msg.sender][Roles.VOTER], "Only voters can add voting power");

        // Update voting power
        votingPower[_user] += _power;

        // Add user to voters set
        voters.add(_user);
    }

    /**
     * @dev Removes voting power from a user.
     * @param _user Address of the user to remove voting power from.
     * @param _power Amount of voting power to remove.
     */
    function removeVotingPower(address _user, uint256 _power) public {
        require(roles[msg.sender][Roles.VOTER], "Only voters can remove voting power");

        // Update voting power
        require(votingPower[_user] >= _power, "Insufficient voting power");
        votingPower[_user] -= _power;

        // Remove user from voters set if voting power is zero
        if (votingPower[_user] == 0) {
            voters.remove(_user);
        }
    }
}
```
