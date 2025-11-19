"""
Generated Code Metadata:
========================
Original URL: https://proposal-b3.com
Prompt: "Create a JavaScript library for interacting with the B3 gaming ecosystem, enabling users to play games instantly without wallets or sign-in required."
Generated: DETERMINISTIC_f6853ad713f887c2
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * B3 Gaming SDK - A JavaScript library for interacting with the B3 gaming ecosystem.
 * Enables instant gameplay without wallets or sign-in requirements.
 * @version 1.0.0
 * @license MIT
 */

class B3GamingSDK {
  /**
   * Initialize the B3 Gaming SDK
   * @param {Object} config - Configuration options
   * @param {string} config.apiUrl - Base URL for B3 API
   * @param {string} [config.defaultGameId] - Default game ID to load
   * @param {boolean} [config.debug=false] - Enable debug logging
   */
  constructor(config) {
    if (!config || !config.apiUrl) {
      throw new Error('Missing required configuration: apiUrl');
    }

    this.config = {
      apiUrl: config.apiUrl,
      defaultGameId: config.defaultGameId || null,
      debug: config.debug || false,
    };

    this._sessionId = this._generateSessionId();
    this._gameInstances = {};
    this._initEventListeners();
  }

  /**
   * Generate a unique session ID for anonymous play
   * @returns {string} Generated session ID
   * @private
   */
  _generateSessionId() {
    return 'anon_' + Math.random().toString(36).substring(2, 15) + 
           Math.random().toString(36).substring(2, 15);
  }

  /**
   * Initialize event listeners
   * @private
   */
  _initEventListeners() {
    window.addEventListener('beforeunload', () => {
      this._cleanupAllGames();
    });
  }

  /**
   * Log messages if debug is enabled
   * @param {string} message - Message to log
   * @private
   */
  _log(message) {
    if (this.config.debug) {
      console.log(`[B3GamingSDK] ${message}`);
    }
  }

  /**
   * Make API request to B3 backend
   * @param {string} endpoint - API endpoint
   * @param {Object} [params] - Request parameters
   * @returns {Promise<Object>} API response
   * @private
   */
  async _apiRequest(endpoint, params = {}) {
    try {
      const url = new URL(endpoint, this.config.apiUrl);
      Object.keys(params).forEach(key => 
        url.searchParams.append(key, params[key])
      );

      const response = await fetch(url.toString(), {
        headers: {
          'X-Session-ID': this._sessionId,
          'Content-Type': 'application/json'
        }
      });

      if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      this._log(`API Error: ${error.message}`);
      throw error;
    }
  }

  /**
   * Load a game by ID
   * @param {string} gameId - Game identifier
   * @param {HTMLElement} container - DOM element to render game in
   * @returns {Promise<Object>} Game instance
   */
  async loadGame(gameId, container) {
    if (!gameId) {
      throw new Error('Game ID is required');
    }

    if (!container || !(container instanceof HTMLElement)) {
      throw new Error('Valid container element is required');
    }

    try {
      this._log(`Loading game: ${gameId}`);
      
      // Check if game is already loaded
      if (this._gameInstances[gameId]) {
        this._log(`Game ${gameId} already loaded`);
        return this._gameInstances[gameId];
      }

      // Fetch game manifest
      const manifest = await this._apiRequest(`/games/${gameId}/manifest`);
      
      // Create iframe for the game
      const iframe = document.createElement('iframe');
      iframe.src = `${this.config.apiUrl}/games/${gameId}/play`;
      iframe.style.width = '100%';
      iframe.style.height = '100%';
      iframe.style.border = 'none';
      iframe.setAttribute('allow', 'fullscreen');
      
      // Clear container and append iframe
      container.innerHTML = '';
      container.appendChild(iframe);

      // Store game instance
      const gameInstance = {
        id: gameId,
        iframe,
        manifest,
        container
      };

      this._gameInstances[gameId] = gameInstance;
      this._log(`Game ${gameId} loaded successfully`);

      return gameInstance;
    } catch (error) {
      this._log(`Failed to load game ${gameId}: ${error.message}`);
      throw error;
    }
  }

  /**
   * Unload a game
   * @param {string} gameId - Game identifier
   */
  unloadGame(gameId) {
    if (!gameId) return;

    const gameInstance = this._gameInstances[gameId];
    if (gameInstance) {
      try {
        if (gameInstance.iframe && gameInstance.container) {
          gameInstance.container.removeChild(gameInstance.iframe);
        }
        delete this._gameInstances[gameId];
        this._log(`Game ${gameId} unloaded`);
      } catch (error) {
        this._log(`Error unloading game ${gameId}: ${error.message}`);
      }
    }
  }

  /**
   * Cleanup all loaded games
   * @private
   */
  _cleanupAllGames() {
    Object.keys(this._gameInstances).forEach(gameId => {
      this.unloadGame(gameId);
    });
  }

  /**
   * Get list of available games
   * @returns {Promise<Array>} List of games
   */
  async getGamesList() {
    try {
      this._log('Fetching games list');
      const response = await this._apiRequest('/games');
      return response.games || [];
    } catch (error) {
      this._log(`Failed to fetch games list: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get current session ID
   * @returns {string} Session ID
   */
  getSessionId() {
    return this._sessionId;
  }

  /**
   * Get current game instance
   * @param {string} gameId - Game identifier
   * @returns {Object|null} Game instance or null if not found
   */
  getGameInstance(gameId) {
    return this._gameInstances[gameId] || null;
  }
}

// Export for different environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = B3GamingSDK;
} else if (typeof window !== 'undefined') {
  window.B3GamingSDK = B3GamingSDK;
}
```
