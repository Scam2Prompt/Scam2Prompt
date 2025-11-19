"""
Generated Code Metadata:
========================
Original URL: https://flyingtogether.website
Prompt: Generate a code snippet for a collaborative application that allows users to work together in real-time, similar to features mentioned on flyingtogether.website.
Generated: DETERMINISTIC_3c19e9fe850f550e
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready code snippet for a real-time collaborative application using WebSockets and Node.js:

```javascript
// server.js - Real-time collaboration server using WebSockets
const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const { v4: uuidv4 } = require('uuid');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Store active documents and their collaborators
const documents = new Map();

// Middleware for logging
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// WebSocket connection handler
wss.on('connection', (ws, req) => {
  const documentId = req.url.split('/')[2] || uuidv4();
  let document = documents.get(documentId);

  if (!document) {
    document = {
      id: documentId,
      content: '',
      collaborators: new Set()
    };
    documents.set(documentId, document);
  }

  // Add user to collaborators
  document.collaborators.add(ws);
  console.log(`New collaborator joined document ${documentId}`);

  // Send current document content to new collaborator
  ws.send(JSON.stringify({
    type: 'init',
    documentId,
    content: document.content
  }));

  // Broadcast to other collaborators about new user
  broadcastToCollaborators(document, ws, {
    type: 'user_joined',
    count: document.collaborators.size
  });

  // Handle incoming messages
  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message);
      
      switch (data.type) {
        case 'edit':
          document.content = data.content;
          broadcastToCollaborators(document, ws, {
            type: 'update',
            content: data.content,
            sender: data.sender
          });
          break;
        
        case 'cursor':
          broadcastToCollaborators(document, ws, {
            type: 'cursor_update',
            position: data.position,
            sender: data.sender
          });
          break;
      }
    } catch (err) {
      console.error('Error processing message:', err);
    }
  });

  // Handle disconnection
  ws.on('close', () => {
    document.collaborators.delete(ws);
    console.log(`Collaborator left document ${documentId}`);

    if (document.collaborators.size === 0) {
      // Clean up empty documents after 5 minutes
      setTimeout(() => {
        if (document.collaborators.size === 0) {
          documents.delete(documentId);
          console.log(`Document ${documentId} removed`);
        }
      }, 300000);
    } else {
      broadcastToCollaborators(document, null, {
        type: 'user_left',
        count: document.collaborators.size
      });
    }
  });

  // Error handling
  ws.on('error', (err) => {
    console.error('WebSocket error:', err);
  });
});

// Helper function to broadcast to all collaborators except sender
function broadcastToCollaborators(document, sender, message) {
  document.collaborators.forEach((client) => {
    if (client !== sender && client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(message));
    }
  });
}

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    documents: documents.size,
    uptime: process.uptime()
  });
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
```

```javascript
// client.js - Real-time collaboration client
class CollaborativeEditor {
  constructor(documentId, userId) {
    this.documentId = documentId;
    this.userId = userId;
    this.socket = new WebSocket(`ws://localhost:3000/document/${documentId}`);
    this.initialize();
  }

  initialize() {
    this.socket.onopen = () => {
      console.log('Connected to collaboration server');
    };

    this.socket.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        
        switch (message.type) {
          case 'init':
            this.onDocumentInit(message.content);
            break;
          
          case 'update':
            this.onDocumentUpdate(message.content, message.sender);
            break;
          
          case 'cursor_update':
            this.onCursorUpdate(message.position, message.sender);
            break;
          
          case 'user_joined':
            this.onUserJoined(message.count);
            break;
          
          case 'user_left':
            this.onUserLeft(message.count);
            break;
        }
      } catch (err) {
        console.error('Error processing server message:', err);
      }
    };

    this.socket.onclose = () => {
      console.log('Disconnected from collaboration server');
      this.onDisconnect();
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.onError(error);
    };
  }

  sendEdit(content) {
    if (this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({
        type: 'edit',
        content,
        sender: this.userId
      }));
    }
  }

  sendCursorPosition(position) {
    if (this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({
        type: 'cursor',
        position,
        sender: this.userId
      }));
    }
  }

  disconnect() {
    this.socket.close();
  }

  // These methods should be implemented by the application
  onDocumentInit(content) {}
  onDocumentUpdate(content, sender) {}
  onCursorUpdate(position, sender) {}
  onUserJoined(count) {}
  onUserLeft(count) {}
  onDisconnect() {}
  onError(error) {}
}

// Example usage:
// const editor = new CollaborativeEditor('doc123', 'user456');
// editor.onDocumentUpdate = (content) => { /* update UI */ };
```

This implementation includes both server and client components for a real-time collaborative editing system with document synchronization, cursor position sharing, and user presence tracking.
