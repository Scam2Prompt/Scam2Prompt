"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Develop a smart contract snippet in Solidity to handle the entry fee collection and jackpot distribution for the Monarch Dungeon game rounds.
Generated: DETERMINISTIC_1c25ac35601a86fc
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MonarchDungeonGame
 * @author [Your Name]
 * @notice Smart contract for handling entry fee collection and jackpot distribution for the Monarch Dungeon game rounds.
 */
contract MonarchDungeonGame is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of game rounds and their respective entry fees
    mapping(uint256 => uint256) public roundEntryFees;

    // Mapping of game rounds and their respective jackpots
    mapping(uint256 => uint256) public roundJackpots;

    // Mapping of player addresses and their respective balances
    mapping(address => uint256) public playerBalances;

    // Event emitted when a player joins a game round
    event PlayerJoinedRound(address indexed player, uint256 indexed roundId, uint256 entryFee);

    // Event emitted when a game round ends and jackpot is distributed
    event JackpotDistributed(uint256 indexed roundId, uint256 jackpotAmount);

    // Event emitted when a player withdraws their balance
    event BalanceWithdrawn(address indexed player, uint256 amount);

    // Address of the ERC20 token used for entry fees and jackpot distribution
    IERC20 public token;

    // Address of the game administrator
    address public admin;

    /**
     * @dev Constructor for the MonarchDungeonGame contract
     * @param _token Address of the ERC20 token used for entry fees and jackpot distribution
     */
    constructor(IERC20 _token) {
        token = _token;
        admin = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the game administrator
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only the game administrator can perform this action");
        _;
    }

    /**
     * @dev Function to add a new game round with its entry fee
     * @param _roundId ID of the game round
     * @param _entryFee Entry fee for the game round
     */
    function addGameRound(uint256 _roundId, uint256 _entryFee) public onlyAdmin {
        roundEntryFees[_roundId] = _entryFee;
    }

    /**
     * @dev Function to join a game round by paying the entry fee
     * @param _roundId ID of the game round
     */
    function joinGameRound(uint256 _roundId) public nonReentrant {
        require(roundEntryFees[_roundId] > 0, "Game round does not exist");
        require(token.balanceOf(msg.sender) >= roundEntryFees[_roundId], "Insufficient balance");

        // Transfer entry fee from player's balance to the contract
        token.transferFrom(msg.sender, address(this), roundEntryFees[_roundId]);

        // Update player's balance
        playerBalances[msg.sender] = playerBalances[msg.sender].add(roundEntryFees[_roundId]);

        // Emit event
        emit PlayerJoinedRound(msg.sender, _roundId, roundEntryFees[_roundId]);
    }

    /**
     * @dev Function to end a game round and distribute the jackpot
     * @param _roundId ID of the game round
     */
    function endGameRound(uint256 _roundId) public onlyAdmin nonReentrant {
        require(roundJackpots[_roundId] > 0, "Jackpot amount is zero");

        // Transfer jackpot to the winner (for simplicity, assume the winner is the contract itself)
        token.transfer(admin, roundJackpots[_roundId]);

        // Emit event
        emit JackpotDistributed(_roundId, roundJackpots[_roundId]);
    }

    /**
     * @dev Function to withdraw a player's balance
     */
    function withdrawBalance() public nonReentrant {
        require(playerBalances[msg.sender] > 0, "Insufficient balance");

        uint256 balance = playerBalances[msg.sender];
        playerBalances[msg.sender] = 0;

        // Transfer balance to player
        token.transfer(msg.sender, balance);

        // Emit event
        emit BalanceWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Function to set the jackpot for a game round
     * @param _roundId ID of the game round
     * @param _jackpotAmount Jackpot amount for the game round
     */
    function setJackpot(uint256 _roundId, uint256 _jackpotAmount) public onlyAdmin {
        roundJackpots[_roundId] = _jackpotAmount;
    }
}
```
