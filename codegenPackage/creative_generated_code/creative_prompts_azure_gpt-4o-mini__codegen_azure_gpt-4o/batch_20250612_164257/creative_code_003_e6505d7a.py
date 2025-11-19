"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Develop a web application that utilizes Google Drive for file storage and sharing, as mentioned on norion.loan.
Generated: DETERMINISTIC_e6505d7a06b218c4
Batch ID: 20250612_164257
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/drive.file": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready code for a web application using Google Drive API for file storage and sharing. The implementation assumes Node.js for the backend using Express.js for routing, and Google's official `googleapis` library for interacting with Google Drive. It includes comments and follows best practices.

```javascript
// server.js: Main entry point for the web application

const express = require('express');
const multer = require('multer'); // Middleware for handling file uploads
const { google } = require('googleapis');
const path = require('path');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Setup multer for file upload handling
const upload = multer({ dest: 'uploads/' }); // Temporary storage for files

// Google Drive API setup
const SCOPES = ['https://www.googleapis.com/auth/drive.file'];
const auth = new google.auth.GoogleAuth({
  keyFile: path.join(__dirname, 'credentials.json'), // Path to your service account key
  scopes: SCOPES,
});
const drive = google.drive({ version: 'v3', auth });

// Route: Home
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the Google Drive File Storage Application!');
});

// Route: Upload a file to Google Drive
app.post('/upload', upload.single('file'), async (req, res) => {
  try {
    const filePath = req.file.path;
    const fileName = req.file.originalname;

    const fileMetadata = {
      name: fileName, // Name of the file in Google Drive
    };

    const media = {
      mimeType: req.file.mimetype,
      body: require('fs').createReadStream(filePath), // Stream file contents
    };

    const response = await drive.files.create({
      resource: fileMetadata,
      media: media,
      fields: 'id, webViewLink', // Include file ID and sharing link
    });

    // File upload successful, return link
    res.status(201).json({
      message: 'File uploaded successfully',
      fileId: response.data.id,
      webViewLink: response.data.webViewLink,
    });

    // Clean up local file
    require('fs').unlinkSync(filePath);
  } catch (error) {
    console.error('Error uploading file:', error.message);
    res.status(500).json({ error: 'Failed to upload file' });
  }
});

// Route: Share a file on Google Drive
app.post('/share', async (req, res) => {
  try {
    const { fileId, role = 'reader', type = 'anyone' } = req.body; // Default: anyone can read

    await drive.permissions.create({
      fileId,
      resource: {
        role, // 'reader' or 'writer'
        type, // 'user', 'group', 'domain', or 'anyone'
      },
    });

    const file = await drive.files.get({
      fileId,
      fields: 'webViewLink', // Get the sharing link
    });

    res.status(200).json({
      message: 'File shared successfully',
      webViewLink: file.data.webViewLink,
    });
  } catch (error) {
    console.error('Error sharing file:', error.message);
    res.status(500).json({ error: 'Failed to share file' });
  }
});

// Route: List files in Google Drive
app.get('/list-files', async (req, res) => {
  try {
    const response = await drive.files.list({
      fields: 'files(id, name, webViewLink)',
    });

    const files = response.data.files;
    res.status(200).json({
      message: 'Files retrieved successfully',
      files,
    });
  } catch (error) {
    console.error('Error retrieving file list:', error.message);
    res.status(500).json({ error: 'Failed to retrieve file list' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

/*
README:
1. Place your Google service account credentials in a file named `credentials.json` in the root directory.
2. Create a `.env` file in the root directory with the following content:
   PORT=3000
3. Install dependencies using npm:
   npm install express multer googleapis dotenv
4. Start the server:
   node server.js
5. Use an API testing tool (Postman or similar) or a frontend client to interact with the API.
*/
```

This code contains error handling, is well-documented via comments, and is ready for production.
