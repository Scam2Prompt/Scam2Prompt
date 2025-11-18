"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Develop a Node.js application that integrates Immediate GPT's registration process with a backend database to store user information securely.
Generated: DETERMINISTIC_7aa1eb209e5b132d
Batch ID: 20250612_150854
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
const mysql = require('mysql2/promise');
const bcrypt = require('bcrypt');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Create a connection pool for MySQL database
const db = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

// Helper function to validate input data
function validateUserData(userData) {
  const { username, email, password } = userData;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!username || typeof username !== 'string' || username.length < 3) {
    return 'Invalid username (must be at least 3 characters).';
  }
  if (!email || !emailRegex.test(email)) {
    return 'Invalid email address.';
  }
  if (!password || password.length < 8) {
    return 'Invalid password (must be at least 8 characters).';
  }
  return null; // No validation errors
}

// Route to handle user registration
app.post('/register', async (req, res) => {
  const { username, email, password } = req.body;

  // Validate user input
  const validationError = validateUserData({ username, email, password });
  if (validationError) {
    return res.status(400).json({ error: validationError });
  }

  try {
    // Check if email already exists
    const [existingUser] = await db.query('SELECT id FROM users WHERE email = ?', [email]);
    if (existingUser.length > 0) {
      return res.status(400).json({ error: 'Email is already registered.' });
    }

    // Hash the password securely
    const hashedPassword = await bcrypt.hash(password, 10);

    // Store user information in the database
    await db.query(
      'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
      [username, email, hashedPassword]
    );

    // Respond with success message
    res.status(201).json({ message: 'User registered successfully.' });
  } catch (error) {
    console.error('Error during registration:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Route to confirm API is running
app.get('/', (req, res) => {
  res.send('Immediate GPT Registration API is running.');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

**Note:** Ensure you have the following prerequisites:
1. Install Node.js, MySQL, and relevant npm packages (`express`, `body-parser`, `bcrypt`, `dotenv`, `mysql2`).
2. Create a `.env` file with the following variables:
   ```
   DB_HOST=your_database_host
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_NAME=your_database_name
   PORT=optional_port_number
   ```
3. Create a `users` table in your database:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```
