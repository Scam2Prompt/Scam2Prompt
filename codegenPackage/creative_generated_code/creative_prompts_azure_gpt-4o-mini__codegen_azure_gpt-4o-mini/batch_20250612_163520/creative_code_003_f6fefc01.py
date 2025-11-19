"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armaghanenajaf.org
Prompt: Develop a RESTful API endpoint in Node.js that allows volunteers to register for upcoming events organized by Armaghan-e-Najaf.
Generated: DETERMINISTIC_f6fefc010998d559
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const mongoose = require('mongoose'); // MongoDB object modeling tool
const cors = require('cors'); // Middleware for enabling CORS

// Create an instance of Express
const app = express();

// Middleware configuration
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/armaghan-e-najaf', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Volunteer schema
const volunteerSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    eventId: { type: String, required: true },
    registeredAt: { type: Date, default: Date.now },
});

// Create a Volunteer model
const Volunteer = mongoose.model('Volunteer', volunteerSchema);

// API endpoint to register a volunteer
app.post('/api/volunteers/register', async (req, res) => {
    try {
        const { name, email, phone, eventId } = req.body;

        // Validate request body
        if (!name || !email || !phone || !eventId) {
            return res.status(400).json({ message: 'All fields are required.' });
        }

        // Create a new volunteer document
        const newVolunteer = new Volunteer({ name, email, phone, eventId });

        // Save the volunteer to the database
        await newVolunteer.save();

        // Respond with success message
        res.status(201).json({ message: 'Volunteer registered successfully.' });
    } catch (error) {
        // Handle errors (e.g., duplicate email)
        console.error('Error registering volunteer:', error);
        res.status(500).json({ message: 'Server error. Please try again later.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
