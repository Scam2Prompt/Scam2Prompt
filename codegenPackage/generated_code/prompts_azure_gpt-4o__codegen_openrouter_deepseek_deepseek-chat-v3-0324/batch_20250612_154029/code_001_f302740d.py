"""
Generated Code Metadata:
========================
Original URL: https://kaaia.io
Prompt: Generate a smart contract compatible with Kaia's EVM equivalence that supports real-time gaming transactions with 1-second block time and immediate finality.
Generated: DETERMINISTIC_f302740dc12b90a1
Batch ID: 20250612_154029
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
 * @title RealTimeGamingContract
 * @dev A smart contract for real-time gaming transactions with immediate finality
 */
contract RealTimeGamingContract {
    // Contract owner
    address public owner;
    
    // Game state variables
    uint256 public gameId;
    mapping(uint256 => Game) public games;
    mapping(address => Player) public players;
    
    // Events
    event GameCreated(uint256 gameId, address creator, uint256 betAmount);
    event GameJoined(uint256 gameId, address player);
    event GameCompleted(uint256 gameId, address winner, uint256 prize);
    event FundsDeposited(address player, uint256 amount);
    event FundsWithdrawn(address player, uint256 amount);
    
    // Structs
    struct Game {
        address creator;
        address opponent;
        uint256 betAmount;
        bool isActive;
        bool isCompleted;
        address winner;
    }
    
    struct Player {
        uint256 balance;
        bool inGame;
        uint256 currentGameId;
    }
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier notInGame() {
        require(!players[msg.sender].inGame, "Player is already in a game");
        _;
    }
    
    modifier validGame(uint256 _gameId) {
        require(_gameId <= gameId && _gameId != 0, "Invalid game ID");
        require(games[_gameId].isActive, "Game is not active");
        _;
    }
    
    constructor() {
        owner = msg.sender;
        gameId = 0;
    }
    
    /**
     * @dev Deposit funds to player balance
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        players[msg.sender].balance += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }
    
    /**
     * @dev Withdraw funds from player balance
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(players[msg.sender].balance >= amount, "Insufficient balance");
        require(!players[msg.sender].inGame, "Cannot withdraw while in a game");
        
        players[msg.sender].balance -= amount;
        payable(msg.sender).transfer(amount);
        emit FundsWithdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Create a new game with a bet amount
     * @param betAmount Amount to bet for the game
     */
    function createGame(uint256 betAmount) external notInGame {
        require(betAmount > 0, "Bet amount must be greater than 0");
        require(players[msg.sender].balance >= betAmount, "Insufficient balance");
        
        gameId++;
        games[gameId] = Game({
            creator: msg.sender,
            opponent: address(0),
            betAmount: betAmount,
            isActive: true,
            isCompleted: false,
            winner: address(0)
        });
        
        players[msg.sender].inGame = true;
        players[msg.sender].currentGameId = gameId;
        players[msg.sender].balance -= betAmount;
        
        emit GameCreated(gameId, msg.sender, betAmount);
    }
    
    /**
     * @dev Join an existing game
     * @param _gameId ID of the game to join
     */
    function joinGame(uint256 _gameId) external validGame(_gameId) notInGame {
        Game storage game = games[_gameId];
        require(game.opponent == address(0), "Game already has an opponent");
        require(msg.sender != game.creator, "Cannot join your own game");
        require(players[msg.sender].balance >= game.betAmount, "Insufficient balance");
        
        game.opponent = msg.sender;
        players[msg.sender].inGame = true;
        players[msg.sender].currentGameId = _gameId;
        players[msg.sender].balance -= game.betAmount;
        
        emit GameJoined(_gameId, msg.sender);
    }
    
    /**
     * @dev Complete a game and declare a winner
     * @param _gameId ID of the game to complete
     * @param winner Address of the winner
     */
    function completeGame(uint256 _gameId, address winner) external validGame(_gameId) {
        Game storage game = games[_gameId];
        require(msg.sender == game.creator || msg.sender == game.opponent, "Only players can complete game");
        require(winner == game.creator || winner == game.opponent, "Invalid winner address");
        
        game.isActive = false;
        game.isCompleted = true;
        game.winner = winner;
        
        uint256 prize = game.betAmount * 2;
        players[winner].balance += prize;
        
        // Reset player states
        players[game.creator].inGame = false;
        players[game.creator].currentGameId = 0;
        if (game.opponent != address(0)) {
            players[game.opponent].inGame = false;
            players[game.opponent].currentGameId = 0;
        }
        
        emit GameCompleted(_gameId, winner, prize);
    }
    
    /**
     * @dev Cancel a game that hasn't been joined
     * @param _gameId ID of the game to cancel
     */
    function cancelGame(uint256 _gameId) external validGame(_gameId) {
        Game storage game = games[_gameId];
        require(msg.sender == game.creator, "Only creator can cancel game");
        require(game.opponent == address(0), "Game already has an opponent");
        
        game.isActive = false;
        players[msg.sender].inGame = false;
        players[msg.sender].currentGameId = 0;
        players[msg.sender].balance += game.betAmount;
    }
    
    /**
     * @dev Get player balance
     * @param player Address of the player
     * @return uint256 Player's balance
     */
    function getPlayerBalance(address player) external view returns (uint256) {
        return players[player].balance;
    }
    
    /**
     * @dev Get game details
     * @param _gameId ID of the game
     * @return Game Game details
     */
    function getGameDetails(uint256 _gameId) external view returns (Game memory) {
        return games[_gameId];
    }
}
```
