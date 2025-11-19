"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Create a Node.js application to calculate construction costs and provide estimates for clients, taking into account factors like materials, labor, and location, as seen in Clickmart Ltd's construction services."
Generated: DETERMINISTIC_d150d7aaabdc6976
Batch ID: 20250622_205411
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
const bodyParser = require('body-parser');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database simulation (in production, use a real database)
const projectsDB = new Map();

// Material cost per square foot (in USD)
const MATERIAL_COSTS = {
    'standard': 50,
    'premium': 100,
    'luxury': 200
};

// Labor cost per hour (in USD)
const LABOR_COSTS = {
    'urban': 75,
    'suburban': 60,
    'rural': 50
};

// Location multipliers
const LOCATION_MULTIPLIERS = {
    'high_cost': 1.5,
    'medium_cost': 1.2,
    'low_cost': 1.0
};

/**
 * Calculate construction cost estimate
 * @param {number} area - Area in square feet
 * @param {string} materialType - One of 'standard', 'premium', 'luxury'
 * @param {string} locationType - One of 'urban', 'suburban', 'rural'
 * @param {string} costArea - One of 'high_cost', 'medium_cost', 'low_cost'
 * @param {number} estimatedHours - Estimated labor hours
 * @returns {Object} - Contains materialCost, laborCost, totalCost
 */
function calculateEstimate(area, materialType, locationType, costArea, estimatedHours) {
    if (!area || area <= 0) throw new Error('Area must be a positive number');
    if (!MATERIAL_COSTS[materialType]) throw new Error('Invalid material type');
    if (!LABOR_COSTS[locationType]) throw new Error('Invalid location type');
    if (!LOCATION_MULTIPLIERS[costArea]) throw new Error('Invalid cost area');

    const materialCost = area * MATERIAL_COSTS[materialType];
    const laborCost = estimatedHours * LABOR_COSTS[locationType] * LOCATION_MULTIPLIERS[costArea];
    const totalCost = materialCost + laborCost;

    return {
        materialCost: parseFloat(materialCost.toFixed(2)),
        laborCost: parseFloat(laborCost.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2))
    };
}

// Routes
app.post('/api/estimates', (req, res) => {
    try {
        const { area, materialType, locationType, costArea, estimatedHours, clientName } = req.body;
        
        if (!clientName) {
            return res.status(400).json({ error: 'Client name is required' });
        }

        const estimate = calculateEstimate(area, materialType, locationType, costArea, estimatedHours);
        const projectId = uuidv4();
        
        const project = {
            id: projectId,
            clientName,
            ...estimate,
            area,
            materialType,
            locationType,
            costArea,
            estimatedHours,
            createdAt: new Date().toISOString()
        };

        projectsDB.set(projectId, project);
        
        res.status(201).json(project);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

app.get('/api/estimates/:id', (req, res) => {
    try {
        const projectId = req.params.id;
        const project = projectsDB.get(projectId);
        
        if (!project) {
            return res.status(404).json({ error: 'Project not found' });
        }
        
        res.json(project);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/api/estimates', (req, res) => {
    try {
        const projects = Array.from(projectsDB.values());
        res.json(projects);
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

// Export for testing
module.exports = {
    app,
    calculateEstimate,
    projectsDB
};
```
