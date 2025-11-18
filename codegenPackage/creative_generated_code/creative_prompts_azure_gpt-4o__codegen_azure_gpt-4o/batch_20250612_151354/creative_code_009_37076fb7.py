"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Develop a tournament lobby system for a blockchain FPS game, referencing ev.io's ability to host minigames and tournaments.
Generated: DETERMINISTIC_37076fb7dafe6c05
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Tournament Lobby System for a Blockchain FPS Game
 * Features:
 * - Create, join, and manage tournament lobbies
 * - Support for hosting minigames and tournaments
 * - Blockchain integration for user authentication and payments
 *
 * Prerequisites:
 * - Node.js runtime
 * - Web3.js or ethers.js for blockchain interactions
 * - Express.js for server management
 */

const express = require('express');
const { ethers } = require('ethers');
require('dotenv').config();

// Initialize Express application
const app = express();
app.use(express.json());

// Blockchain configuration
const provider = new ethers.providers.JsonRpcProvider(process.env.BLOCKCHAIN_RPC_URL);
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// In-memory storage for lobbies
const lobbies = {};

/**
 * Create a new lobby.
 * @param {string} lobbyName - Name of the lobby
 * @param {string} hostAddress - Blockchain address of the host
 */
app.post('/create-lobby', async (req, res) => {
    const { lobbyName, hostAddress } = req.body;

    try {
        // Validate input
        if (!lobbyName || !hostAddress) {
            return res.status(400).json({ error: 'Lobby name and host address are required.' });
        }

        // Ensure the host address is valid
        if (!ethers.utils.isAddress(hostAddress)) {
            return res.status(400).json({ error: 'Invalid blockchain address provided.' });
        }

        // Check if lobby name already exists
        if (lobbies[lobbyName]) {
            return res.status(400).json({ error: 'Lobby name already exists.' });
        }

        // Create lobby
        lobbies[lobbyName] = {
            host: hostAddress,
            players: [hostAddress],
            status: 'waiting', // Possible statuses: waiting, in-progress, completed
        };

        res.status(201).json({ message: 'Lobby created successfully.', lobby: lobbies[lobbyName] });
    } catch (error) {
        console.error('Error creating lobby:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

/**
 * Join an existing lobby.
 * @param {string} lobbyName - Name of the lobby
 * @param {string} playerAddress - Blockchain address of the player
 */
app.post('/join-lobby', async (req, res) => {
    const { lobbyName, playerAddress } = req.body;

    try {
        // Validate input
        if (!lobbyName || !playerAddress) {
            return res.status(400).json({ error: 'Lobby name and player address are required.' });
        }

        // Ensure the player address is valid
        if (!ethers.utils.isAddress(playerAddress)) {
            return res.status(400).json({ error: 'Invalid blockchain address provided.' });
        }

        const lobby = lobbies[lobbyName];
        if (!lobby) {
            return res.status(404).json({ error: 'Lobby not found.' });
        }

        // Check if player is already in the lobby
        if (lobby.players.includes(playerAddress)) {
            return res.status(400).json({ error: 'Player is already in the lobby.' });
        }

        // Add player to the lobby
        lobby.players.push(playerAddress);
        res.status(200).json({ message: 'Joined lobby successfully.', lobby });
    } catch (error) {
        console.error('Error joining lobby:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

/**
 * Start a tournament in the lobby.
 * @param {string} lobbyName - Name of the lobby
 */
app.post('/start-tournament', async (req, res) => {
    const { lobbyName } = req.body;

    try {
        // Validate input
        if (!lobbyName) {
            return res.status(400).json({ error: 'Lobby name is required.' });
        }

        const lobby = lobbies[lobbyName];
        if (!lobby) {
            return res.status(404).json({ error: 'Lobby not found.' });
        }

        // Check lobby status and player count
        if (lobby.status !== 'waiting') {
            return res.status(400).json({ error: 'Lobby is not in a valid state to start a tournament.' });
        }
        if (lobby.players.length < 2) {
            return res.status(400).json({ error: 'Not enough players to start a tournament.' });
        }

        // Start tournament
        lobby.status = 'in-progress';
        res.status(200).json({ message: 'Tournament started successfully.', lobby });
    } catch (error) {
        console.error('Error starting tournament:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

/**
 * End a tournament in the lobby.
 * @param {string} lobbyName - Name of the lobby
 */
app.post('/end-tournament', async (req, res) => {
    const { lobbyName } = req.body;

    try {
        // Validate input
        if (!lobbyName) {
            return res.status(400).json({ error: 'Lobby name is required.' });
        }

        const lobby = lobbies[lobbyName];
        if (!lobby) {
            return res.status(404).json({ error: 'Lobby not found.' });
        }

        // End tournament
        lobby.status = 'completed';
        res.status(200).json({ message: 'Tournament ended successfully.', lobby });
    } catch (error) {
        console.error('Error ending tournament:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Tournament Lobby System running on port ${PORT}`);
});
```
