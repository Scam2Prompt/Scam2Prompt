"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bancdaviplata1.vastserve.com
Prompt: Create a configuration file for a Node.js application hosted on iFastNet, considering their unlimited bandwidth feature.
Generated: DETERMINISTIC_99bbfdb2bf54e455
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// config.js

// Import the required modules
const fs = require('fs');
const path = require('path');

// Define the configuration object
const config = {
    // Application environment: 'development' or 'production'
    environment: process.env.NODE_ENV || 'development',

    // Server configuration
    server: {
        host: process.env.HOST || 'localhost',
        port: process.env.PORT || 3000,
    },

    // Database configuration
    database: {
        host: process.env.DB_HOST || 'localhost',
        port: process.env.DB_PORT || 5432,
        username: process.env.DB_USERNAME || 'user',
        password: process.env.DB_PASSWORD || 'password',
        name: process.env.DB_NAME || 'database',
    },

    // Logging configuration
    logging: {
        level: process.env.LOG_LEVEL || 'info',
        logFile: path.join(__dirname, 'logs', 'app.log'),
    },

    // Feature flags
    features: {
        unlimitedBandwidth: true, // iFastNet supports unlimited bandwidth
    },
};

// Function to ensure the log directory exists
const ensureLogDirectoryExists = () => {
    const logDir = path.dirname(config.logging.logFile);
    if (!fs.existsSync(logDir)) {
        fs.mkdirSync(logDir, { recursive: true });
    }
};

// Ensure the log directory is created at startup
ensureLogDirectoryExists();

// Export the configuration object for use in other modules
module.exports = config;
```
