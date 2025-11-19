"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flyingtogether.website
Prompt: Generate a code snippet for a collaborative application that allows users to work together in real-time, similar to features mentioned on flyingtogether.website.
Generated: DETERMINISTIC_3c19e9fe850f550e
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready code snippet for a collaborative application using Node.js and Socket.IO. This code enables real-time collaboration by synchronizing text updates across multiple users.

```javascript
// collaborative_app.js

// Importing dependencies
const express = require('express');  // For creating the web server
const http = require('http');       // For HTTP server
const { Server } = require('socket.io'); // For real-time communication

// Initialize Express application
const app = express();
const server = http.createServer(app);
const io = new Server(server); // Initialize Socket.IO server

// Middleware to serve static files and parse JSON data
app.use(express.json());
app.use(express.static('public')); // Serve the frontend from 'public' directory

// Default route for the web application
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Object to store current state of the collaborative document
let documentState = { content: "" };

// Handle Socket.IO connections
io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  // Send the current document state to the newly connected user
  socket.emit('document-update', documentState);

  // Listen for updates from the user
  socket.on('text-update', (data) => {
    // Validate incoming data
    if (typeof data.content === 'string') {
      // Update the document state
      documentState = { content: data.content };

      // Broadcast the updated state to all connected clients
      socket.broadcast.emit('document-update', documentState);
    } else {
      console.error('Invalid data format received:', data);
    }
  });

  // Handle user disconnect
  socket.on('disconnect', () => {
    console.log('A user disconnected:', socket.id);
  });
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// public/index.html
/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Real-Time Collaborative Editor</title>
</head>
<body>
  <h1>Collaborative Document Editor</h1>
  <textarea id="editor" rows="20" cols="80" placeholder="Start typing..."></textarea>

  <script src="/socket.io/socket.io.js"></script>
  <script>
    const socket = io();

    const editor = document.getElementById('editor');

    // Event listener for user input
    editor.addEventListener('input', () => {
      socket.emit('text-update', { content: editor.value });
    });

    // Listen for document updates from the server
    socket.on('document-update', (data) => {
      if (editor.value !== data.content) {
        editor.value = data.content; // Update editor with the latest content
      }
    });
  </script>
</body>
</html>
*/

// Note: Create a folder named 'public' in the same directory as this script, 
// and place the HTML code inside a file called 'index.html' in that folder.
```

This code snippet creates a fully functioning collaborative text editor that allows users to work together in real time.
