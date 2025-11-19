"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to vote on governance proposals within the Ondo DAO, ensuring it supports the ONDO token.
Generated: DETERMINISTIC_aa76669311655b59
Batch ID: 20250612_160656
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
 * @title OndoDAO Governance Voting Contract
 * @dev This contract allows users to vote on governance proposals using the ONDO token.
 */
contract OndoDAOVoting {
    // Address of the ONDO token contract
    address public ondoToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 private nextProposalId;

    // Events
    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to ensure the ONDO token contract is set
    modifier tokenContractSet() {
        require(ondoToken != address(0), "ONDO token contract is not set");
        _;
    }

    // Modifier to check proposal existence
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the ONDO token address.
     * @param _ondoToken Address of the ONDO token contract.
     */
    constructor(address _ondoToken) {
        require(_ondoToken != address(0), "Invalid ONDO token address");
        ondoToken = _ondoToken;
    }

    /**
     * @dev Function to create a new proposal.
     * @param description Description of the proposal.
     * @param duration Duration for voting in seconds.
     */
    function createProposal(string memory description, uint256 duration) external tokenContractSet {
        require(bytes(description).length > 0, "Proposal description cannot be empty");
        require(duration > 0, "Proposal duration must be greater than zero");

        uint256 proposalId = nextProposalId++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            deadline: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(proposalId, description, block.timestamp + duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) tokenContractSet {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        // Check ONDO token balance of the sender
        uint256 balance = IERC20(ondoToken).balanceOf(msg.sender);
        require(balance > 0, "You must hold ONDO tokens to vote");

        // Increment vote count based on token balance
        proposal.voteCount += balance;
        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Function to execute a proposal.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Add custom execution logic here (e.g., perform governance actions)

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
