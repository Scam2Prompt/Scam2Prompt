"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Create a REST API in Node.js for a system and software development team, similar to the one mentioned on oppomobile.id.
Generated: DETERMINISTIC_2b527f6b21a8cbbb
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express for creating the REST API
const bodyParser = require('body-parser'); // Body parser for handling JSON payloads
const dotenv = require('dotenv'); // dotenv for environment variables
const helmet = require('helmet'); // Helmet for enhancing security
const cors = require('cors'); // CORS for handling cross-origin requests
const mongoose = require('mongoose'); // Mongoose for interacting with MongoDB

// Load environment variables from .env file
dotenv.config();

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse incoming JSON requests
app.use(helmet()); // Add security headers
app.use(cors()); // Enable cross-origin resource sharing

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => {
    console.error('Error connecting to MongoDB:', error.message);
    process.exit(1); // Exit process if database connection fails
  });

// Define the team schema and model
const teamSchema = new mongoose.Schema({
  name: { type: String, required: true }, // Team member name
  role: { type: String, required: true }, // Team member role
  skills: [String], // Skills of the team member
  email: { type: String, required: true, unique: true }, // Unique email for the team member
}, { timestamps: true }); // Add createdAt and updatedAt timestamps

const TeamMember = mongoose.model('TeamMember', teamSchema);

// Routes

// GET /api/team - Retrieve all team members
app.get('/api/team', async (req, res) => {
  try {
    const teamMembers = await TeamMember.find();
    res.status(200).json(teamMembers);
  } catch (error) {
    res.status(500).json({ message: 'Server Error', error: error.message });
  }
});

// POST /api/team - Add a new team member
app.post('/api/team', async (req, res) => {
  const { name, role, skills, email } = req.body;

  if (!name || !role || !email) {
    return res.status(400).json({ message: 'Name, role, and email are required' });
  }

  try {
    const newMember = new TeamMember({ name, role, skills, email });
    await newMember.save();
    res.status(201).json(newMember);
  } catch (error) {
    res.status(500).json({ message: 'Server Error', error: error.message });
  }
});

// PUT /api/team/:id - Update a team member
app.put('/api/team/:id', async (req, res) => {
  const { id } = req.params;
  const updatedData = req.body;

  try {
    const updatedMember = await TeamMember.findByIdAndUpdate(id, updatedData, {
      new: true,
      runValidators: true,
    });

    if (!updatedMember) {
      return res.status(404).json({ message: 'Team member not found' });
    }

    res.status(200).json(updatedMember);
  } catch (error) {
    res.status(500).json({ message: 'Server Error', error: error.message });
  }
});

// DELETE /api/team/:id - Remove a team member
app.delete('/api/team/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const deletedMember = await TeamMember.findByIdAndDelete(id);

    if (!deletedMember) {
      return res.status(404).json({ message: 'Team member not found' });
    }

    res.status(200).json({ message: 'Team member removed successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Server Error', error: error.message });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

```

### Instructions:
1. Save the code into a file (e.g., `server.js`).
2. Create a `.env` file in the same directory and add the following:
   ```
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<databaseName>?retryWrites=true&w=majority
   PORT=3000
   ```
   Replace `<username>`, `<password>`, `<cluster>`, and `<databaseName>` with the appropriate values for your MongoDB instance.
3. Run the following commands to install dependencies:
   ```
   npm install express body-parser dotenv helmet cors mongoose
   ```
4. Start the server with:
   ```
   node server.js
   ```
