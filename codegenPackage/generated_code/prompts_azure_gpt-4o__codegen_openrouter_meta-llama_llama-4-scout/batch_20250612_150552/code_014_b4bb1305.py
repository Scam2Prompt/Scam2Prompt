"""
Generated Code Metadata:
========================
Original URL: https://lisk-snapshot.vercel.app
Prompt: Generate a code example using the `@liskhq/lisk-framework-monitor-plugin` (v0.5.0) to track node performance metrics in the Lisk network.
Generated: DETERMINISTIC_b4bb130509948d9c
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { MonitorPlugin, NodeStats } = require('@liskhq/lisk-framework-monitor-plugin');
const { Logger } = require('@liskhq/lisk-logging');

// Initialize logger
const logger = Logger('node-performance-monitor');

// Define a custom monitor plugin
class NodePerformanceMonitor extends MonitorPlugin {
  /**
   * @param {Object} options - Plugin options
   * @param {string} options.nodeName - Name of the node
   * @param {number} options.interval - Interval in seconds to collect metrics
   */
  constructor(options) {
    super(options);
    this.nodeName = options.nodeName;
    this.interval = options.interval || 10; // default interval: 10 seconds
  }

  /**
   * Collect node performance metrics
   * @returns {Promise<NodeStats>} Node performance metrics
   */
  async collectMetrics() {
    try {
      const nodeStats = await NodeStats.create();
      return nodeStats;
    } catch (error) {
      logger.error('Error collecting node performance metrics:', error);
      return null;
    }
  }

  /**
   * Process collected metrics
   * @param {NodeStats} metrics - Node performance metrics
   */
  processMetrics(metrics) {
    if (!metrics) return;

    const { cpu, memory, network } = metrics;
    logger.info(`Node performance metrics for ${this.nodeName}:`);
    logger.info(`CPU usage: ${cpu.usage}%`);
    logger.info(`Memory usage: ${memory.usage}%`);
    logger.info(`Network traffic: ${network.tx} tx, ${network.rx} rx`);
  }

  /**
   * Start monitoring node performance
   */
  start() {
    setInterval(async () => {
      const metrics = await this.collectMetrics();
      this.processMetrics(metrics);
    }, this.interval * 1000); // convert seconds to milliseconds
  }

  /**
   * Stop monitoring node performance
   */
  stop() {
    clearInterval(this.intervalId);
  }
}

// Example usage
async function main() {
  try {
    const monitor = new NodePerformanceMonitor({
      nodeName: 'My Lisk Node',
      interval: 5, // collect metrics every 5 seconds
    });
    monitor.start();

    // Stop monitoring after 1 minute
    setTimeout(() => {
      monitor.stop();
    }, 60 * 1000);
  } catch (error) {
    logger.error('Error:', error);
  }
}

main();
```
