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
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/investment_plans', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    investmentPlans: [{ type: mongoose.Schema.Types.ObjectId, ref: 'InvestmentPlan' }],
});

const User = mongoose.model('User', userSchema);

// Define InvestmentPlan schema and model
const investmentPlanSchema = new mongoose.Schema({
    name: { type: String, required: true },
    initialAmount: { type: Number, required: true },
    annualReturnRate: { type: Number, required: true }, // in percentage
});

const InvestmentPlan = mongoose.model('InvestmentPlan', investmentPlanSchema);

// Routes

// Create a new user account
app.post('/users', async (req, res) => {
    try {
        const newUser = new User(req.body);
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get user accounts
app.get('/users', async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Create a new investment plan
app.post('/investment-plans', async (req, res) => {
    try {
        const newPlan = new InvestmentPlan(req.body);
        await newPlan.save();
        res.status(201).json(newPlan);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get all investment plans
app.get('/investment-plans', async (req, res) => {
    try {
        const plans = await InvestmentPlan.find();
        res.status(200).json(plans);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Calculate profit for a given investment plan
app.post('/calculate-profit', async (req, res) => {
    const { initialAmount, annualReturnRate, years } = req.body;
    
    if (!initialAmount || !annualReturnRate || !years) {
        return res.status(400).json({ error: 'Please provide initialAmount, annualReturnRate, and years.' });
    }
    
    try {
        const profit = initialAmount * Math.pow(1 + (annualReturnRate / 100), years) - initialAmount;
        res.status(200).json({ profit });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
