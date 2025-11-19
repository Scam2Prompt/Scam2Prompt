"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: "Design a simple decentralized governance system using blockchain, allowing token holders to vote on platform decisions, inspired by Pushd's governance model."
Generated: DETERMINISTIC_efe3b20cea878e26
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Decentralized Governance Contract
 * @dev Allows token holders to create and vote on proposals
 */
contract Governance is Ownable {
    using SafeMath for uint256;

    IERC20 public governanceToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public minimumQuorum; // Minimum votes required for proposal to pass
    uint256 public debatingPeriodDuration; // Default voting period in seconds

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 createTime,
        uint256 duration
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 id);

    /**
     * @dev Initialize governance contract
     * @param _token Address of the governance token
     * @param _minimumQuorum Minimum votes required for proposal to pass
     * @param _debatingPeriodDuration Default voting period in seconds
     */
    constructor(
        address _token,
        uint256 _minimumQuorum,
        uint256 _debatingPeriodDuration
    ) {
        governanceToken = IERC20(_token);
        minimumQuorum = _minimumQuorum;
        debatingPeriodDuration = _debatingPeriodDuration;
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of voting period in seconds (0 for default)
     */
    function createProposal(string memory _description, uint256 _duration) external {
        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower > 0, "Must hold tokens to create proposal");

        uint256 duration = _duration == 0 ? debatingPeriodDuration : _duration;
        proposalCount++;

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.createTime = block.timestamp;
        newProposal.duration = duration;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            newProposal.proposer,
            newProposal.description,
            newProposal.createTime,
            newProposal.duration
        );
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True if voting in support, false if voting against
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.createTime.add(proposal.duration), "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        }

        emit VoteCast(msg.sender, _proposalId, _support, votingPower);
    }

    /**
     * @dev Execute a proposal if voting passed
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.createTime.add(proposal.duration), "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        require(totalVotes >= minimumQuorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: call another contract, transfer funds, etc.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Update governance parameters (only owner)
     * @param _minimumQuorum New minimum quorum value
     * @param _debatingPeriodDuration New default voting period
     */
    function updateGovernanceParameters(
        uint256 _minimumQuorum,
        uint256 _debatingPeriodDuration
    ) external onlyOwner {
        minimumQuorum = _minimumQuorum;
        debatingPeriodDuration = _debatingPeriodDuration;
    }

    /**
     * @dev Check if voter has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address of the voter
     */
    function hasVoted(uint256 _proposalId, address _voter) public view returns (bool) {
        return proposals[_proposalId].hasVoted[_voter];
    }
}
```
