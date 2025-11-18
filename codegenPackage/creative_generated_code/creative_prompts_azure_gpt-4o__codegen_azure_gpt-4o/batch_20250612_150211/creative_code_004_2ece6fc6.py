"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Create a REST API in Node.js for managing investment plans, user accounts, and profit calculations, inspired by the features on hedgefund-options.com.
Generated: DETERMINISTIC_2ece6fc6f2cf70d8
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database (for demo purposes, replace with a proper database for production)
const users = [];
const investmentPlans = [];

// Utility functions
const calculateProfit = (amount, interestRate, durationInMonths) => {
    return (amount * interestRate * durationInMonths) / 100;
};

// Routes

// User Management Endpoints

// Create a new user
app.post('/users', (req, res) => {
    try {
        const { name, email } = req.body;

        if (!name || !email) {
            return res.status(400).json({ message: 'Name and Email are required.' });
        }

        const newUser = {
            id: uuidv4(),
            name,
            email,
            createdAt: new Date(),
        };

        users.push(newUser);

        res.status(201).json({ message: 'User created successfully.', user: newUser });
    } catch (error) {
        res.status(500).json({ message: 'An error occurred while creating the user.', error: error.message });
    }
});

// Get all users
app.get('/users', (req, res) => {
    res.status(200).json(users);
});

// Investment Plan Endpoints

// Create a new investment plan
app.post('/investment-plans', (req, res) => {
    try {
        const { name, interestRate, durationInMonths } = req.body;

        if (!name || interestRate === undefined || durationInMonths === undefined) {
            return res.status(400).json({ message: 'Name, interest rate, and duration are required.' });
        }

        const newPlan = {
            id: uuidv4(),
            name,
            interestRate,
            durationInMonths,
            createdAt: new Date(),
        };

        investmentPlans.push(newPlan);

        res.status(201).json({ message: 'Investment plan created successfully.', plan: newPlan });
    } catch (error) {
        res.status(500).json({ message: 'An error occurred while creating the investment plan.', error: error.message });
    }
});

// Get all investment plans
app.get('/investment-plans', (req, res) => {
    res.status(200).json(investmentPlans);
});

// Profit Calculation Endpoint

// Calculate profit based on an investment plan
app.post('/calculate-profit', (req, res) => {
    try {
        const { planId, amount } = req.body;

        if (!planId || amount === undefined) {
            return res.status(400).json({ message: 'Plan ID and amount are required.' });
        }

        const plan = investmentPlans.find((p) => p.id === planId);

        if (!plan) {
            return res.status(404).json({ message: 'Investment plan not found.' });
        }

        const profit = calculateProfit(amount, plan.interestRate, plan.durationInMonths);

        res.status(200).json({
            message: 'Profit calculated successfully.',
            profit,
            investmentPlan: plan,
        });
    } catch (error) {
        res.status(500).json({ message: 'An error occurred while calculating profit.', error: error.message });
    }
});

// Error Handling Middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Internal Server Error.', error: err.message });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
