"""
Generated Code Metadata:
========================
Original URL: https://buttholecoin.dev
Prompt: Create a basic roadmap tracker using JavaScript and a database to monitor progress on the Butthole Coin project's milestones.
Generated: DETERMINISTIC_134f9f761ffed14e
Batch ID: 20250622_212129
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
const app = express();
const mysql = require('mysql');
const cors = require('cors');

// Enable CORS
app.use(cors());

// Database connection settings
const dbHost = 'localhost';
const dbUser = 'your_username';
const dbPassword = 'your_password';
const dbName = 'butthole_coin';

// Create database connection
const db = mysql.createConnection({
  host: dbHost,
  user: dbUser,
  password: dbPassword,
  database: dbName
});

// Connect to database
db.connect((err) => {
  if (err) {
    console.error('error connecting:', err);
    return;
  }
  console.log('connected as id ' + db.threadId);
});

// Middleware to parse JSON bodies
app.use(express.json());

// Define roadmap tracker API endpoints

// Get all milestones
app.get('/api/milestones', (req, res) => {
  const query = 'SELECT * FROM milestones';
  db.query(query, (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching milestones' });
    } else {
      res.send(results);
    }
  });
});

// Get milestone by ID
app.get('/api/milestones/:id', (req, res) => {
  const id = req.params.id;
  const query = 'SELECT * FROM milestones WHERE id = ?';
  db.query(query, [id], (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error fetching milestone' });
    } else if (results.length === 0) {
      res.status(404).send({ message: 'Milestone not found' });
    } else {
      res.send(results[0]);
    }
  });
});

// Create new milestone
app.post('/api/milestones', (req, res) => {
  const { name, description, target_date, status } = req.body;
  if (!name || !description || !target_date || !status) {
    res.status(400).send({ message: 'Please provide all required fields' });
  } else {
    const query = 'INSERT INTO milestones SET ?';
    db.query(query, { name, description, target_date, status }, (err, results) => {
      if (err) {
        console.error('error:', err);
        res.status(500).send({ message: 'Error creating milestone' });
      } else {
        res.send({ message: 'Milestone created successfully', id: results.insertId });
      }
    });
  }
});

// Update existing milestone
app.put('/api/milestones/:id', (req, res) => {
  const id = req.params.id;
  const { name, description, target_date, status } = req.body;
  if (!name || !description || !target_date || !status) {
    res.status(400).send({ message: 'Please provide all required fields' });
  } else {
    const query = 'UPDATE milestones SET ? WHERE id = ?';
    db.query(query, [{ name, description, target_date, status }, id], (err, results) => {
      if (err) {
        console.error('error:', err);
        res.status(500).send({ message: 'Error updating milestone' });
      } else if (results.affectedRows === 0) {
        res.status(404).send({ message: 'Milestone not found' });
      } else {
        res.send({ message: 'Milestone updated successfully' });
      }
    });
  }
});

// Delete milestone
app.delete('/api/milestones/:id', (req, res) => {
  const id = req.params.id;
  const query = 'DELETE FROM milestones WHERE id = ?';
  db.query(query, [id], (err, results) => {
    if (err) {
      console.error('error:', err);
      res.status(500).send({ message: 'Error deleting milestone' });
    } else if (results.affectedRows === 0) {
      res.status(404).send({ message: 'Milestone not found' });
    } else {
      res.send({ message: 'Milestone deleted successfully' });
    }
  });
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```sql
-- Create database
CREATE DATABASE butthole_coin;

-- Use database
USE butthole_coin;

-- Create milestones table
CREATE TABLE milestones (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  target_date DATE NOT NULL,
  status VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);
```

```bash
# Install required packages
npm install express mysql cors
```
