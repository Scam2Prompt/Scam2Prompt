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
const mysql = require('mysql');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Create an Express app
const app = express();
app.use(express.json());

// Database connection settings
const dbHost = process.env.DB_HOST;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
const dbName = process.env.DB_NAME;

// Create a database connection
const db = mysql.createConnection({
  host: dbHost,
  user: dbUser,
  password: dbPassword,
  database: dbName
});

// Connect to the database
db.connect((err) => {
  if (err) {
    console.error('Error connecting to database:', err);
    return;
  }
  console.log('Connected to database');
});

// API endpoint to retrieve PPI claims
app.get('/api/ppi-claims', (req, res) => {
  const query = 'SELECT * FROM ppi_claims';

  db.query(query, (err, results) => {
    if (err) {
      console.error('Error retrieving PPI claims:', err);
      res.status(500).send({ message: 'Error retrieving PPI claims' });
      return;
    }

    res.send(results);
  });
});

// API endpoint to retrieve PPI claim by ID
app.get('/api/ppi-claims/:id', (req, res) => {
  const id = req.params.id;
  const query = 'SELECT * FROM ppi_claims WHERE id = ?';

  db.query(query, [id], (err, results) => {
    if (err) {
      console.error('Error retrieving PPI claim:', err);
      res.status(500).send({ message: 'Error retrieving PPI claim' });
      return;
    }

    if (results.length === 0) {
      res.status(404).send({ message: 'PPI claim not found' });
      return;
    }

    res.send(results[0]);
  });
});

// API endpoint to retrieve PPI claim compensation
app.get('/api/ppi-claims/:id/compensation', (req, res) => {
  const id = req.params.id;
  const query = 'SELECT compensation_amount FROM ppi_claims WHERE id = ?';

  db.query(query, [id], (err, results) => {
    if (err) {
      console.error('Error retrieving PPI claim compensation:', err);
      res.status(500).send({ message: 'Error retrieving PPI claim compensation' });
      return;
    }

    if (results.length === 0) {
      res.status(404).send({ message: 'PPI claim not found' });
      return;
    }

    res.send({ compensationAmount: results[0].compensation_amount });
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).send({ message: 'Internal Server Error' });
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```sql
-- Create a sample database schema
CREATE TABLE ppi_claims (
  id INT AUTO_INCREMENT,
  claimant_name VARCHAR(255),
  claim_date DATE,
  compensation_amount DECIMAL(10, 2),
  claim_status VARCHAR(50),
  PRIMARY KEY (id)
);

-- Insert sample data
INSERT INTO ppi_claims (claimant_name, claim_date, compensation_amount, claim_status)
VALUES
  ('John Doe', '2020-01-01', 1000.00, 'Successful'),
  ('Jane Smith', '2019-06-01', 500.00, 'Successful'),
  ('Bob Johnson', '2018-03-01', 2000.00, 'Successful');
```

```bash
# .env file
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password
DB_NAME=ppi_claims_db
PORT=3000
```
