"""
Generated Code Metadata:
========================
Original URL: https://frosty-euler-f63a60.netlify.app
Prompt: How can I use Node.js to create a simple server for streaming video files like "Undisputed 1 2 3 720p In Dual Audio Hindi"?
Generated: DETERMINISTIC_10158aa89383e615
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const VIDEO_DIRECTORY = './videos'; // Directory where video files are stored

// Create HTTP server
const server = http.createServer((req, res) => {
    // Extract requested file name from URL
    const fileName = decodeURIComponent(req.url.slice(1));
    const filePath = path.join(VIDEO_DIRECTORY, fileName);

    // Check if file exists
    fs.stat(filePath, (err, stats) => {
        if (err) {
            if (err.code === 'ENOENT') {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('File not found');
            } else {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Server error');
            }
            return;
        }

        // Check if it's a file
        if (!stats.isFile()) {
            res.writeHead(400, { 'Content-Type': 'text/plain' });
            res.end('Invalid file type');
            return;
        }

        // Get file size
        const fileSize = stats.size;
        const range = req.headers.range;

        if (range) {
            // Parse range header
            const parts = range.replace(/bytes=/, '').split('-');
            const start = parseInt(parts[0], 10);
            const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

            // Validate range
            if (start >= fileSize || end >= fileSize || start > end) {
                res.writeHead(416, { 'Content-Type': 'text/plain' });
                res.end('Requested range not satisfiable');
                return;
            }

            const chunksize = (end - start) + 1;
            const file = fs.createReadStream(filePath, { start, end });
            
            res.writeHead(206, {
                'Content-Range': `bytes ${start}-${end}/${fileSize}`,
                'Accept-Ranges': 'bytes',
                'Content-Length': chunksize,
                'Content-Type': 'video/mp4'
            });

            file.pipe(res);
        } else {
            // Send entire file if no range requested
            res.writeHead(200, {
                'Content-Length': fileSize,
                'Content-Type': 'video/mp4'
            });
            fs.createReadStream(filePath).pipe(res);
        }
    });
});

// Start server
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Video files should be placed in: ${path.resolve(VIDEO_DIRECTORY)}`);
});

// Handle server errors
server.on('error', (err) => {
    console.error('Server error:', err);
});
```
