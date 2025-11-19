"""
Generated Code Metadata:
========================
Original URL: https://sonic-explorer.skavel.cz
Prompt: Create a web application using JavaScript that leverages Sonic Explorer's features for real-time audio visualization.
Generated: DETERMINISTIC_df3016fcbc4ad47b
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import express from 'express';
import http from 'http';
import WebSocket from 'ws';
import { SonicExplorer } from 'sonic-explorer';

// Create an Express application
const app = express();

// Create an HTTP server
const server = http.createServer(app);

// Create a WebSocket server
const wss = new WebSocket.Server({ server });

// Initialize Sonic Explorer
const sonicExplorer = new SonicExplorer({
  // Configuration options
  sampleRate: 44100,
  bufferSize: 1024,
});

// Define a function to handle WebSocket connections
function handleConnection(ws) {
  // Handle incoming messages
  ws.on('message', (message) => {
    try {
      // Parse the incoming message
      const data = JSON.parse(message);

      // Handle different types of messages
      switch (data.type) {
        case 'start':
          // Start the audio visualization
          startVisualization(ws);
          break;
        case 'stop':
          // Stop the audio visualization
          stopVisualization();
          break;
        default:
          console.log('Unknown message type');
      }
    } catch (error) {
      console.error('Error handling message:', error);
    }
  });

  // Handle errors
  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });

  // Handle disconnections
  ws.on('close', () => {
    console.log('WebSocket connection closed');
  });
}

// Define a function to start the audio visualization
function startVisualization(ws) {
  // Initialize the audio context
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream) => {
      // Create a MediaStreamAudioProcessorNode
      const audioContext = new AudioContext();
      const processor = audioContext.createScriptProcessor(1024, 1, 1);

      // Connect the processor to the stream
      stream.connect(audioContext.destination);

      // Define the processor's callback function
      processor.onaudioprocess = (event) => {
        // Get the audio data
        const data = event.inputBuffer.getChannelData(0);

        // Analyze the audio data using Sonic Explorer
        sonicExplorer.analyze(data);

        // Send the visualization data to the client
        const visualizationData = sonicExplorer.getVisualizationData();
        ws.send(JSON.stringify({
          type: 'visualization',
          data: visualizationData,
        }));
      };

      // Start the processor
      processor.connect(audioContext.destination);
    })
    .catch((error) => {
      console.error('Error starting audio visualization:', error);
    });
}

// Define a function to stop the audio visualization
function stopVisualization() {
  // Stop the audio context
  sonicExplorer.stop();
}

// Handle WebSocket connections
wss.on('connection', handleConnection);

// Serve static files
app.use(express.static('public'));

// Start the server
const port = 8080;
server.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sonic Explorer Visualization</title>
  <style>
    /* Add some basic styling */
    body {
      margin: 0;
      background-color: #f0f0f0;
    }
    #visualization {
      width: 800px;
      height: 600px;
      border: 1px solid #ccc;
      margin: 20px auto;
    }
  </style>
</head>
<body>
  <div id="visualization"></div>
  <script>
    // Establish a WebSocket connection
    const ws = new WebSocket('ws://localhost:8080');

    // Handle incoming messages
    ws.onmessage = (event) => {
      try {
        // Parse the incoming message
        const data = JSON.parse(event.data);

        // Handle different types of messages
        switch (data.type) {
          case 'visualization':
            // Update the visualization
            updateVisualization(data.data);
            break;
          default:
            console.log('Unknown message type');
        }
      } catch (error) {
        console.error('Error handling message:', error);
      }
    };

    // Define a function to update the visualization
    function updateVisualization(data) {
      // Use a library like D3.js or Canvas to render the visualization
      const visualizationElement = document.getElementById('visualization');
      const canvas = document.createElement('canvas');
      canvas.width = 800;
      canvas.height = 600;
      const ctx = canvas.getContext('2d');

      // Render the visualization
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.beginPath();
      ctx.moveTo(0, canvas.height / 2);
      for (let i = 0; i < data.length; i++) {
        ctx.lineTo(i * 2, canvas.height / 2 - data[i] * 100);
      }
      ctx.stroke();

      // Add the canvas to the visualization element
      visualizationElement.innerHTML = '';
      visualizationElement.appendChild(canvas);
    }

    // Send a message to start the audio visualization
    ws.send(JSON.stringify({ type: 'start' }));
  </script>
</body>
</html>
```
