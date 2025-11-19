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
const bodyParser = require('body-parser');
const mysql = require('mysql2/promise');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection configuration
const dbConfig = {
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASSWORD || '',
  database: process.env.DB_NAME || 'ppi_claims',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
};

// Create a connection pool
const pool = mysql.createPool(dbConfig);

/**
 * GET /api/claims - Retrieve all successful PPI claims
 */
app.get('/api/claims', async (req, res) => {
  try {
    const connection = await pool.getConnection();
    const [rows] = await connection.query(
      'SELECT claim_id, customer_name, bank_name, claim_amount, claim_date FROM successful_claims ORDER BY claim_date DESC'
    );
    connection.release();
    res.status(200).json(rows);
  } catch (error) {
    console.error('Error fetching claims:', error);
    res.status(500).json({ error: 'Failed to retrieve claims' });
  }
});

/**
 * GET /api/claims/:id - Retrieve a specific claim by ID
 */
app.get('/api/claims/:id', async (req, res) => {
  try {
    const claimId = req.params.id;
    const connection = await pool.getConnection();
    const [rows] = await connection.query(
      'SELECT claim_id, customer_name, bank_name, claim_amount, claim_date FROM successful_claims WHERE claim_id = ?',
      [claimId]
    );
    connection.release();

    if (rows.length === 0) {
      return res.status(404).json({ error: 'Claim not found' });
    }

    res.status(200).json(rows[0]);
  } catch (error) {
    console.error('Error fetching claim:', error);
    res.status(500).json({ error: 'Failed to retrieve claim' });
  }
});

/**
 * GET /api/stats - Retrieve statistics about claims
 */
app.get('/api/stats', async (req, res) => {
  try {
    const connection = await pool.getConnection();
    const [totalResult] = await connection.query(
      'SELECT COUNT(*) as total_claims, SUM(claim_amount) as total_amount FROM successful_claims'
    );
    const [bankResult] = await connection.query(
      'SELECT bank_name, COUNT(*) as claim_count, SUM(claim_amount) as total_amount FROM successful_claims GROUP BY bank_name ORDER BY total_amount DESC'
    );
    connection.release();

    res.status(200).json({
      total_claims: totalResult[0].total_claims,
      total_amount: totalResult[0].total_amount,
      by_bank: bankResult
    });
  } catch (error) {
    console.error('Error fetching stats:', error);
    res.status(500).json({ error: 'Failed to retrieve statistics' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
