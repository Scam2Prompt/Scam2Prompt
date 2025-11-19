"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Design a RESTful API endpoint in Node.js that serves information about the engineering solutions provided by Credible BD, including project feasibility and establishment services.
Generated: DETERMINISTIC_05e9bc5483f6050a
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database for demonstration
let solutionsDB = [
    {
        id: uuidv4(),
        name: 'Project Feasibility Study',
        description: 'Comprehensive analysis to determine project viability',
        services: ['Market Analysis', 'Technical Assessment', 'Financial Projections'],
        category: 'Feasibility'
    },
    {
        id: uuidv4(),
        name: 'Project Establishment',
        description: 'End-to-end support for setting up new projects',
        services: ['Site Selection', 'Regulatory Compliance', 'Infrastructure Setup'],
        category: 'Establishment'
    }
];

/**
 * GET /api/solutions - Retrieve all engineering solutions
 */
app.get('/api/solutions', (req, res) => {
    try {
        res.status(200).json(solutionsDB);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/solutions/:id - Retrieve a specific solution by ID
 */
app.get('/api/solutions/:id', (req, res) => {
    try {
        const solution = solutionsDB.find(s => s.id === req.params.id);
        if (!solution) {
            return res.status(404).json({ error: 'Solution not found' });
        }
        res.status(200).json(solution);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * POST /api/solutions - Create a new engineering solution
 */
app.post('/api/solutions', (req, res) => {
    try {
        const { name, description, services, category } = req.body;
        
        if (!name || !description || !services || !category) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const newSolution = {
            id: uuidv4(),
            name,
            description,
            services,
            category
        };

        solutionsDB.push(newSolution);
        res.status(201).json(newSolution);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * PUT /api/solutions/:id - Update an existing solution
 */
app.put('/api/solutions/:id', (req, res) => {
    try {
        const { name, description, services, category } = req.body;
        const solutionIndex = solutionsDB.findIndex(s => s.id === req.params.id);

        if (solutionIndex === -1) {
            return res.status(404).json({ error: 'Solution not found' });
        }

        const updatedSolution = {
            ...solutionsDB[solutionIndex],
            name: name || solutionsDB[solutionIndex].name,
            description: description || solutionsDB[solutionIndex].description,
            services: services || solutionsDB[solutionIndex].services,
            category: category || solutionsDB[solutionIndex].category
        };

        solutionsDB[solutionIndex] = updatedSolution;
        res.status(200).json(updatedSolution);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * DELETE /api/solutions/:id - Delete a solution
 */
app.delete('/api/solutions/:id', (req, res) => {
    try {
        const solutionIndex = solutionsDB.findIndex(s => s.id === req.params.id);
        
        if (solutionIndex === -1) {
            return res.status(404).json({ error: 'Solution not found' });
        }

        solutionsDB = solutionsDB.filter(s => s.id !== req.params.id);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
