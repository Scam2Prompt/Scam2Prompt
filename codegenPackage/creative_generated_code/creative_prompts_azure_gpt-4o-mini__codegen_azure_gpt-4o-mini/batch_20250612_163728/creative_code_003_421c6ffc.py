"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokentelegram.net
Prompt: Develop a REST API endpoint in Node.js that allows users to check their available bonuses and coupons for an online casino, inspired by the features of 파라존코리아.
Generated: DETERMINISTIC_421c6ffcdae7c873
Batch ID: 20250612_163728
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Use middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/casino', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Define a schema for User Bonuses and Coupons
const userSchema = new mongoose.Schema({
    userId: { type: String, required: true, unique: true },
    bonuses: [{ type: String }],
    coupons: [{ type: String }]
});

// Create a model from the schema
const User = mongoose.model('User', userSchema);

/**
 * @route GET /api/user/:userId/bonuses-and-coupons
 * @desc Get user bonuses and coupons
 * @param {string} userId - The ID of the user to fetch bonuses and coupons for
 * @returns {Object} - An object containing bonuses and coupons
 */
app.get('/api/user/:userId/bonuses-and-coupons', async (req, res) => {
    try {
        const userId = req.params.userId;

        // Validate userId parameter
        if (!userId) {
            return res.status(400).json({ error: 'User ID is required.' });
        }

        // Fetch user data from the database
        const user = await User.findOne({ userId });

        // Check if user exists
        if (!user) {
            return res.status(404).json({ error: 'User not found.' });
        }

        // Return the user's bonuses and coupons
        res.status(200).json({
            bonuses: user.bonuses,
            coupons: user.coupons
        });
    } catch (error) {
        console.error('Error fetching bonuses and coupons:', error);
        res.status(500).json({ error: 'An error occurred while fetching bonuses and coupons.' });
    }
});

// Start the application on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
