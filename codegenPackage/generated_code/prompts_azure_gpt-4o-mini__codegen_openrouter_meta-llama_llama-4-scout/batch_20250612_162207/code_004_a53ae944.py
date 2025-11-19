"""
Generated Code Metadata:
========================
Original URL: https://chaindigital.pages.dev
Prompt: Provide an example of how to implement a DAO voting mechanism in a smart contract, inspired by the Popcorn DAO mentioned on the Chain Digital webpage.
Generated: DETERMINISTIC_a53ae944d5208b79
Batch ID: 20250612_162207
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Popcorn DAO Voting Mechanism
 * @author [Your Name]
 * @notice A simple DAO voting mechanism inspired by Popcorn DAO
 */
contract PopcornDAO {
    using SafeMath for uint256;

    // Mapping of users to their voting power
    mapping(address => uint256) public userVotingPower;

    // Mapping of proposals to their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of users to their votes
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // Total number of proposals
    uint256 public totalProposals;

    // Quorum required for a proposal to pass
    uint256 public quorum;

    // Minimum voting power required to propose
    uint256 public minVotingPower;

    // Token used for voting power
    IERC20 public votingToken;

    /**
     * @notice Event emitted when a new proposal is created
     * @param proposalId ID of the proposal
     * @param creator Address of the proposal creator
     * @param description Description of the proposal
     */
    event NewProposal(uint256 proposalId, address creator, string description);

    /**
     * @notice Event emitted when a user votes on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address of the voter
     * @param vote Whether the user voted for (true) or against (false) the proposal
     */
    event VoteCast(uint256 proposalId, address voter, bool vote);

    /**
     * @notice Event emitted when a proposal is executed
     * @param proposalId ID of the proposal
     */
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Struct representing a proposal
     */
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @notice Constructor for the Popcorn DAO contract
     * @param _votingToken Address of the token used for voting power
     * @param _quorum Quorum required for a proposal to pass
     * @param _minVotingPower Minimum voting power required to propose
     */
    constructor(
        address _votingToken,
        uint256 _quorum,
        uint256 _minVotingPower
    ) public {
        votingToken = IERC20(_votingToken);
        quorum = _quorum;
        minVotingPower = _minVotingPower;
    }

    /**
     * @notice Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public {
        require(
            userVotingPower[msg.sender] >= minVotingPower,
            "User does not have sufficient voting power to propose"
        );

        Proposal memory proposal;
        proposal.id = totalProposals;
        proposal.creator = msg.sender;
        proposal.description = _description;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposals[totalProposals] = proposal;
        totalProposals++;

        emit NewProposal(proposal.id, proposal.creator, proposal.description);
    }

    /**
     * @notice Casts a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote Whether to vote for (true) or against (false) the proposal
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        require(
            proposals[_proposalId].executed == false,
            "Proposal has already been executed"
        );

        Proposal storage proposal = proposals[_proposalId];

        // Check if user has already voted
        require(userVotes[msg.sender][_proposalId] == false, "User has already voted");

        // Update user's vote
        userVotes[msg.sender][_proposalId] = true;

        // Update proposal votes
        if (_vote) {
            proposal.yesVotes = proposal.yesVotes.add(userVotingPower[msg.sender]);
        } else {
            proposal.noVotes = proposal.noVotes.add(userVotingPower[msg.sender]);
        }

        emit VoteCast(_proposalId, msg.sender, _vote);

        // Check if proposal has reached quorum
        if (
            proposal.yesVotes.add(proposal.noVotes) >= quorum &&
            proposal.yesVotes > proposal.noVotes
        ) {
            executeProposal(_proposalId);
        }
    }

    /**
     * @notice Executes a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) internal {
        Proposal storage proposal = proposals[_proposalId];

        // Check if proposal has not been executed before
        require(proposal.executed == false, "Proposal has already been executed");

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Updates a user's voting power
     * @param _user Address of the user
     * @param _votingPower New voting power of the user
     */
    function updateVotingPower(address _user, uint256 _votingPower) public {
        // Only the owner can update voting power
        require(msg.sender == owner(), "Only the owner can update voting power");

        userVotingPower[_user] = _votingPower;
    }

    /**
     * @notice Gets the voting power of a user
     * @param _user Address of the user
     * @return Voting power of the user
     */
    function getVotingPower(address _user) public view returns (uint256) {
        return userVotingPower[_user];
    }
}
```
