"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Write a JavaScript function to monitor and manage the background activity of a Grass-like web extension, ensuring it doesn't interfere with the user's internet experience.
Generated: DETERMINISTIC_c5af5fe740525181
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to monitor and manage the background activity of a Grass-like web extension.
 * Ensures the extension operates efficiently and doesn't interfere with the user's internet experience.
 */

/**
 * Monitors the extension's background activity and adjusts its behavior as needed.
 * @param {Object} options - Configuration options for monitoring.
 * @param {number} options.checkInterval - Interval (in ms) to check background activity.
 * @param {number} options.maxAllowedRequestsPerMinute - Maximum allowed network requests per minute.
 * @param {number} options.maxCpuUsage - Maximum allowed CPU usage percentage.
 */
function monitorBackgroundActivity(options) {
  // Default configuration values
  const config = {
    checkInterval: options?.checkInterval || 5000, // Default: Check every 5 seconds
    maxAllowedRequestsPerMinute: options?.maxAllowedRequestsPerMinute || 100, // Default: 100 requests/min
    maxCpuUsage: options?.maxCpuUsage || 50, // Default: 50% CPU usage
  };

  let requestCount = 0; // Track network requests in the last minute

  // Record the start time of a monitoring cycle
  let monitoringStartTime = Date.now();

  // Simulate periodic monitoring
  setInterval(() => {
    try {
      // Calculate elapsed time since last monitoring cycle
      const elapsedTime = Date.now() - monitoringStartTime;

      // Check network activity
      if (requestCount > config.maxAllowedRequestsPerMinute) {
        console.warn(
          `Warning: Extension exceeded the allowed network requests per minute (${requestCount} requests).`
        );
        throttleNetworkActivity(); // Apply network throttling
      }

      // Check CPU usage (mocked for demonstration purposes)
      const currentCpuUsage = mockGetCpuUsage(); // Replace with actual API if available
      if (currentCpuUsage > config.maxCpuUsage) {
        console.warn(
          `Warning: Extension CPU usage exceeded the limit (${currentCpuUsage}%).`
        );
        optimizeBackgroundTasks(); // Optimize tasks to reduce CPU usage
      }

      // Reset monitoring counters after 1 minute
      if (elapsedTime >= 60000) {
        requestCount = 0;
        monitoringStartTime = Date.now();
      }
    } catch (error) {
      console.error("Error monitoring background activity:", error.message);
    }
  }, config.checkInterval);

  /**
   * Simulates throttling network activity.
   * This function should implement logic to reduce the number of requests made by the extension.
   */
  function throttleNetworkActivity() {
    console.log("Throttling network activity...");
    // Implement logic to limit network requests here
  }

  /**
   * Simulates optimizing background tasks to reduce CPU usage.
   * This function should implement logic to prioritize and scale down background tasks.
   */
  function optimizeBackgroundTasks() {
    console.log("Optimizing background tasks...");
    // Implement logic to reduce CPU usage here
  }

  /**
   * Mock function to get CPU usage percentage.
   * Replace with actual implementation if available.
   * @returns {number} - Simulated CPU usage percentage.
   */
  function mockGetCpuUsage() {
    // Return a random percentage (mock value) for demonstration purposes
    return Math.floor(Math.random() * 100);
  }

  /**
   * Function to record a network request made by the extension.
   * Call this function whenever the extension makes a network request.
   */
  return function recordNetworkRequest() {
    requestCount++;
  };
}

// USAGE EXAMPLE:
// Initialize monitoring with custom options
const recordRequest = monitorBackgroundActivity({
  checkInterval: 5000,
  maxAllowedRequestsPerMinute: 120,
  maxCpuUsage: 60,
});

// Simulate network requests (for demonstration purposes)
setInterval(() => {
  recordRequest();
}, 1000);
```
