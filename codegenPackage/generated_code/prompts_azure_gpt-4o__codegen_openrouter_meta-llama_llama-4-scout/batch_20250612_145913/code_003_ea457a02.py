"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a governance voting system in Solidity for a DeFi platform, inspired by Tenderize's TEND token governance model.
Generated: DETERMINISTIC_ea457a0229dd19f6
Batch ID: 20250612_145913
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GovernanceVotingSystem
 * @author [Your Name]
 * @notice A governance voting system for a DeFi platform inspired by Tenderize's TEND token governance model.
 */
contract GovernanceVotingSystem is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposal votes
    mapping(uint256 => mapping(address => bool)) public proposalVotes;

    // Mapping of proposal details
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCount;

    // Voting power required for a proposal to pass
    uint256 public votingPowerRequired;

    // Time in seconds for a proposal to be active
    uint256 public proposalDuration;

    // Time in seconds for a user to lock their tokens for voting
    uint256 public lockingDuration;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a user votes on a proposal
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @notice Constructor for the GovernanceVotingSystem contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param votingPowerRequired The voting power required for a proposal to pass.
     * @param proposalDuration The time in seconds for a proposal to be active.
     * @param lockingDuration The time in seconds for a user to lock their tokens for voting.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 votingPowerRequired,
        uint256 proposalDuration,
        uint256 lockingDuration
    ) ERC20(name, symbol) {
        require(votingPowerRequired > 0, "Voting power required must be greater than 0");
        require(proposalDuration > 0, "Proposal duration must be greater than 0");
        require(lockingDuration > 0, "Locking duration must be greater than 0");

        this.votingPowerRequired = votingPowerRequired;
        this.proposalDuration = proposalDuration;
        this.lockingDuration = lockingDuration;
    }

    /**
     * @notice Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public {
        require(votingPower[msg.sender] > 0, "User has no voting power");

        Proposal memory proposal;
        proposal.id = ++proposalCount;
        proposal.description = description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(proposalDuration);
        proposal.executed = false;

        proposals[proposalCount] = proposal;

        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @notice Locks tokens for voting.
     * @param amount The amount of tokens to lock.
     */
    function lockTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "User does not have enough tokens");

        votingPower[msg.sender] = votingPower[msg.sender].add(amount);

        _burn(msg.sender, amount);
    }

    /**
     * @notice Unlocks tokens.
     * @param amount The amount of tokens to unlock.
     */
    function unlockTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(votingPower[msg.sender] >= amount, "User does not have enough locked tokens");

        votingPower[msg.sender] = votingPower[msg.sender].sub(amount);

        _mint(msg.sender, amount);
    }

    /**
     * @notice Votes on a proposal.
     * @param proposalId The ID of the proposal.
     * @param support Whether to support the proposal.
     */
    function vote(uint256 proposalId, bool support) public {
        require(proposals[proposalId].startTime > 0, "Proposal does not exist");
        require(proposals[proposalId].endTime > block.timestamp, "Proposal has expired");
        require(votingPower[msg.sender] > 0, "User has no voting power");

        if (support) {
            proposals[proposalId].yesVotes = proposals[proposalId].yesVotes.add(votingPower[msg.sender]);
        } else {
            proposals[proposalId].noVotes = proposals[proposalId].noVotes.add(votingPower[msg.sender]);
        }

        proposalVotes[proposalId][msg.sender] = support;

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has passed.
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].endTime < block.timestamp, "Proposal has not expired");
        require(proposals[proposalId].yesVotes > votingPowerRequired, "Proposal has not passed");
        require(!proposals[proposalId].executed, "Proposal has already been executed");

        proposals[proposalId].executed = true;

        emit ProposalExecuted(proposalId);
    }
}
```
