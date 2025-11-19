"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Create a REST API endpoint in Node.js that allows users to sign up for music lessons at a private music school, including fields for instrument selection and lesson type.
Generated: DETERMINISTIC_d2e442e03f6511c4
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Create an Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/music_school', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define a schema for lesson sign-ups
const lessonSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    instrument: { type: String, required: true },
    lessonType: { type: String, required: true, enum: ['individual', 'group'] },
});

// Create a model based on the schema
const LessonSignup = mongoose.model('LessonSignup', lessonSchema);

// API endpoint to sign up for music lessons
app.post('/api/signup', async (req, res) => {
    try {
        // Validate incoming request data
        const { name, email, instrument, lessonType } = req.body;
        if (!name || !email || !instrument || !lessonType) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new lesson signup
        const newSignup = new LessonSignup({ name, email, instrument, lessonType });
        
        // Save the signup to the database
        await newSignup.save();

        // Respond with a success message
        res.status(201).json({ message: 'Sign up successful!', signup: newSignup });
    } catch (error) {
        // Handle errors appropriately
        if (error.code === 11000) {
            // Duplicate email error
            res.status(409).json({ error: 'Email already exists.' });
        } else {
            // General server error
            console.error(error); // Log error for debugging
            res.status(500).json({ error: 'An error occurred. Please try again later.' });
        }
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required packages by running:
```bash
npm install express body-parser mongoose
``` 

Also, ensure that MongoDB is running on your local machine or update the connection string to point to your MongoDB instance.
