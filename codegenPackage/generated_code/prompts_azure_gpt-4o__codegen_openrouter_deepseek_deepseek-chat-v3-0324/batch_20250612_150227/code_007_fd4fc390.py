"""
Generated Code Metadata:
========================
Original URL: https://polymarketscanner.com
Prompt: Provide an example of how to set up a fetch interval and flush interval in a real-time polling application similar to Polymarket Scanner.
Generated: DETERMINISTIC_fd4fc390afa195b2
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Real-time polling service with configurable fetch and flush intervals
class PollingService {
  /**
   * Initialize the polling service with fetch and flush intervals
   * @param {Object} config - Configuration object
   * @param {number} config.fetchInterval - Interval in ms to fetch new data
   * @param {number} config.flushInterval - Interval in ms to flush old data
   * @param {Function} config.fetchCallback - Callback to fetch new data
   * @param {Function} config.flushCallback - Callback to flush old data
   */
  constructor({ fetchInterval, flushInterval, fetchCallback, flushCallback }) {
    if (!fetchInterval || !flushInterval || !fetchCallback || !flushCallback) {
      throw new Error('Missing required configuration parameters');
    }

    this.fetchInterval = fetchInterval;
    this.flushInterval = flushInterval;
    this.fetchCallback = fetchCallback;
    this.flushCallback = flushCallback;
    this.fetchTimer = null;
    this.flushTimer = null;
    this.isRunning = false;
  }

  /**
   * Start the polling service
   */
  start() {
    if (this.isRunning) {
      console.warn('Polling service is already running');
      return;
    }

    this.isRunning = true;
    this._startFetchTimer();
    this._startFlushTimer();
    console.log('Polling service started');
  }

  /**
   * Stop the polling service
   */
  stop() {
    if (!this.isRunning) {
      console.warn('Polling service is not running');
      return;
    }

    clearTimeout(this.fetchTimer);
    clearTimeout(this.flushTimer);
    this.isRunning = false;
    console.log('Polling service stopped');
  }

  /**
   * Start the fetch timer
   * @private
   */
  _startFetchTimer() {
    this.fetchTimer = setTimeout(async () => {
      try {
        await this.fetchCallback();
      } catch (error) {
        console.error('Error in fetch callback:', error);
      } finally {
        if (this.isRunning) {
          this._startFetchTimer();
        }
      }
    }, this.fetchInterval);
  }

  /**
   * Start the flush timer
   * @private
   */
  _startFlushTimer() {
    this.flushTimer = setTimeout(async () => {
      try {
        await this.flushCallback();
      } catch (error) {
        console.error('Error in flush callback:', error);
      } finally {
        if (this.isRunning) {
          this._startFlushTimer();
        }
      }
    }, this.flushInterval);
  }
}

// Example usage
const exampleService = new PollingService({
  fetchInterval: 5000,    // Fetch new data every 5 seconds
  flushInterval: 30000,   // Flush old data every 30 seconds
  fetchCallback: async () => {
    console.log('Fetching new data...');
    // Implement actual data fetching logic here
  },
  flushCallback: async () => {
    console.log('Flushing old data...');
    // Implement actual data flushing logic here
  }
});

// Start the service
exampleService.start();

// To stop the service later:
// exampleService.stop();
```
