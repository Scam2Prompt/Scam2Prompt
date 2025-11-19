"""
Generated Code Metadata:
========================
Original URL: https://memeskombat.pages.dev
Prompt: Write a function in Solidity that facilitates betting on Meme Kombat battles, allowing users to choose their champion and place bets with their staked $MK tokens.
Generated: DETERMINISTIC_ba13350d0fe906b5
Batch ID: 20250612_152410
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

contract MemeKombatBetting is Ownable, ReentrancyGuard {
    IERC20 public mkToken;

    enum BattleStatus { PENDING, ACTIVE, COMPLETED }
    enum BattleResult { PENDING, CHAMPION1_WON, CHAMPION2_WON, DRAW }

    struct Battle {
        uint256 battleId;
        uint256 champion1Id;
        uint256 champion2Id;
        uint256 startTime;
        uint256 endTime;
        BattleStatus status;
        BattleResult result;
        uint256 totalPoolChampion1;
        uint256 totalPoolChampion2;
    }

    struct Bet {
        address bettor;
        uint256 amount;
        uint256 championId;
        bool claimed;
    }

    mapping(uint256 => Battle) public battles;
    mapping(address => mapping(uint256 => Bet)) public userBets;
    mapping(uint256 => uint256) public battleCounters;

    uint256 public minBetAmount;
    uint256 public maxBetAmount;
    uint256 public currentBattleId;

    event BattleCreated(
        uint256 indexed battleId,
        uint256 champion1Id,
        uint256 champion2Id,
        uint256 startTime,
        uint256 endTime
    );
    event BetPlaced(
        address indexed bettor,
        uint256 indexed battleId,
        uint256 championId,
        uint256 amount
    );
    event BattleResultSet(
        uint256 indexed battleId,
        BattleResult result
    );
    event WinningsClaimed(
        address indexed bettor,
        uint256 indexed battleId,
        uint256 amount
    );

    constructor(address _mkTokenAddress, uint256 _minBetAmount, uint256 _maxBetAmount) {
        mkToken = IERC20(_mkTokenAddress);
        minBetAmount = _minBetAmount;
        maxBetAmount = _maxBetAmount;
    }

    function createBattle(
        uint256 _champion1Id,
        uint256 _champion2Id,
        uint256 _startTime,
        uint256 _duration
    ) external onlyOwner {
        require(_champion1Id != _champion2Id, "Champions must be different");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_duration > 0, "Duration must be positive");

        currentBattleId++;
        uint256 endTime = _startTime + _duration;

        battles[currentBattleId] = Battle({
            battleId: currentBattleId,
            champion1Id: _champion1Id,
            champion2Id: _champion2Id,
            startTime: _startTime,
            endTime: endTime,
            status: BattleStatus.PENDING,
            result: BattleResult.PENDING,
            totalPoolChampion1: 0,
            totalPoolChampion2: 0
        });

        emit BattleCreated(currentBattleId, _champion1Id, _champion2Id, _startTime, endTime);
    }

    function placeBet(uint256 _battleId, uint256 _championId, uint256 _amount) external nonReentrant {
        require(_battleId <= currentBattleId && _battleId > 0, "Invalid battle ID");
        Battle storage battle = battles[_battleId];
        require(battle.status == BattleStatus.PENDING, "Battle not in betting phase");
        require(block.timestamp < battle.startTime, "Betting period has ended");
        require(_championId == battle.champion1Id || _championId == battle.champion2Id, "Invalid champion ID");
        require(_amount >= minBetAmount && _amount <= maxBetAmount, "Bet amount out of bounds");
        require(userBets[msg.sender][_battleId].amount == 0, "Already placed a bet for this battle");

        require(mkToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userBets[msg.sender][_battleId] = Bet({
            bettor: msg.sender,
            amount: _amount,
            championId: _championId,
            claimed: false
        });

        if (_championId == battle.champion1Id) {
            battle.totalPoolChampion1 += _amount;
        } else {
            battle.totalPoolChampion2 += _amount;
        }

        emit BetPlaced(msg.sender, _battleId, _championId, _amount);
    }

    function setBattleResult(uint256 _battleId, BattleResult _result) external onlyOwner {
        require(_battleId <= currentBattleId && _battleId > 0, "Invalid battle ID");
        Battle storage battle = battles[_battleId];
        require(battle.status == BattleStatus.ACTIVE, "Battle not active");
        require(block.timestamp >= battle.endTime, "Battle not yet finished");
        require(_result != BattleResult.PENDING, "Invalid result");

        battle.result = _result;
        battle.status = BattleStatus.COMPLETED;

        emit BattleResultSet(_battleId, _result);
    }

    function claimWinnings(uint256 _battleId) external nonReentrant {
        require(_battleId <= currentBattleId && _battleId > 0, "Invalid battle ID");
        Battle storage battle = battles[_battleId];
        require(battle.status == BattleStatus.COMPLETED, "Battle not completed");
        require(battle.result != BattleResult.PENDING, "Result not set");

        Bet storage bet = userBets[msg.sender][_battleId];
        require(bet.amount > 0, "No bet placed");
        require(!bet.claimed, "Winnings already claimed");

        uint256 winnings = 0;

        if (battle.result == BattleResult.CHAMPION1_WON && bet.championId == battle.champion1Id) {
            winnings = calculateWinnings(bet.amount, battle.totalPoolChampion1, battle.totalPoolChampion2);
        } else if (battle.result == BattleResult.CHAMPION2_WON && bet.championId == battle.champion2Id) {
            winnings = calculateWinnings(bet.amount, battle.totalPoolChampion2, battle.totalPoolChampion1);
        } else if (battle.result == BattleResult.DRAW) {
            winnings = bet.amount;
        }

        require(winnings > 0, "No winnings to claim");
        bet.claimed = true;

        require(mkToken.transfer(msg.sender, winnings), "Token transfer failed");

        emit WinningsClaimed(msg.sender, _battleId, winnings);
    }

    function calculateWinnings(
        uint256 _betAmount,
        uint256 _winningPool,
        uint256 _losingPool
    ) internal pure returns (uint256) {
        uint256 totalPool = _winningPool + _losingPool;
        return (_betAmount * totalPool) / _winningPool;
    }

    function updateBetLimits(uint256 _minBetAmount, uint256 _maxBetAmount) external onlyOwner {
        require(_minBetAmount > 0, "Min bet amount must be positive");
        require(_maxBetAmount > _minBetAmount, "Max must be greater than min");
        minBetAmount = _minBetAmount;
        maxBetAmount = _maxBetAmount;
    }

    function startBattle(uint256 _battleId) external onlyOwner {
        require(_battleId <= currentBattleId && _battleId > 0, "Invalid battle ID");
        Battle storage battle = battles[_battleId];
        require(battle.status == BattleStatus.PENDING, "Battle not pending");
        require(block.timestamp >= battle.startTime, "Battle not ready to start");

        battle.status = BattleStatus.ACTIVE;
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(mkToken.transfer(owner(), _amount), "Token transfer failed");
    }
}
```
