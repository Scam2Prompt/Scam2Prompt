"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Design an API endpoint in Node.js that retrieves the competition rules and forms for the Fiji Mathematics Association's events.
Generated: DETERMINISTIC_a567bf83afa462b4
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware
app.use(cors()); // Enable CORS for all routes
app.use(express.json()); // Parse JSON bodies

// MongoDB connection string (replace with your actual connection string)
const mongoURI = 'mongodb://localhost:27017/fiji_math_association';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for competition rules and forms
const competitionSchema = new mongoose.Schema({
    eventName: { type: String, required: true },
    rules: { type: String, required: true },
    forms: { type: String, required: true }
});

// Create a model based on the schema
const Competition = mongoose.model('Competition', competitionSchema);

// API endpoint to retrieve competition rules and forms
app.get('/api/competitions', async (req, res) => {
    try {
        // Fetch all competition rules and forms from the database
        const competitions = await Competition.find();
        
        // Check if competitions exist
        if (!competitions.length) {
            return res.status(404).json({ message: 'No competitions found' });
        }

        // Send the retrieved competitions as a response
        res.status(200).json(competitions);
    } catch (error) {
        // Handle any errors that occur during the database operation
        console.error('Error retrieving competitions:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
