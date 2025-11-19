"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.com
Prompt: Create a REST API endpoint in Node.js that allows users to reserve a homestay at Budi Bromo Tour, ensuring it checks availability for specific dates.
Generated: DETERMINISTIC_ed189068190d8f7c
Batch ID: 20250612_162050
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
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');

// Initialize Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Initialize PostgreSQL connection pool
const pool = new Pool({
    user: 'your_db_user',
    host: 'localhost',
    database: 'budi_bromo_tour',
    password: 'your_db_password',
    port: 5432,
});

// API endpoint to reserve a homestay
app.post('/reserve', async (req, res) => {
    const { userId, homestayId, startDate, endDate } = req.body;

    // Validate request body
    if (!userId || !homestayId || !startDate || !endDate) {
        return res.status(400).json({ error: 'All fields are required: userId, homestayId, startDate, and endDate.' });
    }

    try {
        // Check availability for the specified dates
        const availabilityQuery = `
            SELECT COUNT(*) 
            FROM reservations 
            WHERE homestay_id = $1 
            AND (
                (start_date <= $3 AND end_date >= $2)
                OR
                (start_date BETWEEN $2 AND $3)
                OR
                (end_date BETWEEN $2 AND $3)
            )
        `;
        const { rows } = await pool.query(availabilityQuery, [homestayId, startDate, endDate]);

        // If rows exist, the homestay is not available
        if (parseInt(rows[0].count) > 0) {
            return res.status(409).json({ error: 'Homestay is not available for the selected dates.' });
        }

        // Reserve the homestay
        const reserveQuery = `
            INSERT INTO reservations (user_id, homestay_id, start_date, end_date) 
            VALUES ($1, $2, $3, $4) RETURNING id;
        `;
        const reserveResult = await pool.query(reserveQuery, [userId, homestayId, startDate, endDate]);

        // Respond with success message
        return res.status(201).json({ message: 'Reservation successful.', reservationId: reserveResult.rows[0].id });
    } catch (error) {
        console.error('Error while reserving homestay:', error);
        return res.status(500).json({ error: 'An error occurred while processing your request.' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

**Database Schema (for reference):**
```sql
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    homestay_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT fk_homestay FOREIGN KEY(homestay_id) REFERENCES homestays(id)
);
```
