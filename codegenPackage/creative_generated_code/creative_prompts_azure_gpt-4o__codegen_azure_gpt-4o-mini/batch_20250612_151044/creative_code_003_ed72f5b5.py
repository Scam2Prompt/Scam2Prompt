"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Develop a backend system in Node.js to manage slot deposit transactions, including features for tracking "ribuan permainan slot online terbaru" and handling deposits starting at 5k IDR.
Generated: DETERMINISTIC_ed72f5b55aafd361
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // For parsing application/json

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/slotDepositDB';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for slot deposit transactions
const slotDepositSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    amount: { type: Number, required: true, min: 5000 }, // Minimum deposit of 5k IDR
    timestamp: { type: Date, default: Date.now },
    gameName: { type: String, required: true }
});

// Create a model based on the schema
const SlotDeposit = mongoose.model('SlotDeposit', slotDepositSchema);

// Endpoint to create a new slot deposit transaction
app.post('/api/deposits', async (req, res) => {
    const { userId, amount, gameName } = req.body;

    // Validate input data
    if (!userId || !amount || !gameName) {
        return res.status(400).json({ error: 'User ID, amount, and game name are required' });
    }

    if (amount < 5000) {
        return res.status(400).json({ error: 'Minimum deposit amount is 5k IDR' });
    }

    try {
        // Create new slot deposit record
        const newDeposit = new SlotDeposit({ userId, amount, gameName });
        await newDeposit.save();
        res.status(201).json(newDeposit);
    } catch (error) {
        console.error('Error saving deposit:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Endpoint to get all deposits for a specific user
app.get('/api/deposits/:userId', async (req, res) => {
    const { userId } = req.params;

    try {
        const deposits = await SlotDeposit.find({ userId }).sort({ timestamp: -1 });
        res.json(deposits);
    } catch (error) {
        console.error('Error retrieving deposits:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
