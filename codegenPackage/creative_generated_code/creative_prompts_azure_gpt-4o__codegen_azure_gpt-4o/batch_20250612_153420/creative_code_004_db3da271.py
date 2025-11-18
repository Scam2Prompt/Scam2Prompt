"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Create a Solidity smart contract for decentralized governance of the HEHE ecosystem, allowing $HEHE token holders to vote on proposals.
Generated: DETERMINISTIC_db3da271317d9777
Batch ID: 20250612_153420
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
 * @title HEHE Governance Contract
 * @dev A smart contract that enables decentralized governance of the HEHE ecosystem.
 *      $HEHE token holders can create and vote on proposals.
 */
contract HEHEGovernance {
    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Address of the $HEHE token contract
    address public heheToken;

    // Minimum number of tokens required to create a proposal
    uint256 public proposalCreationThreshold;

    // Proposal duration in seconds
    uint256 public proposalDuration;

    // Counter for proposal IDs
    uint256 private proposalCounter;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed creator);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId, bool passed);

    /**
     * @dev Modifier to ensure only $HEHE token holders can interact
     */
    modifier onlyTokenHolders() {
        require(balanceOf(msg.sender) > 0, "You must hold $HEHE tokens to participate");
        _;
    }

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _heheToken Address of the $HEHE token contract.
     * @param _proposalCreationThreshold Minimum tokens required to create a proposal.
     * @param _proposalDuration Duration of each proposal (in seconds).
     */
    constructor(address _heheToken, uint256 _proposalCreationThreshold, uint256 _proposalDuration) {
        heheToken = _heheToken;
        proposalCreationThreshold = _proposalCreationThreshold;
        proposalDuration = _proposalDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string calldata _description) external onlyTokenHolders {
        require(balanceOf(msg.sender) >= proposalCreationThreshold, "Insufficient tokens to create proposal");

        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + proposalDuration,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _description, msg.sender);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal being voted on.
     * @param _support True to vote for the proposal, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.startTime, "Voting has not started");
        require(block.timestamp <= proposal.endTime, "Voting has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor += balanceOf(msg.sender);
        } else {
            proposal.votesAgainst += balanceOf(msg.sender);
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param _proposalId ID of the proposal to be executed.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.endTime, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;
        bool passed = proposal.votesFor > proposal.votesAgainst;

        // Logic to execute the proposal (if passed) can be added here

        emit ProposalExecuted(_proposalId, passed);
    }

    /**
     * @dev Helper function: Get the balance of $HEHE tokens for a given address.
     * @param _account Address to query the balance of.
     * @return The balance of $HEHE tokens.
     */
    function balanceOf(address _account) internal view returns (uint256) {
        (bool success, bytes memory data) = heheToken.call(abi.encodeWithSignature("balanceOf(address)", _account));
        require(success, "Failed to query token balance");
        return abi.decode(data, (uint256));
    }
}
```
