"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Create a REST API endpoint in Node.js for submitting loan applications, referencing TymeBank's loan process as an example.
Generated: DETERMINISTIC_95fd795e393d4ca2
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { check, validationResult } = require('express-validator');

// Initialize the express app
const app = express();

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/loan_applications', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define the Loan Application schema
const loanApplicationSchema = new mongoose.Schema({
    applicantName: {
        type: String,
        required: true,
    },
    amountRequested: {
        type: Number,
        required: true,
        min: 1000, // Minimum loan amount
    },
    applicationDate: {
        type: Date,
        default: Date.now,
    },
    status: {
        type: String,
        enum: ['pending', 'approved', 'rejected'],
        default: 'pending',
    },
});

// Create a model for Loan Application
const LoanApplication = mongoose.model('LoanApplication', loanApplicationSchema);

// Define the POST endpoint for submitting loan applications
app.post('/api/loan-applications', [
    // Validation middleware
    check('applicantName').notEmpty().withMessage('Applicant name is required'),
    check('amountRequested').isNumeric().withMessage('Amount requested must be a number')
        .isInt({ min: 1000 }).withMessage('Minimum amount requested is 1000'),
], async (req, res) => {
    // Handle validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    // Extract loan application data from request body
    const { applicantName, amountRequested } = req.body;

    // Create a new loan application
    const loanApplication = new LoanApplication({
        applicantName,
        amountRequested,
    });

    try {
        // Save the loan application to the database
        const savedApplication = await loanApplication.save();
        return res.status(201).json(savedApplication);
    } catch (error) {
        console.error('Error saving loan application:', error);
        return res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
