"""
Generated Code Metadata:
========================
Original URL: https://p-1px.pages.dev
Prompt: Generate a tutorial on setting up a node on Over Protocol using OverNode, including code examples and configuration steps.
Generated: DETERMINISTIC_4e0d5b0f3c6cd6d2
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const { OverNode } = require('overnode');
const fs = require('fs');
const path = require('path');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());

// Configuration constants
const DEFAULT_PORT = 3000;
const CONFIG_FILE = path.join(__dirname, 'overnode-config.json');

// Load or create configuration
function loadOrCreateConfig() {
    try {
        if (fs.existsSync(CONFIG_FILE)) {
            return JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
        }
        
        const defaultConfig = {
            nodeName: 'MyOverNode',
            network: 'testnet',
            port: DEFAULT_PORT,
            peers: [],
            maxConnections: 50,
            logLevel: 'info'
        };
        
        fs.writeFileSync(CONFIG_FILE, JSON.stringify(defaultConfig, null, 2));
        return defaultConfig;
    } catch (error) {
        console.error('Error loading/creating config:', error);
        process.exit(1);
    }
}

// Initialize OverNode instance
function initializeOverNode(config) {
    try {
        const overNode = new OverNode({
            name: config.nodeName,
            network: config.network,
            port: config.port,
            peers: config.peers,
            maxConnections: config.maxConnections,
            logLevel: config.logLevel
        });
        
        return overNode;
    } catch (error) {
        console.error('Error initializing OverNode:', error);
        process.exit(1);
    }
}

// API endpoints
app.get('/api/node/info', (req, res) => {
    try {
        const info = overNode.getNodeInfo();
        res.json(info);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/node/connect', (req, res) => {
    try {
        const { peerAddress } = req.body;
        if (!peerAddress) {
            return res.status(400).json({ error: 'peerAddress is required' });
        }
        
        overNode.connectToPeer(peerAddress);
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start server and node
const config = loadOrCreateConfig();
const overNode = initializeOverNode(config);

overNode.on('ready', () => {
    console.log(`OverNode ${config.nodeName} is ready`);
    
    app.listen(config.port, () => {
        console.log(`API server running on port ${config.port}`);
    });
});

overNode.on('error', (error) => {
    console.error('OverNode error:', error);
});

process.on('SIGINT', () => {
    console.log('Shutting down gracefully...');
    overNode.shutdown();
    process.exit(0);
});

// Example configuration file (overnode-config.json):
/*
{
    "nodeName": "MyOverNode",
    "network": "testnet",
    "port": 3000,
    "peers": [
        "12D3KooWExamplePeer1",
        "12D3KooWExamplePeer2"
    ],
    "maxConnections": 50,
    "logLevel": "info"
}
*/
```
