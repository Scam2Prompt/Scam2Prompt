"""
Generated Code Metadata:
========================
Original URL: https://kinglol.42web.io
Prompt: Generate Node.js code for deploying a web application on a hosting platform that offers modern cPanel and no daily hit limit, referencing features from iFastNet hosting.
Generated: DETERMINISTIC_425db1f510c2c5a6
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const path = require('path');
const fs = require('fs');
const https = require('https');
const http = require('http');
const helmet = require('helmet');
const compression = require('compression');
const morgan = require('morgan');

// Initialize Express app
const app = express();

// Environment variables setup
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const ENVIRONMENT = process.env.NODE_ENV || 'development';
const SSL_CERT_PATH = process.env.SSL_CERT_PATH || null;
const SSL_KEY_PATH = process.env.SSL_KEY_PATH || null;

// Security middleware
app.use(helmet());
app.use(compression());

// Logging middleware
if (ENVIRONMENT === 'development') {
    app.use(morgan('dev'));
} else {
    // Create a write stream for production logs
    const accessLogStream = fs.createWriteStream(
        path.join(__dirname, 'access.log'),
        { flags: 'a' }
    );
    app.use(morgan('combined', { stream: accessLogStream }));
}

// Static files middleware
app.use(express.static(path.join(__dirname, 'public')));

// Body parsing middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// 404 handler
app.use((req, res) => {
    res.status(404).send('Page not found');
});

// Server setup
let server;
if (SSL_CERT_PATH && SSL_KEY_PATH) {
    const options = {
        cert: fs.readFileSync(SSL_CERT_PATH),
        key: fs.readFileSync(SSL_KEY_PATH)
    };
    server = https.createServer(options, app);
} else {
    server = http.createServer(app);
}

// Start server
server.listen(PORT, () => {
    console.log(`Server running in ${ENVIRONMENT} mode on port ${PORT}`);
});

// Handle unhandled promise rejections
process.on('unhandledRejection', (err) => {
    console.error('Unhandled Rejection:', err);
    process.exit(1);
});

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
    console.error('Uncaught Exception:', err);
    process.exit(1);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    console.log('SIGTERM received. Shutting down gracefully...');
    server.close(() => {
        console.log('Process terminated');
    });
});
```

```json
// package.json
{
  "name": "web-app-deployment",
  "version": "1.0.0",
  "description": "Web application deployment for iFastNet hosting",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "node",
    "express",
    "deployment",
    "iFastNet"
  ],
  "author": "Your Name",
  "license": "ISC",
  "dependencies": {
    "compression": "^1.7.4",
    "dotenv": "^16.0.3",
    "express": "^4.18.2",
    "helmet": "^6.0.1",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.20"
  },
  "engines": {
    "node": ">=14.0.0"
  }
}
```

```env
# .env file
PORT=3000
NODE_ENV=development
# SSL_CERT_PATH=/path/to/cert.pem
# SSL_KEY_PATH=/path/to/key.pem
```
