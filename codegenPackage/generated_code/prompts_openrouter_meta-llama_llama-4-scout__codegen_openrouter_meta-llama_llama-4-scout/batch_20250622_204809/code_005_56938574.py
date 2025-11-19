"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Propose an API architecture for a play-to-own game like Narcos Land, incorporating $PABLO tokens for in-game transactions and NFT ownership, ensuring a seamless user experience.
Generated: DETERMINISTIC_569385742406d785
Batch ID: 20250622_204809
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
const mongoose = require('mongoose');
const web3 = require('web3');
const { NFT } = require('./models/NFT');
const { User } = require('./models/User');
const { Transaction } = require('./models/Transaction');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/narcos-land', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the API endpoint for user registration
app.post('/register', async (req, res) => {
    try {
        // Validate user input
        if (!req.body.username || !req.body.email || !req.body.password) {
            return res.status(400).send({ message: 'Please provide all required fields' });
        }

        // Create a new user
        const user = new User(req.body);
        await user.save();

        // Generate a JSON Web Token (JWT) for the user
        const token = user.generateAuthToken();

        // Return the user and JWT
        res.send({ user, token });
    } catch (error) {
        res.status(500).send({ message: 'Failed to register user' });
    }
});

// Define the API endpoint for user login
app.post('/login', async (req, res) => {
    try {
        // Validate user input
        if (!req.body.email || !req.body.password) {
            return res.status(400).send({ message: 'Please provide email and password' });
        }

        // Find the user by email
        const user = await User.findOne({ email: req.body.email });

        // Check if the user exists and the password is correct
        if (!user || !(await user.comparePassword(req.body.password))) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }

        // Generate a JSON Web Token (JWT) for the user
        const token = user.generateAuthToken();

        // Return the user and JWT
        res.send({ user, token });
    } catch (error) {
        res.status(500).send({ message: 'Failed to login user' });
    }
});

// Define the API endpoint for NFT creation
app.post('/nfts', authenticate, async (req, res) => {
    try {
        // Validate NFT input
        if (!req.body.name || !req.body.description || !req.body.image) {
            return res.status(400).send({ message: 'Please provide all required fields' });
        }

        // Create a new NFT
        const nft = new NFT(req.body);
        await nft.save();

        // Return the NFT
        res.send(nft);
    } catch (error) {
        res.status(500).send({ message: 'Failed to create NFT' });
    }
});

// Define the API endpoint for NFT ownership transfer
app.patch('/nfts/:id/transfer', authenticate, async (req, res) => {
    try {
        // Find the NFT by ID
        const nft = await NFT.findById(req.params.id);

        // Check if the NFT exists
        if (!nft) {
            return res.status(404).send({ message: 'NFT not found' });
        }

        // Validate transfer input
        if (!req.body.to) {
            return res.status(400).send({ message: 'Please provide the recipient address' });
        }

        // Transfer NFT ownership
        nft.owner = req.body.to;
        await nft.save();

        // Return the updated NFT
        res.send(nft);
    } catch (error) {
        res.status(500).send({ message: 'Failed to transfer NFT ownership' });
    }
});

// Define the API endpoint for $PABLO token transactions
app.post('/transactions', authenticate, async (req, res) => {
    try {
        // Validate transaction input
        if (!req.body.amount || !req.body.to) {
            return res.status(400).send({ message: 'Please provide all required fields' });
        }

        // Get the user's $PABLO token balance
        const user = await User.findById(req.user._id);
        const balance = user.pabloTokens;

        // Check if the user has sufficient balance
        if (balance < req.body.amount) {
            return res.status(400).send({ message: 'Insufficient $PABLO token balance' });
        }

        // Create a new transaction
        const transaction = new Transaction({
            from: req.user._id,
            to: req.body.to,
            amount: req.body.amount,
        });

        // Update the user's $PABLO token balance
        user.pabloTokens -= req.body.amount;
        await user.save();

        // Save the transaction
        await transaction.save();

        // Return the transaction
        res.send(transaction);
    } catch (error) {
        res.status(500).send({ message: 'Failed to process transaction' });
    }
});

// Middleware to authenticate requests
function authenticate(req, res, next) {
    try {
        // Get the Authorization header
        const token = req.header('Authorization').replace('Bearer ', '');

        // Verify the JWT
        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        // Set the authenticated user
        req.user = decoded;
        next();
    } catch (error) {
        res.status(401).send({ message: 'Please authenticate' });
    }
}

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

```javascript
// models/NFT.js
const mongoose = require('mongoose');

const nftSchema = new mongoose.Schema({
    name: String,
    description: String,
    image: String,
    owner: String,
});

const NFT = mongoose.model('NFT', nftSchema);

module.exports = { NFT };
```

```javascript
// models/User.js
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');

const userSchema = new mongoose.Schema({
    username: String,
    email: String,
    password: String,
    pabloTokens: Number,
});

userSchema.methods.generateAuthToken = function() {
    const token = jwt.sign({ _id: this._id }, process.env.JWT_SECRET, { expiresIn: '1 hour' });
    return token;
};

userSchema.methods.comparePassword = async function(password) {
    return await bcrypt.compare(password, this.password);
};

const User = mongoose.model('User', userSchema);

module.exports = { User };
```

```javascript
// models/Transaction.js
const mongoose = require('mongoose');

const transactionSchema = new mongoose.Schema({
    from: String,
    to: String,
    amount: Number,
});

const Transaction = mongoose.model('Transaction', transactionSchema);

module.exports = { Transaction };
```
