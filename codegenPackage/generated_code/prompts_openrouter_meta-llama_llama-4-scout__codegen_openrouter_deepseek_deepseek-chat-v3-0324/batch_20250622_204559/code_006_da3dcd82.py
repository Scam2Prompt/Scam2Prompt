"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: "Create a RESTful API using Node.js to manage projects, donations, and volunteers for a non-profit organization."
Generated: DETERMINISTIC_da3dcd829ee78d65
Batch ID: 20250622_204559
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
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const Project = mongoose.model('Project', new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    startDate: { type: Date, required: true },
    endDate: { type: Date },
    targetAmount: { type: Number, required: true },
    currentAmount: { type: Number, default: 0 },
    status: { type: String, enum: ['active', 'completed', 'cancelled'], default: 'active' },
    createdAt: { type: Date, default: Date.now }
}));

const Donation = mongoose.model('Donation', new mongoose.Schema({
    projectId: { type: mongoose.Schema.Types.ObjectId, ref: 'Project', required: true },
    donorName: { type: String, required: true },
    amount: { type: Number, required: true },
    email: { type: String, required: true },
    message: { type: String },
    isAnonymous: { type: Boolean, default: false },
    createdAt: { type: Date, default: Date.now }
}));

const Volunteer = mongoose.model('Volunteer', new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    skills: { type: [String], required: true },
    availability: { type: String, enum: ['weekdays', 'weekends', 'both'], required: true },
    projectInterests: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Project' }],
    createdAt: { type: Date, default: Date.now }
}));

// Routes
// Projects
app.get('/api/projects', async (req, res) => {
    try {
        const projects = await Project.find();
        res.json(projects);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/projects', async (req, res) => {
    const project = new Project({
        title: req.body.title,
        description: req.body.description,
        startDate: req.body.startDate,
        endDate: req.body.endDate,
        targetAmount: req.body.targetAmount
    });

    try {
        const newProject = await project.save();
        res.status(201).json(newProject);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.json(project);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.patch('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.json(project);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/projects/:id', async (req, res) => {
    try {
        const project = await Project.findByIdAndDelete(req.params.id);
        if (!project) {
            return res.status(404).json({ message: 'Project not found' });
        }
        res.json({ message: 'Project deleted' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Donations
app.get('/api/donations', async (req, res) => {
    try {
        const donations = await Donation.find().populate('projectId');
        res.json(donations);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/donations', async (req, res) => {
    const donation = new Donation({
        projectId: req.body.projectId,
        donorName: req.body.donorName,
        amount: req.body.amount,
        email: req.body.email,
        message: req.body.message,
        isAnonymous: req.body.isAnonymous
    });

    try {
        const newDonation = await donation.save();
        
        // Update project's current amount
        await Project.findByIdAndUpdate(req.body.projectId, {
            $inc: { currentAmount: req.body.amount }
        });
        
        res.status(201).json(newDonation);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/donations/:id', async (req, res) => {
    try {
        const donation = await Donation.findById(req.params.id).populate('projectId');
        if (!donation) {
            return res.status(404).json({ message: 'Donation not found' });
        }
        res.json(donation);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Volunteers
app.get('/api/volunteers', async (req, res) => {
    try {
        const volunteers = await Volunteer.find().populate('projectInterests');
        res.json(volunteers);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/volunteers', async (req, res) => {
    const volunteer = new Volunteer({
        name: req.body.name,
        email: req.body.email,
        phone: req.body.phone,
        skills: req.body.skills,
        availability: req.body.availability,
        projectInterests: req.body.projectInterests
    });

    try {
        const newVolunteer = await volunteer.save();
        res.status(201).json(newVolunteer);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/volunteers/:id', async (req, res) => {
    try {
        const volunteer = await Volunteer.findById(req.params.id).populate('projectInterests');
        if (!volunteer) {
            return res.status(404).json({ message: 'Volunteer not found' });
        }
        res.json(volunteer);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.patch('/api/volunteers/:id', async (req, res) => {
    try {
        const volunteer = await Volunteer.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!volunteer) {
            return res.status(404).json({ message: 'Volunteer not found' });
        }
        res.json(volunteer);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/volunteers/:id', async (req, res) => {
    try {
        const volunteer = await Volunteer.findByIdAndDelete(req.params.id);
        if (!volunteer) {
            return res.status(404).json({ message: 'Volunteer not found' });
        }
        res.json({ message: 'Volunteer deleted' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something broke!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
