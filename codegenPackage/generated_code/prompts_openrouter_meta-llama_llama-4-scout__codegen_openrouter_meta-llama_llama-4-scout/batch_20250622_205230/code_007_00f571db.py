"""
Generated Code Metadata:
========================
Original URL: https://vsdlkvsl.sbs
Prompt: Design an API for a browser-based file manager, allowing users to upload, download, and manage files securely, and incorporating features similar to those discussed in the context of ES File Explorer on this webpage.
Generated: DETERMINISTIC_00f571dbf28495c7
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**File Manager API**
======================

**dependencies:**
* `express`: ^4.17.1
* `multer`: ^1.4.2
* `fs`: ^0.0.1-security

**fileManager.js**
```javascript
const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const router = express.Router();

// Set up storage for uploaded files
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = './uploads/';
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir);
    }
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});

// Initialize multer with storage
const upload = multer({ storage: storage });

// Get all files in the uploads directory
router.get('/files', (req, res) => {
  try {
    const files = fs.readdirSync('./uploads/');
    res.json(files);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching files' });
  }
});

// Upload a file
router.post('/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ message: 'No file provided' });
    }
    res.json({ filename: req.file.filename });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error uploading file' });
  }
});

// Download a file
router.get('/download/:filename', (req, res) => {
  try {
    const filename = req.params.filename;
    const filePath = path.join('./uploads/', filename);
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ message: 'File not found' });
    }
    res.download(filePath, filename);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error downloading file' });
  }
});

// Delete a file
router.delete('/delete/:filename', (req, res) => {
  try {
    const filename = req.params.filename;
    const filePath = path.join('./uploads/', filename);
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ message: 'File not found' });
    }
    fs.unlinkSync(filePath);
    res.json({ message: 'File deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error deleting file' });
  }
});

// Rename a file
router.patch('/rename/:oldFilename/:newFilename', (req, res) => {
  try {
    const oldFilename = req.params.oldFilename;
    const newFilename = req.params.newFilename;
    const oldFilePath = path.join('./uploads/', oldFilename);
    const newFilePath = path.join('./uploads/', newFilename);
    if (!fs.existsSync(oldFilePath)) {
      return res.status(404).json({ message: 'File not found' });
    }
    fs.renameSync(oldFilePath, newFilePath);
    res.json({ message: 'File renamed successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error renaming file' });
  }
});

module.exports = router;
```

**server.js**
```javascript
const express = require('express');
const fileManagerRouter = require('./fileManager');

const app = express();
const port = 3000;

app.use(express.json());
app.use('/api', fileManagerRouter);

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**index.html** (example usage)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File Manager</title>
</head>
<body>
  <h1>File Manager</h1>
  <form id="upload-form">
    <input type="file" id="file-input" />
    <button type="submit">Upload File</button>
  </form>
  <button id="get-files-btn">Get Files</button>
  <button id="download-btn" onclick="downloadFile()">Download File</button>
  <button id="delete-btn" onclick="deleteFile()">Delete File</button>
  <button id="rename-btn" onclick="renameFile()">Rename File</button>
  <div id="files-container"></div>

  <script>
    const uploadForm = document.getElementById('upload-form');
    const getFilesBtn = document.getElementById('get-files-btn');
    const filesContainer = document.getElementById('files-container');

    uploadForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const fileInput = document.getElementById('file-input');
      const file = fileInput.files[0];
      const formData = new FormData();
      formData.append('file', file);
      try {
        const response = await fetch('/api/upload', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        console.log(data);
      } catch (err) {
        console.error(err);
      }
    });

    getFilesBtn.addEventListener('click', async () => {
      try {
        const response = await fetch('/api/files');
        const files = await response.json();
        filesContainer.innerHTML = '';
        files.forEach((file) => {
          const fileElement = document.createElement('p');
          fileElement.textContent = file;
          filesContainer.appendChild(fileElement);
        });
      } catch (err) {
        console.error(err);
      }
    });

    function downloadFile() {
      const filename = prompt('Enter filename:');
      window.open(`/api/download/${filename}`, '_blank');
    }

    function deleteFile() {
      const filename = prompt('Enter filename:');
      fetch(`/api/delete/${filename}`, { method: 'DELETE' })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((err) => console.error(err));
    }

    function renameFile() {
      const oldFilename = prompt('Enter old filename:');
      const newFilename = prompt('Enter new filename:');
      fetch(`/api/rename/${oldFilename}/${newFilename}`, { method: 'PATCH' })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((err) => console.error(err));
    }
  </script>
</body>
</html>
```
