"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Create a REST API endpoint in Node.js that allows users to query available courses in Derecho and Gestión Pública from ENACIP's database.
Generated: DETERMINISTIC_cab8011868adbc15
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const mysql = require('mysql'); // MySQL database connector
const dotenv = require('dotenv'); // Environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000; // Set the port from environment variables or default to 3000

// Create a MySQL database connection pool
const db = mysql.createPool({
  host: process.env.DB_HOST,       // Database host
  user: process.env.DB_USER,       // Database user
  password: process.env.DB_PASSWORD, // Database password
  database: process.env.DB_NAME    // Database name
});

// Middleware to parse JSON requests
app.use(express.json());

// REST API endpoint to fetch courses in Derecho and Gestión Pública
app.get('/api/courses', (req, res) => {
  const query = `
    SELECT course_name, description
    FROM courses
    WHERE category IN ('Derecho', 'Gestión Pública');
  `;

  // Execute the query
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error querying the database:', err); // Log the error for debugging
      return res.status(500).json({ error: 'Internal Server Error' }); // Respond with 500 if there is a server-side issue
    }

    // Respond with the courses data
    res.status(200).json({ courses: results });
  });
});

// Error handling middleware for unsupported routes
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' }); // Respond with 404 if route is not found
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

/*
  Notes:
  1. Ensure a .env file exists with the following keys:
     - DB_HOST: Hostname of the database
     - DB_USER: Username for database authentication
     - DB_PASSWORD: Password for database authentication
     - DB_NAME: Name of the database containing the courses table
     - PORT (optional): Port on which the server will run
  2. Database schema should include a 'courses' table with columns:
     - course_name (string): Name of the course
     - description (string): Description of the course
     - category (string): Category of the course (e.g., 'Derecho', 'Gestión Pública')
  3. Use a secure method to store and manage your .env file in production.
*/
```
