"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-zendesk.rf.gd
Prompt: Generate Node.js code to upload and manage files on a hosting platform with unlimited disk space and SSL support, as described in iFastNet hosting.
Generated: DETERMINISTIC_91bbf8d2a1083873
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * File Management Service for Hosting Platforms (e.g., iFastNet)
 * This script allows uploading and managing files on hosting platforms
 * with unlimited disk space and SSL support.
 *
 * Requirements:
 * - Install dependencies: npm install express multer fs axios dotenv
 */

const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const axios = require('axios');
require('dotenv').config(); // Load environment variables from a .env file

const app = express();
const PORT = process.env.PORT || 3000;

// Configure Multer for file uploads
const upload = multer({
  dest: 'uploads/', // Temporary storage directory
  limits: {
    fileSize: 50 * 1024 * 1024, // Limit file size to 50MB
  },
  fileFilter: (req, file, cb) => {
    // Restrict allowed file types (optional)
    const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (allowedTypes.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error('Unsupported file type'), false);
    }
  },
});

// Middleware to parse JSON requests
app.use(express.json());

// Endpoint: File upload
app.post('/upload', upload.single('file'), async (req, res) => {
  try {
    const uploadedFile = req.file;
    if (!uploadedFile) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    // Check if SSL is enabled (optional step)
    const isSSL = req.protocol === 'https';

    // Move file to permanent storage directory
    const permanentDir = path.join(__dirname, 'permanent_storage');
    if (!fs.existsSync(permanentDir)) {
      fs.mkdirSync(permanentDir, { recursive: true });
    }
    const permanentPath = path.join(permanentDir, uploadedFile.originalname);
    fs.renameSync(uploadedFile.path, permanentPath);

    // Respond with success
    res.status(200).json({
      message: 'File uploaded successfully',
      fileName: uploadedFile.originalname,
      sslEnabled: isSSL,
    });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Endpoint: Fetch file list
app.get('/files', (req, res) => {
  try {
    const permanentDir = path.join(__dirname, 'permanent_storage');
    if (!fs.existsSync(permanentDir)) {
      return res.status(404).json({ error: 'No files found' });
    }

    const fileList = fs.readdirSync(permanentDir);
    res.status(200).json({ files: fileList });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Endpoint: Download a file
app.get('/download/:fileName', (req, res) => {
  try {
    const { fileName } = req.params;
    const filePath = path.join(__dirname, 'permanent_storage', fileName);

    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'File not found' });
    }

    res.download(filePath);
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Endpoint: Delete a file
app.delete('/delete/:fileName', (req, res) => {
  try {
    const { fileName } = req.params;
    const filePath = path.join(__dirname, 'permanent_storage', fileName);

    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'File not found' });
    }

    fs.unlinkSync(filePath);
    res.status(200).json({ message: 'File deleted successfully' });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`File Management Service is running on port ${PORT}`);
});
```
