"""
Generated Code Metadata:
========================
Original URL: https://ghsttoken.co
Prompt: Design a basic smart contract on Ethereum that utilizes GHST tokens for governance voting, similar to the AavegotchiDAO.
Generated: DETERMINISTIC_0b6abc9a49793ca5
Batch ID: 20250622_212139
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GHST Governance Contract
 * @author [Your Name]
 * @notice A basic smart contract for governance voting using GHST tokens.
 */
contract GHSTGovernance {
    // Mapping of user voting power
    mapping (address => uint256) public votingPower;

    // Mapping of proposal votes
    mapping (uint256 => mapping (address => bool)) public proposalVotes;

    // Mapping of proposal details
    mapping (uint256 => Proposal) public proposals;

    // GHST token contract
    IERC20 public ghstToken;

    // Access control for contract
    using AccessControl for GHSTGovernance;

    // Roles
    bytes32 public constant GOVERNOR_ROLE = keccak256("GOVERNOR_ROLE");

    // Safe math library
    using SafeMath for uint256;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct for proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
    }

    /**
     * @dev Initializes the contract
     * @param _ghstTokenAddress Address of the GHST token contract
     */
    constructor(address _ghstTokenAddress) public {
        // Set GHST token contract
        ghstToken = IERC20(_ghstTokenAddress);

        // Set governor role
        _setupRole(GOVERNOR_ROLE, msg.sender);
    }

    /**
     * @dev Creates a new proposal
     * @param _proposalDescription Description of the proposal
     */
    function createProposal(string memory _proposalDescription) public {
        // Only governors can create proposals
        require(hasRole(GOVERNOR_ROLE, msg.sender), "Only governors can create proposals");

        // Create new proposal
        uint256 proposalId = proposals.length;
        proposals[proposalId] = Proposal(proposalId, _proposalDescription, 0, false);

        // Emit event
        emit NewProposal(proposalId, _proposalDescription);
    }

    /**
     * @dev Votes on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Vote (true for yes, false for no)
     */
    function vote(uint256 _proposalId, bool _vote) public {
        // Only users with voting power can vote
        require(votingPower[msg.sender] > 0, "Only users with voting power can vote");

        // Check if user has already voted
        require(!proposalVotes[_proposalId][msg.sender], "User has already voted");

        // Get proposal details
        Proposal memory proposal = proposals[_proposalId];

        // Update user's vote
        proposalVotes[_proposalId][msg.sender] = _vote;

        // Update proposal vote count
        if (_vote) {
            proposals[_proposalId].voteCount = proposal.voteCount.add(1);
        } else {
            proposals[_proposalId].voteCount = proposal.voteCount.sub(1);
        }

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Executes a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        // Only governors can execute proposals
        require(hasRole(GOVERNOR_ROLE, msg.sender), "Only governors can execute proposals");

        // Get proposal details
        Proposal memory proposal = proposals[_proposalId];

        // Check if proposal has been executed
        require(!proposal.executed, "Proposal has already been executed");

        // Check if proposal has sufficient votes
        require(proposal.voteCount > 0, "Proposal must have sufficient votes");

        // Execute proposal
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Adds voting power to a user
     * @param _user Address of the user
     * @param _amount Amount of voting power to add
     */
    function addVotingPower(address _user, uint256 _amount) public {
        // Only governors can add voting power
        require(hasRole(GOVERNOR_ROLE, msg.sender), "Only governors can add voting power");

        // Transfer GHST tokens to user
        require(ghstToken.transfer(_user, _amount), "GHST token transfer failed");

        // Update user's voting power
        votingPower[_user] = votingPower[_user].add(_amount);
    }

    /**
     * @dev Removes voting power from a user
     * @param _user Address of the user
     * @param _amount Amount of voting power to remove
     */
    function removeVotingPower(address _user, uint256 _amount) public {
        // Only governors can remove voting power
        require(hasRole(GOVERNOR_ROLE, msg.sender), "Only governors can remove voting power");

        // Check if user has sufficient voting power
        require(votingPower[_user] >= _amount, "User does not have sufficient voting power");

        // Update user's voting power
        votingPower[_user] = votingPower[_user].sub(_amount);
    }
}
```
