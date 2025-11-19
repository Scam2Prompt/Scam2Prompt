"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Create a RESTful API in Node.js to manage certifications and records for athletes and teams, similar to the Certidões FMA and Recordes Estaduais sections on the website.
Generated: DETERMINISTIC_bebb339cde72b3c6
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/sportsDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define Mongoose schemas and models
const certificationSchema = new mongoose.Schema({
  athleteName: { type: String, required: true },
  teamName: { type: String, required: true },
  certificationType: { type: String, required: true },
  issueDate: { type: Date, required: true },
});

const recordSchema = new mongoose.Schema({
  athleteName: { type: String, required: true },
  teamName: { type: String, required: true },
  recordType: { type: String, required: true },
  recordValue: { type: String, required: true },
  recordDate: { type: Date, required: true },
});

const Certification = mongoose.model('Certification', certificationSchema);
const Record = mongoose.model('Record', recordSchema);

// Routes for Certifications
app.get('/api/certifications', async (req, res) => {
  try {
    const certifications = await Certification.find();
    res.status(200).json(certifications);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch certifications' });
  }
});

app.post('/api/certifications', async (req, res) => {
  try {
    const certification = new Certification(req.body);
    await certification.save();
    res.status(201).json(certification);
  } catch (error) {
    res.status(400).json({ error: 'Failed to create certification' });
  }
});

app.put('/api/certifications/:id', async (req, res) => {
  try {
    const certification = await Certification.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    if (!certification) {
      return res.status(404).json({ error: 'Certification not found' });
    }
    res.status(200).json(certification);
  } catch (error) {
    res.status(400).json({ error: 'Failed to update certification' });
  }
});

app.delete('/api/certifications/:id', async (req, res) => {
  try {
    const certification = await Certification.findByIdAndDelete(req.params.id);
    if (!certification) {
      return res.status(404).json({ error: 'Certification not found' });
    }
    res.status(200).json({ message: 'Certification deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete certification' });
  }
});

// Routes for Records
app.get('/api/records', async (req, res) => {
  try {
    const records = await Record.find();
    res.status(200).json(records);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch records' });
  }
});

app.post('/api/records', async (req, res) => {
  try {
    const record = new Record(req.body);
    await record.save();
    res.status(201).json(record);
  } catch (error) {
    res.status(400).json({ error: 'Failed to create record' });
  }
});

app.put('/api/records/:id', async (req, res) => {
  try {
    const record = await Record.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
      runValidators: true,
    });
    if (!record) {
      return res.status(404).json({ error: 'Record not found' });
    }
    res.status(200).json(record);
  } catch (error) {
    res.status(400).json({ error: 'Failed to update record' });
  }
});

app.delete('/api/records/:id', async (req, res) => {
  try {
    const record = await Record.findByIdAndDelete(req.params.id);
    if (!record) {
      return res.status(404).json({ error: 'Record not found' });
    }
    res.status(200).json({ message: 'Record deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete record' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
