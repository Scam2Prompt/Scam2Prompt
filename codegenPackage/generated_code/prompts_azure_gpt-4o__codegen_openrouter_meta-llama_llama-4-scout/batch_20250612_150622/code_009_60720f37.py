"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Generate a Solidity implementation for the 48-hour timelock mechanism described in the OUSD governance protocol to protect against malicious governance votes.
Generated: DETERMINISTIC_60720f37d39fff1c
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Timelock contract for OUSD governance protocol
 * @author [Your Name]
 * @notice This contract implements a 48-hour timelock mechanism to protect against malicious governance votes.
 */
contract OUSD48HourTimelock {
    using SafeMath for uint256;

    // Mapping of proposal IDs to their respective details
    mapping (uint256 => Proposal) public proposals;

    // Mapping of governance voters to their voting status
    mapping (address => mapping (uint256 => bool)) public voterStatus;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, uint256 timelockEnd);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Event emitted when a voter casts their vote
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);

    // Struct to represent a proposal
    struct Proposal {
        address creator;
        uint256 timelockEnd;
        bool executed;
    }

    // Time duration for the timelock in seconds (48 hours)
    uint256 public constant TIMELOCK_DURATION = 48 hours;

    /**
     * @notice Creates a new proposal with a 48-hour timelock
     * @param proposalId The ID of the proposal
     */
    function createProposal(uint256 proposalId) public {
        require(proposals[proposalId].timelockEnd == 0, "Proposal already exists");

        proposals[proposalId] = Proposal(msg.sender, block.timestamp.add(TIMELOCK_DURATION), false);
        emit NewProposal(proposalId, msg.sender, proposals[proposalId].timelockEnd);
    }

    /**
     * @notice Casts a vote for a proposal
     * @param proposalId The ID of the proposal
     * @param support Whether to support the proposal
     */
    function castVote(uint256 proposalId, bool support) public {
        require(proposals[proposalId].timelockEnd > 0, "Proposal does not exist");
        require(proposals[proposalId].executed == false, "Proposal already executed");
        require(voterStatus[msg.sender][proposalId] == false, "Already voted");

        voterStatus[msg.sender][proposalId] = true;
        emit VoteCast(msg.sender, proposalId, support);
    }

    /**
     * @notice Executes a proposal after the timelock has expired
     * @param proposalId The ID of the proposal
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].timelockEnd > 0, "Proposal does not exist");
        require(proposals[proposalId].executed == false, "Proposal already executed");
        require(block.timestamp >= proposals[proposalId].timelockEnd, "Timelock has not expired");

        proposals[proposalId].executed = true;
        emit ProposalExecuted(proposalId);

        // Add logic here to execute the proposal (e.g., transfer tokens, call another contract)
    }

    /**
     * @notice Checks if a proposal can be executed
     * @param proposalId The ID of the proposal
     * @return bool Whether the proposal can be executed
     */
    function canExecuteProposal(uint256 proposalId) public view returns (bool) {
        return proposals[proposalId].timelockEnd > 0 &&
               proposals[proposalId].executed == false &&
               block.timestamp >= proposals[proposalId].timelockEnd;
    }
}
```
