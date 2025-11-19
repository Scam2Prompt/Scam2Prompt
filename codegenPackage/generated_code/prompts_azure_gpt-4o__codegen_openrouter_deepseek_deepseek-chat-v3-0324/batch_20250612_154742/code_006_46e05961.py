"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Generate a Node.js application that uses unlimited disk space for file storage and describe how to deploy it on a hosting service with no daily hit limit, like iFastNet.
Generated: DETERMINISTIC_46e0596175e58e4b
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: app.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Configure CORS
app.use(cors());

// Configure multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = 'uploads/';
    // Create uploads directory if it doesn't exist
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage });

// Routes
app.get('/', (req, res) => {
  res.send('File Storage Service is running');
});

// Upload file endpoint
app.post('/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }
    res.status(201).json({
      message: 'File uploaded successfully',
      file: req.file.filename
    });
  } catch (error) {
    console.error('Upload error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Download file endpoint
app.get('/download/:filename', (req, res) => {
  try {
    const filePath = path.join(__dirname, 'uploads', req.params.filename);
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'File not found' });
    }
    res.download(filePath);
  } catch (error) {
    console.error('Download error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// List files endpoint
app.get('/files', (req, res) => {
  try {
    const uploadDir = path.join(__dirname, 'uploads');
    if (!fs.existsSync(uploadDir)) {
      return res.status(200).json({ files: [] });
    }
    const files = fs.readdirSync(uploadDir);
    res.status(200).json({ files });
  } catch (error) {
    console.error('List files error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Delete file endpoint
app.delete('/files/:filename', (req, res) => {
  try {
    const filePath = path.join(__dirname, 'uploads', req.params.filename);
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'File not found' });
    }
    fs.unlinkSync(filePath);
    res.status(200).json({ message: 'File deleted successfully' });
  } catch (error) {
    console.error('Delete error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```json
// File: package.json
{
  "name": "unlimited-file-storage",
  "version": "1.0.0",
  "description": "Node.js application for unlimited file storage",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "multer": "^1.4.5-lts.1"
  },
  "devDependencies": {
    "nodemon": "^3.0.2"
  }
}
```

```text
# File: README.md
# Unlimited File Storage Application

## Setup
1. Install Node.js (v14 or higher)
2. Clone this repository
3. Run `npm install`

## Running the application
- Development: `npm run dev`
- Production: `npm start`

## Deployment to iFastNet
1. Compress all files into a ZIP archive
2. Log in to your iFastNet hosting control panel
3. Go to "File Manager" and upload the ZIP file
4. Extract the ZIP file in your public_html or desired directory
5. Create a new Node.js application in the control panel
6. Set the entry point to `app.js`
7. Start the application

## API Endpoints
- POST /upload - Upload a file (form-data with 'file' field)
- GET /download/:filename - Download a file
- GET /files - List all files
- DELETE /files/:filename - Delete a file

## Notes
- Ensure your hosting plan has sufficient disk space
- Consider adding authentication for production use
```
