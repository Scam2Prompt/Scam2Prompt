"""
Generated Code Metadata:
========================
Original URL: https://de-agent.com
Prompt: Write a smart contract in Solidity that manages a prize pool for a guessing game, inspired by the 16,000,000+ prize pool mentioned on de-agent.com.
Generated: DETERMINISTIC_619398dcbbda3435
Batch ID: 20250612_155153
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

contract GuessingGame {
    // State variables
    address public owner; // Owner of the contract
    uint256 public prizePool; // Total prize pool
    uint256 public winningNumber; // The number to be guessed
    uint256 public guessFee; // Fee to make a guess
    mapping(address => uint256) public playerGuesses; // Mapping of player addresses to their guesses
    bool public gameActive; // Status of the game

    // Events
    event GameStarted(uint256 winningNumber, uint256 guessFee);
    event GameEnded(uint256 winningNumber, uint256 prizePool);
    event Guessed(address indexed player, uint256 guess);
    event PrizeClaimed(address indexed winner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier gameIsActive() {
        require(gameActive, "The game is not active");
        _;
    }

    modifier gameIsNotActive() {
        require(!gameActive, "The game is currently active");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        gameActive = false; // Initialize the game as inactive
    }

    // Function to start a new game
    function startGame(uint256 _winningNumber, uint256 _guessFee) external onlyOwner gameIsNotActive {
        require(_winningNumber > 0 && _winningNumber <= 100, "Winning number must be between 1 and 100");
        require(_guessFee > 0, "Guess fee must be greater than zero");

        winningNumber = _winningNumber;
        guessFee = _guessFee;
        gameActive = true;
        prizePool = 0; // Reset prize pool

        emit GameStarted(winningNumber, guessFee);
    }

    // Function to make a guess
    function makeGuess(uint256 _guess) external payable gameIsActive {
        require(msg.value == guessFee, "Incorrect guess fee");
        require(_guess > 0 && _guess <= 100, "Guess must be between 1 and 100");
        require(playerGuesses[msg.sender] == 0, "You have already guessed");

        playerGuesses[msg.sender] = _guess; // Store the player's guess
        prizePool += msg.value; // Add the fee to the prize pool

        emit Guessed(msg.sender, _guess);
    }

    // Function to end the game and distribute the prize
    function endGame() external onlyOwner gameIsActive {
        gameActive = false; // Deactivate the game
        emit GameEnded(winningNumber, prizePool);

        // Check if there are any winners
        address winner;
        for (uint256 i = 0; i < 100; i++) {
            address player = address(uint160(i)); // Simulate player addresses
            if (playerGuesses[player] == winningNumber) {
                winner = player; // Found a winner
                break;
            }
        }

        // If there is a winner, transfer the prize
        if (winner != address(0)) {
            uint256 prizeAmount = prizePool;
            prizePool = 0; // Reset prize pool
            payable(winner).transfer(prizeAmount); // Transfer prize to the winner
            emit PrizeClaimed(winner, prizeAmount);
        }
    }

    // Function to withdraw funds in case of emergency
    function withdrawFunds() external onlyOwner gameIsNotActive {
        require(prizePool > 0, "No funds to withdraw");
        uint256 amount = prizePool;
        prizePool = 0; // Reset prize pool
        payable(owner).transfer(amount); // Transfer funds to the owner
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
