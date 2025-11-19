"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth.net
Prompt: Generate code to display a portfolio balance for users in a web app that supports multiple wallets, inspired by Common Wealth.
Generated: DETERMINISTIC_507b232155aca0d9
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a simple web application backend (using Node.js with Express and MongoDB) to display a portfolio balance for users with multiple wallets:

```javascript
// Import required modules
const express = require('express'); // Web framework
const mongoose = require('mongoose'); // MongoDB connection
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Enable JSON parsing in request bodies

// Connect to MongoDB
mongoose
  .connect('mongodb://localhost:27017/portfolioDB', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define Mongoose schema and model for Wallet and User
const walletSchema = new mongoose.Schema({
  name: { type: String, required: true }, // Wallet name (e.g., "Savings", "Investments")
  balance: { type: Number, required: true, min: 0 }, // Wallet balance
});

const userSchema = new mongoose.Schema({
  name: { type: String, required: true }, // User's name
  email: { type: String, required: true, unique: true }, // User's email
  wallets: [walletSchema], // Array of wallets for the user
});

const User = mongoose.model('User', userSchema);

// Route to get portfolio balance for a user
app.get('/portfolio-balance/:email', async (req, res) => {
  try {
    const { email } = req.params; // Extract user email from request parameters

    // Fetch user details from the database
    const user = await User.findOne({ email }).exec();

    if (!user) {
      // Return 404 if user is not found
      return res.status(404).json({ error: 'User not found' });
    }

    // Calculate portfolio balance by summing up wallet balances
    const portfolioBalance = user.wallets.reduce((total, wallet) => total + wallet.balance, 0);

    // Respond with the portfolio balance and wallet details
    res.json({
      user: user.name,
      email: user.email,
      portfolioBalance,
      wallets: user.wallets,
    });
  } catch (error) {
    // Handle server errors
    console.error('Error fetching portfolio balance:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to add a wallet to a user
app.post('/add-wallet', async (req, res) => {
  try {
    const { email, walletName, walletBalance } = req.body;

    if (!email || !walletName || walletBalance === undefined) {
      // Validate request body
      return res.status(400).json({ error: 'Invalid request: Missing parameters' });
    }

    const user = await User.findOne({ email }).exec();

    if (!user) {
      // Return 404 if user is not found
      return res.status(404).json({ error: 'User not found' });
    }

    // Add new wallet to user's wallets array
    user.wallets.push({ name: walletName, balance: walletBalance });
    await user.save();

    // Respond with updated user details
    res.json({ message: 'Wallet added successfully', user });
  } catch (error) {
    // Handle server errors
    console.error('Error adding wallet:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to create a new user
app.post('/create-user', async (req, res) => {
  try {
    const { name, email } = req.body;

    if (!name || !email) {
      // Validate request body
      return res.status(400).json({ error: 'Invalid request: Missing parameters' });
    }

    // Check if user already exists
    const existingUser = await User.findOne({ email }).exec();

    if (existingUser) {
      // Return 409 if user already exists
      return res.status(409).json({ error: 'User already exists' });
    }

    // Create and save new user
    const newUser = new User({ name, email, wallets: [] });
    await newUser.save();

    // Respond with created user details
    res.status(201).json({ message: 'User created successfully', user: newUser });
  } catch (error) {
    // Handle server errors
    console.error('Error creating user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment port if available, otherwise default to 3000
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Notes:**
1. Replace `'mongodb://localhost:27017/portfolioDB'` with your actual MongoDB connection string.
2. The code includes routes for creating users (`POST /create-user`), adding wallets (`POST /add-wallet`), and fetching portfolio balance (`GET /portfolio-balance/:email`).
3. Error handling validates input and handles server/database errors properly.
