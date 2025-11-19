"""
Generated Code Metadata:
========================
Original URL: https://swanchain-airdrop.pages.dev
Prompt: Create a decentralized application on Swan Chain that combines its computing, storage, and CDN capabilities into a seamless user experience.
Generated: DETERMINISTIC_b177ec3a847f893c
Batch ID: 20250612_152439
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://${storageResponse.cid}.ipfs.swanchain.io`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${uploadResponse.cid}.ipfs.swanchain.io`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${cid}.ipfs.swanchain.io`;": {
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
// Import required libraries and SDKs
const { SwanClient } = require('@swanchain/sdk');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

// Initialize Swan Client
const swanClient = new SwanClient({
  apiKey: process.env.SWAN_API_KEY,
  network: 'mainnet' // or 'testnet' for testing
});

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// Upload file to Swan Storage
app.post('/upload', async (req, res) => {
  try {
    if (!req.files || !req.files.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    const file = req.files.file;
    const uploadPath = path.join(__dirname, 'uploads', file.name);

    // Save file temporarily
    await file.mv(uploadPath);

    // Upload to Swan Storage
    const storageResponse = await swanClient.storage.upload(uploadPath, {
      pin: true,
      replication: 3
    });

    // Clean up temp file
    fs.unlinkSync(uploadPath);

    res.status(200).json({
      cid: storageResponse.cid,
      url: `https://${storageResponse.cid}.ipfs.swanchain.io`
    });
  } catch (error) {
    console.error('Upload error:', error);
    res.status(500).json({ error: 'Failed to upload file' });
  }
});

// Compute task using Swan Compute
app.post('/compute', async (req, res) => {
  try {
    const { code, input } = req.body;

    if (!code || !input) {
      return res.status(400).json({ error: 'Missing code or input' });
    }

    const computeResponse = await swanClient.compute.execute({
      code,
      input,
      environment: 'nodejs-18',
      timeout: 300 // seconds
    });

    res.status(200).json(computeResponse);
  } catch (error) {
    console.error('Compute error:', error);
    res.status(500).json({ error: 'Failed to execute computation' });
  }
});

// Serve content via Swan CDN
app.get('/cdn/:cid', async (req, res) => {
  try {
    const { cid } = req.params;
    const cdnUrl = `https://${cid}.ipfs.swanchain.io`;

    // Proxy the request through our server for additional control
    const response = await fetch(cdnUrl);
    const data = await response.text();

    res.status(200).send(data);
  } catch (error) {
    console.error('CDN error:', error);
    res.status(500).json({ error: 'Failed to fetch content' });
  }
});

// Combined workflow example
app.post('/workflow', async (req, res) => {
  try {
    const { file, computeCode } = req.body;

    if (!file || !computeCode) {
      return res.status(400).json({ error: 'Missing file or compute code' });
    }

    // 1. Upload file to storage
    const uploadResponse = await swanClient.storage.upload(file.buffer, {
      pin: true
    });

    // 2. Process file with compute
    const computeResponse = await swanClient.compute.execute({
      code: computeCode,
      input: { cid: uploadResponse.cid },
      environment: 'nodejs-18'
    });

    // 3. Return results with CDN URL
    res.status(200).json({
      storage: uploadResponse,
      compute: computeResponse,
      cdnUrl: `https://${uploadResponse.cid}.ipfs.swanchain.io`
    });
  } catch (error) {
    console.error('Workflow error:', error);
    res.status(500).json({ error: 'Failed to complete workflow' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
  });
});
```
