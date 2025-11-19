"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Develop a voting system in Solidity for the Puff Puff Pandas DAO that allows holders to propose and vote on community initiatives using $PUFFS tokens.
Generated: DETERMINISTIC_b6bd1d1b43d613c0
Batch ID: 20250612_152235
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
 * @title PuffPuffPandasDAO
 * @author Puff Puff Pandas DAO
 * @notice A voting system for the Puff Puff Pandas DAO
 */
contract PuffPuffPandasDAO is Ownable {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal details
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

    // Token used for voting power
    IERC20 public token;

    // Minimum voting power required to propose
    uint256 public minVotingPowerToPropose;

    // Minimum voting power required to vote
    uint256 public minVotingPowerToVote;

    // Quorum required for a proposal to pass
    uint256 public quorum;

    // Proposal ID counter
    uint256 public proposalIdCounter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        uint256 votingDeadline;
    }

    /**
     * @notice Constructor
     * @param _token Address of the $PUFFS token
     * @param _minVotingPowerToPropose Minimum voting power required to propose
     * @param _minVotingPowerToVote Minimum voting power required to vote
     * @param _quorum Quorum required for a proposal to pass
     */
    constructor(
        IERC20 _token,
        uint256 _minVotingPowerToPropose,
        uint256 _minVotingPowerToVote,
        uint256 _quorum
    ) {
        token = _token;
        minVotingPowerToPropose = _minVotingPowerToPropose;
        minVotingPowerToVote = _minVotingPowerToVote;
        quorum = _quorum;
        proposalIdCounter = 0;
    }

    /**
     * @notice Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) public {
        require(
            token.balanceOf(msg.sender) >= minVotingPowerToPropose,
            "Insufficient voting power to propose"
        );

        Proposal memory proposal;
        proposal.id = proposalIdCounter;
        proposal.description = _description;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;
        proposal.votingDeadline = block.timestamp.add(30 days);

        proposals[proposalIdCounter] = proposal;

        emit NewProposal(proposalIdCounter, _description);

        proposalIdCounter++;
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _vote True for yes, false for no
     */
    function vote(uint256 _proposalId, bool _vote) public {
        require(
            token.balanceOf(msg.sender) >= minVotingPowerToVote,
            "Insufficient voting power to vote"
        );

        require(proposals[_proposalId].votingDeadline > block.timestamp, "Voting period has ended");

        require(!votes[_proposalId][msg.sender], "Already voted");

        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(token.balanceOf(msg.sender));
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(token.balanceOf(msg.sender));
        }

        votes[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId ID of the proposal
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].votingDeadline <= block.timestamp, "Voting period has not ended");

        uint256 totalVotes = proposals[_proposalId].yesVotes.add(proposals[_proposalId].noVotes);

        require(totalVotes >= quorum, "Quorum not met");

        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal did not pass");

        require(!proposals[_proposalId].executed, "Proposal already executed");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Update voting power
     * @param _user Address of the user
     * @param _power New voting power
     */
    function updateVotingPower(address _user, uint256 _power) public onlyOwner {
        votingPower[_user] = _power;
    }

    /**
     * @notice Get proposal details
     * @param _proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 _proposalId) public view returns (uint256, string memory, uint256, uint256, bool) {
        return (
            proposals[_proposalId].id,
            proposals[_proposalId].description,
            proposals[_proposalId].yesVotes,
            proposals[_proposalId].noVotes,
            proposals[_proposalId].executed
        );
    }
}
```
