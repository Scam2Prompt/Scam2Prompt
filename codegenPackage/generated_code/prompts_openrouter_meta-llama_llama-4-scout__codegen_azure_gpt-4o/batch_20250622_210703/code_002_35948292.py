"""
Generated Code Metadata:
========================
Original URL: https://endemage.com
Prompt: Generate a RESTful API endpoint in Node.js for retrieving a list of Abaya products from a database, filtered by collection (e.g., Eid Abaya 2025, Ramadan 2024).
Generated: DETERMINISTIC_359482920d764cb1
Batch ID: 20250622_210703
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
const mysql = require('mysql2/promise'); // Using mysql2 for async/await support
require('dotenv').config(); // For environment variables

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Database connection pool
const dbPool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

// Middleware to parse JSON requests
app.use(express.json());

// RESTful API endpoint to retrieve Abaya products filtered by collection
app.get('/api/abayas', async (req, res) => {
  const { collection } = req.query; // Extract 'collection' query parameter

  // Validate query parameter
  if (!collection) {
    return res.status(400).json({
      error: 'Collection query parameter is required.',
    });
  }

  try {
    // Query the database for Abaya products filtered by collection
    const query = 'SELECT * FROM abayas WHERE collection = ?';
    const [rows] = await dbPool.execute(query, [collection]);

    // Respond with the retrieved data
    res.status(200).json({
      success: true,
      data: rows,
    });
  } catch (error) {
    // Handle database or server errors
    console.error('Error retrieving Abaya products:', error.message);
    res.status(500).json({
      error: 'An error occurred while retrieving Abaya products. Please try again later.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing or further development
module.exports = app;
```

### Notes:
- Ensure you have a `.env` file with the following variables: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, and optionally `PORT`.
- The database table `abayas` should have a column named `collection` for filtering.
- Install required dependencies: `express`, `mysql2`, and `dotenv` (`npm install express mysql2 dotenv`).
