"""
Generated Code Metadata:
========================
Original URL: https://baboons.vercel.app
Prompt: Design a simple backend API using Node.js that can support the Golden Baboons Mining Club application's functionality.
Generated: DETERMINISTIC_d19c7e316bc3835a
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies
const cors = require('cors'); // Middleware to enable Cross-Origin Resource Sharing
const helmet = require('helmet'); // Middleware to enhance security
const morgan = require('morgan'); // Middleware for logging HTTP requests

// Initialize the Express application
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(cors()); // Enable CORS for all routes
app.use(helmet()); // Add security headers to responses
app.use(morgan('combined')); // Log HTTP requests

// In-memory database (for simplicity, replace with a real database in production)
const members = []; // Array to store club members
const transactions = []; // Array to store mining transactions

// Routes

/**
 * GET /api/members
 * Fetch all members of the Golden Baboons Mining Club.
 */
app.get('/api/members', (req, res) => {
  res.status(200).json({ success: true, data: members });
});

/**
 * POST /api/members
 * Add a new member to the club.
 * Request body: { name: string, email: string }
 */
app.post('/api/members', (req, res) => {
  const { name, email } = req.body;

  // Validate input
  if (!name || !email) {
    return res.status(400).json({ success: false, message: 'Name and email are required.' });
  }

  // Create new member
  const newMember = { id: members.length + 1, name, email };
  members.push(newMember);

  res.status(201).json({ success: true, data: newMember });
});

/**
 * GET /api/transactions
 * Fetch all mining transactions.
 */
app.get('/api/transactions', (req, res) => {
  res.status(200).json({ success: true, data: transactions });
});

/**
 * POST /api/transactions
 * Record a new mining transaction.
 * Request body: { memberId: number, amount: number }
 */
app.post('/api/transactions', (req, res) => {
  const { memberId, amount } = req.body;

  // Validate input
  if (!memberId || !amount || amount <= 0) {
    return res.status(400).json({ success: false, message: 'Valid memberId and positive amount are required.' });
  }

  // Check if member exists
  const member = members.find((m) => m.id === memberId);
  if (!member) {
    return res.status(404).json({ success: false, message: 'Member not found.' });
  }

  // Create new transaction
  const newTransaction = { id: transactions.length + 1, memberId, amount, date: new Date() };
  transactions.push(newTransaction);

  res.status(201).json({ success: true, data: newTransaction });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack trace
  res.status(500).json({ success: false, message: 'Internal Server Error' });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
