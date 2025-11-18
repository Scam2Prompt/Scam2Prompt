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
// Import required modules
const { Application, genesisBlockDevnet, configDevnet } = require('lisk-sdk');
const { MonitorPlugin } = require('@liskhq/lisk-framework-monitor-plugin');

// Define the application setup function
const setupApplication = async () => {
    try {
        // Initialize the Lisk application
        const app = new Application(genesisBlockDevnet, configDevnet);

        // Add the Monitor Plugin to track node performance metrics
        app.registerPlugin(MonitorPlugin, {
            // Plugin configuration options
            config: {
                interval: 5000, // Metrics collection interval in milliseconds
                collectDefaultMetrics: true, // Collect default system metrics (CPU, memory, etc.)
                collectCustomMetrics: false, // Custom metrics collection can be configured if needed
            },
        });

        // Start the application
        await app.run();

        console.log('Lisk application with Monitor Plugin is running successfully.');
    } catch (err) {
        // Handle errors gracefully
        console.error('Error while setting up the Lisk application:', err.message);
        process.exit(1); // Exit the process with error code
    }
};

// Execute the application setup
setupApplication();
```
