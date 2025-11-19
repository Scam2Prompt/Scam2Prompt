"""
Generated Code Metadata:
========================
Original URL: https://rectify-noder.epizy.com
Prompt: Generate a Node.js application configuration file for a web hosting service that offers Node.js support and unlimited disk space.
Generated: DETERMINISTIC_df5e56df48f6993b
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Node.js Application Configuration File
 * 
 * This configuration file is designed for a web hosting service with Node.js support.
 * It includes settings for server, database, security, and environment variables.
 */

require('dotenv').config(); // Load environment variables from .env file

const config = {
  // Server Configuration
  server: {
    port: process.env.PORT || 3000,
    host: process.env.HOST || '0.0.0.0',
    environment: process.env.NODE_ENV || 'development',
    clusterMode: process.env.CLUSTER_MODE === 'true' || false,
    maxUploadSize: process.env.MAX_UPLOAD_SIZE || '50mb'
  },

  // Database Configuration
  database: {
    url: process.env.DATABASE_URL || 'mongodb://localhost:27017/appdb',
    options: {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      poolSize: process.env.DB_POOL_SIZE || 10,
      connectTimeoutMS: process.env.DB_CONNECT_TIMEOUT || 5000
    }
  },

  // Security Configuration
  security: {
    cors: {
      origin: process.env.CORS_ORIGIN || '*',
      methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
      allowedHeaders: ['Content-Type', 'Authorization']
    },
    rateLimit: {
      windowMs: process.env.RATE_LIMIT_WINDOW || 15 * 60 * 1000, // 15 minutes
      max: process.env.RATE_LIMIT_MAX || 100
    },
    helmet: {
      enabled: true
    },
    csrf: {
      enabled: process.env.CSRF_ENABLED === 'true' || false
    }
  },

  // Logging Configuration
  logging: {
    level: process.env.LOG_LEVEL || 'info',
    file: {
      enabled: process.env.LOG_FILE_ENABLED === 'true' || false,
      path: process.env.LOG_FILE_PATH || './logs/app.log'
    },
    console: {
      enabled: true
    }
  },

  // Email Configuration
  email: {
    service: process.env.EMAIL_SERVICE || 'sendgrid',
    host: process.env.EMAIL_HOST || 'smtp.sendgrid.net',
    port: process.env.EMAIL_PORT || 587,
    secure: process.env.EMAIL_SECURE === 'true' || false,
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASSWORD
    }
  },

  // Session Configuration
  session: {
    secret: process.env.SESSION_SECRET || 'your-secret-key',
    resave: false,
    saveUninitialized: false,
    cookie: {
      secure: process.env.NODE_ENV === 'production',
      maxAge: 24 * 60 * 60 * 1000 // 24 hours
    }
  },

  // Storage Configuration (Unlimited disk space)
  storage: {
    tempDir: process.env.TEMP_DIR || './temp',
    uploadDir: process.env.UPLOAD_DIR || './uploads',
    maxFileCount: process.env.MAX_FILE_COUNT || 100
  }
};

// Validate required environment variables
const requiredEnvVars = ['DATABASE_URL', 'SESSION_SECRET'];
requiredEnvVars.forEach((envVar) => {
  if (!process.env[envVar] && config.server.environment === 'production') {
    throw new Error(`Missing required environment variable: ${envVar}`);
  }
});

module.exports = config;
```
