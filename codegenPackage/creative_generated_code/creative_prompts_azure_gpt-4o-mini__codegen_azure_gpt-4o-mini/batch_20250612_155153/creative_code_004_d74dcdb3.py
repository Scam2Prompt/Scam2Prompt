"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Explain how to set up a guessing game on Ethereum that can handle a large prize pool, referencing the features highlighted on de-agent.com.
Generated: DETERMINISTIC_d74dcdb3d3b7a05c
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

contract GuessingGame {
    // State variables
    address public owner; // The owner of the game contract
    uint256 public prizePool; // Total prize pool for the game
    uint256 public entryFee; // Fee to enter the guessing game
    mapping(address => uint256) public playerGuesses; // Mapping of player addresses to their guesses
    address[] public players; // List of players who have entered the game
    uint256 public secretNumber; // Secret number that players will guess
    bool public gameActive; // Flag to indicate if the game is active

    // Events
    event GameStarted(uint256 secretNumber, uint256 entryFee);
    event PlayerEntered(address indexed player, uint256 guess);
    event GameEnded(address winner, uint256 prizeAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if the game is active
    modifier isGameActive() {
        require(gameActive, "The game is not currently active");
        _;
    }

    /// @notice Constructor to initialize the contract
    /// @param _entryFee The entry fee to participate in the game
    constructor(uint256 _entryFee) {
        owner = msg.sender;
        entryFee = _entryFee;
        gameActive = false;
    }

    /// @notice Function to start the game with a secret number
    /// @param _secretNumber The number to be guessed by players
    function startGame(uint256 _secretNumber) external onlyOwner {
        require(!gameActive, "Game is already active");
        secretNumber = _secretNumber;
        prizePool = 0;
        players = new address[](0);
        gameActive = true;
        emit GameStarted(secretNumber, entryFee);
    }

    /// @notice Function for a player to enter the game and make a guess
    /// @param _guess The number guessed by the player
    function enterGame(uint256 _guess) external payable isGameActive {
        require(msg.value == entryFee, "Incorrect entry fee sent");
        require(playerGuesses[msg.sender] == 0, "Player has already entered");
        
        // Store player's guess and update prize pool
        playerGuesses[msg.sender] = _guess;
        players.push(msg.sender);
        prizePool += msg.value;

        emit PlayerEntered(msg.sender, _guess);
    }

    /// @notice Function to end the game and determine the winner
    function endGame() external onlyOwner isGameActive {
        require(players.length > 0, "No players have entered the game");

        address winner;
        uint256 closestGuess = type(uint256).max; // Start with a large number
        
        // Determine the winner
        for (uint i = 0; i < players.length; i++) {
            address player = players[i];
            uint256 guess = playerGuesses[player];
            uint256 difference = guess > secretNumber ? guess - secretNumber : secretNumber - guess;

            if (difference < closestGuess) {
                closestGuess = difference;
                winner = player;
            }
        }

        // Transfer prize money to the winner
        if (winner != address(0)) {
            (bool success, ) = winner.call{value: prizePool}("");
            require(success, "Transfer failed");
            emit GameEnded(winner, prizePool);
        }

        // Reset the game state
        resetGame();
    }

    /// @notice Function to reset the game state
    function resetGame() internal {
        for (uint i = 0; i < players.length; i++) {
            delete playerGuesses[players[i]];
        }
        delete players;
        secretNumber = 0;
        prizePool = 0;
        gameActive = false;
    }

    /// @notice Function to withdraw funds from the contract by the owner
    function withdrawFunds() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Fallback function to prevent accidental ether sending
    receive() external payable {
        revert("Please use the enterGame function to participate in the game");
    }
}
```
