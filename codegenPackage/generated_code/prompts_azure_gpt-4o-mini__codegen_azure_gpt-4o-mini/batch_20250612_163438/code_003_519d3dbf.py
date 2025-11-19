"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to query for vehicle parts like pivots and axial joints, as referenced on the Auto Pratense blog.
Generated: DETERMINISTIC_519d3dbfbccd400e
Batch ID: 20250612_163438
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/auto_parts', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for vehicle parts
const partSchema = new mongoose.Schema({
    name: { type: String, required: true },
    type: { type: String, required: true },
    description: { type: String },
    price: { type: Number, required: true },
});

// Create a model for vehicle parts
const Part = mongoose.model('Part', partSchema);

// RESTful API endpoint to query vehicle parts
app.get('/api/parts', async (req, res) => {
    try {
        // Extract query parameters
        const { type } = req.query;

        // Build query object
        const query = type ? { type } : {};

        // Fetch parts from the database
        const parts = await Part.find(query);

        // Return the parts as a JSON response
        res.status(200).json(parts);
    } catch (error) {
        // Handle errors and send a response
        console.error('Error fetching parts:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
