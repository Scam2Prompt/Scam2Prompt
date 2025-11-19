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
const { Application, configDevnet } = require('lisk-sdk');
const { MonitorPlugin } = require('@liskhq/lisk-framework-monitor-plugin');

// Define the application configuration
const appConfig = {
    ...configDevnet,
    rpc: {
        enable: true,
        mode: 'ipc',
        port: 8080,
    },
    network: {
        port: 5000,
    },
};

// Initialize the application
const app = Application.defaultApplication(appConfig);

// Configure the monitor plugin
const monitorPluginConfig = {
    port: 5001, // Port for the monitor plugin
    host: '0.0.0.0', // Host for the monitor plugin
    whiteList: ['127.0.0.1'], // Allowed IPs to access the metrics
    limits: {
        cpu: {
            enable: true,
            interval: 1000, // Interval in ms for CPU monitoring
            historyLimit: 100, // Number of historical records to keep
            threshold: 90, // CPU usage threshold percentage
        },
        memory: {
            enable: true,
            interval: 1000, // Interval in ms for memory monitoring
            historyLimit: 100, // Number of historical records to keep
            threshold: 90, // Memory usage threshold percentage
        },
        transactionPool: {
            enable: true,
            interval: 1000, // Interval in ms for transaction pool monitoring
            historyLimit: 100, // Number of historical records to keep
            threshold: 1000, // Transaction pool size threshold
        },
    },
};

// Register the monitor plugin
app.registerPlugin(new MonitorPlugin(monitorPluginConfig));

// Start the application
app.run()
    .then(() => {
        console.log('Application started with monitor plugin');
    })
    .catch(error => {
        console.error('Application failed to start:', error);
        process.exit(1);
    });

// Handle process termination
process.on('SIGINT', async () => {
    console.log('Shutting down application...');
    await app.shutdown();
    process.exit(0);
});
```
