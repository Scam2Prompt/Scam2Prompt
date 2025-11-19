"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Develop a chatbot script using Node.js and natural language processing (NLP) to handle customer inquiries about housekeeping and cleaning services provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_c61c871523b95503
Batch ID: 20250622_210703
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
const bodyParser = require('body-parser');
const { NlpManager } = require('node-nlp');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Create an instance of the NLP manager
const manager = new NlpManager({ languages: ['en'] });

// Function to train the NLP model
async function trainNLP() {
    // Add intents and responses for housekeeping inquiries
    manager.addDocument('en', 'What cleaning services do you offer?', 'services.cleaning');
    manager.addDocument('en', 'Tell me about your housekeeping services.', 'services.housekeeping');
    manager.addDocument('en', 'How can I book a cleaning service?', 'services.booking');
    manager.addDocument('en', 'What are your rates for cleaning?', 'services.rates');
    manager.addDocument('en', 'Do you provide deep cleaning?', 'services.deep_cleaning');

    // Add responses for the intents
    manager.addAnswer('en', 'services.cleaning', 'We offer a variety of cleaning services including residential, commercial, and specialized cleaning.');
    manager.addAnswer('en', 'services.housekeeping', 'Our housekeeping services include regular cleaning, laundry, and organizing your space.');
    manager.addAnswer('en', 'services.booking', 'You can book a cleaning service by visiting our website or calling our customer service.');
    manager.addAnswer('en', 'services.rates', 'Our rates vary based on the type of service and the size of the area. Please contact us for a quote.');
    manager.addAnswer('en', 'services.deep_cleaning', 'Yes, we provide deep cleaning services that cover every corner of your home or office.');

    // Train the model
    await manager.train();
    manager.save();
}

// Endpoint to handle incoming chat messages
app.post('/chat', async (req, res) => {
    const { message } = req.body;

    // Validate incoming message
    if (!message) {
        return res.status(400).json({ error: 'Message is required' });
    }

    try {
        // Process the message using the NLP manager
        const response = await manager.process('en', message);
        
        // Send the response back to the client
        return res.json({ response: response.answer || 'I am sorry, I did not understand that.' });
    } catch (error) {
        console.error('Error processing message:', error);
        return res.status(500).json({ error: 'An error occurred while processing your request.' });
    }
});

// Start the server and train the NLP model
app.listen(PORT, async () => {
    console.log(`Server is running on port ${PORT}`);
    await trainNLP();
    console.log('NLP model trained and ready to handle inquiries.');
});
```
