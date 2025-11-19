"""
Generated Code Metadata:
========================
Original URL: https://seriesflix2tv.live
Prompt: Construct a RESTful API in Node.js that allows users to query SeriesFlix for series based on specific criteria such as 'Lançamentos' or 'Dubladas'.
Generated: DETERMINISTIC_89fcc1fbcb99ff38
Batch ID: 20250612_155531
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
const cors = require('cors');

// Sample data - in a real app, this would come from a database
const seriesData = [
  { id: 1, title: 'Stranger Things', category: 'Lançamentos', dubbed: false },
  { id: 2, title: 'The Witcher', category: 'Lançamentos', dubbed: true },
  { id: 3, title: 'Breaking Bad', category: 'Clássicos', dubbed: true },
  { id: 4, title: 'Dark', category: 'Internacionais', dubbed: false },
  { id: 5, title: 'Money Heist', category: 'Internacionais', dubbed: true }
];

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

/**
 * GET /series - Get all series or filter by criteria
 * Query params:
 * - category: filter by category (e.g., 'Lançamentos')
 * - dubbed: filter by dubbed status (true/false)
 */
app.get('/series', (req, res) => {
  try {
    let results = [...seriesData];
    
    // Filter by category if provided
    if (req.query.category) {
      results = results.filter(series => 
        series.category.toLowerCase() === req.query.category.toLowerCase()
      );
    }
    
    // Filter by dubbed status if provided
    if (req.query.dubbed) {
      const dubbedFilter = req.query.dubbed.toLowerCase() === 'true';
      results = results.filter(series => series.dubbed === dubbedFilter);
    }
    
    res.json(results);
  } catch (error) {
    console.error('Error fetching series:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /series/:id - Get a specific series by ID
 */
app.get('/series/:id', (req, res) => {
  try {
    const series = seriesData.find(s => s.id === parseInt(req.params.id));
    
    if (!series) {
      return res.status(404).json({ error: 'Series not found' });
    }
    
    res.json(series);
  } catch (error) {
    console.error('Error fetching series:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
