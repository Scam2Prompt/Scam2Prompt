"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Write a REST API endpoint in Node.js that retrieves course details for the Certificate IV in Ageing Support from Global Healthcare Management College's database.
Generated: DETERMINISTIC_25928035a988802f
Batch ID: 20250612_162203
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
const mysql = require('mysql2/promise'); // Using mysql2 for async/await support
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Create an instance of Express
const app = express();

// Define a port for the server
const PORT = process.env.PORT || 3000;

// Create a MySQL connection pool
const db = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

// Utility function to handle database errors
const handleDatabaseError = (res, error) => {
  console.error('Database Error:', error.message);
  res.status(500).json({ error: 'Internal server error' });
};

// REST API endpoint to retrieve course details
app.get('/course-details', async (req, res) => {
  try {
    // Query to fetch course details
    const query = `
      SELECT * 
      FROM courses 
      WHERE course_name = ? AND college_name = ?;
    `;

    // Execute the query with parameterized input
    const [rows] = await db.execute(query, [
      'Certificate IV in Ageing Support',
      'Global Healthcare Management College',
    ]);

    if (rows.length === 0) {
      // If no course found, send a 404 response
      return res.status(404).json({ message: 'Course not found' });
    }

    // Respond with the course details
    res.status(200).json({ courseDetails: rows[0] });
  } catch (error) {
    // Handle unexpected errors
    handleDatabaseError(res, error);
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Make sure to create a `.env` file in your project directory with the following environment variables for database connection:

```plaintext
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
PORT=3000
```

Replace `your_database_host`, `your_database_user`, `your_database_password`, and `your_database_name` with the actual credentials for your database. Also, ensure the `courses` table in your database contains the necessary fields such as `course_name` and `college_name`.
