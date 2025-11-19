"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Generate JavaScript code to create a simple status update page that displays the current uptime and status of the TTEC STC Cluster.
Generated: DETERMINISTIC_1a7386bf4d4789f6
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Status Update Page for TTEC STC Cluster
 * Displays current uptime and cluster status
 */

// Import required modules
const express = require('express');
const os = require('os');
const process = require('process');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to serve static files
app.use(express.static('public'));

// Function to format uptime into human-readable format
function formatUptime(seconds) {
    const days = Math.floor(seconds / (3600 * 24));
    const hours = Math.floor((seconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);

    return `${days}d ${hours}h ${minutes}m ${secs}s`;
}

// Function to get system status
function getSystemStatus() {
    try {
        const load = os.loadavg()[0];
        const freeMem = os.freemem() / 1024 / 1024; // MB
        const totalMem = os.totalmem() / 1024 / 1024; // MB
        
        return {
            status: load < 0.7 ? 'Operational' : 'High Load',
            loadAverage: load.toFixed(2),
            memoryUsage: `${(totalMem - freeMem).toFixed(2)}MB / ${totalMem.toFixed(2)}MB`,
            uptime: formatUptime(os.uptime())
        };
    } catch (error) {
        console.error('Error getting system status:', error);
        return {
            status: 'Unknown',
            error: 'Failed to retrieve system status'
        };
    }
}

// Route to serve status page
app.get('/', (req, res) => {
    try {
        const status = getSystemStatus();
        
        res.send(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>TTEC STC Cluster Status</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        line-height: 1.6;
                        margin: 0;
                        padding: 20px;
                        color: #333;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    h1 {
                        color: #2c3e50;
                        text-align: center;
                    }
                    .status-card {
                        padding: 15px;
                        margin: 10px 0;
                        border-radius: 5px;
                        background-color: ${status.status === 'Operational' ? '#d4edda' : '#f8d7da'};
                        color: ${status.status === 'Operational' ? '#155724' : '#721c24'};
                    }
                    .metrics {
                        display: grid;
                        grid-template-columns: repeat(2, 1fr);
                        gap: 10px;
                    }
                    .metric {
                        padding: 10px;
                        background-color: #f8f9fa;
                        border-radius: 3px;
                    }
                    .timestamp {
                        text-align: right;
                        font-size: 0.8em;
                        color: #6c757d;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>TTEC STC Cluster Status</h1>
                    
                    <div class="status-card">
                        <h2>Current Status: ${status.status}</h2>
                        ${status.error ? `<p><strong>Error:</strong> ${status.error}</p>` : ''}
                    </div>
                    
                    <div class="metrics">
                        <div class="metric">
                            <h3>Uptime</h3>
                            <p>${status.uptime}</p>
                        </div>
                        <div class="metric">
                            <h3>Load Average</h3>
                            <p>${status.loadAverage}</p>
                        </div>
                        <div class="metric">
                            <h3>Memory Usage</h3>
                            <p>${status.memoryUsage}</p>
                        </div>
                    </div>
                    
                    <div class="timestamp">
                        Last updated: ${new Date().toLocaleString()}
                    </div>
                </div>
            </body>
            </html>
        `);
    } catch (error) {
        console.error('Error generating status page:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Handle shutdown gracefully
process.on('SIGTERM', () => {
    console.log('SIGTERM received. Shutting down gracefully...');
    process.exit(0);
});

process.on('SIGINT', () => {
    console.log('SIGINT received. Shutting down gracefully...');
    process.exit(0);
});
```
