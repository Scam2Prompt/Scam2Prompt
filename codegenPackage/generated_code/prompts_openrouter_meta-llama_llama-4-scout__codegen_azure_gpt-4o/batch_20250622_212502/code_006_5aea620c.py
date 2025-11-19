"""
Generated Code Metadata:
========================
Original URL: https://defiprot.pages.dev
Prompt: Write a code example for fixing gas issues in a DeFi protocol, using a decentralized governance model and non-custodial management.
Generated: DETERMINISTIC_5aea620c61a98729
Batch ID: 20250622_212502
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

/**
 * @title GasOptimizationGovernance
 * @dev A decentralized governance contract for proposing and voting on gas optimization fixes
 *      in a DeFi protocol. Implements non-custodial management.
 */
contract GasOptimizationGovernance {
    // Events
    event ProposalCreated(uint256 proposalId, address proposer, string description);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    // Structs
    struct Proposal {
        string description; // Description of the gas optimization fix
        uint256 voteCountFor; // Votes in favor
        uint256 voteCountAgainst; // Votes against
        uint256 deadline; // Voting deadline
        bool executed; // Whether the proposal has been executed
    }

    // State variables
    address public immutable protocolOwner; // Address of the protocol owner
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposalId to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    // Constants
    uint256 public constant VOTING_PERIOD = 3 days; // Voting period duration

    // Modifiers
    modifier onlyProtocolOwner() {
        require(msg.sender == protocolOwner, "Only protocol owner can execute this");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].deadline != 0, "Proposal does not exist");
        _;
    }

    modifier votingActive(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].deadline, "Voting period has ended");
        _;
    }

    modifier votingEnded(uint256 proposalId) {
        require(block.timestamp > proposals[proposalId].deadline, "Voting period is still active");
        _;
    }

    constructor() {
        protocolOwner = msg.sender; // Set the protocol owner
    }

    /**
     * @dev Create a new proposal for a gas optimization fix.
     * @param description A brief description of the proposed fix.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            deadline: block.timestamp + VOTING_PERIOD,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support)
        external
        proposalExists(proposalId)
        votingActive(proposalId)
    {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposals[proposalId].voteCountFor++;
        } else {
            proposals[proposalId].voteCountAgainst++;
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId)
        external
        onlyProtocolOwner
        proposalExists(proposalId)
        votingEnded(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        // Check if the proposal passed
        require(
            proposal.voteCountFor > proposal.voteCountAgainst,
            "Proposal did not pass"
        );

        // Mark the proposal as executed
        proposal.executed = true;

        // Logic for applying the gas optimization fix would go here
        // For example, calling a function on the protocol contract

        emit ProposalExecuted(proposalId);
    }
}
```
