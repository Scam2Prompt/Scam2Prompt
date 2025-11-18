"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Create a REST API endpoint using Node.js and Express to retrieve EarthMeta token presale statistics, including raised funds, current price, and bonus stages.
Generated: DETERMINISTIC_10b603de64f01813
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express'); // Express framework for building APIs
const app = express(); // Initialize the Express application
const PORT = 3000; // Port number for the server to listen on

// Mock data simulating presale statistics
const presaleStatistics = {
    raisedFunds: 250000, // Total funds raised (in USD or other currency)
    currentPrice: 0.05, // Current token price (in USD or other currency)
    bonusStages: [
        { stage: 1, bonusPercentage: 20, threshold: 50000 }, // Stage 1 with a 20% bonus and a $50,000 threshold
        { stage: 2, bonusPercentage: 10, threshold: 150000 }, // Stage 2 with a 10% bonus and a $150,000 threshold
        { stage: 3, bonusPercentage: 5, threshold: 300000 } // Stage 3 with a 5% bonus and a $300,000 threshold
    ]
};

// Middleware to parse JSON requests
app.use(express.json());

// Define a REST API endpoint to retrieve presale statistics
/**
 * @route   GET /api/presale-stats
 * @desc    Retrieve EarthMeta token presale statistics
 * @access  Public
 */
app.get('/api/presale-stats', (req, res) => {
    try {
        // Respond with the mock data for presale statistics
        res.status(200).json({
            success: true, // Indicate the request was successful
            data: presaleStatistics // Include the presale statistics
        });
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error retrieving presale statistics:', error);
        res.status(500).json({
            success: false, // Indicate the request failed
            message: 'An error occurred while retrieving presale statistics.', // Provide an error message
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`); // Log the server start message
});

// Export the app for modularity/testing purposes
module.exports = app;
```
