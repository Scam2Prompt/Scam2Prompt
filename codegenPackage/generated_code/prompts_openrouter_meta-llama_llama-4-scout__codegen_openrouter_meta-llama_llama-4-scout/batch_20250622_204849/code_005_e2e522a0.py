"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Write a code snippet in JavaScript to create a simple web application that allows users to search for pediatric dentists in Pune by location.
Generated: DETERMINISTIC_e2e522a098ccb7ea
Batch ID: 20250622_204849
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

// Sample in-memory data store for pediatric dentists
let dentists = [
  { id: 1, name: 'Dr. Smith', location: 'Pune, Maharashtra' },
  { id: 2, name: 'Dr. Johnson', location: 'Pune, Maharashtra' },
  { id: 3, name: 'Dr. Williams', location: 'Mumbai, Maharashtra' },
  { id: 4, name: 'Dr. Brown', location: 'Pune, Maharashtra' },
];

// API endpoint to search for pediatric dentists by location
app.get('/dentists', (req, res) => {
  try {
    const location = req.query.location;
    if (!location) {
      return res.status(400).json({ error: 'Location is required' });
    }

    const filteredDentists = dentists.filter((dentist) => {
      return dentist.location.toLowerCase().includes(location.toLowerCase());
    });

    if (filteredDentists.length === 0) {
      return res.status(404).json({ error: 'No dentists found' });
    }

    res.json(filteredDentists);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to add a new pediatric dentist
app.post('/dentists', (req, res) => {
  try {
    const { name, location } = req.body;
    if (!name || !location) {
      return res.status(400).json({ error: 'Name and location are required' });
    }

    const newDentist = { id: dentists.length + 1, name, location };
    dentists.push(newDentist);
    res.json(newDentist);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Error handler for unhandled routes
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});
```
