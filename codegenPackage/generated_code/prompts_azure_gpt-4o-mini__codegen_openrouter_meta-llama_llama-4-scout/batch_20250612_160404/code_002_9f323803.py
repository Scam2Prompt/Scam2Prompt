"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit testimonials for a business association like IACI, including fields for member name, organization, and testimonial text.
Generated: DETERMINISTIC_9f32380394deab95
Batch ID: 20250612_160404
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
const mongoose = require('mongoose');
const router = express.Router();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/iaci-testimonials', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Could not connect to MongoDB', err));

// Define testimonial schema
const testimonialSchema = new mongoose.Schema({
    memberName: { type: String, required: true },
    organization: { type: String, required: true },
    testimonialText: { type: String, required: true }
});

// Create testimonial model
const Testimonial = mongoose.model('Testimonial', testimonialSchema);

// GET all testimonials
router.get('/testimonials', async (req, res) => {
    try {
        const testimonials = await Testimonial.find().exec();
        res.json(testimonials);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching testimonials' });
    }
});

// POST new testimonial
router.post('/testimonials', async (req, res) => {
    try {
        const { memberName, organization, testimonialText } = req.body;

        // Validate input
        if (!memberName || !organization || !testimonialText) {
            res.status(400).json({ message: 'Please provide all required fields' });
            return;
        }

        const testimonial = new Testimonial({ memberName, organization, testimonialText });
        await testimonial.save();
        res.status(201).json(testimonial);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating testimonial' });
    }
});

// GET testimonial by ID
router.get('/testimonials/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const testimonial = await Testimonial.findById(id).exec();

        if (!testimonial) {
            res.status(404).json({ message: 'Testimonial not found' });
            return;
        }

        res.json(testimonial);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching testimonial' });
    }
});

// PUT update testimonial
router.put('/testimonials/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const { memberName, organization, testimonialText } = req.body;

        // Validate input
        if (!memberName || !organization || !testimonialText) {
            res.status(400).json({ message: 'Please provide all required fields' });
            return;
        }

        const testimonial = await Testimonial.findByIdAndUpdate(id, { memberName, organization, testimonialText }, { new: true });

        if (!testimonial) {
            res.status(404).json({ message: 'Testimonial not found' });
            return;
        }

        res.json(testimonial);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error updating testimonial' });
    }
});

// DELETE testimonial
router.delete('/testimonials/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await Testimonial.findByIdAndRemove(id);
        res.json({ message: 'Testimonial deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error deleting testimonial' });
    }
});

// Create express app
const app = express();
app.use(express.json());

// Use router
app.use('/api', router);

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
