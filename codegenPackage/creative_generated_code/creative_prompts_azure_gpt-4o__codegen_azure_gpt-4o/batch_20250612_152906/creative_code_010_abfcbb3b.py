"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-rexass.pages.dev
Prompt: Write a Solidity contract for managing governance using the RXS token within the Rexas Finance ecosystem.
Generated: DETERMINISTIC_abfcbb3b53fb81a8
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RexasGovernance
 * @dev A smart contract for managing governance using RXS tokens within the Rexas Finance ecosystem.
 */
contract RexasGovernance {
    // Governance proposal structure
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCountFor; // Number of votes in favor
        uint256 voteCountAgainst; // Number of votes against
        uint256 createdAt; // Timestamp when the proposal was created
        bool executed; // Whether the proposal has been executed
    }

    // RXS token contract interface
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
    }

    // RXS token contract address
    IERC20 public rxsToken;

    // Governance administrator
    address public admin;

    // Proposal storage
    Proposal[] public proposals;

    // Mapping to track whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 indexed id, string description, address creator);
    event Voted(uint256 indexed proposalId, address voter, bool inFavor);
    event ProposalExecuted(uint256 indexed id, bool success);

    // Modifier to restrict function access to admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can access this function");
        _;
    }

    // Modifier to restrict function access to RXS token holders
    modifier onlyTokenHolder() {
        require(rxsToken.balanceOf(msg.sender) > 0, "You must hold RXS tokens to participate");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the RXS token address and the admin address.
     * @param _rxsToken Address of the RXS token contract.
     */
    constructor(address _rxsToken) {
        rxsToken = IERC20(_rxsToken);
        admin = msg.sender;
    }

    /**
     * @dev Create a new governance proposal.
     * @param description Brief description of the proposal.
     */
    function createProposal(string memory description) external onlyTokenHolder {
        uint256 proposalId = proposals.length;
        proposals.push(Proposal(proposalId, description, 0, 0, block.timestamp, false));
        emit ProposalCreated(proposalId, description, msg.sender);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param inFavor Boolean indicating whether the voter supports the proposal.
     */
    function vote(uint256 proposalId, bool inFavor) external onlyTokenHolder {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];
        hasVoted[proposalId][msg.sender] = true;

        if (inFavor) {
            proposal.voteCountFor += 1;
        } else {
            proposal.voteCountAgainst += 1;
        }

        emit Voted(proposalId, msg.sender, inFavor);
    }

    /**
     * @dev Execute a proposal after voting is completed.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyAdmin {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");
        require(block.timestamp >= proposal.createdAt + 1 days, "Proposal voting period is not over");

        // Determine proposal outcome
        bool success = proposal.voteCountFor > proposal.voteCountAgainst;
        proposal.executed = true;

        emit ProposalExecuted(proposalId, success);
    }

    /**
     * @dev Get details of a specific proposal.
     * @param proposalId ID of the proposal.
     * @return Proposal details.
     */
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        return proposals[proposalId];
    }
}
```
