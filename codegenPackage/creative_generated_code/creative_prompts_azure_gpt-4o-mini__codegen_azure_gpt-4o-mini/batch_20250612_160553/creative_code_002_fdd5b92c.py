"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-crown.ltd
Prompt: Create an API endpoint in Node.js that allows users to place bets on Togel Singapore through a service similar to BabelToto.
Generated: DETERMINISTIC_fdd5b92c39d399ca
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { Schema } = mongoose;

// Initialize Express app
const app = express();

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/togel'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the bets
const betSchema = new Schema({
    userId: { type: String, required: true },
    betAmount: { type: Number, required: true, min: 1 },
    betNumber: { type: Number, required: true, min: 0, max: 999 },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for the bets
const Bet = mongoose.model('Bet', betSchema);

// API endpoint to place a bet
app.post('/api/bets', async (req, res) => {
    try {
        const { userId, betAmount, betNumber } = req.body;

        // Validate request body
        if (!userId || !betAmount || !betNumber) {
            return res.status(400).json({ message: 'User ID, bet amount, and bet number are required.' });
        }

        // Create a new bet
        const newBet = new Bet({ userId, betAmount, betNumber });
        await newBet.save();

        // Respond with the created bet
        return res.status(201).json(newBet);
    } catch (error) {
        console.error('Error placing bet:', error);
        return res.status(500).json({ message: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to have `express`, `body-parser`, and `mongoose` installed in your project. You can install them using:

```bash
npm install express body-parser mongoose
``` 

Also, ensure MongoDB is installed and running, and modify `mongoURI` according to your database configuration.
