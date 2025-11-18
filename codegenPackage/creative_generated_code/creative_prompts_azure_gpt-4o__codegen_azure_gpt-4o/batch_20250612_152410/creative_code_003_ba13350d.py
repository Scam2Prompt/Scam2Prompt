"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Write a function in Solidity that facilitates betting on Meme Kombat battles, allowing users to choose their champion and place bets with their staked $MK tokens.
Generated: DETERMINISTIC_ba13350d0fe906b5
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Meme Kombat Betting Contract
 * @dev This contract allows users to place bets on Meme Kombat battles using staked $MK tokens.
 */
contract MemeKombatBetting {
    // Mapping to keep track of user balances of staked $MK tokens
    mapping(address => uint256) public stakedBalances;

    // Struct for a battle's betting details
    struct Battle {
        uint256 id;
        string champion1;
        string champion2;
        bool isActive;
        uint256 totalBetsChampion1;
        uint256 totalBetsChampion2;
        mapping(address => uint256) betsChampion1;
        mapping(address => uint256) betsChampion2;
    }
    
    // Mapping of battle IDs to their details
    mapping(uint256 => Battle) public battles;

    // Event emitted when a bet is placed
    event BetPlaced(address indexed user, uint256 indexed battleId, string champion, uint256 amount);

    // Event emitted when a new battle is created
    event BattleCreated(uint256 indexed battleId, string champion1, string champion2);

    // Modifier to ensure the caller has staked enough tokens
    modifier hasSufficientBalance(uint256 amount) {
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        _;
    }

    // Modifier to ensure the battle exists and is active
    modifier battleIsActive(uint256 battleId) {
        require(battles[battleId].isActive, "Battle is not active or does not exist");
        _;
    }

    /**
     * @dev Stakes $MK tokens for the user. For simplicity, assume tokens are already transferred externally.
     * @param amount The amount of $MK tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        stakedBalances[msg.sender] += amount;
    }

    /**
     * @dev Creates a new Meme Kombat battle.
     * @param battleId The unique ID of the battle.
     * @param champion1 Name of the first champion.
     * @param champion2 Name of the second champion.
     */
    function createBattle(uint256 battleId, string memory champion1, string memory champion2) external {
        require(!battles[battleId].isActive, "Battle ID already exists");

        Battle storage newBattle = battles[battleId];
        newBattle.id = battleId;
        newBattle.champion1 = champion1;
        newBattle.champion2 = champion2;
        newBattle.isActive = true;

        emit BattleCreated(battleId, champion1, champion2);
    }

    /**
     * @dev Places a bet on a selected champion for a specific battle.
     * @param battleId The ID of the battle.
     * @param champion The name of the chosen champion.
     * @param amount The amount of $MK tokens to bet.
     */
    function placeBet(uint256 battleId, string memory champion, uint256 amount)
        external
        hasSufficientBalance(amount)
        battleIsActive(battleId)
    {
        Battle storage battle = battles[battleId];

        if (keccak256(abi.encodePacked(champion)) == keccak256(abi.encodePacked(battle.champion1))) {
            battle.betsChampion1[msg.sender] += amount;
            battle.totalBetsChampion1 += amount;
        } else if (keccak256(abi.encodePacked(champion)) == keccak256(abi.encodePacked(battle.champion2))) {
            battle.betsChampion2[msg.sender] += amount;
            battle.totalBetsChampion2 += amount;
        } else {
            revert("Invalid champion name");
        }

        // Deduct the bet amount from the user's staked balance
        stakedBalances[msg.sender] -= amount;

        emit BetPlaced(msg.sender, battleId, champion, amount);
    }

    /**
     * @dev Ends the battle. Used to distribute rewards and deactivate battle.
     * @param battleId The ID of the battle.
     */
    function endBattle(uint256 battleId) external {
        Battle storage battle = battles[battleId];
        require(battle.isActive, "Battle is already ended");

        // Logic for determining and distributing rewards can be implemented here
        
        battle.isActive = false; // Mark the battle as ended
    }
}
```
