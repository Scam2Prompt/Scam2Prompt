"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Create a Node.js application that takes advantage of iFastNet's unlimited bandwidth and disk space.
Generated: DETERMINISTIC_4cdfb9293102682b
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**iFastNet Node.js Application**
=====================================

**package.json**
```json
{
  "name": "ifastnet-app",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "multer": "^1.4.2"
  }
}
```

**app.js**
```javascript
// Import required modules
const express = require('express');
const multer = require('multer');
const path = require('path');

// Create Express app
const app = express();

// Set up storage for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  }
});

// Create multer instance
const upload = multer({ storage });

// Serve static files from ./public
app.use(express.static(path.join(__dirname, 'public')));

// Serve file uploads
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// API endpoint for file uploads
app.post('/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).send({ message: 'No file uploaded' });
    }

    res.send({ message: 'File uploaded successfully', file: req.file });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error uploading file' });
  }
});

// API endpoint for listing uploaded files
app.get('/files', (req, res) => {
  try {
    const files = [];
    const dir = path.join(__dirname, 'uploads');

    fs.readdirSync(dir).forEach(file => {
      files.push(file);
    });

    res.send(files);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error listing files' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>iFastNet Node.js Application</title>
</head>
<body>
  <h1>iFastNet Node.js Application</h1>
  <form id="upload-form" enctype="multipart/form-data">
    <input type="file" id="file" name="file">
    <button type="submit">Upload File</button>
  </form>

  <script>
    const form = document.getElementById('upload-form');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const fileInput = document.getElementById('file');
      const file = fileInput.files[0];

      if (!file) {
        alert('Please select a file to upload');
        return;
      }

      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch('/upload', {
          method: 'POST',
          body: formData
        });

        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    });
  </script>
</body>
</html>
```

**fs.js (optional)**
```javascript
const fs = require('fs');
const path = require('path');

// Create uploads directory if it doesn't exist
const dir = path.join(__dirname, 'uploads');

if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir);
}
```
