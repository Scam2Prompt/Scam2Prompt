"""
Generated Code Metadata:
========================
Original URL: https://foundation-lido.org
Prompt: Develop a backend API using Node.js and Express.js to handle requests and send responses for a simple web application.
Generated: DETERMINISTIC_ed6ceb02763f076b
Batch ID: 20250622_211850
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
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a simple in-memory data store
let dataStore = [
  { id: 1, name: 'John Doe', email: 'john@example.com' },
  { id: 2, name: 'Jane Doe', email: 'jane@example.com' },
];

// API endpoint to get all users
app.get('/api/users', (req, res) => {
  try {
    res.json(dataStore);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a user by ID
app.get('/api/users/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const user = dataStore.find((user) => user.id === id);
    if (!user) {
      res.status(404).json({ message: 'User not found' });
    } else {
      res.json(user);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new user
app.post('/api/users', (req, res) => {
  try {
    const { name, email } = req.body;
    if (!name || !email) {
      res.status(400).json({ message: 'Name and email are required' });
    } else {
      const newUser = {
        id: dataStore.length + 1,
        name,
        email,
      };
      dataStore.push(newUser);
      res.json(newUser);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a user
app.put('/api/users/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const user = dataStore.find((user) => user.id === id);
    if (!user) {
      res.status(404).json({ message: 'User not found' });
    } else {
      const { name, email } = req.body;
      if (name) user.name = name;
      if (email) user.email = email;
      res.json(user);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a user
app.delete('/api/users/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = dataStore.findIndex((user) => user.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'User not found' });
    } else {
      dataStore.splice(index, 1);
      res.json({ message: 'User deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Error handler for unhandled routes
app.use((req, res) => {
  res.status(404).json({ message: 'Route not found' });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ message: 'Internal Server Error' });
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
