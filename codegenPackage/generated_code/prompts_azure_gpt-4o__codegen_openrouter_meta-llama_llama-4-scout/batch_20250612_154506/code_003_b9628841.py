"""
Generated Code Metadata:
========================
Original URL: https://geoweb.land
Prompt: Generate code to create a shared geospatial experience using Geo Web's framework. Include instructions for enabling JavaScript and handling spatial data.
Generated: DETERMINISTIC_b96288417425cc00
Batch ID: 20250612_154506
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://unpkg.com/leaflet@1.7.1/dist/leaflet.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.openstreetmap.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB for storing geospatial data
mongoose.connect('mongodb://localhost/geospatial', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for geospatial data
const geospatialDataSchema = new mongoose.Schema({
    type: String,
    coordinates: [Number]
}, { collection: 'geospatial_data' });

// Create model for geospatial data
const GeospatialData = mongoose.model('GeospatialData', geospatialDataSchema);

// Enable CORS for cross-origin requests
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Serve static files from the public directory
app.use(express.static('public'));

// Handle GET requests to the root URL
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

// Handle WebSocket connections
io.on('connection', (socket) => {
    console.log('Client connected');

    // Handle new geospatial data from client
    socket.on('new_data', (data) => {
        const geospatialData = new GeospatialData({
            type: data.type,
            coordinates: data.coordinates
        });

        // Save geospatial data to MongoDB
        geospatialData.save((err) => {
            if (err) {
                console.error(err);
                socket.emit('error', 'Failed to save geospatial data');
            } else {
                // Broadcast new geospatial data to all connected clients
                io.emit('new_data', data);
            }
        });
    });

    // Handle client disconnection
    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

// Handle errors
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).send('Internal Server Error');
});

// Start server
const port = 3000;
http.listen(port, () => {
    console.log(`Server started on port ${port}`);
});

// Enable JavaScript in the client-side code (in public/index.html)
// <script src="/socket.io/socket.io.js"></script>
// <script>
//     const socket = io();

//     // Handle new geospatial data from server
//     socket.on('new_data', (data) => {
//         // Update the map with new geospatial data
//         updateMap(data);
//     });

//     // Send new geospatial data to server
//     function sendData(data) {
//         socket.emit('new_data', data);
//     }
// </script>
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shared Geospatial Experience</title>
    <style>
        #map {
            width: 800px;
            height: 600px;
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script src="/socket.io/socket.io.js"></script>
    <script>
        // Create a Leaflet map
        const map = L.map('map').setView([51.505, -0.09], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
            subdomains: ['a', 'b', 'c']
        }).addTo(map);

        // Handle new geospatial data from server
        const socket = io();
        socket.on('new_data', (data) => {
            // Update the map with new geospatial data
            const layer = L.geoJSON(data);
            layer.addTo(map);
        });

        // Send new geospatial data to server
        function sendData(data) {
            socket.emit('new_data', data);
        }

        // Example usage
        const exampleData = {
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [-0.09, 51.505]
            }
        };
        sendData(exampleData);
    </script>
</body>
</html>
```
