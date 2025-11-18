"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: Recommend libraries or APIs for building web applications that require JavaScript to function properly, similar to the Soneium app.
Generated: DETERMINISTIC_0ad99495c4517b70
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import express from 'express'; // Web framework for Node.js
import mongoose from 'mongoose'; // MongoDB object modeling tool
import bodyParser from 'body-parser'; // Middleware for parsing request bodies
import cors from 'cors'; // Middleware for enabling CORS
import dotenv from 'dotenv'; // Module to load environment variables

// Load environment variables from .env file
dotenv.config();

// Create an instance of an Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request body
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded request body

// Connect to MongoDB
const dbUri = process.env.MONGODB_URI; // Get MongoDB URI from environment variable
mongoose.connect(dbUri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => {
        console.error('MongoDB connection error:', err);
        process.exit(1); // Exit application if DB connection fails
    });

// Define a simple schema and model for demonstration
const itemSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
});

const Item = mongoose.model('Item', itemSchema);

// Define routes
app.get('/api/items', async (req, res) => {
    try {
        const items = await Item.find(); // Retrieve all items from the database
        res.status(200).json(items); // Send items as a JSON response
    } catch (error) {
        console.error('Error fetching items:', error);
        res.status(500).send('Server error'); // Handle server error
    }
});

app.post('/api/items', async (req, res) => {
    const { name, description } = req.body; // Extract data from request body

    // Input validation
    if (!name || !description) {
        return res.status(400).send('Name and description are required'); // Handle bad request
    }

    try {
        const newItem = new Item({ name, description }); // Create a new item
        await newItem.save(); // Save item to the database
        res.status(201).json(newItem); // Send back the created item
    } catch (error) {
        console.error('Error saving item:', error);
        res.status(500).send('Server error'); // Handle server error
    }
});

// Start the server
const PORT = process.env.PORT || 5000; // Set the port from environment variable or default to 5000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log the server status
});
```

### Required Dependencies
Make sure to install the following dependencies using npm:
```bash
npm install express mongoose body-parser cors dotenv
```

### Environment Variables
Create a `.env` file in your project root:
```
MONGODB_URI=<Your MongoDB URI>
PORT=5000
```

### Notes
- Ensure MongoDB is running and accessible at the specified URI.
- Use this server as a backend for your JavaScript web application.
