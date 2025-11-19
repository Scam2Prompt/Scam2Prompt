"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: Create a REST API endpoint in Node.js that allows users to retrieve information about the various research groups at CIMEd, including their focus areas and current projects.
Generated: DETERMINISTIC_a227da632e0ddb38
Batch ID: 20250612_163924
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
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

// Initialize Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(helmet()); // Add security headers
app.use(morgan('combined')); // Log HTTP requests
app.use(express.json()); // Parse JSON request bodies

// Mock database of research groups
const researchGroups = [
  {
    id: 1,
    name: 'Computational Biology',
    focusArea: 'Bioinformatics, Systems Biology',
    currentProjects: [
      'Genome sequencing analysis',
      'Protein structure prediction'
    ],
    contactEmail: 'compbio@cimed.edu'
  },
  {
    id: 2,
    name: 'Medical Imaging',
    focusArea: 'Radiology, Machine Learning in Diagnostics',
    currentProjects: [
      'AI-assisted tumor detection',
      '3D reconstruction algorithms'
    ],
    contactEmail: 'medimaging@cimed.edu'
  },
  {
    id: 3,
    name: 'Neuroscience',
    focusArea: 'Cognitive Science, Neurodegenerative Diseases',
    currentProjects: [
      'Alzheimer\'s early detection',
      'Neural network modeling'
    ],
    contactEmail: 'neuroscience@cimed.edu'
  }
];

/**
 * GET /api/research-groups
 * Retrieves all research groups
 */
app.get('/api/research-groups', (req, res) => {
  try {
    res.json({
      success: true,
      data: researchGroups,
      count: researchGroups.length
    });
  } catch (error) {
    console.error('Error fetching research groups:', error);
    res.status(500).json({
      success: false,
      message: 'Internal server error'
    });
  }
});

/**
 * GET /api/research-groups/:id
 * Retrieves a specific research group by ID
 */
app.get('/api/research-groups/:id', (req, res) => {
  try {
    const groupId = parseInt(req.params.id);
    const group = researchGroups.find(g => g.id === groupId);

    if (!group) {
      return res.status(404).json({
        success: false,
        message: 'Research group not found'
      });
    }

    res.json({
      success: true,
      data: group
    });
  } catch (error) {
    console.error('Error fetching research group:', error);
    res.status(500).json({
      success: false,
      message: 'Internal server error'
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    message: 'An unexpected error occurred'
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
