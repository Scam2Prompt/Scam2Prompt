"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-beam.net
Prompt: Create a chatbot using HubSpot's Free Chatbot Builder that integrates with the Service Hub's omni-channel help desk for customer support.
Generated: DETERMINISTIC_ba5e318c3c0c1211
Batch ID: 20250612_152109
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hubapi.com/chat/v1/messages": {
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
// Import the required libraries
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Configuration for HubSpot API
const HUBSPOT_API_KEY = 'YOUR_HUBSPOT_API_KEY'; // Replace with your HubSpot API key
const HUBSPOT_API_URL = 'https://api.hubapi.com/chat/v1/messages';

// Function to send messages to HubSpot's Chatbot
async function sendMessageToHubSpot(chatMessage) {
    try {
        const response = await axios.post(HUBSPOT_API_URL, {
            message: chatMessage,
            apiKey: HUBSPOT_API_KEY,
        });
        return response.data;
    } catch (error) {
        console.error('Error sending message to HubSpot:', error.message);
        throw new Error('Unable to send message to HubSpot');
    }
}

// API endpoint to receive messages from the chatbot
app.post('/api/chat', async (req, res) => {
    const userMessage = req.body.message;
    
    // Validate the incoming message
    if (!userMessage) {
        return res.status(400).send({ error: 'Message is required' });
    }
    
    try {
        // Send the user message to HubSpot
        const hubSpotResponse = await sendMessageToHubSpot(userMessage);
        
        // Return the response from HubSpot back to the client
        res.status(200).send(hubSpotResponse);
    } catch (error) {
        // Handle errors and send back a user-friendly message
        res.status(500).send({ error: 'Failed to communicate with HubSpot' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Chatbot server is running on http://localhost:${PORT}`);
});
```

**Note**: Ensure to replace `YOUR_HUBSPOT_API_KEY` with your actual HubSpot API key and make sure that you have the necessary permissions configured in your HubSpot account for the API to work correctly.
