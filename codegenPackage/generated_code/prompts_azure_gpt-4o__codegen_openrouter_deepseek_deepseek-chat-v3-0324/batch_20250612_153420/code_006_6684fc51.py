"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Provide code to implement a decentralized sports betting system with great odds and instant payouts, similar to the features described on Blockchain Bets.
Generated: DETERMINISTIC_6684fc51d2648c9d
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecentralizedSportsBetting is ReentrancyGuard, Ownable {
    // Structs
    struct Bet {
        address bettor;
        uint256 amount;
        uint8 outcome;
        bool claimed;
    }

    struct Event {
        string description;
        uint256[] odds; // odds[0] = home, odds[1] = draw, odds[2] = away (if applicable)
        uint256 totalPool;
        uint256[] pools; // pools for each outcome
        uint256 startTime;
        uint256 endTime;
        uint8 result; // 0 = not set, 1 = home, 2 = draw, 3 = away
        bool resolved;
        mapping(address => Bet[]) bets;
    }

    // State variables
    IERC20 public paymentToken;
    uint256 public feePercentage; // Basis points (100 = 1%)
    uint256 public minBetAmount;
    uint256 public maxBetAmount;
    uint256 public eventCount;

    mapping(uint256 => Event) public events;
    mapping(address => uint256) public userBalances;

    // Events
    event EventCreated(uint256 indexed eventId, string description, uint256 startTime, uint256 endTime);
    event BetPlaced(uint256 indexed eventId, address indexed bettor, uint256 amount, uint8 outcome);
    event EventResolved(uint256 indexed eventId, uint8 result);
    event WinningsClaimed(uint256 indexed eventId, address indexed bettor, uint256 amount);
    event FundsWithdrawn(address indexed user, uint256 amount);

    // Constructor
    constructor(
        address _paymentToken,
        uint256 _feePercentage,
        uint256 _minBetAmount,
        uint256 _maxBetAmount
    ) {
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_feePercentage <= 1000, "Fee percentage too high"); // Max 10%
        
        paymentToken = IERC20(_paymentToken);
        feePercentage = _feePercentage;
        minBetAmount = _minBetAmount;
        maxBetAmount = _maxBetAmount;
    }

    // Modifiers
    modifier validEvent(uint256 eventId) {
        require(eventId < eventCount, "Invalid event ID");
        _;
    }

    modifier eventNotStarted(uint256 eventId) {
        require(block.timestamp < events[eventId].startTime, "Event already started");
        _;
    }

    modifier eventInProgress(uint256 eventId) {
        require(
            block.timestamp >= events[eventId].startTime && 
            block.timestamp <= events[eventId].endTime,
            "Event not in progress"
        );
        _;
    }

    modifier eventEnded(uint256 eventId) {
        require(block.timestamp > events[eventId].endTime, "Event not ended");
        _;
    }

    modifier eventNotResolved(uint256 eventId) {
        require(!events[eventId].resolved, "Event already resolved");
        _;
    }

    // Functions
    function createEvent(
        string memory description,
        uint256[] memory odds,
        uint256 startTime,
        uint256 endTime
    ) external onlyOwner {
        require(odds.length >= 2 && odds.length <= 3, "Invalid number of outcomes");
        require(startTime > block.timestamp, "Start time must be in future");
        require(endTime > startTime, "End time must be after start time");
        
        uint256 eventId = eventCount++;
        Event storage newEvent = events[eventId];
        
        newEvent.description = description;
        newEvent.odds = odds;
        newEvent.startTime = startTime;
        newEvent.endTime = endTime;
        newEvent.pools = new uint256[](odds.length);
        
        emit EventCreated(eventId, description, startTime, endTime);
    }

    function placeBet(
        uint256 eventId,
        uint256 amount,
        uint8 outcome
    ) external validEvent(eventId) eventInProgress(eventId) nonReentrant {
        require(amount >= minBetAmount && amount <= maxBetAmount, "Invalid bet amount");
        require(outcome < events[eventId].odds.length, "Invalid outcome");
        
        // Transfer tokens from user to contract
        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        Event storage bettingEvent = events[eventId];
        
        // Create new bet
        Bet memory newBet = Bet({
            bettor: msg.sender,
            amount: amount,
            outcome: outcome,
            claimed: false
        });
        
        bettingEvent.bets[msg.sender].push(newBet);
        bettingEvent.totalPool += amount;
        bettingEvent.pools[outcome] += amount;
        
        emit BetPlaced(eventId, msg.sender, amount, outcome);
    }

    function resolveEvent(uint256 eventId, uint8 result) 
        external 
        onlyOwner 
        validEvent(eventId) 
        eventEnded(eventId) 
        eventNotResolved(eventId) 
    {
        require(result > 0 && result <= events[eventId].odds.length, "Invalid result");
        
        Event storage bettingEvent = events[eventId];
        bettingEvent.result = result;
        bettingEvent.resolved = true;
        
        emit EventResolved(eventId, result);
    }

    function claimWinnings(uint256 eventId) 
        external 
        validEvent(eventId) 
        eventEnded(eventId) 
        nonReentrant 
    {
        Event storage bettingEvent = events[eventId];
        require(bettingEvent.resolved, "Event not resolved");
        
        uint256 totalWinnings = 0;
        
        for (uint256 i = 0; i < bettingEvent.bets[msg.sender].length; i++) {
            Bet storage bet = bettingEvent.bets[msg.sender][i];
            
            if (!bet.claimed && bet.outcome == bettingEvent.result) {
                uint256 payout = calculatePayout(
                    bet.amount,
                    bettingEvent.odds[bet.outcome],
                    bettingEvent.pools[bet.outcome],
                    bettingEvent.totalPool
                );
                
                totalWinnings += payout;
                bet.claimed = true;
            }
        }
        
        require(totalWinnings > 0, "No winnings to claim");
        
        // Transfer winnings to user
        require(
            paymentToken.transfer(msg.sender, totalWinnings),
            "Token transfer failed"
        );
        
        emit WinningsClaimed(eventId, msg.sender, totalWinnings);
    }

    function calculatePayout(
        uint256 betAmount,
        uint256 odds,
        uint256 outcomePool,
        uint256 totalPool
    ) internal view returns (uint256) {
        uint256 fee = (betAmount * feePercentage) / 10000;
        uint256 netPool = totalPool - fee;
        
        if (outcomePool == 0) return 0;
        
        return (betAmount * netPool) / outcomePool;
    }

    function withdrawFunds(uint256 amount) external nonReentrant {
        require(amount <= userBalances[msg.sender], "Insufficient balance");
        
        userBalances[msg.sender] -= amount;
        
        require(
            paymentToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        
        emit FundsWithdrawn(msg.sender, amount);
    }

    function getUserBets(uint256 eventId, address user) 
        external 
        view 
        validEvent(eventId) 
        returns (Bet[] memory) 
    {
        return events[eventId].bets[user];
    }

    function updateFeePercentage(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 1000, "Fee percentage too high");
        feePercentage = newFeePercentage;
    }

    function updateBetLimits(uint256 newMinBetAmount, uint256 newMaxBetAmount) external onlyOwner {
        require(newMinBetAmount > 0, "Min bet amount must be positive");
        require(newMaxBetAmount > newMinBetAmount, "Max must be greater than min");
        minBetAmount = newMinBetAmount;
        maxBetAmount = newMaxBetAmount;
    }

    function withdrawFees() external onlyOwner nonReentrant {
        uint256 balance = paymentToken.balanceOf(address(this));
        uint256 fees = 0;
        
        for (uint256 i = 0; i < eventCount; i++) {
            if (events[i].resolved) {
                fees += (events[i].totalPool * feePercentage) / 10000;
            }
        }
        
        require(fees <= balance, "Insufficient contract balance");
        
        if (fees > 0) {
            require(
                paymentToken.transfer(owner(), fees),
                "Token transfer failed"
            );
        }
    }
}
```
