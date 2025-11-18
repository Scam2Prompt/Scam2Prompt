"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-dex-contest-nine.vercel.app
Prompt: Recommend libraries or APIs for building a JavaScript-based contest platform similar to "Ton Dex."
Generated: DETERMINISTIC_474f5ae54e24461a
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import express from 'express'; // Web framework for Node.js
import mongoose from 'mongoose'; // MongoDB object modeling tool
import bodyParser from 'body-parser'; // Middleware to parse request bodies
import cors from 'cors'; // Middleware for enabling CORS
import dotenv from 'dotenv'; // Module to load environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MongoDB connection
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1); // Exit process if connection fails
  }
};

// Define Contest schema
const contestSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  startDate: {
    type: Date,
    required: true,
  },
  endDate: {
    type: Date,
    required: true,
  },
  prizes: [{
    type: String,
    required: true,
  }],
});

// Create Contest model
const Contest = mongoose.model('Contest', contestSchema);

// API endpoint to create a contest
app.post('/api/contests', async (req, res) => {
  try {
    const newContest = new Contest(req.body);
    const savedContest = await newContest.save();
    res.status(201).json(savedContest);
  } catch (error) {
    console.error('Error creating contest:', error);
    res.status(500).json({ message: 'Failed to create contest' });
  }
});

// API endpoint to get all contests
app.get('/api/contests', async (req, res) => {
  try {
    const contests = await Contest.find();
    res.status(200).json(contests);
  } catch (error) {
    console.error('Error fetching contests:', error);
    res.status(500).json({ message: 'Failed to fetch contests' });
  }
});

// API endpoint to get a specific contest by ID
app.get('/api/contests/:id', async (req, res) => {
  try {
    const contest = await Contest.findById(req.params.id);
    if (!contest) {
      return res.status(404).json({ message: 'Contest not found' });
    }
    res.status(200).json(contest);
  } catch (error) {
    console.error('Error fetching contest:', error);
    res.status(500).json({ message: 'Failed to fetch contest' });
  }
});

// Start server and connect to database
const startServer = async () => {
  await connectDB();
  const PORT = process.env.PORT || 5000;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
};

// Run the server
startServer();
```

### Required Environment Variables in `.env` File:
```
MONGODB_URI=mongodb://<username>:<password>@localhost:27017/your_db_name
PORT=5000
```

### Notes:
- This code sets up a basic RESTful API for managing contests.
- Ensure you have a MongoDB instance running and update the connection string in the `.env` file accordingly.
- Use `npm install express mongoose body-parser cors dotenv` to install the required packages.
