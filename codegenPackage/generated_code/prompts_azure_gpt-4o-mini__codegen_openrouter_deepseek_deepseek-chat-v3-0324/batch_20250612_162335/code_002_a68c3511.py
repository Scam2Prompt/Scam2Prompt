"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Explain how to integrate vote escrow models in a DeFi project to enhance user participation and governance, based on the mechanisms used by Shadow Exchange.
Generated: DETERMINISTIC_a68c3511ec215dd2
Batch ID: 20250612_162335
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

/**
 * @title Vote Escrow Contract
 * @notice Implements a vote escrow mechanism similar to Shadow Exchange
 * @dev Users can lock tokens to receive voting power that decays over time
 */
contract VoteEscrow is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using Math for uint256;

    // Token to be locked
    IERC20 public immutable stakingToken;

    // Struct to store user lock information
    struct LockedBalance {
        uint256 amount;
        uint256 end;
    }

    // Duration constants
    uint256 public constant MAX_LOCK_TIME = 4 * 365 days; // 4 years max lock
    uint256 public constant MIN_LOCK_TIME = 1 weeks; // 1 week min lock

    // Mapping of user to their locked balance
    mapping(address => LockedBalance) public locked;

    // Total locked supply
    uint256 public totalLocked;

    // Events
    event LockCreated(address indexed user, uint256 amount, uint256 unlockTime);
    event LockIncreased(address indexed user, uint256 amount);
    event LockExtended(address indexed user, uint256 newUnlockTime);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the token to be locked
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @notice Lock tokens to gain voting power
     * @param amount Amount of tokens to lock
     * @param unlockTime When the lock expires (must be in the future)
     */
    function createLock(uint256 amount, uint256 unlockTime) external nonReentrant {
        require(amount > 0, "Cannot lock 0 tokens");
        require(unlockTime > block.timestamp, "Unlock time must be in future");
        require(unlockTime <= block.timestamp + MAX_LOCK_TIME, "Lock time too long");
        require(unlockTime >= block.timestamp + MIN_LOCK_TIME, "Lock time too short");
        require(locked[msg.sender].amount == 0, "Existing lock found");

        _createLock(msg.sender, amount, unlockTime);
    }

    /**
     * @notice Increase amount in existing lock
     * @param amount Additional amount to lock
     */
    function increaseLockAmount(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot lock 0 tokens");
        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(userLock.end > block.timestamp, "Lock expired");

        _increaseLockAmount(msg.sender, amount);
    }

    /**
     * @notice Extend lock duration
     * @param newUnlockTime New unlock time (must be later than current)
     */
    function extendLock(uint256 newUnlockTime) external nonReentrant {
        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(newUnlockTime > userLock.end, "New unlock time must be later");
        require(newUnlockTime <= block.timestamp + MAX_LOCK_TIME, "Lock time too long");

        _extendLock(msg.sender, newUnlockTime);
    }

    /**
     * @notice Withdraw tokens after lock expires
     */
    function withdraw() external nonReentrant {
        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(block.timestamp >= userLock.end, "Lock not expired");

        uint256 amount = userLock.amount;
        userLock.amount = 0;
        totalLocked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Calculate voting power based on lock amount and time remaining
     * @param user Address to check voting power for
     * @return Voting power
     */
    function getVotingPower(address user) external view returns (uint256) {
        LockedBalance storage userLock = locked[user];
        if (userLock.amount == 0 || block.timestamp >= userLock.end) {
            return 0;
        }

        // Voting power is proportional to amount and remaining lock duration
        uint256 timeRemaining = userLock.end - block.timestamp;
        return (userLock.amount * timeRemaining) / MAX_LOCK_TIME;
    }

    // Internal functions

    function _createLock(address user, uint256 amount, uint256 unlockTime) internal {
        locked[user] = LockedBalance(amount, unlockTime);
        totalLocked += amount;

        stakingToken.safeTransferFrom(user, address(this), amount);
        emit LockCreated(user, amount, unlockTime);
    }

    function _increaseLockAmount(address user, uint256 amount) internal {
        LockedBalance storage userLock = locked[user];
        userLock.amount += amount;
        totalLocked += amount;

        stakingToken.safeTransferFrom(user, address(this), amount);
        emit LockIncreased(user, amount);
    }

    function _extendLock(address user, uint256 newUnlockTime) internal {
        LockedBalance storage userLock = locked[user];
        userLock.end = newUnlockTime;
        emit LockExtended(user, newUnlockTime);
    }
}

/**
 * @title Governance Contract
 * @notice Uses vote escrow tokens for governance decisions
 */
contract Governance {
    VoteEscrow public immutable voteEscrow;

    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        string description;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    uint256 public proposalCount;
    uint256 public constant VOTING_DURATION = 1 weeks;
    uint256 public constant MIN_PROPOSAL_POWER = 1000 * 1e18; // 1000 tokens required to propose

    event ProposalCreated(uint256 id, address proposer, string description);
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votingPower);
    event ProposalExecuted(uint256 id);

    constructor(address _voteEscrow) {
        voteEscrow = VoteEscrow(_voteEscrow);
    }

    function propose(string memory description) external returns (uint256) {
        uint256 votingPower = voteEscrow.getVotingPower(msg.sender);
        require(votingPower >= MIN_PROPOSAL_POWER, "Insufficient voting power");

        uint256 proposalId = proposalCount++;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.startTime = block.timestamp;
        newProposal.endTime = block.timestamp + VOTING_DURATION;
        newProposal.description = description;

        emit ProposalCreated(proposalId, msg.sender, description);
        return proposalId;
    }

    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 votingPower = voteEscrow.getVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");

        // Simple majority wins
        if (proposal.forVotes > proposal.againstVotes) {
            // Proposal passed - implement your logic here
            // e.g., call external contracts, update parameters, etc.
        }

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}
```
