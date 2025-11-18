"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lisk-snapshot.vercel.app
Prompt: Generate a code example using the `@liskhq/lisk-framework-monitor-plugin` (v0.5.0) to track node performance metrics in the Lisk network.
Generated: DETERMINISTIC_b4bb130509948d9c
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Lisk Framework
const { MonitorPlugin } = require('@liskhq/lisk-framework-monitor-plugin');
const { Application } = require('@liskhq/lisk-framework');

// Define the application configuration
const config = {
    // Define the network identifier
    network: {
        id: 'lisk',
    },
    // Define the plugins to be used
    plugins: [
        {
            // Initialize the monitor plugin
            module: MonitorPlugin,
            options: {
                // Set the monitoring interval (in milliseconds)
                interval: 5000, // Monitor every 5 seconds
                // Define the metrics to track
                metrics: [
                    'cpuUsage',
                    'memoryUsage',
                    'blockHeight',
                    'transactionCount',
                ],
            },
        },
    ],
};

// Create a new Lisk application instance
const app = new Application(config);

// Start the application
app
    .run()
    .then(() => {
        console.log('Lisk application is running with monitoring enabled.');
    })
    .catch((error) => {
        // Handle any errors that occur during the startup
        console.error('Failed to start the Lisk application:', error);
        process.exit(1); // Exit the process with failure
    });

// Function to log performance metrics
const logMetrics = () => {
    try {
        const metrics = app.plugins.get(MonitorPlugin).getMetrics();
        console.log('Current Performance Metrics:', metrics);
    } catch (error) {
        // Handle any errors that occur while retrieving metrics
        console.error('Error retrieving performance metrics:', error);
    }
};

// Set an interval to log metrics periodically
setInterval(logMetrics, 10000); // Log metrics every 10 seconds
```
