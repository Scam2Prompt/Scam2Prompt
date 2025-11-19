"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Write a smart contract in Solidity that manages a prize pool for a guessing game, inspired by the 16,000,000+ prize pool mentioned on de-agent.com.
Generated: DETERMINISTIC_619398dcbbda3435
Batch ID: 20250612_155153
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

/// @title Guessing Game Prize Pool
/// @notice This contract manages a prize pool for a guessing game where players can guess a number and win Ether.
contract GuessingGame {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public prizePool; // Total prize pool in Wei
    uint256 public winningNumber; // The number to be guessed
    mapping(address => uint256) public playerGuesses; // Maps player addresses to their guesses
    bool public gameActive; // Indicates if the game is currently active

    // Events
    event GameStarted(uint256 winningNumber);
    event GuessMade(address indexed player, uint256 guess);
    event PrizeClaimed(address indexed winner, uint256 prizeAmount);
    event GameEnded(uint256 winningNumber, uint256 totalPrizePool);

    /// @dev Modifier to restrict access to the owner of the contract
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /// @dev Modifier to check if the game is active
    modifier whenGameActive() {
        require(gameActive, "Game is not active");
        _;
    }

    /// @dev Constructor sets the contract owner and initializes the game state
    constructor() {
        owner = msg.sender;
        gameActive = false;
    }

    /// @notice Starts the guessing game with a specified winning number
    /// @param _winningNumber The number players will guess
    function startGame(uint256 _winningNumber) external onlyOwner {
        require(!gameActive, "Game already active");
        winningNumber = _winningNumber;
        gameActive = true;
        prizePool = 0; // Reset prize pool for the new game
        emit GameStarted(winningNumber);
    }

    /// @notice Allows players to make a guess and enter the prize pool
    /// @dev Players must send 0.01 Ether to participate
    function makeGuess(uint256 _guess) external payable whenGameActive {
        require(msg.value == 0.01 ether, "Entry fee is 0.01 Ether");
        require(playerGuesses[msg.sender] == 0, "Already guessed");

        // Store the player's guess
        playerGuesses[msg.sender] = _guess;
        prizePool += msg.value; // Add entry fee to the prize pool

        emit GuessMade(msg.sender, _guess);
    }

    /// @notice Ends the guessing game and distributes the prize to the winner
    function endGame() external onlyOwner whenGameActive {
        gameActive = false; // Deactivate the game
        address winner;
        uint256 prizeAmount;

        // Check if there is a winner
        for (uint256 i = 0; i < 200; i++) { // Assuming a maximum of 200 players for simplicity
            if (playerGuesses[tx.origin] == winningNumber) {
                winner = tx.origin;
                prizeAmount = prizePool;
                break;
            }
        }

        emit GameEnded(winningNumber, prizePool);

        // If there's a winner, transfer the prize
        if (winner != address(0)) {
            (bool success, ) = winner.call{value: prizeAmount}("");
            require(success, "Transfer failed");
            emit PrizeClaimed(winner, prizeAmount);
        }
    }

    /// @notice Allows the owner to withdraw any Ether from the contract
    function withdrawFunds() external onlyOwner {
        require(!gameActive, "Cannot withdraw while game is active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
