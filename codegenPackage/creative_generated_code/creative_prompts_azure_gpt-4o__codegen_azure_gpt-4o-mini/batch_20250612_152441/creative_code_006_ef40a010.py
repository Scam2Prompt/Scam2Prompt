"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Create a REST API in Node.js to retrieve real-time data about CNK token transactions and supply chain details for farmers, traders, roasters, and retailers.
Generated: DETERMINISTIC_ef40a01071117d2b
Batch ID: 20250612_152441
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
const axios = require('axios');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware for parsing JSON payloads
app.use(express.json());

// MongoDB connection string from environment variables
const mongoURI = process.env.MONGODB_URI;

// Connecting to MongoDB
mongoose.connect(mongoURI, { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for CNK transactions
const cnkTransactionSchema = new mongoose.Schema({
    farmerId: String,
    traderId: String,
    roasterId: String,
    retailerId: String,
    amount: Number,
    timestamp: { type: Date, default: Date.now }
});

// Create a model for CNK transactions
const CnkTransaction = mongoose.model('CnkTransaction', cnkTransactionSchema);

// Route to retrieve real-time CNK token transactions
app.get('/api/cnk/transactions', async (req, res) => {
    try {
        const transactions = await CnkTransaction.find();
        res.status(200).json(transactions);
    } catch (error) {
        console.error('Error fetching transactions:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Route to fetch supply chain details
app.get('/api/cnk/supply-chain', async (req, res) => {
    try {
        // Dummy data for supply chain details, replace with real data fetching logic
        const supplyChainDetails = {
            farmers: 120,
            traders: 50,
            roasters: 30,
            retailers: 75
        };
        res.status(200).json(supplyChainDetails);
    } catch (error) {
        console.error('Error fetching supply chain details:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```

### .env file example
```
MONGODB_URI=mongodb://<username>:<password>@localhost:27017/cnkdb
PORT=3000
```

### Instructions
1. Make sure you have Node.js and MongoDB installed.
2. Create a `.env` file with your MongoDB URI and desired port.
3. Run `npm install express mongoose axios dotenv` to install dependencies.
4. Start the server with `node <filename>.js`.
