"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-littlerabbits.pages.dev
Prompt: Explain how to use the governance features of the LTRBT token in a smart contract for the LittleRabbit MMORPG.
Generated: DETERMINISTIC_b5a7437dc1126577
Batch ID: 20250612_155727
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
 * @title LTRBT Governance Smart Contract for LittleRabbit MMORPG
 * @dev This contract enables token-based governance for the LittleRabbit MMORPG using the LTRBT token.
 * Users can propose actions, vote, and execute proposals based on LTRBT token holdings.
 */
contract LittleRabbitGovernance {
    // State Variables
    address public admin; // Contract admin
    IERC20 public ltrbtToken; // LTRBT token contract address
    uint256 public proposalCount; // Counter for proposals

    // Structs
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Mappings
    mapping(uint256 => Proposal) public proposals; // Proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public votes; // Proposal ID => Voter => Voted?

    // Events
    event ProposalCreated(uint256 id, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 id);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Invalid proposal");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the admin and LTRBT token contract address.
     * @param _ltrbtToken Address of the LTRBT token contract.
     */
    constructor(address _ltrbtToken) {
        require(_ltrbtToken != address(0), "Invalid token address");
        admin = msg.sender;
        ltrbtToken = IERC20(_ltrbtToken);
    }

    /**
     * @dev Function to create a new proposal.
     * @param description Short description of the proposal.
     * @param votingDuration Duration for which voting is open (in seconds).
     */
    function createProposal(string memory description, uint256 votingDuration) external onlyAdmin {
        require(bytes(description).length > 0, "Proposal description cannot be empty");
        require(votingDuration > 0, "Voting duration must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.timestamp, block.timestamp + votingDuration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime, "Voting has not started yet");
        require(block.timestamp <= proposal.endTime, "Voting has already ended");
        require(!votes[proposalId][msg.sender], "You have already voted on this proposal");
        require(ltrbtToken.balanceOf(msg.sender) > 0, "You must hold LTRBT tokens to vote");

        votes[proposalId][msg.sender] = true;
        proposal.voteCount += ltrbtToken.balanceOf(msg.sender);

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Function to execute a proposal after voting has ended.
     * @param proposalId The ID of the proposal to be executed.
     */
    function executeProposal(uint256 proposalId) external onlyAdmin validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting has not ended yet");
        require(!proposal.executed, "Proposal has already been executed");

        // Logic for executing the proposal can be added here
        // e.g., making in-game adjustments or triggering specific in-game behavior

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Function to retrieve a proposal's details.
     * @param proposalId The ID of the proposal to retrieve.
     * @return Proposal details including description, vote count, timestamps, and execution status.
     */
    function getProposal(uint256 proposalId)
        external
        view
        validProposal(proposalId)
        returns (
            string memory description,
            uint256 voteCount,
            uint256 startTime,
            uint256 endTime,
            bool executed
        )
    {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.startTime, proposal.endTime, proposal.executed);
    }
}

/**
 * @dev Interface for the LTRBT token contract (ERC-20).
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function allowance(address owner, address spender) external view returns (uint256);
}
```
