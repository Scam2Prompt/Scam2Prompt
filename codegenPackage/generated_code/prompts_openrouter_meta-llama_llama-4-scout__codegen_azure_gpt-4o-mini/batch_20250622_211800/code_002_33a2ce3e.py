"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang654879.buzz
Prompt: Develop a Node.js API to manage and stream adult video content, handling user requests and content metadata.
Generated: DETERMINISTIC_33a2ce3e4afd200b
Batch ID: 20250622_211800
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
const multer = require('multer');
const path = require('path');
const fs = require('fs');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/adult_video_content';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for video content
const videoSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    filePath: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for video content
const Video = mongoose.model('Video', videoSchema);

// Configure multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const dir = './uploads';
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir);
        }
        cb(null, dir);
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname)); // Append timestamp to filename
    }
});

const upload = multer({ storage });

// API endpoint to upload a new video
app.post('/api/videos', upload.single('video'), async (req, res) => {
    try {
        const { title, description } = req.body;
        const filePath = req.file.path;

        const newVideo = new Video({ title, description, filePath });
        await newVideo.save();

        res.status(201).json({ message: 'Video uploaded successfully', video: newVideo });
    } catch (error) {
        console.error('Error uploading video:', error);
        res.status(500).json({ message: 'Error uploading video', error: error.message });
    }
});

// API endpoint to get all videos
app.get('/api/videos', async (req, res) => {
    try {
        const videos = await Video.find();
        res.status(200).json(videos);
    } catch (error) {
        console.error('Error fetching videos:', error);
        res.status(500).json({ message: 'Error fetching videos', error: error.message });
    }
});

// API endpoint to stream a video by ID
app.get('/api/videos/:id/stream', async (req, res) => {
    try {
        const video = await Video.findById(req.params.id);
        if (!video) {
            return res.status(404).json({ message: 'Video not found' });
        }

        const filePath = video.filePath;
        const stat = fs.statSync(filePath);
        const fileSize = stat.size;
        const range = req.headers.range;

        if (range) {
            const parts = range.replace(/bytes=/, '').split('-');
            const start = parseInt(parts[0], 10);
            const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

            if (start >= fileSize || end >= fileSize || start > end) {
                return res.status(416).send('Requested range not satisfiable');
            }

            res.writeHead(206, {
                'Content-Range': `bytes ${start}-${end}/${fileSize}`,
                'Accept-Ranges': 'bytes',
                'Content-Length': end - start + 1,
                'Content-Type': 'video/mp4'
            });

            const stream = fs.createReadStream(filePath, { start, end });
            stream.pipe(res);
        } else {
            res.writeHead(200, {
                'Content-Length': fileSize,
                'Content-Type': 'video/mp4'
            });
            fs.createReadStream(filePath).pipe(res);
        }
    } catch (error) {
        console.error('Error streaming video:', error);
        res.status(500).json({ message: 'Error streaming video', error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
