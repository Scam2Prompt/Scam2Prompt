"""
Generated Code Metadata:
========================
Original URL: https://wir-c5v.pages.dev
Prompt: Create a help and support chatbot using JavaScript for a cryptocurrency exchange platform like WazirX.
Generated: DETERMINISTIC_ef7fc24b98db081f
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const app = express();
const { WebhookClient } = require('dialogflow-fulfillment');
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/wazirx-chatbot', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for user queries
const querySchema = new mongoose.Schema({
  query: String,
  response: String
});

// Create model for user queries
const Query = mongoose.model('Query', querySchema);

// Enable JSON body parsing
app.use(express.json());

// Dialogflow fulfillment webhook
const webhook = new WebhookClient({
  // Replace with your Dialogflow project's ID
  projectId: 'wazirx-chatbot',
  // Replace with your Dialogflow agent's credentials
  credentials: JSON.parse(process.env.DIALOGFLOW_CREDENTIALS)
});

// Handle user queries
app.post('/query', async (req, res) => {
  try {
    const userQuery = req.body.query;
    const query = new Query({ query: userQuery });
    await query.save();

    // Process user query using Dialogflow
    const sessionPath = webhook.sessionPath('wazirx-chatbot', req.body.sessionId);
    const request = {
      session: sessionPath,
      queryInput: {
        text: {
          text: userQuery,
          languageCode: 'en-US'
        }
      }
    };

    const response = await webhook.send(request);
    const fulfillmentText = response[0].queryResult.fulfillmentText;

    // Save response to database
    query.response = fulfillmentText;
    await query.save();

    res.json({ response: fulfillmentText });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Handle common support queries
const supportQueries = {
  'account_balance': 'You can check your account balance by logging into your WazirX account and navigating to the dashboard.',
  'deposit_bitcoin': 'To deposit Bitcoin, navigate to the deposit section, select Bitcoin, and follow the instructions.',
  'withdraw_bitcoin': 'To withdraw Bitcoin, navigate to the withdraw section, select Bitcoin, and follow the instructions.'
};

// Handle support queries
app.post('/support', async (req, res) => {
  try {
    const query = req.body.query;
    const response = supportQueries[query.toLowerCase()];

    if (response) {
      res.json({ response });
    } else {
      res.status(404).json({ error: 'Query not found' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
