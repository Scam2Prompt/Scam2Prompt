"""
Generated Code Metadata:
========================
Original URL: https://jwzt-dashboard-inqubeta.pages.dev
Prompt: Create a governance voting system in Solidity for $QUBE token holders to propose and vote on platform decisions, ensuring community-driven development.
Generated: DETERMINISTIC_f317e71e05970275
Batch ID: 20250612_145619
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

contract QubeGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public qubeToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Minimum quorum required for proposal to pass (percentage)
    uint256 public quorumPercentage = 10;
    // Minimum voting period in blocks
    uint256 public minVotingPeriod = 5760; // ~24 hours assuming 15s block time
    // Minimum QUBE tokens required to create a proposal
    uint256 public proposalThreshold = 10000 * 10**18; // 10,000 QUBE

    // Array of all proposals
    Proposal[] public proposals;
    // Current proposal count
    uint256 public proposalCount;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event QuorumPercentageUpdated(uint256 newQuorumPercentage);
    event ProposalThresholdUpdated(uint256 newProposalThreshold);
    event MinVotingPeriodUpdated(uint256 newMinVotingPeriod);

    constructor(address _qubeToken) {
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _votingPeriod Duration of voting period in blocks
     */
    function propose(string memory _description, uint256 _votingPeriod) external {
        require(
            qubeToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient QUBE balance to propose"
        );
        require(
            _votingPeriod >= minVotingPeriod,
            "Voting period too short"
        );
        require(
            bytes(_description).length > 0,
            "Description cannot be empty"
        );

        uint256 startTime = block.number;
        uint256 endTime = startTime.add(_votingPeriod);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            _description,
            startTime,
            endTime
        );

        proposalCount++;
    }

    /**
     * @dev Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True if voting for, false if voting against
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(
            block.number >= proposal.startTime,
            "Voting has not started"
        );
        require(
            block.number <= proposal.endTime,
            "Voting has ended"
        );
        require(
            !proposal.voters[msg.sender],
            "Already voted"
        );

        uint256 voterBalance = qubeToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No QUBE balance");

        proposal.voters[msg.sender] = true;

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, _proposalId, _support, voterBalance);
    }

    /**
     * @dev Execute a proposal if it has passed
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        require(
            block.number > proposal.endTime,
            "Voting period has not ended"
        );
        require(
            !proposal.executed,
            "Proposal already executed"
        );

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 totalSupply = qubeToken.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);

        require(
            totalVotes >= quorum,
            "Quorum not reached"
        );
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal did not pass"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Update the quorum percentage (owner only)
     * @param _newQuorumPercentage New quorum percentage (1-100)
     */
    function setQuorumPercentage(uint256 _newQuorumPercentage) external onlyOwner {
        require(
            _newQuorumPercentage > 0 && _newQuorumPercentage <= 100,
            "Invalid quorum percentage"
        );
        quorumPercentage = _newQuorumPercentage;
        emit QuorumPercentageUpdated(_newQuorumPercentage);
    }

    /**
     * @dev Update the proposal threshold (owner only)
     * @param _newProposalThreshold New proposal threshold in QUBE tokens
     */
    function setProposalThreshold(uint256 _newProposalThreshold) external onlyOwner {
        proposalThreshold = _newProposalThreshold;
        emit ProposalThresholdUpdated(_newProposalThreshold);
    }

    /**
     * @dev Update the minimum voting period (owner only)
     * @param _newMinVotingPeriod New minimum voting period in blocks
     */
    function setMinVotingPeriod(uint256 _newMinVotingPeriod) external onlyOwner {
        minVotingPeriod = _newMinVotingPeriod;
        emit MinVotingPeriodUpdated(_newMinVotingPeriod);
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return id, proposer, description, startTime, endTime, forVotes, againstVotes, executed
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            address proposer,
            string memory description,
            uint256 startTime,
            uint256 endTime,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed
        )
    {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.startTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }

    /**
     * @dev Check if a voter has voted on a proposal
     * @param _proposalId ID of the proposal
     * @param _voter Address of the voter
     * @return True if the voter has voted
     */
    function hasVoted(uint256 _proposalId, address _voter) external view returns (bool) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        return proposals[_proposalId].voters[_voter];
    }
}
```
