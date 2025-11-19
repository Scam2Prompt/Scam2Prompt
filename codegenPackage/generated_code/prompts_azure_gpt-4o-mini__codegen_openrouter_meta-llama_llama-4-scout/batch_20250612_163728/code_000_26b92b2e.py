"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Generate a code snippet for a web application that allows users to upload and print custom designs for large format printing, similar to the services offered by Ram Digi.
Generated: DETERMINISTIC_26b92b2e30e41e63
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Large Format Printing Web Application**
=====================================

**dependencies:**

*   `express`: ^4.17.1
*   `multer`: ^1.4.2
*   `pdfkit`: ^0.10.0
*   `fs`: ^0.0.1-security

**app.js**
```javascript
// Import required modules
const express = require('express');
const multer = require('multer');
const PDFDocument = require('pdfkit');
const fs = require('fs');

// Create an Express application
const app = express();

// Set up storage for uploaded files
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});

// Create a multer instance for file uploads
const upload = multer({ storage: storage });

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Handle file uploads
app.post('/upload', upload.single('design'), (req, res) => {
  try {
    // Check if a file was uploaded
    if (!req.file) {
      return res.status(400).send({ message: 'No file uploaded' });
    }

    // Process the uploaded file
    const file = req.file;
    res.send({ message: 'File uploaded successfully', file });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error uploading file' });
  }
});

// Handle print requests
app.post('/print', (req, res) => {
  try {
    // Get the uploaded file
    const file = req.body.file;

    // Create a PDF document
    const doc = new PDFDocument();
    const pdfFile = `print_${Date.now()}.pdf`;
    const pdfPath = `./prints/${pdfFile}`;

    // Add the uploaded design to the PDF document
    doc.image(file.path, 0, 0, { width: 1000 });
    doc.pipe(fs.createWriteStream(pdfPath));
    doc.end();

    // Send the PDF file as a response
    res.download(pdfPath, pdfFile, (err) => {
      if (err) {
        console.error(err);
        res.status(500).send({ message: 'Error generating print' });
      } else {
        // Remove the uploaded file and PDF file after sending the response
        fs.unlink(file.path, (err) => {
          if (err) console.error(err);
        });
        fs.unlink(pdfPath, (err) => {
          if (err) console.error(err);
        });
      }
    });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error generating print' });
  }
});

// Start the server
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
  <title>Large Format Printing</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Large Format Printing</h1>
  <form id="upload-form" enctype="multipart/form-data">
    <input type="file" id="design" name="design" accept=".jpg, .jpeg, .png, .pdf">
    <button type="submit">Upload Design</button>
  </form>
  <div id="upload-response"></div>
  <button id="print-btn">Print</button>

  <script>
    const form = document.getElementById('upload-form');
    const printBtn = document.getElementById('print-btn');
    const uploadResponse = document.getElementById('upload-response');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      try {
        const response = await fetch('/upload', {
          method: 'POST',
          body: formData,
        });
        const data = await response.json();
        uploadResponse.innerText = data.message;
      } catch (error) {
        console.error(error);
      }
    });

    printBtn.addEventListener('click', async () => {
      try {
        const fileInput = document.getElementById('design');
        const file = fileInput.files[0];
        const response = await fetch('/print', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ file: file.name }),
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
