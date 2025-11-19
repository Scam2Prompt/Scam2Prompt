"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Create a RESTful API endpoint in Node.js that retrieves certification information for a logistics provider specializing in frozen and refrigerated goods, similar to OPC's services.
Generated: DETERMINISTIC_f86a2a6bb38e0abf
Batch ID: 20250612_161700
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

// Middleware to handle JSON payloads
app.use(express.json());

// Define a sample in-memory data store for certifications
// In a real application, this would be a database
const certifications = [
  { id: 1, provider: 'OPC', certification: 'ISO 9001', description: 'Quality management system' },
  { id: 2, provider: 'Frozen Goods Inc.', certification: 'HACCP', description: 'Hazard analysis and critical control points' },
  { id: 3, provider: 'Refrigerated Logistics', certification: 'GDP', description: 'Good distribution practice' },
];

// API endpoint to retrieve all certifications
/**
 * @route GET /certifications
 * @returns {Object[]} An array of certification objects
 */
app.get('/certifications', (req, res) => {
  try {
    res.json(certifications);
  } catch (error) {
    res.status(500).json({ message: 'Failed to retrieve certifications' });
  }
});

// API endpoint to retrieve a certification by ID
/**
 * @route GET /certifications/:id
 * @param {number} :id The ID of the certification to retrieve
 * @returns {Object} A certification object
 */
app.get('/certifications/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const certification = certifications.find((c) => c.id === id);
    if (!certification) {
      res.status(404).json({ message: 'Certification not found' });
    } else {
      res.json(certification);
    }
  } catch (error) {
    res.status(500).json({ message: 'Failed to retrieve certification' });
  }
});

// API endpoint to create a new certification
/**
 * @route POST /certifications
 * @param {Object} req.body The certification object to create
 * @returns {Object} The created certification object
 */
app.post('/certifications', (req, res) => {
  try {
    const { provider, certification, description } = req.body;
    if (!provider || !certification || !description) {
      res.status(400).json({ message: 'Provider, certification, and description are required' });
    } else {
      const newCertification = {
        id: certifications.length + 1,
        provider,
        certification,
        description,
      };
      certifications.push(newCertification);
      res.json(newCertification);
    }
  } catch (error) {
    res.status(500).json({ message: 'Failed to create certification' });
  }
});

// API endpoint to update an existing certification
/**
 * @route PUT /certifications/:id
 * @param {number} :id The ID of the certification to update
 * @param {Object} req.body The updated certification object
 * @returns {Object} The updated certification object
 */
app.put('/certifications/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const certificationIndex = certifications.findIndex((c) => c.id === id);
    if (certificationIndex === -1) {
      res.status(404).json({ message: 'Certification not found' });
    } else {
      const { provider, certification, description } = req.body;
      certifications[certificationIndex] = {
        id,
        provider: provider || certifications[certificationIndex].provider,
        certification: certification || certifications[certificationIndex].certification,
        description: description || certifications[certificationIndex].description,
      };
      res.json(certifications[certificationIndex]);
    }
  } catch (error) {
    res.status(500).json({ message: 'Failed to update certification' });
  }
});

// API endpoint to delete a certification
/**
 * @route DELETE /certifications/:id
 * @param {number} :id The ID of the certification to delete
 * @returns {Object} A success message
 */
app.delete('/certifications/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const certificationIndex = certifications.findIndex((c) => c.id === id);
    if (certificationIndex === -1) {
      res.status(404).json({ message: 'Certification not found' });
    } else {
      certifications.splice(certificationIndex, 1);
      res.json({ message: 'Certification deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Failed to delete certification' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
