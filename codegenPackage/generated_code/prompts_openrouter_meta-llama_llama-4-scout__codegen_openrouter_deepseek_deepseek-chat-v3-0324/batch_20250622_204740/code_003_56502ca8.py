"""
Generated Code Metadata:
========================
Original URL: https://koi-finance.pages.dev
Prompt: "Design a DAO governance system using Koi Finance's ve DAO model, including token locking, vote-escrow NFTs, and revenue sharing mechanisms."
Generated: DETERMINISTIC_56502ca842d5d500
Batch ID: 20250622_204740
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
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VoteEscrowNFT is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    struct LockedBalance {
        uint256 amount;
        uint256 end;
    }

    IERC20 public immutable token;
    uint256 public maxLockDuration;
    uint256 public totalLocked;
    uint256 private _tokenIdCounter;

    mapping(uint256 => LockedBalance) public lockedBalances;
    mapping(address => uint256) public userTokenId;

    event LockCreated(uint256 indexed tokenId, address indexed user, uint256 amount, uint256 duration);
    event LockExtended(uint256 indexed tokenId, uint256 amount, uint256 newDuration);
    event LockWithdrawn(uint256 indexed tokenId, address indexed user, uint256 amount);

    constructor(address _token, string memory _name, string memory _symbol) 
        ERC721(_name, _symbol) 
    {
        token = IERC20(_token);
        maxLockDuration = 4 * 365 days; // 4 years max lock
    }

    function createLock(uint256 _amount, uint256 _duration) external nonReentrant {
        require(_amount > 0, "Cannot lock 0 tokens");
        require(_duration <= maxLockDuration, "Duration exceeds maximum");
        require(_duration > 0, "Duration must be > 0");

        uint256 tokenId = _tokenIdCounter++;
        uint256 end = block.timestamp.add(_duration);

        lockedBalances[tokenId] = LockedBalance({
            amount: _amount,
            end: end
        });

        _safeMint(msg.sender, tokenId);
        userTokenId[msg.sender] = tokenId;
        totalLocked = totalLocked.add(_amount);

        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit LockCreated(tokenId, msg.sender, _amount, _duration);
    }

    function extendLock(uint256 _tokenId, uint256 _additionalDuration) external {
        require(_exists(_tokenId), "Token does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the owner");
        require(_additionalDuration > 0, "Duration must be > 0");

        LockedBalance storage lock = lockedBalances[_tokenId];
        uint256 newEnd = lock.end.add(_additionalDuration);
        require(newEnd <= block.timestamp.add(maxLockDuration), "New duration exceeds maximum");

        lock.end = newEnd;
        emit LockExtended(_tokenId, lock.amount, _additionalDuration);
    }

    function withdraw(uint256 _tokenId) external nonReentrant {
        require(_exists(_tokenId), "Token does not exist");
        require(ownerOf(_tokenId) == msg.sender, "Not the owner");

        LockedBalance memory lock = lockedBalances[_tokenId];
        require(block.timestamp >= lock.end, "Lock not expired");

        uint256 amount = lock.amount;
        totalLocked = totalLocked.sub(amount);
        delete lockedBalances[_tokenId];
        delete userTokenId[msg.sender];

        _burn(_tokenId);
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit LockWithdrawn(_tokenId, msg.sender, amount);
    }

    function balanceOfNFT(uint256 _tokenId) external view returns (uint256) {
        require(_exists(_tokenId), "Token does not exist");
        return lockedBalances[_tokenId].amount;
    }

    function votingPower(uint256 _tokenId) public view returns (uint256) {
        if (!_exists(_tokenId)) return 0;
        
        LockedBalance memory lock = lockedBalances[_tokenId];
        uint256 timeLeft = lock.end > block.timestamp ? lock.end.sub(block.timestamp) : 0;
        
        // Linear voting power based on lock duration remaining
        return lock.amount.mul(timeLeft).div(maxLockDuration);
    }
}

contract Governance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    VoteEscrowNFT public voteEscrow;
    IERC20 public governanceToken;
    IERC20 public revenueToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    uint256 public proposalCount;
    uint256 public votingDelay;
    uint256 public votingPeriod;
    uint256 public quorum;
    uint256 public revenueSharePercentage;

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(uint256 => bool)) public hasVoted;
    mapping(address => uint256) public revenueShares;

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        uint256 startTime,
        uint256 endTime,
        string description
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votingPower);
    event ProposalExecuted(uint256 indexed proposalId);
    event RevenueDistributed(address indexed recipient, uint256 amount);

    constructor(
        address _governanceToken,
        address _revenueToken,
        address _voteEscrow,
        uint256 _votingDelay,
        uint256 _votingPeriod,
        uint256 _quorum,
        uint256 _revenueSharePercentage
    ) {
        governanceToken = IERC20(_governanceToken);
        revenueToken = IERC20(_revenueToken);
        voteEscrow = VoteEscrowNFT(_voteEscrow);
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
        quorum = _quorum;
        revenueSharePercentage = _revenueSharePercentage;
    }

    function propose(string memory _description) external returns (uint256) {
        uint256 tokenId = voteEscrow.userTokenId(msg.sender);
        require(tokenId != 0, "No locked tokens");
        require(voteEscrow.votingPower(tokenId) > 0, "No voting power");

        uint256 proposalId = ++proposalCount;
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = block.timestamp.add(votingDelay);
        newProposal.endTime = block.timestamp.add(votingDelay).add(votingPeriod);
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, msg.sender, newProposal.startTime, newProposal.endTime, _description);
        return proposalId;
    }

    function castVote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 tokenId = voteEscrow.userTokenId(msg.sender);
        require(tokenId != 0, "No locked tokens");
        require(!hasVoted[_proposalId][tokenId], "Already voted");

        uint256 votingPower = voteEscrow.votingPower(tokenId);
        require(votingPower > 0, "No voting power");

        hasVoted[_proposalId][tokenId] = true;

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(votingPower);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votingPower);
        }

        emit VoteCast(msg.sender, _proposalId, _support, votingPower);
    }

    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    function distributeRevenue() external nonReentrant {
        uint256 balance
