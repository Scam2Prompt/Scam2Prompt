"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Explain how to set up a governance voting mechanism using the veNFT model from iZUMi Finance.
Generated: DETERMINISTIC_0349ccf8a98296d4
Batch ID: 20250612_155554
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract veNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    struct LockedBalance {
        uint256 amount;
        uint256 end;
    }

    // Token ID to locked balance mapping
    mapping(uint256 => LockedBalance) public locked;

    // User address to token IDs mapping
    mapping(address => uint256[]) public userTokenIds;

    // Total locked supply
    uint256 public totalLocked;

    // Voting power decay parameters
    uint256 public constant MAX_TIME = 4 * 365 * 86400; // 4 years
    uint256 public constant WEEK = 7 * 86400; // 1 week in seconds

    // Governance parameters
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public voted;

    enum VoteType { FOR, AGAINST }
    enum ProposalState { ACTIVE, PASSED, FAILED }

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        ProposalState state;
    }

    event LockCreated(uint256 tokenId, address indexed user, uint256 amount, uint256 end);
    event VoteCast(address indexed voter, uint256 proposalId, VoteType voteType, uint256 votingPower);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 startTime, uint256 endTime);
    event ProposalStateChanged(uint256 indexed proposalId, ProposalState state);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @notice Create a new veNFT by locking tokens
     * @param amount Amount of tokens to lock
     * @param duration Lock duration in seconds
     */
    function createLock(uint256 amount, uint256 duration) external {
        require(amount > 0, "Cannot lock 0 amount");
        require(duration <= MAX_TIME, "Lock duration too long");
        
        uint256 tokenId = totalSupply() + 1;
        uint256 end = block.timestamp + duration;
        
        locked[tokenId] = LockedBalance({
            amount: amount,
            end: end
        });
        
        userTokenIds[msg.sender].push(tokenId);
        totalLocked = totalLocked.add(amount);
        
        _mint(msg.sender, tokenId);
        emit LockCreated(tokenId, msg.sender, amount, end);
    }

    /**
     * @notice Get voting power for a specific token at current time
     * @param tokenId The veNFT token ID
     */
    function getVotingPower(uint256 tokenId) public view returns (uint256) {
        LockedBalance memory lock = locked[tokenId];
        if (block.timestamp >= lock.end) return 0;
        
        uint256 remainingTime = lock.end - block.timestamp;
        return lock.amount.mul(remainingTime).div(MAX_TIME);
    }

    /**
     * @notice Get total voting power for an address
     * @param user The user address
     */
    function getTotalVotingPower(address user) public view returns (uint256) {
        uint256 total = 0;
        uint256[] memory tokenIds = userTokenIds[user];
        
        for (uint256 i = 0; i < tokenIds.length; i++) {
            total = total.add(getVotingPower(tokenIds[i]));
        }
        
        return total;
    }

    /**
     * @notice Create a new governance proposal
     * @param description Proposal description
     * @param duration Voting duration in seconds
     */
    function createProposal(string memory description, uint256 duration) external {
        require(getTotalVotingPower(msg.sender) > 0, "No voting power");
        require(duration >= WEEK && duration <= 4 * WEEK, "Invalid duration");
        
        proposalCount++;
        
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            description: description,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            forVotes: 0,
            againstVotes: 0,
            state: ProposalState.ACTIVE
        });
        
        emit ProposalCreated(proposalCount, msg.sender, description, block.timestamp, block.timestamp + duration);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param proposalId The proposal ID
     * @param voteType Vote type (FOR or AGAINST)
     */
    function castVote(uint256 proposalId, VoteType voteType) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.ACTIVE, "Proposal not active");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!voted[proposalId][msg.sender], "Already voted");
        
        uint256 votingPower = getTotalVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");
        
        if (voteType == VoteType.FOR) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        }
        
        voted[proposalId][msg.sender] = true;
        emit VoteCast(msg.sender, proposalId, voteType, votingPower);
    }

    /**
     * @notice Execute a proposal after voting ends
     * @param proposalId The proposal ID
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.ACTIVE, "Proposal not active");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        
        if (proposal.forVotes > proposal.againstVotes) {
            proposal.state = ProposalState.PASSED;
        } else {
            proposal.state = ProposalState.FAILED;
        }
        
        emit ProposalStateChanged(proposalId, proposal.state);
    }

    /**
     * @notice Get current voting power for all user tokens
     * @param user The user address
     */
    function getUserVotingPowers(address user) external view returns (uint256[] memory, uint256[] memory) {
        uint256[] memory tokenIds = userTokenIds[user];
        uint256[] memory powers = new uint256[](tokenIds.length);
        
        for (uint256 i = 0; i < tokenIds.length; i++) {
            powers[i] = getVotingPower(tokenIds[i]);
        }
        
        return (tokenIds, powers);
    }
}
```
