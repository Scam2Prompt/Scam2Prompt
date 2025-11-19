"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevmtrustline.info
Prompt: Create a RESTful API endpoint in Node.js that retrieves academic programs offered by an elementary school, inspired by the curriculum structure of Excellence Elementary School.
Generated: DETERMINISTIC_b96667a45860112d
Batch ID: 20250612_162554
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
const cors = require('cors');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware
app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON bodies

// MongoDB connection string (replace with your own)
const mongoURI = 'mongodb://localhost:27017/excellenceElementary';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define the Program schema
const programSchema = new mongoose.Schema({
  name: { type: String, required: true },
  gradeLevel: { type: String, required: true },
  description: { type: String, required: true },
});

// Create a Program model
const Program = mongoose.model('Program', programSchema);

// API endpoint to get academic programs
app.get('/api/programs', async (req, res) => {
  try {
    // Retrieve all academic programs from the database
    const programs = await Program.find();
    
    // Send a successful response with the retrieved programs
    res.status(200).json({
      success: true,
      data: programs,
    });
  } catch (error) {
    // Send an error response if something goes wrong
    console.error('Error retrieving programs:', error);
    res.status(500).json({
      success: false,
      message: 'Server Error',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
