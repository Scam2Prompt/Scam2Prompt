"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Develop a basic API using Node.js to retrieve information about successful PPI claims and their corresponding compensation amounts from a database, similar to Financial Recovery Solutions' services.
Generated: DETERMINISTIC_b0009de8f4eb0901
Batch ID: 20250622_205639
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
const mysql = require('mysql2');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Create a MySQL database connection pool
const db = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

// Endpoint to retrieve successful PPI claims and their compensation amounts
app.get('/api/ppi-claims', async (req, res) => {
  try {
    // Query to fetch PPI claims data
    const query = 'SELECT claim_id, claimant_name, compensation_amount FROM ppi_claims WHERE status = "successful"';

    // Execute the query
    db.query(query, (err, results) => {
      if (err) {
        // Handle database query errors
        console.error('Database query error:', err);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Respond with the retrieved data
      res.status(200).json({ claims: results });
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Unexpected error:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
  Notes:
  - Ensure you have a `.env` file with the following variables:
    DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, PORT
  - The database table `ppi_claims` should have columns:
    claim_id (INT), claimant_name (VARCHAR), compensation_amount (DECIMAL), status (VARCHAR)
  - Use a secure method to store and access sensitive credentials.
  - This code is production-ready but should be tested thoroughly before deployment.
*/
```
