"""
Generated Code Metadata:
========================
Original URL: https://hdadpanaderos.es
Prompt: Develop a RESTful API in Node.js to manage the documentation and hoja informativa for the Hermandad de los Panaderos.
Generated: DETERMINISTIC_554a727aff3fdcfc
Batch ID: 20250622_211614
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory database (for demonstration purposes)
const documents = [];
const hojasInformativas = [];

// Helper function for error handling
const handleError = (res, message, statusCode = 400) => {
  res.status(statusCode).json({ error: message });
};

// Routes for managing "documentation"

// GET all documentation
app.get('/api/documentation', (req, res) => {
  res.status(200).json(documents);
});

// GET a specific documentation by ID
app.get('/api/documentation/:id', (req, res) => {
  const doc = documents.find((d) => d.id === req.params.id);
  if (!doc) {
    return handleError(res, 'Documentation not found', 404);
  }
  res.status(200).json(doc);
});

// POST to create new documentation
app.post('/api/documentation', (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return handleError(res, 'Title and content are required');
  }
  const newDoc = { id: uuidv4(), title, content };
  documents.push(newDoc);
  res.status(201).json(newDoc);
});

// PUT to update existing documentation
app.put('/api/documentation/:id', (req, res) => {
  const { title, content } = req.body;
  const docIndex = documents.findIndex((d) => d.id === req.params.id);
  if (docIndex === -1) {
    return handleError(res, 'Documentation not found', 404);
  }
  if (!title || !content) {
    return handleError(res, 'Title and content are required');
  }
  documents[docIndex] = { ...documents[docIndex], title, content };
  res.status(200).json(documents[docIndex]);
});

// DELETE a specific documentation by ID
app.delete('/api/documentation/:id', (req, res) => {
  const docIndex = documents.findIndex((d) => d.id === req.params.id);
  if (docIndex === -1) {
    return handleError(res, 'Documentation not found', 404);
  }
  const deletedDoc = documents.splice(docIndex, 1);
  res.status(200).json(deletedDoc[0]);
});

// Routes for managing "hoja informativa"

// GET all hojas informativas
app.get('/api/hojas-informativas', (req, res) => {
  res.status(200).json(hojasInformativas);
});

// GET a specific hoja informativa by ID
app.get('/api/hojas-informativas/:id', (req, res) => {
  const hoja = hojasInformativas.find((h) => h.id === req.params.id);
  if (!hoja) {
    return handleError(res, 'Hoja informativa not found', 404);
  }
  res.status(200).json(hoja);
});

// POST to create new hoja informativa
app.post('/api/hojas-informativas', (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return handleError(res, 'Title and content are required');
  }
  const newHoja = { id: uuidv4(), title, content };
  hojasInformativas.push(newHoja);
  res.status(201).json(newHoja);
});

// PUT to update existing hoja informativa
app.put('/api/hojas-informativas/:id', (req, res) => {
  const { title, content } = req.body;
  const hojaIndex = hojasInformativas.findIndex((h) => h.id === req.params.id);
  if (hojaIndex === -1) {
    return handleError(res, 'Hoja informativa not found', 404);
  }
  if (!title || !content) {
    return handleError(res, 'Title and content are required');
  }
  hojasInformativas[hojaIndex] = { ...hojasInformativas[hojaIndex], title, content };
  res.status(200).json(hojasInformativas[hojaIndex]);
});

// DELETE a specific hoja informativa by ID
app.delete('/api/hojas-informativas/:id', (req, res) => {
  const hojaIndex = hojasInformativas.findIndex((h) => h.id === req.params.id);
  if (hojaIndex === -1) {
    return handleError(res, 'Hoja informativa not found', 404);
  }
  const deletedHoja = hojasInformativas.splice(hojaIndex, 1);
  res.status(200).json(deletedHoja[0]);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
