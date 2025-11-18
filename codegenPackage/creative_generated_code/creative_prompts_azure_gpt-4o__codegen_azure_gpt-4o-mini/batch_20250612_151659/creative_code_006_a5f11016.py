"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetaria.world
Prompt: Provide a step-by-step guide to integrate the Planetaria metaverse with a web application using JavaScript.
Generated: DETERMINISTIC_a5f110167302b5bf
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Import necessary libraries
import { Planetaria } from 'planetaria-sdk'; // Assuming there's an SDK for Planetaria
import express from 'express'; // For creating a web server
import http from 'http'; // For handling HTTP requests
import { Server } from 'socket.io'; // For real-time communication

// Step 2: Initialize the Express application
const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Step 3: Set up middleware to parse JSON requests
app.use(express.json());

// Step 4: Initialize Planetaria connection
const planetaria = new Planetaria({
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
    // Additional configuration options can be added here
});

// Step 5: Handle connection errors
planetaria.on('error', (error) => {
    console.error('Error connecting to Planetaria:', error);
});

// Step 6: Define a route for the main application
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html'); // Serve your main HTML file
});

// Step 7: Set up a Socket.io connection
io.on('connection', (socket) => {
    console.log('A user connected:', socket.id);

    // Step 8: Listen for events from the client
    socket.on('joinPlanet', async (planetId) => {
        try {
            const planetData = await planetaria.joinPlanet(planetId);
            socket.emit('planetData', planetData); // Send planet data to the client
        } catch (error) {
            console.error('Error joining planet:', error);
            socket.emit('error', 'Failed to join the planet.');
        }
    });

    // Step 9: Handle disconnection
    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
    });
});

// Step 10: Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Note: Make sure to create the 'index.html' file with the necessary frontend code to interact with this backend.
```
