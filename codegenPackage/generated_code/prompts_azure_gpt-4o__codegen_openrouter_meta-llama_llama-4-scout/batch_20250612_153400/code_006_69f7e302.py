"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-in.pages.dev
Prompt: Create a governance voting system in Solidity that allows QUBE token holders to propose and vote on platform updates, following InQubeta's governance token model.
Generated: DETERMINISTIC_69f7e302ba209339
Batch ID: 20250612_153400
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
 * @title Governance Voting System Contract
 * @author [Your Name]
 * @notice This contract enables QUBE token holders to propose and vote on platform updates.
 */
contract GovernanceVotingSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their voting history
    mapping(address => mapping(uint256 => bool)) public votingHistory;

    // QUBE token contract instance
    IERC20 public qubeToken;

    // Proposal count
    uint256 public proposalCount;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Quorum percentage for proposals to pass
    uint256 public quorumPercentage;

    // Minimum tokens required to propose
    uint256 public minTokensRequired;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed proposer, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @param _qubeToken QUBE token contract address
     * @param _votingDuration Voting duration in seconds
     * @param _quorumPercentage Quorum percentage for proposals to pass
     * @param _minTokensRequired Minimum tokens required to propose
     */
    constructor(
        address _qubeToken,
        uint256 _votingDuration,
        uint256 _quorumPercentage,
        uint256 _minTokensRequired
    ) public {
        qubeToken = IERC20(_qubeToken);
        votingDuration = _votingDuration;
        quorumPercentage = _quorumPercentage;
        minTokensRequired = _minTokensRequired;
    }

    /**
     * @dev Create a new proposal
     * @param _description Proposal description
     */
    function propose(string memory _description) public {
        // Ensure user has minimum tokens required
        require(qubeToken.balanceOf(msg.sender) >= minTokensRequired, "Insufficient tokens to propose");

        // Create a new proposal
        Proposal memory proposal;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.createdAt = block.timestamp;
        proposal.votesFor = 0;
        proposal.votesAgainst = 0;
        proposal.executed = false;

        // Increment proposal count and store proposal
        proposalCount++;
        proposals[proposalCount] = proposal;

        // Emit event
        emit NewProposal(proposalCount, msg.sender, _description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        // Ensure proposal exists and is within voting duration
        require(proposals[_proposalId].createdAt != 0, "Proposal does not exist");
        require(block.timestamp.sub(proposals[_proposalId].createdAt) <= votingDuration, "Voting period has ended");

        // Ensure user has not voted before
        require(!votingHistory[msg.sender][_proposalId], "User has already voted");

        // Update user's voting power
        votingPower[msg.sender] = qubeToken.balanceOf(msg.sender);

        // Update proposal votes
        if (_support) {
            proposals[_proposalId].votesFor = proposals[_proposalId].votesFor.add(votingPower[msg.sender]);
        } else {
            proposals[_proposalId].votesAgainst = proposals[_proposalId].votesAgainst.add(votingPower[msg.sender]);
        }

        // Update user's voting history
        votingHistory[msg.sender][_proposalId] = true;

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal if it passes
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public {
        // Ensure proposal exists and has not been executed
        require(proposals[_proposalId].createdAt != 0, "Proposal does not exist");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        // Calculate quorum
        uint256 quorum = qubeToken.totalSupply().mul(quorumPercentage).div(100);

        // Ensure proposal has met quorum and has more votes for than against
        require(proposals[_proposalId].votesFor.add(proposals[_proposalId].votesAgainst) >= quorum, "Proposal has not met quorum");
        require(proposals[_proposalId].votesFor > proposals[_proposalId].votesAgainst, "Proposal has not been supported");

        // Mark proposal as executed
        proposals[_proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    // Proposal structure
    struct Proposal {
        address proposer;
        string description;
        uint256 createdAt;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }
}
```
