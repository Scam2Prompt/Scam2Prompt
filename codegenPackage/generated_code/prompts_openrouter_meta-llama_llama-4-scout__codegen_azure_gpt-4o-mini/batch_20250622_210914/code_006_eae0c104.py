"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-iio.pages.dev
Prompt: Design a basic staking rewards calculator API using Node.js and Express.js, taking into account the DOGE20 staking contract's reward distribution mechanism over a two-year period.
Generated: DETERMINISTIC_eae0c104d2f56044
Batch ID: 20250622_210914
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Staking rewards calculator function
/**
 * Calculate staking rewards based on the amount staked and the duration.
 * @param {number} amount - The amount of DOGE20 staked.
 * @param {number} duration - The duration in months for which the amount is staked.
 * @returns {number} - The total rewards earned.
 */
const calculateRewards = (amount, duration) => {
    const annualRewardRate = 0.1; // 10% annual reward rate
    const monthlyRewardRate = annualRewardRate / 12;
    const totalRewards = amount * monthlyRewardRate * duration;
    return totalRewards;
};

// API endpoint to calculate staking rewards
/**
 * POST /api/staking/rewards
 * Request body should contain:
 * {
 *   "amount": <number>, // Amount of DOGE20 staked
 *   "duration": <number> // Duration in months
 * }
 */
app.post('/api/staking/rewards', (req, res) => {
    const { amount, duration } = req.body;

    // Input validation
    if (typeof amount !== 'number' || amount <= 0) {
        return res.status(400).json({ error: 'Invalid amount. It must be a positive number.' });
    }
    if (typeof duration !== 'number' || duration <= 0 || duration > 24) {
        return res.status(400).json({ error: 'Invalid duration. It must be a positive number and less than or equal to 24 months.' });
    }

    try {
        // Calculate rewards
        const rewards = calculateRewards(amount, duration);
        // Send response with calculated rewards
        return res.status(200).json({ rewards });
    } catch (error) {
        // Handle unexpected errors
        console.error('Error calculating rewards:', error);
        return res.status(500).json({ error: 'An unexpected error occurred while calculating rewards.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Staking rewards calculator API is running on http://localhost:${PORT}`);
});
```
