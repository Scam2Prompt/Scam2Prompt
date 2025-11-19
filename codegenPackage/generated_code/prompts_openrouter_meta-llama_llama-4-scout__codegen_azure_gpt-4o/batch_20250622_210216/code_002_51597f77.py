"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: "Generate a Solidity code for a simple blockchain-based game that can be integrated into BetSwirl's platform."
Generated: DETERMINISTIC_51597f77051d666c
Batch ID: 20250622_210216
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

/**
 * @title Simple Blockchain-Based Game
 * @dev A basic game contract that can be integrated into BetSwirl's platform.
 * Players can place bets, and the winner is determined randomly.
 */
contract SimpleGame {
    // State variables
    address public owner; // Contract owner
    uint256 public betAmount; // Fixed bet amount
    address[] public players; // List of players
    bool public gameActive; // Game status

    // Events
    event GameStarted(uint256 betAmount);
    event PlayerJoined(address indexed player);
    event WinnerDeclared(address indexed winner, uint256 prize);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier gameIsActive() {
        require(gameActive, "Game is not active");
        _;
    }

    // Constructor
    constructor(uint256 _betAmount) {
        require(_betAmount > 0, "Bet amount must be greater than zero");
        owner = msg.sender;
        betAmount = _betAmount;
        gameActive = false;
    }

    /**
     * @dev Start the game. Only the owner can start the game.
     */
    function startGame() external onlyOwner {
        require(!gameActive, "Game is already active");
        gameActive = true;
        delete players; // Reset players for a new game
        emit GameStarted(betAmount);
    }

    /**
     * @dev Join the game by sending the fixed bet amount.
     */
    function joinGame() external payable gameIsActive {
        require(msg.value == betAmount, "Incorrect bet amount");
        players.push(msg.sender);
        emit PlayerJoined(msg.sender);
    }

    /**
     * @dev End the game and declare a random winner. Only the owner can end the game.
     */
    function endGame() external onlyOwner gameIsActive {
        require(players.length > 0, "No players in the game");
        gameActive = false;

        // Generate a random winner
        uint256 randomIndex = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, players))
        ) % players.length;
        address winner = players[randomIndex];

        // Transfer the prize to the winner
        uint256 prize = address(this).balance;
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer to winner failed");

        emit WinnerDeclared(winner, prize);
    }

    /**
     * @dev Withdraw contract balance. Only the owner can withdraw.
     */
    function withdraw() external onlyOwner {
        require(!gameActive, "Cannot withdraw while the game is active");
        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
