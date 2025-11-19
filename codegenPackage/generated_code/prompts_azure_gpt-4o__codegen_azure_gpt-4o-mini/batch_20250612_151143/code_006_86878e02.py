"""
Generated Code Metadata:
========================
Original URL: https://fdn-eeo.pages.dev
Prompt: Create a smart contract example that allows DRIFT token holders to propose and vote on governance decisions within the Drift ecosystem.
Generated: DETERMINISTIC_86878e0278b632a6
Batch ID: 20250612_151143
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DriftGovernance
 * @dev A smart contract that allows DRIFT token holders to propose and vote on governance decisions.
 */
contract DriftGovernance is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a governance proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public driftToken; // The DRIFT token contract
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the caller has voting rights
    modifier onlyTokenHolder() {
        require(driftToken.balanceOf(msg.sender) > 0, "Not a token holder");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the DRIFT token address and voting duration.
     * @param _driftToken Address of the DRIFT token contract.
     * @param _votingDuration Duration for voting in seconds.
     */
    constructor(IERC20 _driftToken, uint256 _votingDuration) {
        driftToken = _driftToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();
        uint256 endTime = block.timestamp + votingDuration;

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, msg.sender, _description, endTime);
    }

    /**
     * @dev Vote on a governance proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += driftToken.balanceOf(msg.sender);

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a governance proposal if the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal already executed");

        // Logic to execute the proposal can be added here

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return id, proposer, description, voteCount, endTime, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 voteCount,
        uint256 endTime,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.voteCount,
            proposal.endTime,
            proposal.executed
        );
    }
}
```
