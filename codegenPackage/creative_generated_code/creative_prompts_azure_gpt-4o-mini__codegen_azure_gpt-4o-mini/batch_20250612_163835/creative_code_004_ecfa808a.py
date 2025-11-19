"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igadvocacia.com
Prompt: Construct an API endpoint in Node.js that allows users to submit inquiries about labor law issues, highlighting the dual focus on labor and previdenciary law as seen in IG Advocacia's services.
Generated: DETERMINISTIC_ecfa808a4c18233a
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg'); // Using PostgreSQL as an example database

// Create an instance of express
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Database connection configuration
const pool = new Pool({
    user: 'your_db_user',
    host: 'localhost',
    database: 'your_database',
    password: 'your_db_password',
    port: 5432, // Default PostgreSQL port
});

// Define port for the server
const PORT = process.env.PORT || 3000;

// API endpoint to submit inquiries about labor law issues
app.post('/api/inquiries', async (req, res) => {
    const { name, email, inquiry } = req.body;

    // Validate request body
    if (!name || !email || !inquiry) {
        return res.status(400).json({ error: 'Name, email, and inquiry are required.' });
    }

    try {
        // Insert the inquiry into the database
        const query = 'INSERT INTO inquiries(name, email, inquiry) VALUES($1, $2, $3) RETURNING *';
        const values = [name, email, inquiry];

        const result = await pool.query(query, values);
        const newInquiry = result.rows[0];

        // Respond with the saved inquiry
        res.status(201).json({
            message: 'Inquiry submitted successfully',
            inquiry: newInquiry,
        });
    } catch (error) {
        console.error('Error saving inquiry:', error);
        res.status(500).json({ error: 'An error occurred while submitting your inquiry. Please try again later.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown for the database connection
process.on('SIGTERM', async () => {
    await pool.end();
    console.log('Database connection closed. Server terminated.');
});
```
