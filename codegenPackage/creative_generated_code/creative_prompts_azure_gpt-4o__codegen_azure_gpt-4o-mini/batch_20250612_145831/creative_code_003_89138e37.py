"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicevm.pages.dev
Prompt: Provide an example of how to use Sonic's sandbox utilities to build business logic for on-chain gaming applications.
Generated: DETERMINISTIC_89138e3704280895
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Sonic's SDK
const { Sonic } = require('sonic-sdk'); // Adjust the import based on Sonic SDK structure

// Initialize the Sonic instance
const sonic = new Sonic({
    network: 'mainnet', // Specify the network you are connecting to
    apiKey: 'YOUR_API_KEY', // Use your Sonic API key
});

// Function to create a new game
async function createGame(gameData) {
    try {
        // Validate the game data
        if (!gameData.name || !gameData.description) {
            throw new Error('Game name and description are required.');
        }

        // Build the transaction for creating a game
        const transaction = await sonic.createTransaction({
            type: 'create_game',
            data: gameData,
        });

        // Send the transaction to the blockchain
        const response = await sonic.sendTransaction(transaction);
        console.log('Game created successfully:', response);
        
        return response;
    } catch (error) {
        console.error('Error creating game:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Function to join a game
async function joinGame(gameId, playerData) {
    try {
        // Validate player data
        if (!playerData.username) {
            throw new Error('Player username is required.');
        }

        // Build the transaction for joining a game
        const transaction = await sonic.createTransaction({
            type: 'join_game',
            data: { gameId, playerData },
        });

        // Send the transaction to the blockchain
        const response = await sonic.sendTransaction(transaction);
        console.log('Player joined the game successfully:', response);
        
        return response;
    } catch (error) {
        console.error('Error joining game:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Function to start the game
async function startGame(gameId) {
    try {
        // Build the transaction for starting the game
        const transaction = await sonic.createTransaction({
            type: 'start_game',
            data: { gameId },
        });

        // Send the transaction to the blockchain
        const response = await sonic.sendTransaction(transaction);
        console.log('Game started successfully:', response);
        
        return response;
    } catch (error) {
        console.error('Error starting game:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Example usage
(async () => {
    try {
        const gameData = {
            name: 'Adventure Quest',
            description: 'An epic adventure game.',
        };

        const gameResponse = await createGame(gameData);
        
        const playerData = {
            username: 'Player1',
        };

        await joinGame(gameResponse.id, playerData);
        await startGame(gameResponse.id);
        
    } catch (error) {
        console.error('An error occurred during the game operations:', error.message);
    }
})();
```
