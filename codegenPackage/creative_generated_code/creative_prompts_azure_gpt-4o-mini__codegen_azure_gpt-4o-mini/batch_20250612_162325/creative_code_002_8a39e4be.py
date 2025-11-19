"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tidhholding.com
Prompt: Create a RESTful API endpoint using Node.js that allows users to submit project proposals to TIDH Holding for potential investment collaboration.
Generated: DETERMINISTIC_8a39e4bebacd25d9
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (make sure to replace <DB_CONNECTION_STRING> with your actual connection string)
mongoose.connect('<DB_CONNECTION_STRING>', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Proposal schema
const proposalSchema = new mongoose.Schema({
    name: { type: String, required: true }, // Proposer's name
    email: { type: String, required: true, match: /.+\@.+\..+/ }, // Proposer's email
    projectTitle: { type: String, required: true }, // Project title
    projectDescription: { type: String, required: true }, // Project description
    createdAt: { type: Date, default: Date.now } // Timestamp
});

// Create a Proposal model
const Proposal = mongoose.model('Proposal', proposalSchema);

// POST endpoint to submit a project proposal
app.post('/api/proposals', async (req, res) => {
    try {
        const { name, email, projectTitle, projectDescription } = req.body;

        // Validate request body
        if (!name || !email || !projectTitle || !projectDescription) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new proposal
        const proposal = new Proposal({
            name,
            email,
            projectTitle,
            projectDescription
        });

        // Save the proposal to the database
        await proposal.save();
        
        // Respond with the created proposal
        res.status(201).json({ message: 'Proposal submitted successfully', proposal });

    } catch (error) {
        console.error('Error submitting proposal:', error);
        res.status(500).json({ error: 'An error occurred while submitting your proposal' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to replace `<DB_CONNECTION_STRING>` with your actual MongoDB connection string before running the code.
