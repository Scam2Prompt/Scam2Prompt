"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-a.infinityfreeapp.com
Prompt: Generate a Node.js application that can be hosted on a platform with unlimited bandwidth and disk space, such as iFastNet.
Generated: DETERMINISTIC_4bc20b065f70e606
Batch ID: 20250612_154423
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Create an instance of the Express application
const app = express();

// Middleware configuration
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Database connection configuration
const dbURI = 'mongodb://localhost:27017/mydatabase'; // Update with your MongoDB URI
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => {
        console.error('MongoDB connection error:', err);
        process.exit(1); // Exit process with failure
    });

// Define a simple schema for demonstration
const ItemSchema = new mongoose.Schema({
    name: { type: String, required: true },
    quantity: { type: Number, required: true }
});

// Create a model based on the schema
const Item = mongoose.model('Item', ItemSchema);

// RESTful API routes

// Create a new item
app.post('/items', async (req, res) => {
    try {
        const newItem = new Item(req.body);
        await newItem.save();
        res.status(201).json(newItem);
    } catch (error) {
        console.error('Error creating item:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get all items
app.get('/items', async (req, res) => {
    try {
        const items = await Item.find();
        res.status(200).json(items);
    } catch (error) {
        console.error('Error retrieving items:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Instructions for Hosting:**
1. Ensure you have Node.js and MongoDB installed.
2. Update the `dbURI` variable with your MongoDB connection string.
3. Run `npm install express mongoose body-parser cors` to install required packages.
4. Start the application using `node app.js`.
5. Deploy on a platform with unlimited bandwidth and disk space, ensuring proper environment setup.
