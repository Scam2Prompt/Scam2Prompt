"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write a JavaScript function to display real-time RTP statistics for games on a platform like Pelangi189, updating dynamically based on user activity.
Generated: DETERMINISTIC_82da7c7dadb5208d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays real-time RTP (Return to Player) statistics for games.
 * Updates dynamically based on user activity and server push events.
 * 
 * @param {string} apiEndpoint - The API endpoint to fetch RTP data from
 * @param {number} refreshInterval - Interval in milliseconds for polling updates (default: 5000)
 * @param {HTMLElement} container - DOM element to render the statistics
 */
class RTPMonitor {
  constructor(apiEndpoint, refreshInterval = 5000, container) {
    this.apiEndpoint = apiEndpoint;
    this.refreshInterval = refreshInterval;
    this.container = container;
    this.rtpData = {};
    this.socket = null;
    this.pollingInterval = null;
    this.isConnected = false;
  }

  /**
   * Initializes the RTP monitor with WebSocket connection and polling fallback
   */
  initialize() {
    this._setupWebSocket();
    this._setupPollingFallback();
    this._renderLoadingState();
  }

  /**
   * Sets up WebSocket connection for real-time updates
   */
  _setupWebSocket() {
    try {
      const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsEndpoint = `${wsProtocol}//${window.location.host}${this.apiEndpoint.replace('/api', '/ws')}`;
      
      this.socket = new WebSocket(wsEndpoint);

      this.socket.onopen = () => {
        this.isConnected = true;
        console.log('WebSocket connected for real-time RTP updates');
        this._clearPolling();
      };

      this.socket.onmessage = (event) => {
        this._processUpdate(JSON.parse(event.data));
      };

      this.socket.onclose = () => {
        this.isConnected = false;
        console.log('WebSocket disconnected, falling back to polling');
        this._setupPollingFallback();
      };

      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
        this.isConnected = false;
      };
    } catch (error) {
      console.error('WebSocket initialization failed:', error);
      this.isConnected = false;
    }
  }

  /**
   * Sets up polling as fallback when WebSocket is not available
   */
  _setupPollingFallback() {
    if (this.pollingInterval) return;

    this.pollingInterval = setInterval(async () => {
      if (!this.isConnected) {
        await this._fetchRTPData();
      }
    }, this.refreshInterval);

    // Initial fetch
    this._fetchRTPData();
  }

  /**
   * Clears the polling interval
   */
  _clearPolling() {
    if (this.pollingInterval) {
      clearInterval(this.pollingInterval);
      this.pollingInterval = null;
    }
  }

  /**
   * Fetches RTP data from the API endpoint
   */
  async _fetchRTPData() {
    try {
      const response = await fetch(this.apiEndpoint);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      this._processUpdate(data);
    } catch (error) {
      console.error('Failed to fetch RTP data:', error);
      this._renderErrorState();
    }
  }

  /**
   * Processes incoming RTP data updates
   * @param {Object} data - New RTP data
   */
  _processUpdate(data) {
    if (!data || typeof data !== 'object') {
      console.error('Invalid RTP data received');
      return;
    }

    this.rtpData = data;
    this._renderRTPStats();
  }

  /**
   * Renders the loading state UI
   */
  _renderLoadingState() {
    this.container.innerHTML = `
      <div class="rtp-loading">
        <div class="spinner"></div>
        <p>Loading RTP statistics...</p>
      </div>
    `;
  }

  /**
   * Renders the error state UI
   */
  _renderErrorState() {
    this.container.innerHTML = `
      <div class="rtp-error">
        <p>⚠️ Failed to load RTP data. Trying to reconnect...</p>
      </div>
    `;
  }

  /**
   * Renders the RTP statistics UI
   */
  _renderRTPStats() {
    if (!this.rtpData || Object.keys(this.rtpData).length === 0) {
      this._renderErrorState();
      return;
    }

    let html = `
      <div class="rtp-header">
        <h3>Real-Time RTP Statistics</h3>
        <div class="rtp-connection-status ${this.isConnected ? 'connected' : 'disconnected'}">
          ${this.isConnected ? 'Live' : 'Polling'}
        </div>
      </div>
      <div class="rtp-games">
    `;

    for (const [gameId, stats] of Object.entries(this.rtpData)) {
      html += `
        <div class="rtp-game-card">
          <div class="game-header">
            <h4>${stats.gameName || gameId}</h4>
            <div class="rtp-value ${this._getRTPClass(stats.currentRTP)}">
              ${(stats.currentRTP * 100).toFixed(2)}%
            </div>
          </div>
          <div class="game-stats">
            <div class="stat">
              <span class="label">24h Avg:</span>
              <span class="value">${(stats.dailyAvgRTP * 100).toFixed(2)}%</span>
            </div>
            <div class="stat">
              <span class="label">Players:</span>
              <span class="value">${stats.activePlayers}</span>
            </div>
            <div class="stat">
              <span class="label">Last Update:</span>
              <span class="value">${new Date(stats.lastUpdated).toLocaleTimeString()}</span>
            </div>
          </div>
        </div>
      `;
    }

    html += `</div>`;
    this.container.innerHTML = html;
  }

  /**
   * Determines CSS class based on RTP value
   * @param {number} rtp - RTP value (0-1)
   * @returns {string} CSS class name
   */
  _getRTPClass(rtp) {
    if (rtp >= 0.95) return 'high';
    if (rtp >= 0.9) return 'medium';
    if (rtp >= 0.85) return 'low';
    return 'very-low';
  }

  /**
   * Cleans up resources when the monitor is no longer needed
   */
  destroy() {
    if (this.socket) {
      this.socket.close();
    }
    this._clearPolling();
    this.container.innerHTML = '';
  }
}

// Example usage:
// const rtpMonitor = new RTPMonitor(
//   '/api/games/rtp-stats',
//   5000,
//   document.getElementById('rtp-container')
// );
// rtpMonitor.initialize();

// Later when needed:
// rtpMonitor.destroy();
```
