"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Create a RESTful API in Node.js to manage law firm services, including endpoints for retrieving information about different areas of law, such as civil, matrimonial, and labor law.
Generated: DETERMINISTIC_c200432a7c6f0ab3
Batch ID: 20250622_210650
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

// Middleware to parse JSON bodies
app.use(express.json());

// Define areas of law data
const areasOfLaw = {
  civil: {
    description: 'Civil law deals with disputes between individuals, organizations, or businesses.',
    services: ['Contract disputes', 'Personal injury claims', 'Property disputes']
  },
  matrimonial: {
    description: 'Matrimonial law deals with family and marital issues.',
    services: ['Divorce', 'Child custody', 'Spousal support']
  },
  labor: {
    description: 'Labor law deals with employment and workplace issues.',
    services: ['Wrongful termination', 'Workplace harassment', 'Employment contracts']
  }
};

// GET endpoint to retrieve all areas of law
app.get('/api/law-areas', (req, res) => {
  try {
    const lawAreas = Object.keys(areasOfLaw);
    res.json(lawAreas);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// GET endpoint to retrieve information about a specific area of law
app.get('/api/law-areas/:area', (req, res) => {
  try {
    const area = req.params.area;
    if (!areasOfLaw[area]) {
      res.status(404).json({ message: `Area of law not found: ${area}` });
    } else {
      res.json(areasOfLaw[area]);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// GET endpoint to retrieve services for a specific area of law
app.get('/api/law-areas/:area/services', (req, res) => {
  try {
    const area = req.params.area;
    if (!areasOfLaw[area]) {
      res.status(404).json({ message: `Area of law not found: ${area}` });
    } else {
      res.json(areasOfLaw[area].services);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Error handler for 404 Not Found
app.use((req, res) => {
  res.status(404).json({ message: 'Endpoint not found' });
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
