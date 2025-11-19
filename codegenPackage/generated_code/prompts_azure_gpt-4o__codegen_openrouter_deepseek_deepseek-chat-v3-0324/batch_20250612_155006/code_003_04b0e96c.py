"""
Generated Code Metadata:
========================
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: Write code to implement a voting mechanism for governance in a Uniswap clone project.
Generated: DETERMINISTIC_04b0e96c98edd765
Batch ID: 20250612_155006
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Governance is Ownable {
    using SafeMath for uint256;

    // The governance token
    IERC20 public governanceToken;

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

    // Minimum voting power required to create a proposal
    uint256 public proposalThreshold;

    // Voting delay in blocks
    uint256 public votingDelay;

    // Voting period in blocks
    uint256 public votingPeriod;

    // Proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Total number of proposals
    uint256 public proposalCount;

    // Events
    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor
     * @param _governanceToken Address of the governance token
     * @param _proposalThreshold Minimum tokens needed to submit a proposal
     * @param _votingDelay Delay in blocks before voting starts
     * @param _votingPeriod Duration in blocks of the voting period
     */
    constructor(
        address _governanceToken,
        uint256 _proposalThreshold,
        uint256 _votingDelay,
        uint256 _votingPeriod
    ) {
        governanceToken = IERC20(_governanceToken);
        proposalThreshold = _proposalThreshold;
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        require(
            governanceToken.balanceOf(msg.sender) >= proposalThreshold,
            "Governance::propose: proposer votes below proposal threshold"
        );

        uint256 startTime = block.number.add(votingDelay);
        uint256 endTime = startTime.add(votingPeriod);

        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.description = description;
        proposal.startTime = startTime;
        proposal.endTime = endTime;
        proposal.forVotes = 0;
        proposal.againstVotes = 0;
        proposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            description,
            startTime,
            endTime
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True if voting for, false if voting against
     */
    function castVote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.number >= proposal.startTime,
            "Governance::castVote: voting not started"
        );
        require(
            block.number <= proposal.endTime,
            "Governance::castVote: voting already ended"
        );
        require(
            !proposal.voters[msg.sender],
            "Governance::castVote: voter already voted"
        );

        uint256 votes = governanceToken.balanceOf(msg.sender);
        require(votes > 0, "Governance::castVote: no voting power");

        if (support) {
            proposal.forVotes = proposal.forVotes.add(votes);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votes);
        }

        proposal.voters[msg.sender] = true;

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @dev Execute a proposal if it has succeeded
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.number > proposal.endTime,
            "Governance::executeProposal: voting not ended"
        );
        require(
            !proposal.executed,
            "Governance::executeProposal: proposal already executed"
        );
        require(
            proposal.forVotes > proposal.againstVotes,
            "Governance::executeProposal: proposal did not pass"
        );

        proposal.executed = true;

        // Here you would implement the actual proposal execution logic
        // For example: call a function, transfer funds, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update proposal threshold
     * @param newProposalThreshold New proposal threshold
     */
    function setProposalThreshold(uint256 newProposalThreshold) external onlyOwner {
        proposalThreshold = newProposalThreshold;
    }

    /**
     * @dev Update voting delay
     * @param newVotingDelay New voting delay in blocks
     */
    function setVotingDelay(uint256 newVotingDelay) external onlyOwner {
        votingDelay = newVotingDelay;
    }

    /**
     * @dev Update voting period
     * @param newVotingPeriod New voting period in blocks
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        votingPeriod = newVotingPeriod;
    }
}
```
