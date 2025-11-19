"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Develop a JavaScript application that connects users with legal advisors, referencing the experience of Fachri Ahyani in handling criminal and civil cases.
Generated: DETERMINISTIC_ad3fa41e113db731
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Legal Advisor Connection Application
// Connects users with legal advisors based on expertise in criminal and civil cases
// Inspired by Fachri Ahyani's experience in handling such cases

// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect('mongodb://localhost:27017/legalAdvisorDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('Database connection error:', err);
    process.exit(1);
});

// Define Legal Advisor Schema
const legalAdvisorSchema = new mongoose.Schema({
    name: { type: String, required: true },
    expertise: { 
        type: String, 
        required: true,
        enum: ['Criminal', 'Civil', 'Both']
    },
    experienceYears: { type: Number, required: true },
    contactEmail: { 
        type: String, 
        required: true,
        match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'Please fill a valid email address']
    },
    phone: { type: String },
    bio: { type: String },
    languages: { type: [String] },
    rating: { type: Number, min: 1, max: 5 }
});

// Define User Schema
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { 
        type: String, 
        required: true,
        match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'Please fill a valid email address']
    },
    phone: { type: String },
    caseType: { 
        type: String, 
        required: true,
        enum: ['Criminal', 'Civil']
    },
    caseDescription: { type: String, required: true }
});

// Create models
const LegalAdvisor = mongoose.model('LegalAdvisor', legalAdvisorSchema);
const User = mongoose.model('User', userSchema);

// Routes

// Get all legal advisors
app.get('/api/advisors', async (req, res) => {
    try {
        const advisors = await LegalAdvisor.find();
        res.json(advisors);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get advisors by expertise
app.get('/api/advisors/:expertise', async (req, res) => {
    try {
        const expertise = req.params.expertise;
        if (!['Criminal', 'Civil', 'Both'].includes(expertise)) {
            return res.status(400).json({ message: 'Invalid expertise type' });
        }

        let query = { expertise };
        if (expertise === 'Both') {
            query = { expertise: 'Both' };
        }

        const advisors = await LegalAdvisor.find(query);
        res.json(advisors);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Create a new user request
app.post('/api/users', async (req, res) => {
    try {
        const { name, email, phone, caseType, caseDescription } = req.body;

        if (!name || !email || !caseType || !caseDescription) {
            return res.status(400).json({ message: 'Missing required fields' });
        }

        const newUser = new User({
            name,
            email,
            phone,
            caseType,
            caseDescription
        });

        const savedUser = await newUser.save();
        
        // Find matching advisors
        const matchingAdvisors = await LegalAdvisor.find({
            $or: [
                { expertise: caseType },
                { expertise: 'Both' }
            ]
        }).sort({ experienceYears: -1, rating: -1 }).limit(3);

        res.status(201).json({
            user: savedUser,
            recommendedAdvisors: matchingAdvisors
        });
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Add a new legal advisor (admin function)
app.post('/api/advisors', async (req, res) => {
    try {
        const { name, expertise, experienceYears, contactEmail, phone, bio, languages, rating } = req.body;

        if (!name || !expertise || !experienceYears || !contactEmail) {
            return res.status(400).json({ message: 'Missing required fields' });
        }

        const newAdvisor = new LegalAdvisor({
            name,
            expertise,
            experienceYears,
            contactEmail,
            phone,
            bio,
            languages,
            rating
        });

        const savedAdvisor = await newAdvisor.save();
        res.status(201).json(savedAdvisor);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
