"""
Generated Code Metadata:
========================
Original URL: https://christineheart.com
Prompt: Generate a code snippet for a travel blog that integrates Polaroid photo uploads and displays them in a gallery format.
Generated: DETERMINISTIC_5cc6eaf325df115e
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Travel Blog with Polaroid Photo Uploads and Gallery**
=====================================================

**dependencies:**

*   `express`: ^4.17.1
*   `multer`: ^1.4.2
*   `mongodb`: ^3.6.3

**travelBlog.js**
```javascript
// Import required modules
const express = require('express');
const multer = require('multer');
const MongoClient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectId;

// Initialize Express app
const app = express();
app.use(express.json());

// Connect to MongoDB
const mongoUrl = 'mongodb://localhost:27017';
const dbName = 'travelBlog';
let db;

// Initialize Multer for photo uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});

const upload = multer({ storage: storage });

// Connect to MongoDB on app start
MongoClient.connect(mongoUrl, (err, client) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Connected to MongoDB');
    db = client.db(dbName);
  }
});

// API endpoint to upload photo
app.post('/upload', upload.single('photo'), (req, res) => {
  // Check if photo was uploaded
  if (!req.file) {
    return res.status(400).send({ message: 'No photo uploaded' });
  }

  // Save photo to MongoDB
  const photo = {
    filename: req.file.filename,
    uploadedAt: new Date(),
  };

  db.collection('photos').insertOne(photo, (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).send({ message: 'Error uploading photo' });
    }

    res.send({ message: 'Photo uploaded successfully' });
  });
});

// API endpoint to get all photos
app.get('/photos', (req, res) => {
  db.collection('photos')
    .find({})
    .toArray((err, photos) => {
      if (err) {
        console.error(err);
        return res.status(500).send({ message: 'Error fetching photos' });
      }

      res.send(photos);
    });
});

// API endpoint to delete photo by ID
app.delete('/photos/:id', (req, res) => {
  const id = req.params.id;

  db.collection('photos')
    .findOneAndDelete({ _id: new ObjectId(id) }, (err, result) => {
      if (err) {
        console.error(err);
        return res.status(500).send({ message: 'Error deleting photo' });
      }

      if (!result.value) {
        return res.status(404).send({ message: 'Photo not found' });
      }

      res.send({ message: 'Photo deleted successfully' });
    });
});

// Serve static files from uploads directory
app.use('/uploads', express.static('uploads'));

// Serve gallery HTML
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/gallery.html');
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**gallery.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Travel Blog Gallery</title>
  <style>
    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    .photo {
      margin: 10px;
      width: 200px;
      height: 200px;
      background-size: cover;
      background-position: center;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Travel Blog Gallery</h1>
  <form id="upload-form">
    <input type="file" id="photo" name="photo">
    <button type="submit">Upload Photo</button>
  </form>
  <div class="gallery" id="gallery"></div>

  <script>
    // Get photos from API and display in gallery
    fetch('/photos')
      .then(response => response.json())
      .then(photos => {
        const gallery = document.getElementById('gallery');
        photos.forEach(photo => {
          const photoElement = document.createElement('div');
          photoElement.classList.add('photo');
          photoElement.style.backgroundImage = `url('/uploads/${photo.filename}')`;
          gallery.appendChild(photoElement);
        });
      })
      .catch(error => console.error(error));

    // Handle photo upload
    const uploadForm = document.getElementById('upload-form');
    uploadForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const formData = new FormData();
      formData.append('photo', document.getElementById('photo').files[0]);

      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
    });
  </script>
</body>
</html>
```
