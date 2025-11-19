"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Provide a step-by-step implementation plan for building a tool similar to the "dudeminecraft server problems diagnoser" on dudemine.com, using Node.js and Minecraft server APIs.
Generated: DETERMINISTIC_fba4a5dc01c2b302
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mcsrvstat.us/2/${ip}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const axios = require('axios');
const { RCON } = require('minecraft-rcon-client');
const { Server } = require('socket.io');
const http = require('http');
const path = require('path');

// Initialize Express app and HTTP server
const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Configuration constants
const PORT = process.env.PORT || 3000;
const MC_SERVER_IP = process.env.MC_SERVER_IP || 'localhost';
const MC_SERVER_PORT = process.env.MC_SERVER_PORT || 25565;
const RCON_PORT = process.env.RCON_PORT || 25575;
const RCON_PASSWORD = process.env.RCON_PASSWORD || 'password';

// Middleware setup
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API Endpoints
app.post('/api/diagnose', async (req, res) => {
    try {
        const { serverIp } = req.body;
        
        // Step 1: Check server status
        const serverStatus = await checkServerStatus(serverIp || MC_SERVER_IP);
        
        // Step 2: If online, get detailed info
        let serverInfo = {};
        if (serverStatus.online) {
            serverInfo = await getServerInfo(serverIp || MC_SERVER_IP);
        }
        
        // Step 3: Check RCON connection if credentials provided
        let rconStatus = { connected: false };
        if (RCON_PASSWORD) {
            rconStatus = await checkRCONConnection();
        }
        
        res.json({
            status: 'success',
            data: {
                serverStatus,
                serverInfo,
                rconStatus
            }
        });
    } catch (error) {
        console.error('Diagnosis error:', error);
        res.status(500).json({
            status: 'error',
            message: 'Failed to diagnose server',
            error: error.message
        });
    }
});

// Server status check function
async function checkServerStatus(ip) {
    try {
        const response = await axios.get(`https://api.mcsrvstat.us/2/${ip}`);
        return {
            online: response.data.online,
            hostname: response.data.hostname || ip,
            version: response.data.version || 'Unknown',
            players: response.data.players || { online: 0, max: 0 }
        };
    } catch (error) {
        console.error('Server status check failed:', error);
        return { online: false, error: error.message };
    }
}

// Get detailed server info
async function getServerInfo(ip) {
    try {
        const response = await axios.get(`https://api.mcsrvstat.us/2/${ip}`);
        return {
            motd: response.data.motd || {},
            software: response.data.software || 'Unknown',
            plugins: response.data.plugins || [],
            mods: response.data.mods || []
        };
    } catch (error) {
        console.error('Server info fetch failed:', error);
        return { error: error.message };
    }
}

// RCON connection check
async function checkRCONConnection() {
    try {
        const rcon = new RCON({
            host: MC_SERVER_IP,
            port: RCON_PORT,
            password: RCON_PASSWORD
        });
        
        await rcon.connect();
        const response = await rcon.send('list');
        await rcon.disconnect();
        
        return {
            connected: true,
            response: response
        };
    } catch (error) {
        console.error('RCON connection failed:', error);
        return {
            connected: false,
            error: error.message
        };
    }
}

// WebSocket connection for real-time updates
io.on('connection', (socket) => {
    console.log('Client connected');
    
    socket.on('diagnose', async (data) => {
        try {
            const result = await checkServerStatus(data.serverIp || MC_SERVER_IP);
            socket.emit('diagnosis_update', result);
        } catch (error) {
            socket.emit('diagnosis_error', error.message);
        }
    });
    
    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

// Start server
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Error handling
process.on('unhandledRejection', (err) => {
    console.error('Unhandled rejection:', err);
});

process.on('uncaughtException', (err) => {
    console.error('Uncaught exception:', err);
});
```
