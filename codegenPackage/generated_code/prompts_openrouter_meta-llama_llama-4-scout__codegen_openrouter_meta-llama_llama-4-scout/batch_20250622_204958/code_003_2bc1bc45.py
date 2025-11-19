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
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/handyman', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for technicians
const technicianSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    jobs: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Job' }]
});

// Define schema for jobs
const jobSchema = new mongoose.Schema({
    title: String,
    description: String,
    scheduledDate: Date,
    assignedTechnician: { type: mongoose.Schema.Types.ObjectId, ref: 'Technician' },
    status: String
});

// Compile schemas into models
const Technician = mongoose.model('Technician', technicianSchema);
const Job = mongoose.model('Job', jobSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new technician
app.post('/technicians', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10);
        const technician = new Technician({
            name: req.body.name,
            email: req.body.email,
            password: hashedPassword
        });
        await technician.save();
        res.status(201).send({ message: 'Technician created successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error creating technician', error });
    }
});

// Login a technician
app.post('/login', async (req, res) => {
    try {
        const technician = await Technician.findOne({ email: req.body.email });
        if (!technician) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, technician.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ technicianId: technician._id }, 'secretkey', { expiresIn: '1h' });
        res.send({ token });
    } catch (error) {
        res.status(400).send({ message: 'Error logging in', error });
    }
});

// Create a new job
app.post('/jobs', authenticateToken, async (req, res) => {
    try {
        const job = new Job({
            title: req.body.title,
            description: req.body.description,
            scheduledDate: req.body.scheduledDate,
            status: 'pending'
        });
        await job.save();
        res.status(201).send({ message: 'Job created successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error creating job', error });
    }
});

// Schedule a job
app.patch('/jobs/:id/schedule', authenticateToken, async (req, res) => {
    try {
        const job = await Job.findById(req.params.id);
        if (!job) {
            return res.status(404).send({ message: 'Job not found' });
        }
        job.scheduledDate = req.body.scheduledDate;
        await job.save();
        res.send({ message: 'Job scheduled successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error scheduling job', error });
    }
});

// Assign a job to a technician
app.patch('/jobs/:id/assign', authenticateToken, async (req, res) => {
    try {
        const job = await Job.findById(req.params.id);
        if (!job) {
            return res.status(404).send({ message: 'Job not found' });
        }
        const technician = await Technician.findById(req.body.technicianId);
        if (!technician) {
            return res.status(404).send({ message: 'Technician not found' });
        }
        job.assignedTechnician = technician._id;
        job.status = 'assigned';
        await job.save();
        technician.jobs.push(job._id);
        await technician.save();
        res.send({ message: 'Job assigned successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error assigning job', error });
    }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied' });
    try {
        const verified = jwt.verify(token, 'secretkey');
        req.technician = verified;
        next();
    } catch (error) {
        res.status(400).send({ message: 'Invalid token', error });
    }
}

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
