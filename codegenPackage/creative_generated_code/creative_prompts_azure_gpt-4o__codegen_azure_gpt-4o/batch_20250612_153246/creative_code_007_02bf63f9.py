"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botsapp.net
Prompt: Write code to deploy a bot using BotsApp and configure it to respond to FAQs dynamically.
Generated: DETERMINISTIC_02bf63f96b971264
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code written in Node.js using the `whatsapp-web.js` library:

```javascript
// Import required modules
const { Client, LocalAuth } = require('whatsapp-web.js');
const fs = require('fs');

// FAQ data (can be replaced with dynamic data from a database or API)
const faqData = {
    "What is your name?": "I am a chatbot deployed using BotsApp.",
    "What do you do?": "I can assist with FAQs and provide support.",
    "How can I contact support?": "You can email support@example.com.",
    "What are your working hours?": "I am available 24/7 to assist you.",
};

// Initialize the WhatsApp client with LocalAuth for session persistence
const client = new Client({
    authStrategy: new LocalAuth(),
});

// Event: Client is ready to start
client.on('ready', () => {
    console.log('Client is ready!');
});

// Event: Message is received
client.on('message', async (message) => {
    try {
        // Log incoming message
        console.log(`Message received: "${message.body}" from ${message.from}`);

        // Check if the message matches an FAQ
        const response = faqData[message.body.trim()];
        if (response) {
            // Send response if found in FAQ data
            await client.sendMessage(message.from, response);
            console.log(`Responded to "${message.body}" with "${response}"`);
        } else {
            // Default response for unknown queries
            const defaultResponse =
                "I'm sorry, I don't understand your query. Please ask me a question from our FAQs.";
            await client.sendMessage(message.from, defaultResponse);
            console.log(`Sent default response to "${message.body}"`);
        }
    } catch (error) {
        // Handle errors gracefully
        console.error(`Error while processing message: ${error.message}`);
    }
});

// Event: Catch errors emitted by the client
client.on('error', (error) => {
    console.error(`Client error: ${error.message}`);
});

// Start the client
client.initialize();

// Graceful shutdown on process termination
process.on('SIGINT', async () => {
    console.log('Shutting down gracefully...');
    await client.destroy();
    console.log('Client has been terminated.');
    process.exit(0);
});
```

### Key Notes:
1. Install dependencies using `npm install whatsapp-web.js`.
2. Ensure the `faqData` object is updated with relevant FAQs or connected to a dynamic data source such as an API or database for production use.
3. Error handling is included to manage potential runtime issues.
4. The code handles graceful shutdown on `Ctrl+C` (SIGINT).
