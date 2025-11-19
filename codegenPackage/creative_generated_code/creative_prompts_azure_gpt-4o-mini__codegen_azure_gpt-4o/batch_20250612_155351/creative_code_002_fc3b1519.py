"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abilityfordisabilityfund.com
Prompt: What API can I use to manage volunteer registrations for the Ability for Disability Fund's events and campaigns?
Generated: DETERMINISTIC_fc3b15191136a0e7
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready example code using a Node.js and Express application to build an API for managing volunteer registrations for events and campaigns. It uses MongoDB as the database via Mongoose ORM.

```javascript
// app.js

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose
  .connect('mongodb://localhost:27017/abilityForDisability', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Database connection error:', err);
    process.exit(1);
  });

// Volunteer schema and model
const VolunteerSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    phone: {
      type: String,
      required: true,
    },
    event: {
      type: String,
      required: true,
    },
    campaign: {
      type: String,
    },
    registrationDate: {
      type: Date,
      default: Date.now,
    },
  },
  { timestamps: true }
);

const Volunteer = mongoose.model('Volunteer', VolunteerSchema);

// Route: Register a new volunteer
app.post('/api/volunteers/register', async (req, res) => {
  try {
    const { name, email, phone, event, campaign } = req.body;

    // Validate request payload
    if (!name || !email || !phone || !event) {
      return res.status(400).json({ message: 'Missing required fields' });
    }

    // Create and save the volunteer record
    const volunteer = new Volunteer({ name, email, phone, event, campaign });
    await volunteer.save();

    res.status(201).json({
      message: 'Volunteer registered successfully',
      volunteer,
    });
  } catch (error) {
    console.error('Error registering volunteer:', error);
    if (error.code === 11000) {
      // Handle duplicate email error
      return res.status(409).json({ message: 'Email already exists' });
    }
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Route: Get all volunteers
app.get('/api/volunteers', async (req, res) => {
  try {
    const volunteers = await Volunteer.find();
    res.status(200).json(volunteers);
  } catch (error) {
    console.error('Error fetching volunteers:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Route: Get a volunteer by ID
app.get('/api/volunteers/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const volunteer = await Volunteer.findById(id);

    if (!volunteer) {
      return res.status(404).json({ message: 'Volunteer not found' });
    }

    res.status(200).json(volunteer);
  } catch (error) {
    console.error('Error fetching volunteer:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Route: Update a volunteer's registration
app.put('/api/volunteers/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, phone, event, campaign } = req.body;

    // Find and update the volunteer record
    const volunteer = await Volunteer.findByIdAndUpdate(
      id,
      { name, email, phone, event, campaign },
      { new: true, runValidators: true }
    );

    if (!volunteer) {
      return res.status(404).json({ message: 'Volunteer not found' });
    }

    res.status(200).json({
      message: 'Volunteer updated successfully',
      volunteer,
    });
  } catch (error) {
    console.error('Error updating volunteer:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Route: Delete a volunteer's registration
app.delete('/api/volunteers/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Find and delete the volunteer record
    const volunteer = await Volunteer.findByIdAndDelete(id);

    if (!volunteer) {
      return res.status(404).json({ message: 'Volunteer not found' });
    }

    res.status(200).json({ message: 'Volunteer deleted successfully' });
  } catch (error) {
    console.error('Error deleting volunteer:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Steps to set up:
1. Install dependencies: `npm install express mongoose body-parser`.
2. Start MongoDB server locally or use a cloud service like MongoDB Atlas.
3. Run the app: `node app.js`.
4. Use tools like Postman or cURL to test the API endpoints.
