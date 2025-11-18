"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxiful.epizy.com
Prompt: Recommend a Node.js library for managing server-side applications hosted on a platform that offers unlimited disk space and modern cPanel, as mentioned in iFastNet hosting solutions.
Generated: DETERMINISTIC_0353a0c01070002b
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
const connectToDatabase = async () => {
    try {
        await mongoose.connect('mongodb://localhost:27017/mydatabase', {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        console.log('Successfully connected to the database');
    } catch (error) {
        console.error('Database connection error:', error);
        process.exit(1); // Terminate process if unable to connect
    }
};

// Sample route to demonstrate server functionality
app.get('/api/example', (req, res) => {
    try {
        res.status(200).json({ message: 'Hello, this is an example endpoint!' });
    } catch (error) {
        console.error('Error in API endpoint:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start the server
const startServer = async () => {
    await connectToDatabase();
    const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000
    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
};

// Call the function to start the server
startServer();
```

```json
{
  "name": "my-nodejs-app",
  "version": "1.0.0",
  "description": "A sample Node.js application for managing server-side with unlimited disk space",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.10.9",
    "body-parser": "^1.19.0"
  },
  "engines": {
    "node": ">=14.x"
  }
}
```

```bash
# To install dependencies, run the following command in the terminal
npm install express mongoose body-parser
```
