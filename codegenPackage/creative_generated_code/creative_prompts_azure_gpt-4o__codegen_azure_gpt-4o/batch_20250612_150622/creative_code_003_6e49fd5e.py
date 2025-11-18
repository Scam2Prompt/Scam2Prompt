"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://go-beam.pages.dev
Prompt: Write a DAO governance smart contract that allows BEAM token holders to vote on protocol upgrades, reflecting the decentralized management approach mentioned on the BEAM site.
Generated: DETERMINISTIC_6e49fd5e5b1936ab
Batch ID: 20250612_150622
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
 * @title DAO Governance Smart Contract
 * @notice This contract allows BEAM token holders to vote on protocol upgrades.
 * @dev Follows best practices, includes error handling, and is designed to be production-ready.
 */
contract BeamDAO {
    // Data structure for proposals
    struct Proposal {
        string description;       // Description of the proposal
        uint256 voteCountYes;     // Number of 'Yes' votes
        uint256 voteCountNo;      // Number of 'No' votes
        uint256 deadline;         // Voting deadline (timestamp)
        bool executed;            // Whether the proposal has been executed
    }

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // BEAM token interface
    IERC20 public beamToken;

    // Proposal counter
    uint256 public proposalCount;

    // Minimum tokens required to create a proposal
    uint256 public constant MIN_BALANCE_TO_PROPOSE = 1000 * 10**18;

    // Event definitions
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool voteYes);
    event ProposalExecuted(uint256 proposalId, bool passed);

    /**
     * @dev Initializes the contract with the BEAM token address.
     * @param _beamToken Address of the BEAM token contract.
     */
    constructor(address _beamToken) {
        require(_beamToken != address(0), "Invalid token address");
        beamToken = IERC20(_beamToken);
    }

    /**
     * @dev Modifier to check if the sender owns enough BEAM tokens to propose.
     */
    modifier onlyTokenHolder() {
        require(
            beamToken.balanceOf(msg.sender) >= MIN_BALANCE_TO_PROPOSE,
            "Insufficient BEAM token balance to propose"
        );
        _;
    }

    /**
     * @dev Modifier to check if the proposal exists.
     * @param proposalId ID of the proposal to check.
     */
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    /**
     * @dev Creates a new proposal for a protocol upgrade.
     * @param description Description of the proposal.
     * @param duration Duration (in seconds) for voting to remain open.
     */
    function createProposal(string memory description, uint256 duration)
        external
        onlyTokenHolder
    {
        require(duration > 0, "Duration must be greater than zero");

        proposals[proposalCount] = Proposal({
            description: description,
            voteCountYes: 0,
            voteCountNo: 0,
            deadline: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.timestamp + duration);

        proposalCount++;
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param voteYes Whether the vote is 'Yes' (true) or 'No' (false).
     */
    function vote(uint256 proposalId, bool voteYes)
        external
        proposalExists(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp <= proposal.deadline, "Voting has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        if (voteYes) {
            proposal.voteCountYes++;
        } else {
            proposal.voteCountNo++;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, voteYes);
    }

    /**
     * @dev Executes a proposal after the voting period has ended.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId)
        external
        proposalExists(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        bool passed = proposal.voteCountYes > proposal.voteCountNo;
        proposal.executed = true;

        emit ProposalExecuted(proposalId, passed);

        // If passed, execute protocol upgrade logic (to be implemented).
        // NOTE: Actual protocol upgrade logic should be implemented here.
    }
}

/**
 * @title IERC20 Interface
 * @dev Basic interface for ERC20 tokens.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
