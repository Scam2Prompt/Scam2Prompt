"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Develop a backend service in Node.js to manage and serve MFO data, including features like sorting offers by interest rates and filtering by client region, as described on nocreditcheck.online.
Generated: DETERMINISTIC_baac814e3b6bb3cd
Batch ID: 20250612_145727
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

// Sample in-memory data store (replace with a database in production)
let mfoData = [
  { id: 1, name: 'MFO 1', interestRate: 20, region: 'North' },
  { id: 2, name: 'MFO 2', interestRate: 15, region: 'South' },
  { id: 3, name: 'MFO 3', interestRate: 25, region: 'East' },
  { id: 4, name: 'MFO 4', interestRate: 10, region: 'West' },
  { id: 5, name: 'MFO 5', interestRate: 18, region: 'North' },
];

// API endpoint to retrieve all MFO data
app.get('/mfo', (req, res) => {
  try {
    res.json(mfoData);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to retrieve MFO data sorted by interest rate
app.get('/mfo/sort/interest-rate', (req, res) => {
  try {
    const sortedData = mfoData.sort((a, b) => a.interestRate - b.interestRate);
    res.json(sortedData);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to filter MFO data by client region
app.get('/mfo/filter/region/:region', (req, res) => {
  try {
    const region = req.params.region;
    const filteredData = mfoData.filter((mfo) => mfo.region.toLowerCase() === region.toLowerCase());
    if (filteredData.length === 0) {
      res.status(404).json({ message: `No MFO data found for region ${region}` });
    } else {
      res.json(filteredData);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to add new MFO data
app.post('/mfo', (req, res) => {
  try {
    const { name, interestRate, region } = req.body;
    if (!name || !interestRate || !region) {
      res.status(400).json({ message: 'Name, interest rate, and region are required' });
    } else {
      const newMfo = { id: mfoData.length + 1, name, interestRate, region };
      mfoData.push(newMfo);
      res.json(newMfo);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update existing MFO data
app.put('/mfo/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const { name, interestRate, region } = req.body;
    const mfoIndex = mfoData.findIndex((mfo) => mfo.id === id);
    if (mfoIndex === -1) {
      res.status(404).json({ message: `MFO with ID ${id} not found` });
    } else {
      if (name) mfoData[mfoIndex].name = name;
      if (interestRate) mfoData[mfoIndex].interestRate = interestRate;
      if (region) mfoData[mfoIndex].region = region;
      res.json(mfoData[mfoIndex]);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete MFO data
app.delete('/mfo/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const mfoIndex = mfoData.findIndex((mfo) => mfo.id === id);
    if (mfoIndex === -1) {
      res.status(404).json({ message: `MFO with ID ${id} not found` });
    } else {
      mfoData.splice(mfoIndex, 1);
      res.status(204).send();
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
