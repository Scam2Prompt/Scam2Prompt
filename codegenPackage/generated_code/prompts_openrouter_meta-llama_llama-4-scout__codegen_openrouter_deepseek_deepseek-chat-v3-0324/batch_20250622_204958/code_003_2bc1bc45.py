"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Create a RESTful API in Node.js for managing handyman services, including job creation, scheduling, and assignment to technicians.
Generated: DETERMINISTIC_2bc1bc45b243b0bf
Batch ID: 20250622_204958
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
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/handymanDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define Mongoose Schemas
const technicianSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  skills: { type: [String], required: true },
  availability: { type: Boolean, default: true }
});

const jobSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  title: { type: String, required: true },
  description: { type: String, required: true },
  clientName: { type: String, required: true },
  clientPhone: { type: String, required: true },
  address: { type: String, required: true },
  scheduledDate: { type: Date, required: true },
  status: { type: String, enum: ['pending', 'assigned', 'completed', 'cancelled'], default: 'pending' },
  assignedTechnician: { type: String, ref: 'Technician' },
  createdAt: { type: Date, default: Date.now }
});

// Create Mongoose Models
const Technician = mongoose.model('Technician', technicianSchema);
const Job = mongoose.model('Job', jobSchema);

// Routes for Technicians
app.get('/api/technicians', async (req, res) => {
  try {
    const technicians = await Technician.find();
    res.json(technicians);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/technicians', async (req, res) => {
  const technician = new Technician({
    name: req.body.name,
    skills: req.body.skills
  });

  try {
    const newTechnician = await technician.save();
    res.status(201).json(newTechnician);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.get('/api/technicians/:id', async (req, res) => {
  try {
    const technician = await Technician.findById(req.params.id);
    if (!technician) {
      return res.status(404).json({ message: 'Technician not found' });
    }
    res.json(technician);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.put('/api/technicians/:id', async (req, res) => {
  try {
    const technician = await Technician.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    if (!technician) {
      return res.status(404).json({ message: 'Technician not found' });
    }
    res.json(technician);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/technicians/:id', async (req, res) => {
  try {
    const technician = await Technician.findByIdAndDelete(req.params.id);
    if (!technician) {
      return res.status(404).json({ message: 'Technician not found' });
    }
    res.json({ message: 'Technician deleted' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Routes for Jobs
app.get('/api/jobs', async (req, res) => {
  try {
    const jobs = await Job.find().populate('assignedTechnician');
    res.json(jobs);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/jobs', async (req, res) => {
  const job = new Job({
    title: req.body.title,
    description: req.body.description,
    clientName: req.body.clientName,
    clientPhone: req.body.clientPhone,
    address: req.body.address,
    scheduledDate: req.body.scheduledDate
  });

  try {
    const newJob = await job.save();
    res.status(201).json(newJob);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.get('/api/jobs/:id', async (req, res) => {
  try {
    const job = await Job.findById(req.params.id).populate('assignedTechnician');
    if (!job) {
      return res.status(404).json({ message: 'Job not found' });
    }
    res.json(job);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.put('/api/jobs/:id', async (req, res) => {
  try {
    const job = await Job.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    ).populate('assignedTechnician');
    if (!job) {
      return res.status(404).json({ message: 'Job not found' });
    }
    res.json(job);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/jobs/:id', async (req, res) => {
  try {
    const job = await Job.findByIdAndDelete(req.params.id);
    if (!job) {
      return res.status(404).json({ message: 'Job not found' });
    }
    res.json({ message: 'Job deleted' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Assign Technician to Job
app.put('/api/jobs/:id/assign', async (req, res) => {
  try {
    const { technicianId } = req.body;
    
    // Check if technician exists
    const technician = await Technician.findById(technicianId);
    if (!technician) {
      return res.status(404).json({ message: 'Technician not found' });
    }

    // Check if technician is available
    if (!technician.availability) {
      return res.status(400).json({ message: 'Technician is not available' });
    }

    // Update job
    const job = await Job.findByIdAndUpdate(
      req.params.id,
      { 
        assignedTechnician: technicianId,
        status: 'assigned'
      },
      { new: true }
    ).populate('assignedTechnician');

    if (!job) {
      return res.status(404).json({ message: 'Job not found' });
    }

    // Update technician availability
    technician.availability = false;
    await technician.save();

    res.json(job);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Complete Job
app.put('/api/jobs/:id/complete', async (req, res) => {
  try {
    const job = await Job.findById(req.params.id);
    if (!job) {
      return res.status(404).json({ message: 'Job not found' });
    }

    if (!job.assignedTechnician) {
      return res.status(400).json({ message: 'Job is not assigned to a technician' });
    }

    // Update job status
    job.status = 'completed';
    await job.save();

    // Update technician availability
    const technician = await Technician.findById(job.assignedTechnician);
    if (technician) {
      technician.availability = true;
      await technician.save();
    }

    res.json(job);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something broke!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
