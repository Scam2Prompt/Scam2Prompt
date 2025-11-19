"""
Generated Code Metadata:
========================
Original URL: https://defikingdoms.pages.dev
Prompt: "Propose a system for implementing governance votes in DeFi Kingdoms using blockchain-based voting mechanisms."
Generated: DETERMINISTIC_9b0cf6ebfda1e3c2
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GovernanceVote
 * @author [Your Name]
 * @notice A blockchain-based voting mechanism for DeFi Kingdoms governance votes.
 */
contract GovernanceVote is Ownable {
    using SafeMath for uint256;

    // Mapping of voters to their voting power
    mapping(address => uint256) public voterPower;

    // Mapping of proposals to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voters to their votes on proposals
    mapping(address => mapping(uint256 => bool)) public voterVotes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a voter casts a vote
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votingPowerRequired;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Mapping to keep track of proposal IDs
    uint256 public proposalCount;

    // Address of the token used for voting power
    IERC20 public votingToken;

    /**
     * @notice Initializes the GovernanceVote contract.
     * @param _votingToken Address of the token used for voting power.
     */
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
        proposalCount = 0;
    }

    /**
     * @notice Creates a new proposal.
     * @param _description Description of the proposal.
     * @param _votingPowerRequired Voting power required for the proposal to pass.
     */
    function createProposal(string memory _description, uint256 _votingPowerRequired) public onlyOwner {
        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.description = _description;
        proposal.votingPowerRequired = _votingPowerRequired;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposals[proposal.id] = proposal;

        emit NewProposal(proposal.id, proposal.description);

        proposalCount++;
    }

    /**
     * @notice Casts a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote True for yes, false for no.
     */
    function castVote(uint256 _proposalId, bool _vote) public {
        // Check if the proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        // Check if the voter has voting power
        require(voterPower[msg.sender] > 0, "Voter has no voting power");

        // Check if the voter has not already voted
        require(!voterVotes[msg.sender][_proposalId], "Voter has already voted");

        // Update the voter's voting power
        voterVotes[msg.sender][_proposalId] = true;

        // Update the proposal's vote count
        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(voterPower[msg.sender]);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(voterPower[msg.sender]);
        }

        emit VoteCast(msg.sender, _proposalId, _vote);

        // Check if the proposal has passed
        if (proposals[_proposalId].yesVotes >= proposals[_proposalId].votingPowerRequired) {
            executeProposal(_proposalId);
        }
    }

    /**
     * @notice Executes a proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) internal {
        // Check if the proposal exists and has not been executed
        require(proposals[_proposalId].id != 0, "Proposal does not exist");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Mark the proposal as executed
        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Sets the voting power of an address.
     * @param _address Address to set voting power for.
     * @param _power Voting power to set.
     */
    function setVoterPower(address _address, uint256 _power) public onlyOwner {
        voterPower[_address] = _power;
    }

    /**
     * @notice Updates the voting power required for a proposal.
     * @param _proposalId ID of the proposal to update.
     * @param _newVotingPowerRequired New voting power required.
     */
    function updateVotingPowerRequired(uint256 _proposalId, uint256 _newVotingPowerRequired) public onlyOwner {
        // Check if the proposal exists
        require(proposals[_proposalId].id != 0, "Proposal does not exist");

        proposals[_proposalId].votingPowerRequired = _newVotingPowerRequired;
    }
}
```
