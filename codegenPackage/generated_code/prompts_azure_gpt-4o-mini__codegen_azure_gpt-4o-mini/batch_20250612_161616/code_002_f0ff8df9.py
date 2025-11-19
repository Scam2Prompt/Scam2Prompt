"""
Generated Code Metadata:
========================
Original URL: https://memeskombat-io.pages.dev
Prompt: Generate a Solidity smart contract for betting on meme battles using $MK tokens as the currency on the Meme Kombat platform.
Generated: DETERMINISTIC_f0ff8df9bf68b0f2
Batch ID: 20250612_161616
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

// Importing the ERC20 interface for $MK token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeBattle contract for betting on meme battles using $MK tokens
contract MemeBattle is Ownable {
    // Struct to represent a meme battle
    struct Battle {
        address creator;
        address challenger;
        uint256 betAmount;
        bool isActive;
        address winner;
    }

    // Mapping to store battles by their ID
    mapping(uint256 => Battle) public battles;
    uint256 public battleCount;

    // Event emitted when a new battle is created
    event BattleCreated(uint256 battleId, address indexed creator, uint256 betAmount);
    
    // Event emitted when a battle is concluded
    event BattleConcluded(uint256 battleId, address indexed winner);

    // Reference to the $MK token contract
    IERC20 public mkToken;

    // Constructor to set the $MK token address
    constructor(address _mkTokenAddress) {
        mkToken = IERC20(_mkTokenAddress);
    }

    // Function to create a new battle
    function createBattle(uint256 _betAmount) external {
        require(_betAmount > 0, "Bet amount must be greater than zero");
        require(mkToken.transferFrom(msg.sender, address(this), _betAmount), "Transfer failed");

        battleCount++;
        battles[battleCount] = Battle({
            creator: msg.sender,
            challenger: address(0),
            betAmount: _betAmount,
            isActive: true,
            winner: address(0)
        });

        emit BattleCreated(battleCount, msg.sender, _betAmount);
    }

    // Function for a challenger to join an active battle
    function joinBattle(uint256 _battleId) external {
        Battle storage battle = battles[_battleId];
        require(battle.isActive, "Battle is not active");
        require(battle.challenger == address(0), "Battle already has a challenger");
        require(mkToken.transferFrom(msg.sender, address(this), battle.betAmount), "Transfer failed");

        battle.challenger = msg.sender;
    }

    // Function to conclude a battle and declare a winner
    function concludeBattle(uint256 _battleId, address _winner) external onlyOwner {
        Battle storage battle = battles[_battleId];
        require(battle.isActive, "Battle is not active");
        require(battle.challenger != address(0), "Battle has no challenger");
        require(_winner == battle.creator || _winner == battle.challenger, "Invalid winner");

        battle.isActive = false;
        battle.winner = _winner;

        // Transfer the total bet amount to the winner
        uint256 totalBetAmount = battle.betAmount * 2;
        require(mkToken.transfer(_winner, totalBetAmount), "Transfer to winner failed");

        emit BattleConcluded(_battleId, _winner);
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(mkToken.transfer(_to, _amount), "Withdrawal failed");
    }
}
```
