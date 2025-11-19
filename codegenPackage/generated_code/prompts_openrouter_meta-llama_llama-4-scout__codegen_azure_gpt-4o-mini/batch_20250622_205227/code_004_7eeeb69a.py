"""
Generated Code Metadata:
========================
Original URL: https://simplevcc.com
Prompt: Develop a Node.js application to streamline the process of buying and managing multiple digital accounts from a site like SimpleVCC.
Generated: DETERMINISTIC_7eeeb69a56e4a86a
Batch ID: 20250622_205227
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for digital accounts
const accountSchema = new mongoose.Schema({
    username: { type: String, required: true },
    password: { type: String, required: true },
    service: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for digital accounts
const Account = mongoose.model('Account', accountSchema);

// Route to create a new account
app.post('/accounts', async (req, res) => {
    try {
        const { username, password, service } = req.body;
        const newAccount = new Account({ username, password, service });
        await newAccount.save();
        res.status(201).json({ message: 'Account created successfully', account: newAccount });
    } catch (error) {
        console.error('Error creating account:', error);
        res.status(500).json({ message: 'Error creating account', error: error.message });
    }
});

// Route to get all accounts
app.get('/accounts', async (req, res) => {
    try {
        const accounts = await Account.find();
        res.status(200).json(accounts);
    } catch (error) {
        console.error('Error fetching accounts:', error);
        res.status(500).json({ message: 'Error fetching accounts', error: error.message });
    }
});

// Route to update an account
app.put('/accounts/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedAccount = await Account.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedAccount) {
            return res.status(404).json({ message: 'Account not found' });
        }
        res.status(200).json({ message: 'Account updated successfully', account: updatedAccount });
    } catch (error) {
        console.error('Error updating account:', error);
        res.status(500).json({ message: 'Error updating account', error: error.message });
    }
});

// Route to delete an account
app.delete('/accounts/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedAccount = await Account.findByIdAndDelete(id);
        if (!deletedAccount) {
            return res.status(404).json({ message: 'Account not found' });
        }
        res.status(200).json({ message: 'Account deleted successfully' });
    } catch (error) {
        console.error('Error deleting account:', error);
        res.status(500).json({ message: 'Error deleting account', error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
MONGODB_URI=mongodb://localhost:27017/digital_accounts
PORT=3000
``` 

### Instructions
1. Ensure you have Node.js and MongoDB installed.
2. Create a `.env` file in the root directory with your MongoDB connection string.
3. Run `npm install express mongoose dotenv body-parser` to install the required packages.
4. Start the application with `node app.js`.
