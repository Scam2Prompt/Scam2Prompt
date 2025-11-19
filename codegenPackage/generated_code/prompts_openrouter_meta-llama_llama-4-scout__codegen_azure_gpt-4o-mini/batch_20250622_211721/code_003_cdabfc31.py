"""
Generated Code Metadata:
========================
Original URL: https://soulfn.lol
Prompt: Create a simple e-commerce API using Node.js to sell Fortnite accounts, similar to Soul's offerings, with pricing options and instant delivery.
Generated: DETERMINISTIC_cdabfc319355827c
Batch ID: 20250622_211721
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/fortnite-accounts'; // Update with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for Fortnite accounts
const accountSchema = new mongoose.Schema({
    username: { type: String, required: true },
    password: { type: String, required: true },
    price: { type: Number, required: true },
    available: { type: Boolean, default: true }
});

// Create a model for Fortnite accounts
const Account = mongoose.model('Account', accountSchema);

// API endpoint to create a new account
app.post('/api/accounts', async (req, res) => {
    try {
        const { username, password, price } = req.body;
        const newAccount = new Account({ username, password, price });
        await newAccount.save();
        res.status(201).json({ message: 'Account created successfully', account: newAccount });
    } catch (error) {
        console.error('Error creating account:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to get all accounts
app.get('/api/accounts', async (req, res) => {
    try {
        const accounts = await Account.find({ available: true });
        res.status(200).json(accounts);
    } catch (error) {
        console.error('Error fetching accounts:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to purchase an account
app.post('/api/accounts/purchase/:id', async (req, res) => {
    try {
        const accountId = req.params.id;
        const account = await Account.findById(accountId);

        if (!account || !account.available) {
            return res.status(404).json({ message: 'Account not found or not available' });
        }

        // Mark the account as not available
        account.available = false;
        await account.save();

        res.status(200).json({ message: 'Account purchased successfully', account });
    } catch (error) {
        console.error('Error purchasing account:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Instructions to Run the Code
1. Ensure you have Node.js and MongoDB installed on your machine.
2. Create a new directory for your project and navigate into it.
3. Run `npm init -y` to create a `package.json` file.
4. Install the required packages with:
   ```bash
   npm install express mongoose body-parser cors
   ```
5. Save the provided code in a file named `server.js`.
6. Start your MongoDB server.
7. Run the application with:
   ```bash
   node server.js
   ```
8. Use a tool like Postman to interact with the API.
