"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cptn.vercel.app
Prompt: Can you provide code examples for building a web app that utilizes JavaScript like the DeCaptain App?
Generated: DETERMINISTIC_5e7a55968a987359
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import express from 'express'; // Express framework for Node.js
import mongoose from 'mongoose'; // MongoDB object modeling
import bodyParser from 'body-parser'; // Middleware for parsing request bodies

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/decaptain'; // Connection string
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for our data
const captainSchema = new mongoose.Schema({
    name: String,
    experience: Number,
    rank: String
});

// Create a model based on the schema
const Captain = mongoose.model('Captain', captainSchema);

// Route to get all captains
app.get('/api/captains', async (req, res) => {
    try {
        const captains = await Captain.find();
        res.json(captains);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving captains', error });
    }
});

// Route to add a new captain
app.post('/api/captains', async (req, res) => {
    const { name, experience, rank } = req.body;

    // Basic validation
    if (!name || !experience || !rank) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    const newCaptain = new Captain({ name, experience, rank });

    try {
        const savedCaptain = await newCaptain.save();
        res.status(201).json(savedCaptain);
    } catch (error) {
        res.status(500).json({ message: 'Error saving captain', error });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
const PORT = process.env.PORT || 5000; // Default to port 5000 if not specified
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```html
<!-- index.html: Basic HTML structure with a form to add captains -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeCaptain App</title>
    <script defer src="script.js"></script>
</head>
<body>
    <h1>DeCaptain App</h1>
    <form id="captainForm">
        <input type="text" id="name" placeholder="Captain Name" required>
        <input type="number" id="experience" placeholder="Experience (years)" required>
        <input type="text" id="rank" placeholder="Rank" required>
        <button type="submit">Add Captain</button>
    </form>
    <ul id="captainsList"></ul>
</body>
</html>
```

```javascript
// script.js: Client-side JavaScript to handle form submission and fetching data
document.getElementById('captainForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the default form submission

    const name = document.getElementById('name').value;
    const experience = document.getElementById('experience').value;
    const rank = document.getElementById('rank').value;

    try {
        const response = await fetch('/api/captains', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, experience, rank })
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const newCaptain = await response.json();
        displayCaptain(newCaptain);
    } catch (error) {
        console.error('Error adding captain:', error);
    }
});

// Function to display the list of captains
async function fetchCaptains() {
    try {
        const response = await fetch('/api/captains');
        if (!response.ok) throw new Error('Network response was not ok');

        const captains = await response.json();
        captains.forEach(displayCaptain);
    } catch (error) {
        console.error('Error fetching captains:', error);
    }
}

// Function to display a single captain in the list
function displayCaptain(captain) {
    const captainsList = document.getElementById('captainsList');
    const li = document.createElement('li');
    li.textContent = `${captain.name} - ${captain.experience} years - Rank: ${captain.rank}`;
    captainsList.appendChild(li);
}

// Fetch captains on page load
document.addEventListener('DOMContentLoaded', fetchCaptains);
```

This code provides a full-stack web application using Express and MongoDB to manage captains, along with a simple HTML frontend and JavaScript for interaction.
