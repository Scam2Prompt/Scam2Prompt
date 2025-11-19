"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Develop a feature in Solidity for Meme Kombat that supports the introduction of new battle types and rewards in Season 2, ensuring compatibility with the existing staking and betting mechanisms.
Generated: DETERMINISTIC_8b0bc54495010166
Batch ID: 20250612_152924
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MemeKombatSeason2 is Ownable, ReentrancyGuard {
    // Battle types for Season 2
    enum BattleType {
        CLASSIC,    // 0
        TEAM,       // 1
        ROYALE,     // 2
        SPECIAL     // 3
    }

    // Battle struct
    struct Battle {
        uint256 id;
        BattleType battleType;
        uint256[] memeIds;
        uint256 startTime;
        uint256 endTime;
        uint256 totalPrizePool;
        bool isActive;
        bool isSettled;
    }

    // Reward struct
    struct Reward {
        uint256 battleId;
        uint256 winnerMemeId;
        address[] winners;
        uint256[] rewards;
    }

    // Staking contract interface
    IERC20 public stakingToken;

    // Battles mapping
    mapping(uint256 => Battle) public battles;
    mapping(BattleType => uint256) public battleTypeMultipliers;

    // Rewards mapping
    mapping(uint256 => Reward) public battleRewards;
    mapping(address => uint256) public userRewards;

    // Events
    event BattleCreated(uint256 indexed battleId, BattleType battleType);
    event BattleStarted(uint256 indexed battleId);
    event BattleEnded(uint256 indexed battleId);
    event RewardDistributed(uint256 indexed battleId, address[] winners, uint256[] rewards);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyActiveBattle(uint256 battleId) {
        require(battles[battleId].isActive, "Battle is not active");
        _;
    }

    modifier onlyUnsettledBattle(uint256 battleId) {
        require(!battles[battleId].isSettled, "Battle is already settled");
        _;
    }

    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
        
        // Initialize battle type multipliers
        battleTypeMultipliers[BattleType.CLASSIC] = 100; // 1x
        battleTypeMultipliers[BattleType.TEAM] = 150;    // 1.5x
        battleTypeMultipliers[BattleType.ROYALE] = 200;  // 2x
        battleTypeMultipliers[BattleType.SPECIAL] = 300; // 3x
    }

    /**
     * @dev Create a new battle
     */
    function createBattle(
        BattleType battleType,
        uint256[] memory memeIds,
        uint256 startTime,
        uint256 duration
    ) external onlyOwner {
        uint256 battleId = uint256(keccak256(abi.encodePacked(block.timestamp, battleType, memeIds[0])));
        
        battles[battleId] = Battle({
            id: battleId,
            battleType: battleType,
            memeIds: memeIds,
            startTime: startTime,
            endTime: startTime + duration,
            totalPrizePool: 0,
            isActive: false,
            isSettled: false
        });

        emit BattleCreated(battleId, battleType);
    }

    /**
     * @dev Start a battle
     */
    function startBattle(uint256 battleId) external onlyOwner {
        Battle storage battle = battles[battleId];
        require(block.timestamp >= battle.startTime, "Battle start time not reached");
        require(!battle.isActive, "Battle already active");
        
        battle.isActive = true;
        emit BattleStarted(battleId);
    }

    /**
     * @dev End a battle and prepare for rewards distribution
     */
    function endBattle(uint256 battleId, uint256 winnerMemeId) external onlyOwner onlyActiveBattle(battleId) {
        Battle storage battle = battles[battleId];
        require(block.timestamp >= battle.endTime, "Battle end time not reached");
        
        battle.isActive = false;
        emit BattleEnded(battleId);
    }

    /**
     * @dev Distribute rewards for a battle
     */
    function distributeRewards(
        uint256 battleId,
        address[] memory winners,
        uint256[] memory rewards
    ) external onlyOwner onlyUnsettledBattle(battleId) {
        require(winners.length == rewards.length, "Arrays length mismatch");
        
        Battle storage battle = battles[battleId];
        uint256 totalRewards = 0;
        
        for (uint256 i = 0; i < rewards.length; i++) {
            totalRewards += rewards[i];
            userRewards[winners[i]] += rewards[i];
        }
        
        require(totalRewards <= battle.totalPrizePool, "Rewards exceed prize pool");
        
        battleRewards[battleId] = Reward({
            battleId: battleId,
            winnerMemeId: battle.memeIds[0], // Placeholder - actual winner should be set
            winners: winners,
            rewards: rewards
        });
        
        battle.isSettled = true;
        battle.totalPrizePool -= totalRewards;
        
        emit RewardDistributed(battleId, winners, rewards);
    }

    /**
     * @dev Claim rewards by user
     */
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        
        userRewards[msg.sender] = 0;
        require(stakingToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Add to prize pool (can be called by staking contract)
     */
    function addToPrizePool(uint256 battleId, uint256 amount) external {
        require(amount > 0, "Amount must be positive");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        battles[battleId].totalPrizePool += amount;
    }

    /**
     * @dev Get battle details
     */
    function getBattle(uint256 battleId) external view returns (Battle memory) {
        return battles[battleId];
    }

    /**
     * @dev Get reward details for a battle
     */
    function getBattleReward(uint256 battleId) external view returns (Reward memory) {
        return battleRewards[battleId];
    }

    /**
     * @dev Get user's pending rewards
     */
    function getUserRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     */
    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
