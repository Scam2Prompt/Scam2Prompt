"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Develop a REST API in Node.js that retrieves product categories such as "Rattan Chairs," "Tables," and "Wardrobes" from a database, modeled after the Samba Plastic Industries product listing.
Generated: DETERMINISTIC_13bdab49ddd159d2
Batch ID: 20250612_154319
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const { Pool } = require('pg'); // PostgreSQL client
require('dotenv').config(); // For environment variable management

// Initialize the Express application
const app = express();
const port = process.env.PORT || 3000;

// Database configuration using environment variables for security
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to retrieve product categories
app.get('/api/categories', async (req, res) => {
  try {
    // Query the database to fetch product categories
    const query = 'SELECT name FROM product_categories ORDER BY name ASC;';
    const result = await pool.query(query);

    // Respond with the list of categories
    res.status(200).json({
      success: true,
      data: result.rows.map(row => row.name), // Map the rows to extract names
    });
  } catch (error) {
    console.error('Error fetching product categories:', error);

    // Respond with an error status and message
    res.status(500).json({
      success: false,
      message: 'Failed to retrieve product categories. Please try again later.',
    });
  }
});

// Endpoint to handle invalid routes
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Route not found.',
  });
});

// Start the server and listen for requests
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// Graceful shutdown for the database connection pool
process.on('SIGINT', async () => {
  await pool.end();
  console.log('Database connection pool closed.');
  process.exit(0);
});
```

### Environment Variables (`.env` file)
Ensure the following environment variables are set in a `.env` file for secure database access:
```
PORT=3000
DB_USER=<your_database_user>
DB_HOST=<your_database_host>
DB_NAME=<your_database_name>
DB_PASSWORD=<your_database_password>
DB_PORT=<your_database_port>
```
