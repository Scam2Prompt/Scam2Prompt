"""
Generated Code Metadata:
========================
Original URL: https://initia.co
Prompt: Write code to integrate a full-stack app into the Initia multichain ecosystem using its interwoven infrastructure. Include steps for aligning the app with Initia's economic model.
Generated: DETERMINISTIC_02d025267ccf6f41
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { initiaClient } = require('initia-sdk'); // Hypothetical Initia SDK
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = process.env.MONGO_URI || 'mongodb://localhost:27017/initiaApp';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a simple User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    walletAddress: { type: String, required: true, unique: true },
    balance: { type: Number, default: 0 }
});

// Create a User model
const User = mongoose.model('User', userSchema);

// Initialize Initia client
const initia = initiaClient({
    apiKey: process.env.INITIA_API_KEY,
    network: 'mainnet' // or 'testnet' based on your environment
});

// Endpoint to register a new user
app.post('/api/register', async (req, res) => {
    const { username, walletAddress } = req.body;

    try {
        // Check if user already exists
        const existingUser = await User.findOne({ walletAddress });
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }

        // Create a new user
        const newUser = new User({ username, walletAddress });
        await newUser.save();

        // Align with Initia's economic model (hypothetical)
        await initia.economicModel.alignUser(walletAddress);

        res.status(201).json({ message: 'User registered successfully', user: newUser });
    } catch (error) {
        console.error('Error registering user:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to get user balance
app.get('/api/balance/:walletAddress', async (req, res) => {
    const { walletAddress } = req.params;

    try {
        const user = await User.findOne({ walletAddress });
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }

        // Fetch balance from Initia
        const balance = await initia.getBalance(walletAddress);
        user.balance = balance; // Update local balance
        await user.save();

        res.status(200).json({ walletAddress, balance });
    } catch (error) {
        console.error('Error fetching balance:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGINT', async () => {
    await mongoose.connection.close();
    console.log('MongoDB connection closed');
    process.exit(0);
});
```

### Environment Variables
Make sure to set the following environment variables in your production environment:
- `MONGO_URI`: MongoDB connection string
- `INITIA_API_KEY`: API key for Initia SDK

### Note
This code assumes the existence of a hypothetical `initia-sdk` for interacting with the Initia multichain ecosystem. Adjust the SDK methods and parameters according to the actual SDK documentation.
