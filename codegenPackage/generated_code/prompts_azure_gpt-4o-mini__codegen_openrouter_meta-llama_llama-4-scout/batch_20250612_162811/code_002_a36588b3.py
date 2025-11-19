"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Create an API endpoint in Node.js that provides information on private equity investment opportunities, reflecting the expertise and services offered by Alghanim Capital in the private equity domain.
Generated: DETERMINISTIC_a36588b3bed35de6
Batch ID: 20250612_162811
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
const app = express();
const port = 3000;

// Middleware to handle JSON data
app.use(express.json());

// Define a class for Private Equity Investment Opportunity
class PrivateEquityOpportunity {
    /**
     * Constructor for PrivateEquityOpportunity
     * @param {string} id - Unique identifier for the opportunity
     * @param {string} name - Name of the opportunity
     * @param {string} description - Brief description of the opportunity
     * @param {number} investmentAmount - Investment amount required
     * @param {string} industry - Industry of the opportunity
     */
    constructor(id, name, description, investmentAmount, industry) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.investmentAmount = investmentAmount;
        this.industry = industry;
    }
}

// In-memory storage for private equity investment opportunities
let opportunities = [
    new PrivateEquityOpportunity("1", "Opportunity 1", "Description 1", 1000000, "Technology"),
    new PrivateEquityOpportunity("2", "Opportunity 2", "Description 2", 500000, "Healthcare"),
];

// API endpoint to get all private equity investment opportunities
app.get('/api/private-equity/opportunities', (req, res) => {
    try {
        res.json(opportunities);
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to get a private equity investment opportunity by ID
app.get('/api/private-equity/opportunities/:id', (req, res) => {
    try {
        const id = req.params.id;
        const opportunity = opportunities.find((opportunity) => opportunity.id === id);
        if (!opportunity) {
            res.status(404).json({ message: 'Opportunity not found' });
        } else {
            res.json(opportunity);
        }
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to create a new private equity investment opportunity
app.post('/api/private-equity/opportunities', (req, res) => {
    try {
        const { id, name, description, investmentAmount, industry } = req.body;
        if (!id || !name || !description || !investmentAmount || !industry) {
            res.status(400).json({ message: 'All fields are required' });
        } else {
            const newOpportunity = new PrivateEquityOpportunity(id, name, description, investmentAmount, industry);
            opportunities.push(newOpportunity);
            res.json(newOpportunity);
        }
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to update an existing private equity investment opportunity
app.put('/api/private-equity/opportunities/:id', (req, res) => {
    try {
        const id = req.params.id;
        const { name, description, investmentAmount, industry } = req.body;
        const opportunity = opportunities.find((opportunity) => opportunity.id === id);
        if (!opportunity) {
            res.status(404).json({ message: 'Opportunity not found' });
        } else {
            opportunity.name = name;
            opportunity.description = description;
            opportunity.investmentAmount = investmentAmount;
            opportunity.industry = industry;
            res.json(opportunity);
        }
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to delete a private equity investment opportunity
app.delete('/api/private-equity/opportunities/:id', (req, res) => {
    try {
        const id = req.params.id;
        const index = opportunities.findIndex((opportunity) => opportunity.id === id);
        if (index === -1) {
            res.status(404).json({ message: 'Opportunity not found' });
        } else {
            opportunities.splice(index, 1);
            res.json({ message: 'Opportunity deleted successfully' });
        }
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
