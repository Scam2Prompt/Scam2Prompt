"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a Solidity implementation for decentralized governance that allows Bulldogito Coin holders to propose and vote on asset management strategies using their voting power.
Generated: DETERMINISTIC_19815f3a3d0e94e1
Batch ID: 20250612_154239
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
 * @title Bulldogito Governance Contract
 * @author [Your Name]
 * @notice Decentralized governance for Bulldogito Coin holders to propose and vote on asset management strategies.
 */
contract BulldogitoGovernance {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user votes on proposals
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 proposalId, address proposer, string strategy);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string strategy;
        uint256 votingPowerRequired;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Bulldogito Coin token contract
    IERC20 public bulldogitoToken;

    // Total number of proposals
    uint256 public proposalCount;

    // Voting power threshold for proposal execution
    uint256 public votingPowerThreshold;

    /**
     * @dev Initializes the governance contract.
     * @param _bulldogitoToken Bulldogito Coin token contract address.
     * @param _votingPowerThreshold Voting power threshold for proposal execution.
     */
    constructor(IERC20 _bulldogitoToken, uint256 _votingPowerThreshold) public {
        bulldogitoToken = _bulldogitoToken;
        votingPowerThreshold = _votingPowerThreshold;
    }

    /**
     * @dev Updates a user's voting power.
     * @param _user User address.
     * @param _votingPower New voting power.
     */
    function updateVotingPower(address _user, uint256 _votingPower) public {
        require(msg.sender == address(bulldogitoToken), "Only Bulldogito Coin token contract can update voting power");
        votingPower[_user] = _votingPower;
    }

    /**
     * @dev Creates a new proposal.
     * @param _strategy Proposed asset management strategy.
     * @param _votingPowerRequired Voting power required for proposal execution.
     */
    function createProposal(string memory _strategy, uint256 _votingPowerRequired) public {
        Proposal memory proposal;
        proposal.id = proposalCount++;
        proposal.proposer = msg.sender;
        proposal.strategy = _strategy;
        proposal.votingPowerRequired = _votingPowerRequired;
        proposal.votesFor = 0;
        proposal.votesAgainst = 0;
        proposal.executed = false;

        proposals[proposal.id] = proposal;

        emit NewProposal(proposal.id, proposal.proposer, proposal.strategy);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId Proposal ID.
     * @param _support Whether to vote for or against the proposal.
     */
    function castVote(uint256 _proposalId, bool _support) public {
        require(votingPower[msg.sender] > 0, "User has no voting power");
        require(proposals[_proposalId].executed == false, "Proposal has already been executed");

        if (_support) {
            proposals[_proposalId].votesFor = proposals[_proposalId].votesFor.add(votingPower[msg.sender]);
        } else {
            proposals[_proposalId].votesAgainst = proposals[_proposalId].votesAgainst.add(votingPower[msg.sender]);
        }

        userVotes[msg.sender][_proposalId] = _support;

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal if it has met the voting power threshold.
     * @param _proposalId Proposal ID.
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].executed == false, "Proposal has already been executed");
        require(proposals[_proposalId].votesFor > proposals[_proposalId].votingPowerRequired, "Proposal has not met voting power threshold");

        proposals[_proposalId].executed = true;

        // Execute the proposal (e.g., update asset management strategy)
        // NOTE: This is a placeholder and should be replaced with actual execution logic

        emit ProposalExecuted(_proposalId);
    }
}
```
