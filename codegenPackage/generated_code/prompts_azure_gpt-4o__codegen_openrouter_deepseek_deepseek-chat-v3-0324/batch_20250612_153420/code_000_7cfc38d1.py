"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized betting platform that incorporates token staking functionality, similar to the $BCB staking system described on Blockchain Bets.
Generated: DETERMINISTIC_7cfc38d1f64cdce7
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedBetting is Ownable, ReentrancyGuard {
    IERC20 public bettingToken;

    struct Bet {
        uint256 amount;
        uint256 eventId;
        uint256 outcome;
        bool claimed;
    }

    struct StakingInfo {
        uint256 amount;
        uint256 stakedAt;
        uint256 unlockTime;
        bool isStaked;
    }

    struct BettingEvent {
        uint256 id;
        string description;
        uint256[] possibleOutcomes;
        uint256 startTime;
        uint256 endTime;
        bool isSettled;
        uint256 winningOutcome;
    }

    mapping(address => Bet[]) public userBets;
    mapping(address => StakingInfo) public stakers;
    mapping(uint256 => BettingEvent) public events;
    mapping(uint256 => mapping(uint256 => uint256)) public totalBetsPerOutcome;

    uint256 public totalStaked;
    uint256 public stakingLockDuration;
    uint256 public stakingRewardRate; // Reward per token per second

    event BetPlaced(address indexed user, uint256 eventId, uint256 outcome, uint256 amount);
    event BetClaimed(address indexed user, uint256 eventId, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EventCreated(uint256 indexed eventId, string description);
    event EventSettled(uint256 indexed eventId, uint256 winningOutcome);

    constructor(address _tokenAddress, uint256 _stakingLockDuration, uint256 _stakingRewardRate) {
        bettingToken = IERC20(_tokenAddress);
        stakingLockDuration = _stakingLockDuration;
        stakingRewardRate = _stakingRewardRate;
    }

    function createEvent(
        uint256 _eventId,
        string memory _description,
        uint256[] memory _possibleOutcomes,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(events[_eventId].id == 0, "Event already exists");
        require(_startTime < _endTime, "Invalid time range");
        require(_possibleOutcomes.length > 1, "At least 2 outcomes required");

        events[_eventId] = BettingEvent({
            id: _eventId,
            description: _description,
            possibleOutcomes: _possibleOutcomes,
            startTime: _startTime,
            endTime: _endTime,
            isSettled: false,
            winningOutcome: 0
        });

        emit EventCreated(_eventId, _description);
    }

    function placeBet(uint256 _eventId, uint256 _outcome, uint256 _amount) external nonReentrant {
        BettingEvent storage bettingEvent = events[_eventId];
        require(bettingEvent.id != 0, "Event does not exist");
        require(block.timestamp >= bettingEvent.startTime, "Event not started");
        require(block.timestamp < bettingEvent.endTime, "Event ended");
        require(!bettingEvent.isSettled, "Event already settled");
        require(_amount > 0, "Amount must be greater than 0");
        require(isValidOutcome(_eventId, _outcome), "Invalid outcome");

        bool outcomeExists = false;
        for (uint256 i = 0; i < bettingEvent.possibleOutcomes.length; i++) {
            if (bettingEvent.possibleOutcomes[i] == _outcome) {
                outcomeExists = true;
                break;
            }
        }
        require(outcomeExists, "Outcome not valid for this event");

        require(bettingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userBets[msg.sender].push(Bet({
            amount: _amount,
            eventId: _eventId,
            outcome: _outcome,
            claimed: false
        }));

        totalBetsPerOutcome[_eventId][_outcome] += _amount;

        emit BetPlaced(msg.sender, _eventId, _outcome, _amount);
    }

    function settleEvent(uint256 _eventId, uint256 _winningOutcome) external onlyOwner {
        BettingEvent storage bettingEvent = events[_eventId];
        require(bettingEvent.id != 0, "Event does not exist");
        require(block.timestamp >= bettingEvent.endTime, "Event not ended");
        require(!bettingEvent.isSettled, "Event already settled");
        require(isValidOutcome(_eventId, _winningOutcome), "Invalid winning outcome");

        bettingEvent.isSettled = true;
        bettingEvent.winningOutcome = _winningOutcome;

        emit EventSettled(_eventId, _winningOutcome);
    }

    function claimBet(uint256 _eventId) external nonReentrant {
        BettingEvent storage bettingEvent = events[_eventId];
        require(bettingEvent.isSettled, "Event not settled");

        uint256 totalWinnings = 0;
        uint256 totalBetsOnWinningOutcome = totalBetsPerOutcome[_eventId][bettingEvent.winningOutcome];
        uint256 totalBetsOnEvent = 0;

        for (uint256 i = 0; i < bettingEvent.possibleOutcomes.length; i++) {
            totalBetsOnEvent += totalBetsPerOutcome[_eventId][bettingEvent.possibleOutcomes[i]];
        }

        for (uint256 i = 0; i < userBets[msg.sender].length; i++) {
            Bet storage bet = userBets[msg.sender][i];
            if (bet.eventId == _eventId && !bet.claimed) {
                if (bet.outcome == bettingEvent.winningOutcome) {
                    uint256 winningAmount = (bet.amount * totalBetsOnEvent) / totalBetsOnWinningOutcome;
                    totalWinnings += winningAmount;
                }
                bet.claimed = true;
            }
        }

        require(totalWinnings > 0, "No winnings to claim");
        require(bettingToken.transfer(msg.sender, totalWinnings), "Token transfer failed");

        emit BetClaimed(msg.sender, _eventId, totalWinnings);
    }

    function stakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(!stakers[msg.sender].isStaked, "Already staked");

        require(bettingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakers[msg.sender] = StakingInfo({
            amount: _amount,
            stakedAt: block.timestamp,
            unlockTime: block.timestamp + stakingLockDuration,
            isStaked: true
        });

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    function unstakeTokens() external nonReentrant {
        StakingInfo storage staker = stakers[msg.sender];
        require(staker.isStaked, "No active stake");
        require(block.timestamp >= staker.unlockTime, "Stake is still locked");

        uint256 amount = staker.amount;
        uint256 reward = calculateReward(msg.sender);

        totalStaked -= amount;
        staker.isStaked = false;
        staker.amount = 0;

        uint256 totalToTransfer = amount + reward;
        require(bettingToken.transfer(msg.sender, totalToTransfer), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
        if (reward > 0) {
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function claimReward() external nonReentrant {
        StakingInfo storage staker = stakers[msg.sender];
        require(staker.isStaked, "No active stake");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        staker.stakedAt = block.timestamp;

        require(bettingToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address _staker) public view returns (uint256) {
        StakingInfo storage staker = stakers[_staker];
        if (!staker.isStaked) return 0;

        uint256 stakingDuration = block.timestamp - staker.stakedAt;
        return (staker.amount * stakingDuration * stakingRewardRate) / 1e18;
    }

    function isValidOutcome(uint256 _eventId, uint256 _outcome) private view returns (bool) {
        for (uint256 i = 0; i < events[_eventId].
