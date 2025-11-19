"""
Generated Code Metadata:
========================
Original URL: https://brettsol.io
Prompt: Generate a JavaScript code to display real-time server status and network metrics, similar to the one used on https://brettsol.io.
Generated: DETERMINISTIC_358a36add4238d7c
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const os = require('os');
const si = require('systeminformation');
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

// Set up interval for updating metrics
const UPDATE_INTERVAL = 1000; // 1 second

// Initialize metrics object
let metrics = {
  cpu: {},
  memory: {},
  network: {},
  uptime: 0,
};

// Function to update metrics
async function updateMetrics() {
  try {
    // Get CPU metrics
    const cpuData = await si.currentLoad();
    metrics.cpu = {
      load: cpuData.currentload,
      cores: os.cpus().length,
    };

    // Get memory metrics
    const memoryData = await si.mem();
    metrics.memory = {
      total: memoryData.total,
      used: memoryData.used,
      percentage: memoryData.used / memoryData.total * 100,
    };

    // Get network metrics
    const networkData = await si.network();
    metrics.network = {
      rx: networkData.rx,
      tx: networkData.tx,
    };

    // Get uptime
    metrics.uptime = process.uptime();
  } catch (error) {
    console.error('Error updating metrics:', error);
  }
}

// Update metrics initially
updateMetrics();

// Set up interval for updating metrics
setInterval(updateMetrics, UPDATE_INTERVAL);

// Set up Express to serve static files
app.use(express.static('public'));

// Set up Socket.IO to emit metrics
io.on('connection', (socket) => {
  console.log('Client connected');

  // Emit initial metrics
  socket.emit('metrics', metrics);

  // Emit updated metrics at interval
  const intervalId = setInterval(() => {
    socket.emit('metrics', metrics);
  }, UPDATE_INTERVAL);

  // Clear interval on client disconnection
  socket.on('disconnect', () => {
    console.log('Client disconnected');
    clearInterval(intervalId);
  });
});

// Start server
const PORT = 3000;
http.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).send('Internal Server Error');
});
```

```javascript
// Client-side code (in public/index.html)
// Import Socket.IO client library
const socket = io();

// Get elements to display metrics
const cpuLoadElement = document.getElementById('cpu-load');
const cpuCoresElement = document.getElementById('cpu-cores');
const memoryTotalElement = document.getElementById('memory-total');
const memoryUsedElement = document.getElementById('memory-used');
const memoryPercentageElement = document.getElementById('memory-percentage');
const networkRxElement = document.getElementById('network-rx');
const networkTxElement = document.getElementById('network-tx');
const uptimeElement = document.getElementById('uptime');

// Listen for metrics updates
socket.on('metrics', (metrics) => {
  // Update CPU metrics
  cpuLoadElement.textContent = `${metrics.cpu.load}%`;
  cpuCoresElement.textContent = metrics.cpu.cores;

  // Update memory metrics
  memoryTotalElement.textContent = formatBytes(metrics.memory.total);
  memoryUsedElement.textContent = formatBytes(metrics.memory.used);
  memoryPercentageElement.textContent = `${metrics.memory.percentage.toFixed(2)}%`;

  // Update network metrics
  networkRxElement.textContent = formatBytes(metrics.network.rx);
  networkTxElement.textContent = formatBytes(metrics.network.tx);

  // Update uptime
  uptimeElement.textContent = formatUptime(metrics.uptime);
});

// Function to format bytes
function formatBytes(bytes) {
  if (bytes < 1024) {
    return `${bytes} B`;
  } else if (bytes < 1024 ** 2) {
    return `${(bytes / 1024).toFixed(2)} KB`;
  } else if (bytes < 1024 ** 3) {
    return `${(bytes / 1024 ** 2).toFixed(2)} MB`;
  } else {
    return `${(bytes / 1024 ** 3).toFixed(2)} GB`;
  }
}

// Function to format uptime
function formatUptime(uptime) {
  const seconds = Math.floor(uptime % 60);
  const minutes = Math.floor((uptime / 60) % 60);
  const hours = Math.floor((uptime / 3600) % 24);
  const days = Math.floor(uptime / 86400);

  return `${days}d ${hours}h ${minutes}m ${seconds}s`;
}
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Server Status</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .metrics {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }
    .metric {
      margin: 20px;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Server Status</h1>
  <div class="metrics">
    <div class="metric">
      <h2>CPU</h2>
      <p>Load: <span id="cpu-load"></span></p>
      <p>Cores: <span id="cpu-cores"></span></p>
    </div>
    <div class="metric">
      <h2>Memory</h2>
      <p>Total: <span id="memory-total"></span></p>
      <p>Used: <span id="memory-used"></span></p>
      <p>Percentage: <span id="memory-percentage"></span></p>
    </div>
    <div class="metric">
      <h2>Network</h2>
      <p>RX: <span id="network-rx"></span></p>
      <p>TX: <span id="network-tx"></span></p>
    </div>
    <div class="metric">
      <h2>Uptime</h2>
      <p><span id="uptime"></span></p>
    </div>
  </div>

  <script src="/socket.io/socket.io.js"></script>
  <script src="script.js"></script>
</body>
</html>
```
