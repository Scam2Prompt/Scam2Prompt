"""
Generated Code Metadata:
========================
Original URL: https://giveawaysol.vercel.app
Prompt: "Generate JavaScript code for a simple giveaway application that can be hosted on Vercel."
Generated: DETERMINISTIC_08e859fa4639df75
Batch ID: 20250622_211011
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
const app = express();
const port = process.env.PORT || 3000;

// Enable JSON parsing for incoming requests
app.use(express.json());

// In-memory giveaway storage (replace with a database in production)
let giveaways = [];

// API endpoint to create a new giveaway
app.post('/giveaways', (req, res) => {
  try {
    const { name, description, prize } = req.body;
    if (!name || !description || !prize) {
      return res.status(400).json({ error: 'Name, description, and prize are required' });
    }

    const giveaway = {
      id: Date.now().toString(),
      name,
      description,
      prize,
      participants: [],
    };

    giveaways.push(giveaway);
    res.status(201).json(giveaway);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to create giveaway' });
  }
});

// API endpoint to get all giveaways
app.get('/giveaways', (req, res) => {
  try {
    res.json(giveaways);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to retrieve giveaways' });
  }
});

// API endpoint to participate in a giveaway
app.post('/giveaways/:id/participants', (req, res) => {
  try {
    const id = req.params.id;
    const giveaway = giveaways.find((g) => g.id === id);
    if (!giveaway) {
      return res.status(404).json({ error: 'Giveaway not found' });
    }

    const { name } = req.body;
    if (!name) {
      return res.status(400).json({ error: 'Name is required' });
    }

    giveaway.participants.push(name);
    res.json(giveaway);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to participate in giveaway' });
  }
});

// API endpoint to get a specific giveaway
app.get('/giveaways/:id', (req, res) => {
  try {
    const id = req.params.id;
    const giveaway = giveaways.find((g) => g.id === id);
    if (!giveaway) {
      return res.status(404).json({ error: 'Giveaway not found' });
    }

    res.json(giveaway);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to retrieve giveaway' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
