"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-209--nervous-kare-6f3c45.netlify.app
Prompt: Write a JavaScript code snippet to create a simple web application for tracking refuse and recycling collection schedules.
Generated: DETERMINISTIC_d2c091b064d631f2
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// refuse-tracker.js

/**
 * Refuse Tracker Application
 * 
 * This application allows users to track refuse and recycling collection schedules.
 */

// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Data storage for collection schedules
let collectionSchedules = [
  { id: 1, address: '123 Main St', refuse: 'Monday', recycling: 'Thursday' },
  { id: 2, address: '456 Elm St', refuse: 'Tuesday', recycling: 'Friday' },
];

// Middleware to parse JSON requests
app.use(express.json());

// Get all collection schedules
app.get('/schedules', (req, res) => {
  try {
    res.json(collectionSchedules);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching collection schedules' });
  }
});

// Get collection schedule by ID
app.get('/schedules/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const schedule = collectionSchedules.find((schedule) => schedule.id === id);
    if (!schedule) {
      res.status(404).json({ message: 'Collection schedule not found' });
    } else {
      res.json(schedule);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching collection schedule' });
  }
});

// Create new collection schedule
app.post('/schedules', (req, res) => {
  try {
    const { address, refuse, recycling } = req.body;
    if (!address || !refuse || !recycling) {
      res.status(400).json({ message: 'Address, refuse, and recycling dates are required' });
    } else {
      const newSchedule = {
        id: collectionSchedules.length + 1,
        address,
        refuse,
        recycling,
      };
      collectionSchedules.push(newSchedule);
      res.json(newSchedule);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error creating collection schedule' });
  }
});

// Update existing collection schedule
app.put('/schedules/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const schedule = collectionSchedules.find((schedule) => schedule.id === id);
    if (!schedule) {
      res.status(404).json({ message: 'Collection schedule not found' });
    } else {
      const { address, refuse, recycling } = req.body;
      if (address) schedule.address = address;
      if (refuse) schedule.refuse = refuse;
      if (recycling) schedule.recycling = recycling;
      res.json(schedule);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error updating collection schedule' });
  }
});

// Delete collection schedule
app.delete('/schedules/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = collectionSchedules.findIndex((schedule) => schedule.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Collection schedule not found' });
    } else {
      collectionSchedules.splice(index, 1);
      res.json({ message: 'Collection schedule deleted successfully' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error deleting collection schedule' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Refuse Tracker Application listening on port ${port}`);
});
```
