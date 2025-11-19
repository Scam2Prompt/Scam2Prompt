"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Write a JavaScript function to create a game lobby for games like 'Tricky Trip' and '1212!'."
Generated: DETERMINISTIC_37815d11ce2a7b26
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Game Lobby Class for managing multiplayer game lobbies.
 * Supports games like 'Tricky Trip' and '1212!'.
 */
class GameLobby {
  /**
   * Initialize a new game lobby
   * @param {string} gameName - Name of the game ('Tricky Trip', '1212!', etc.)
   * @param {number} maxPlayers - Maximum number of players allowed in the lobby
   */
  constructor(gameName, maxPlayers) {
    if (!gameName || typeof gameName !== 'string') {
      throw new Error('Invalid game name provided');
    }
    if (!maxPlayers || typeof maxPlayers !== 'number' || maxPlayers < 2) {
      throw new Error('Max players must be a number greater than 1');
    }

    this.gameName = gameName;
    this.maxPlayers = maxPlayers;
    this.players = new Map();
    this.isGameStarted = false;
    this.lobbyId = this.generateLobbyId();
  }

  /**
   * Generate a unique lobby ID
   * @returns {string} - Unique lobby identifier
   */
  generateLobbyId() {
    return Math.random().toString(36).substring(2, 10).toUpperCase();
  }

  /**
   * Add a player to the lobby
   * @param {string} playerId - Unique player identifier
   * @param {string} playerName - Player display name
   * @returns {boolean} - True if player was added successfully
   */
  addPlayer(playerId, playerName) {
    if (this.isGameStarted) {
      throw new Error('Cannot add player - game has already started');
    }
    if (this.players.size >= this.maxPlayers) {
      throw new Error('Lobby is full');
    }
    if (!playerId || !playerName) {
      throw new Error('Player ID and name are required');
    }
    if (this.players.has(playerId)) {
      throw new Error('Player already exists in lobby');
    }

    this.players.set(playerId, {
      name: playerName,
      ready: false
    });
    return true;
  }

  /**
   * Remove a player from the lobby
   * @param {string} playerId - Unique player identifier
   * @returns {boolean} - True if player was removed successfully
   */
  removePlayer(playerId) {
    if (!this.players.has(playerId)) {
      throw new Error('Player not found in lobby');
    }
    this.players.delete(playerId);
    return true;
  }

  /**
   * Toggle player ready status
   * @param {string} playerId - Unique player identifier
   * @returns {boolean} - New ready status
   */
  toggleReady(playerId) {
    if (!this.players.has(playerId)) {
      throw new Error('Player not found in lobby');
    }
    const player = this.players.get(playerId);
    player.ready = !player.ready;
    return player.ready;
  }

  /**
   * Check if all players are ready to start the game
   * @returns {boolean} - True if all players are ready
   */
  allPlayersReady() {
    if (this.players.size < 2) return false;
    for (const player of this.players.values()) {
      if (!player.ready) return false;
    }
    return true;
  }

  /**
   * Start the game if conditions are met
   * @returns {boolean} - True if game was started successfully
   */
  startGame() {
    if (this.isGameStarted) {
      throw new Error('Game is already in progress');
    }
    if (this.players.size < 2) {
      throw new Error('Not enough players to start the game');
    }
    if (!this.allPlayersReady()) {
      throw new Error('Not all players are ready');
    }

    this.isGameStarted = true;
    return true;
  }

  /**
   * End the current game session
   * @returns {boolean} - True if game was ended successfully
   */
  endGame() {
    if (!this.isGameStarted) {
      throw new Error('No game in progress');
    }
    this.isGameStarted = false;
    return true;
  }

  /**
   * Get lobby status
   * @returns {object} - Lobby status object
   */
  getStatus() {
    return {
      lobbyId: this.lobbyId,
      gameName: this.gameName,
      maxPlayers: this.maxPlayers,
      currentPlayers: this.players.size,
      players: Array.from(this.players.entries()).map(([id, data]) => ({
        id,
        name: data.name,
        ready: data.ready
      })),
      isGameStarted: this.isGameStarted,
      canStart: this.allPlayersReady() && this.players.size >= 2
    };
  }
}

/**
 * Game Lobby Manager for handling multiple game lobbies
 */
class GameLobbyManager {
  constructor() {
    this.lobbies = new Map();
  }

  /**
   * Create a new game lobby
   * @param {string} gameName - Name of the game
   * @param {number} maxPlayers - Maximum number of players
   * @returns {GameLobby} - The created lobby instance
   */
  createLobby(gameName, maxPlayers) {
    const lobby = new GameLobby(gameName, maxPlayers);
    this.lobbies.set(lobby.lobbyId, lobby);
    return lobby;
  }

  /**
   * Get a lobby by ID
   * @param {string} lobbyId - Lobby identifier
   * @returns {GameLobby} - The lobby instance
   */
  getLobby(lobbyId) {
    if (!this.lobbies.has(lobbyId)) {
      throw new Error('Lobby not found');
    }
    return this.lobbies.get(lobbyId);
  }

  /**
   * Remove a lobby
   * @param {string} lobbyId - Lobby identifier
   * @returns {boolean} - True if lobby was removed
   */
  removeLobby(lobbyId) {
    if (!this.lobbies.has(lobbyId)) {
      throw new Error('Lobby not found');
    }
    this.lobbies.delete(lobbyId);
    return true;
  }

  /**
   * Get all active lobbies
   * @returns {Array} - Array of lobby status objects
   */
  getAllLobbies() {
    return Array.from(this.lobbies.values()).map(lobby => lobby.getStatus());
  }
}

// Export the classes for use in other modules
module.exports = { GameLobby, GameLobbyManager };
```
