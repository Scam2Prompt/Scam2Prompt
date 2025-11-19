"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-datagrid.xyz
Prompt: Develop a RESTful API endpoint in Node.js that retrieves the latest promotions and bonuses for a casino app, similar to what Royal Joker offers.
Generated: DETERMINISTIC_7a31034af287bd42
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express to create the API
const bodyParser = require('body-parser'); // Middleware to parse JSON data
const { Pool } = require('pg'); // PostgreSQL client for database interaction
const dotenv = require('dotenv'); // For environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Database connection pool
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

// Helper function to fetch promotions from the database
async function getLatestPromotions() {
  try {
    // Query the database for promotions ordered by creation date (latest first)
    const result = await pool.query(`
      SELECT id, name, description, bonus_amount, created_at
      FROM promotions
      WHERE active = true
      ORDER BY created_at DESC
    `);
    return result.rows; // Return rows from the database query
  } catch (error) {
    // Log error and rethrow for proper API error handling
    console.error('Error fetching promotions from database:', error);
    throw new Error('DatabaseError');
  }
}

// Define the GET endpoint for retrieving latest promotions
app.get('/api/promotions/latest', async (req, res) => {
  try {
    // Fetch promotions using the helper function
    const promotions = await getLatestPromotions();

    // Respond with the promotions as JSON
    res.status(200).json({
      success: true,
      data: promotions,
    });
  } catch (error) {
    // Handle errors gracefully
    if (error.message === 'DatabaseError') {
      res.status(500).json({
        success: false,
        message: 'An error occurred while retrieving promotions.',
      });
    } else {
      res.status(500).json({
        success: false,
        message: 'Unexpected error.',
      });
    }
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown and cleanup
process.on('SIGTERM', async () => {
  console.log('Shutting down gracefully...');
  await pool.end(); // Close database connection pool
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('Shutting down gracefully...');
  await pool.end(); // Close database connection pool
  process.exit(0);
});
```

**Notes in code comments**:
- Replace `promotions` table and fields with the actual database schema if different.
- Make sure to configure the `.env` file with appropriate database connection details and other environment variables.
- Ensure that database credentials and sensitive information are not hardcoded in the code.
