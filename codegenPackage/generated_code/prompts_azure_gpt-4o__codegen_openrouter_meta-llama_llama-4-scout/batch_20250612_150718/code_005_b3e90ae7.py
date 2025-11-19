"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Create a script to run your own node for sui.direct and customize its functionality for decentralized version control.
Generated: DETERMINISTIC_b3e90ae7490f7ad3
Batch ID: 20250612_150718
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
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/sui-direct', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for version control data
const versionControlSchema = new mongoose.Schema({
    fileName: String,
    fileContent: String,
    version: Number,
    author: String
});

// Create model for version control data
const VersionControl = mongoose.model('VersionControl', versionControlSchema);

// Middleware to parse JSON requests
app.use(express.json());

// API endpoint to create a new file
app.post('/api/files', async (req, res) => {
    try {
        const { fileName, fileContent, author } = req.body;
        const existingFile = await VersionControl.findOne({ fileName });
        if (existingFile) {
            res.status(400).send({ message: 'File already exists' });
            return;
        }
        const newFile = new VersionControl({ fileName, fileContent, version: 1, author });
        await newFile.save();
        res.send({ message: 'File created successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error creating file' });
    }
});

// API endpoint to update a file
app.put('/api/files/:fileName', async (req, res) => {
    try {
        const { fileName } = req.params;
        const { fileContent, author } = req.body;
        const existingFile = await VersionControl.findOne({ fileName });
        if (!existingFile) {
            res.status(404).send({ message: 'File not found' });
            return;
        }
        const updatedFile = await VersionControl.findByIdAndUpdate(existingFile._id, { fileContent, version: existingFile.version + 1, author }, { new: true });
        res.send({ message: 'File updated successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error updating file' });
    }
});

// API endpoint to get file history
app.get('/api/files/:fileName/history', async (req, res) => {
    try {
        const { fileName } = req.params;
        const fileHistory = await VersionControl.find({ fileName }).sort({ version: 1 });
        res.send(fileHistory);
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error retrieving file history' });
    }
});

// Socket.io event to broadcast file updates
io.on('connection', (socket) => {
    console.log('Client connected');

    // Handle file update event
    socket.on('update-file', async (fileName, fileContent, author) => {
        try {
            const existingFile = await VersionControl.findOne({ fileName });
            if (!existingFile) {
                socket.emit('file-not-found');
                return;
            }
            const updatedFile = await VersionControl.findByIdAndUpdate(existingFile._id, { fileContent, version: existingFile.version + 1, author }, { new: true });
            io.emit('file-updated', updatedFile);
        } catch (err) {
            console.error(err);
            socket.emit('error', 'Error updating file');
        }
    });

    // Handle client disconnection
    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

// Start server
const port = 3000;
http.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
