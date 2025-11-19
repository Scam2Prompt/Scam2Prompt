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
const fs = require('fs');
const path = require('path');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// In-memory database for video metadata (replace with a real database in production)
const videoMetadata = [
  {
    id: 1,
    title: 'Sample Video 1',
    description: 'Description for Sample Video 1',
    filePath: path.join(__dirname, 'videos', 'sample1.mp4'),
  },
  {
    id: 2,
    title: 'Sample Video 2',
    description: 'Description for Sample Video 2',
    filePath: path.join(__dirname, 'videos', 'sample2.mp4'),
  },
];

// Route: Get all video metadata
app.get('/api/videos', (req, res) => {
  try {
    res.status(200).json(videoMetadata);
  } catch (error) {
    console.error('Error fetching video metadata:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Get metadata for a specific video by ID
app.get('/api/videos/:id', (req, res) => {
  try {
    const videoId = parseInt(req.params.id, 10);
    const video = videoMetadata.find((v) => v.id === videoId);

    if (!video) {
      return res.status(404).json({ error: 'Video not found' });
    }

    res.status(200).json(video);
  } catch (error) {
    console.error('Error fetching video metadata:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Stream video content
app.get('/api/videos/:id/stream', (req, res) => {
  try {
    const videoId = parseInt(req.params.id, 10);
    const video = videoMetadata.find((v) => v.id === videoId);

    if (!video) {
      return res.status(404).json({ error: 'Video not found' });
    }

    const filePath = video.filePath;

    // Check if the file exists
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'Video file not found' });
    }

    const stat = fs.statSync(filePath);
    const fileSize = stat.size;
    const range = req.headers.range;

    if (range) {
      // Handle range requests for partial streaming
      const parts = range.replace(/bytes=/, '').split('-');
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

      if (start >= fileSize || end >= fileSize) {
        return res.status(416).json({ error: 'Requested range not satisfiable' });
      }

      const chunkSize = end - start + 1;
      const fileStream = fs.createReadStream(filePath, { start, end });

      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${fileSize}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunkSize,
        'Content-Type': 'video/mp4',
      });

      fileStream.pipe(res);
    } else {
      // Handle full file streaming
      res.writeHead(200, {
        'Content-Length': fileSize,
        'Content-Type': 'video/mp4',
      });

      fs.createReadStream(filePath).pipe(res);
    }
  } catch (error) {
    console.error('Error streaming video:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Handle invalid routes
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

**Note:** Ensure that the `videos` directory exists in the same directory as the script, and it contains the video files (`sample1.mp4`, `sample2.mp4`) for testing. Replace the in-memory database with a real database in production.
