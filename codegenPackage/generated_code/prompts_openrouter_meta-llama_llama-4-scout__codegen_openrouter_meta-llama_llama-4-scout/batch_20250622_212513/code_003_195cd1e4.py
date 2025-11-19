"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Create a RESTful API using Node.js to manage shoe inventory, including endpoints for sapatos femininos and sapatos masculinos.
Generated: DETERMINISTIC_195cd1e4e152d0ca
Batch ID: 20250622_212513
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
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost/shoe-inventory', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for Sapatos Femininos
const femininoSchema = new mongoose.Schema({
    name: String,
    size: String,
    color: String,
    quantity: Number
});

// Define schema for Sapatos Masculinos
const masculinoSchema = new mongoose.Schema({
    name: String,
    size: String,
    color: String,
    quantity: Number
});

// Create models for Sapatos Femininos and Sapatos Masculinos
const Feminino = mongoose.model('Feminino', femininoSchema);
const Masculino = mongoose.model('Masculino', masculinoSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to get all Sapatos Femininos
app.get('/sapatos-femininos', async (req, res) => {
    try {
        const sapatos = await Feminino.find();
        res.json(sapatos);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching Sapatos Femininos' });
    }
});

// Endpoint to get all Sapatos Masculinos
app.get('/sapatos-masculinos', async (req, res) => {
    try {
        const sapatos = await Masculino.find();
        res.json(sapatos);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching Sapatos Masculinos' });
    }
});

// Endpoint to create a new Sapatos Femininos
app.post('/sapatos-femininos', async (req, res) => {
    try {
        const sapato = new Feminino(req.body);
        await sapato.save();
        res.json(sapato);
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Error creating Sapatos Femininos' });
    }
});

// Endpoint to create a new Sapatos Masculinos
app.post('/sapatos-masculinos', async (req, res) => {
    try {
        const sapato = new Masculino(req.body);
        await sapato.save();
        res.json(sapato);
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Error creating Sapatos Masculinos' });
    }
});

// Endpoint to get a Sapatos Femininos by ID
app.get('/sapatos-femininos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const sapato = await Feminino.findById(id);
        if (!sapato) {
            res.status(404).json({ message: 'Sapatos Femininos not found' });
        } else {
            res.json(sapato);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching Sapatos Femininos' });
    }
});

// Endpoint to get a Sapatos Masculinos by ID
app.get('/sapatos-masculinos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const sapato = await Masculino.findById(id);
        if (!sapato) {
            res.status(404).json({ message: 'Sapatos Masculinos not found' });
        } else {
            res.json(sapato);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching Sapatos Masculinos' });
    }
});

// Endpoint to update a Sapatos Femininos
app.put('/sapatos-femininos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const sapato = await Feminino.findByIdAndUpdate(id, req.body, { new: true });
        if (!sapato) {
            res.status(404).json({ message: 'Sapatos Femininos not found' });
        } else {
            res.json(sapato);
        }
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Error updating Sapatos Femininos' });
    }
});

// Endpoint to update a Sapatos Masculinos
app.put('/sapatos-masculinos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const sapato = await Masculino.findByIdAndUpdate(id, req.body, { new: true });
        if (!sapato) {
            res.status(404).json({ message: 'Sapatos Masculinos not found' });
        } else {
            res.json(sapato);
        }
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Error updating Sapatos Masculinos' });
    }
});

// Endpoint to delete a Sapatos Femininos
app.delete('/sapatos-femininos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await Feminino.findByIdAndRemove(id);
        res.json({ message: 'Sapatos Femininos deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(404).json({ message: 'Sapatos Femininos not found' });
    }
});

// Endpoint to delete a Sapatos Masculinos
app.delete('/sapatos-masculinos/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await Masculino.findByIdAndRemove(id);
        res.json({ message: 'Sapatos Masculinos deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(404).json({ message: 'Sapatos Masculinos not found' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
