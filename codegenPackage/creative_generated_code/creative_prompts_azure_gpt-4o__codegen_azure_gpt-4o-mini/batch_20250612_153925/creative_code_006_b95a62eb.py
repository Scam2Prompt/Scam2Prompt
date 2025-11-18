"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Create a REST API endpoint to manage Fixed Deposit Receipt (FDR) plans, allowing users to apply for plans and calculate total returns based on the interval and interest rate provided by Express Finance Banking.
Generated: DETERMINISTIC_b95a62eb28e4e400
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// In-memory storage for FDR plans
const fdrPlans = [];

// Error handling middleware
const errorHandler = (err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
};

// Apply for a new FDR plan
app.post('/api/fdr', (req, res, next) => {
    const { investorName, amount, interestRate, duration } = req.body;

    // Input validation
    if (!investorName || !amount || !interestRate || !duration) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    if (isNaN(amount) || isNaN(interestRate) || isNaN(duration)) {
        return res.status(400).json({ error: 'Amount, interest rate, and duration must be numbers.' });
    }

    // Create a new FDR plan
    const newFDR = {
        id: uuidv4(),
        investorName,
        amount: parseFloat(amount),
        interestRate: parseFloat(interestRate),
        duration: parseInt(duration),
        createdAt: new Date(),
    };

    fdrPlans.push(newFDR);
    res.status(201).json(newFDR);
});

// Calculate total returns based on the parameters
app.post('/api/fdr/calculate', (req, res) => {
    const { amount, interestRate, duration } = req.body;

    // Input validation
    if (!amount || !interestRate || !duration) {
        return res.status(400).json({ error: 'Amount, interest rate, and duration are required.' });
    }

    if (isNaN(amount) || isNaN(interestRate) || isNaN(duration)) {
        return res.status(400).json({ error: 'Amount, interest rate, and duration must be numbers.' });
    }

    // Calculate total returns (Simple Interest)
    const principal = parseFloat(amount);
    const rate = parseFloat(interestRate) / 100;
    const time = parseInt(duration);

    const totalReturns = principal + (principal * rate * time);

    res.status(200).json({ totalReturns });
});

// List all FDR plans
app.get('/api/fdr', (req, res) => {
    res.status(200).json(fdrPlans);
});

// Attach error handler middleware
app.use(errorHandler);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
