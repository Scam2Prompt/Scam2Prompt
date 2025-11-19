"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Create a governance contract for a DAO with veNFT-based voting, boosting, and staking reward mechanisms, similar to iZUMi Finance's governance model.
Generated: DETERMINISTIC_c32d651506712888
Batch ID: 20250612_153424
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DAOGovernance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Structs
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        string description;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    struct LockedBalance {
        uint256 amount;
        uint256 unlockTime;
    }

    // Constants
    uint256 public constant MIN_LOCK_DURATION = 1 weeks;
    uint256 public constant MAX_LOCK_DURATION = 4 * 365 days;
    uint256 public constant MIN_PROPOSAL_DURATION = 3 days;
    uint256 public constant MAX_PROPOSAL_DURATION = 30 days;
    uint256 public constant VOTE_QUORUM = 30; // 30% of total veNFT power required
    uint256 public constant VOTE_THRESHOLD = 50; // 50%+1 required to pass

    // State variables
    IERC20 public immutable governanceToken;
    IERC721Enumerable public immutable veNFT;
    uint256 public proposalCount;
    uint256 public totalLocked;
    uint256 public totalBoostedPower;

    mapping(uint256 => Proposal) public proposals;
    mapping(address => LockedBalance) public lockedBalances;
    mapping(address => uint256) public boostedPower;
    mapping(address => uint256) public lastVoteTime;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, address proposer, uint256 startTime, uint256 endTime, string description);
    event Voted(uint256 indexed proposalId, address voter, uint256 power, uint8 support);
    event ProposalExecuted(uint256 indexed proposalId);
    event Boosted(address indexed user, uint256 tokenId, uint256 power);
    event Unboosted(address indexed user, uint256 tokenId);

    // Modifiers
    modifier onlyProposer() {
        require(lockedBalances[msg.sender].amount > 0, "No locked tokens");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId <= proposalCount && proposalId != 0, "Invalid proposal");
        _;
    }

    modifier proposalActive(uint256 proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime, "Not active");
        _;
    }

    constructor(address _governanceToken, address _veNFT) {
        require(_governanceToken != address(0), "Invalid token");
        require(_veNFT != address(0), "Invalid veNFT");
        governanceToken = IERC20(_governanceToken);
        veNFT = IERC721Enumerable(_veNFT);
    }

    /**
     * @notice Lock governance tokens to participate in governance
     * @param amount Amount of tokens to lock
     * @param duration Lock duration in seconds
     */
    function lockTokens(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(duration >= MIN_LOCK_DURATION && duration <= MAX_LOCK_DURATION, "Invalid duration");
        
        LockedBalance storage locked = lockedBalances[msg.sender];
        require(locked.unlockTime == 0 || locked.unlockTime > block.timestamp, "Existing lock expired");

        uint256 unlockTime = block.timestamp.add(duration);
        locked.amount = locked.amount.add(amount);
        locked.unlockTime = unlockTime;
        totalLocked = totalLocked.add(amount);

        require(governanceToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    /**
     * @notice Withdraw locked tokens after unlock time
     */
    function withdrawTokens() external nonReentrant {
        LockedBalance storage locked = lockedBalances[msg.sender];
        require(locked.amount > 0, "No locked tokens");
        require(block.timestamp >= locked.unlockTime, "Lock not expired");

        uint256 amount = locked.amount;
        locked.amount = 0;
        locked.unlockTime = 0;
        totalLocked = totalLocked.sub(amount);

        require(governanceToken.transfer(msg.sender, amount), "Transfer failed");
        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Create a new proposal
     * @param duration Proposal voting duration in seconds
     * @param description Proposal description
     */
    function createProposal(uint256 duration, string memory description) external onlyProposer {
        require(bytes(description).length > 0, "Empty description");
        require(duration >= MIN_PROPOSAL_DURATION && duration <= MAX_PROPOSAL_DURATION, "Invalid duration");

        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(duration);
        proposal.description = description;

        emit ProposalCreated(proposalCount, msg.sender, proposal.startTime, proposal.endTime, description);
    }

    /**
     * @notice Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support 0=against, 1=for, 2=abstain
     */
    function vote(uint256 proposalId, uint8 support) external proposalExists(proposalId) proposalActive(proposalId) {
        require(support <= 2, "Invalid vote");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 votingPower = getVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support == 0) {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        } else if (support == 1) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else if (support == 2) {
            proposal.abstainVotes = proposal.abstainVotes.add(votingPower);
        }

        lastVoteTime[msg.sender] = block.timestamp;
        emit Voted(proposalId, msg.sender, votingPower, support);
    }

    /**
     * @notice Execute a proposal if quorum and threshold are met
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes).add(proposal.abstainVotes);
        uint256 quorum = totalLocked.mul(VOTE_QUORUM).div(100);
        
        require(totalVotes >= quorum, "Quorum not met");
        require(proposal.forVotes > proposal.againstVotes, "Threshold not met");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Boost voting power with veNFT
     * @param tokenId ID of the veNFT to boost with
     */
    function boost(uint256 tokenId) external {
        require(veNFT.ownerOf(tokenId) == msg.sender, "Not owner");
        require(boostedPower[msg.sender] == 0, "Already boosted");

        uint256 power = calculateVeNFTPower(tokenId);
        boostedPower[msg.sender] = power;
        totalBoostedPower = totalBoostedPower.add(power);

        emit Boosted(msg.sender, tokenId, power);
    }

    /**
     * @notice Remove veNFT boost
     */
    function unboost() external {
        uint256 power = boostedPower[msg.sender];
        require(power > 0, "
