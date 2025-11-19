"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: Develop a voting system in Solidity for a decentralized governance model like Pushd, where token holders can propose and vote on platform changes.
Generated: DETERMINISTIC_128f23c5d690f61f
Batch ID: 20250612_151232
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Voting System Contract for Decentralized Governance
 * @author [Your Name]
 * @notice This contract enables token holders to propose and vote on platform changes.
 */
contract VotingSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their vote history
    mapping(address => mapping(uint256 => bool)) public voteHistory;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // IERC20 token instance for voting power
    IERC20 public token;

    // Minimum voting power required to create a proposal
    uint256 public minVotingPower;

    // Proposal ID counter
    uint256 public proposalIdCounter;

    /**
     * @notice Initializes the voting system contract
     * @param _token IERC20 token instance for voting power
     * @param _minVotingPower Minimum voting power required to create a proposal
     */
    constructor(IERC20 _token, uint256 _minVotingPower) {
        token = _token;
        minVotingPower = _minVotingPower;
        proposalIdCounter = 0;
    }

    /**
     * @notice Creates a new proposal
     * @param _description Proposal description
     * @return uint256 The ID of the newly created proposal
     */
    function createProposal(string memory _description) public returns (uint256) {
        require(votingPower[msg.sender] >= minVotingPower, "Insufficient voting power");

        Proposal memory proposal;
        proposal.id = proposalIdCounter;
        proposal.description = _description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(30 days);
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposals[proposalIdCounter] = proposal;

        emit ProposalCreated(proposalIdCounter, _description);

        proposalIdCounter++;

        return proposal.id;
    }

    /**
     * @notice Votes on a proposal
     * @param _proposalId The ID of the proposal to vote on
     * @param _support Whether to support (true) or oppose (false) the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].startTime != 0, "Proposal does not exist");
        require(proposals[_proposalId].endTime > block.timestamp, "Voting period has ended");
        require(!voteHistory[msg.sender][_proposalId], "User has already voted");

        if (_support) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(votingPower[msg.sender]);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(votingPower[msg.sender]);
        }

        voteHistory[msg.sender][_proposalId] = true;

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @notice Executes a proposal if it has passed
     * @param _proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].endTime <= block.timestamp, "Voting period has not ended");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal did not pass");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Updates the voting power of a user
     * @param _user The address of the user
     * @param _power The new voting power of the user
     */
    function updateVotingPower(address _user, uint256 _power) public onlyOwner {
        votingPower[_user] = _power;
    }

    /**
     * @notice Updates the minimum voting power required to create a proposal
     * @param _power The new minimum voting power
     */
    function updateMinVotingPower(uint256 _power) public onlyOwner {
        minVotingPower = _power;
    }
}
```
