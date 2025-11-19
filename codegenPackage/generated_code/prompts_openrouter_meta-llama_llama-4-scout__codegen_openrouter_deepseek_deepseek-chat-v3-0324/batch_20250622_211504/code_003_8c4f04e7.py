"""
Generated Code Metadata:
========================
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: Generate a Node.js application deployment script for iFastNet Web Hosting, considering the service's support for Node.js and unlimited resources.
Generated: DETERMINISTIC_8c4f04e745281229
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const readline = require('readline');

// Configuration constants
const DEPLOY_DIR = '/path/to/your/deployment/directory'; // Update this to your iFastNet deployment directory
const NODE_VERSION = '16'; // Update to your required Node.js version
const APP_ENTRY_POINT = 'app.js'; // Update to your app's entry point file
const LOG_FILE = 'deploy.log';

// Initialize readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Logging function
const log = (message) => {
  const timestamp = new Date().toISOString();
  const logMessage = `[${timestamp}] ${message}\n`;
  fs.appendFileSync(LOG_FILE, logMessage);
  console.log(message);
};

// Error handling function
const handleError = (error) => {
  log(`ERROR: ${error.message}`);
  process.exit(1);
};

// Check if deployment directory exists
const checkDeploymentDir = () => {
  try {
    if (!fs.existsSync(DEPLOY_DIR)) {
      throw new Error(`Deployment directory ${DEPLOY_DIR} does not exist`);
    }
    log(`Verified deployment directory: ${DEPLOY_DIR}`);
  } catch (error) {
    handleError(error);
  }
};

// Install dependencies
const installDependencies = () => {
  return new Promise((resolve, reject) => {
    log('Installing dependencies...');
    exec(`cd ${DEPLOY_DIR} && npm install --production`, (error, stdout, stderr) => {
      if (error) {
        reject(new Error(`Dependency installation failed: ${stderr}`));
        return;
      }
      log('Dependencies installed successfully');
      resolve();
    });
  });
};

// Set Node.js version
const setNodeVersion = () => {
  return new Promise((resolve, reject) => {
    log(`Setting Node.js version to ${NODE_VERSION}...`);
    exec(`cd ${DEPLOY_DIR} && nvm use ${NODE_VERSION}`, (error, stdout, stderr) => {
      if (error) {
        reject(new Error(`Failed to set Node.js version: ${stderr}`));
        return;
      }
      log(`Node.js version set to ${NODE_VERSION}`);
      resolve();
    });
  });
};

// Restart application
const restartApplication = () => {
  return new Promise((resolve, reject) => {
    log('Restarting application...');
    exec(`cd ${DEPLOY_DIR} && pm2 restart ${APP_ENTRY_POINT}`, (error, stdout, stderr) => {
      if (error) {
        reject(new Error(`Failed to restart application: ${stderr}`));
        return;
      }
      log('Application restarted successfully');
      resolve();
    });
  });
};

// Main deployment function
const deploy = async () => {
  try {
    log('Starting deployment process...');
    
    // Verify deployment directory
    checkDeploymentDir();
    
    // Set Node.js version
    await setNodeVersion();
    
    // Install dependencies
    await installDependencies();
    
    // Restart application
    await restartApplication();
    
    log('Deployment completed successfully');
  } catch (error) {
    handleError(error);
  } finally {
    rl.close();
  }
};

// Confirm deployment with user
rl.question('Are you sure you want to deploy? (yes/no) ', (answer) => {
  if (answer.toLowerCase() === 'yes') {
    deploy();
  } else {
    log('Deployment cancelled by user');
    rl.close();
  }
});

// Handle process termination
process.on('SIGINT', () => {
  log('Process terminated by user');
  rl.close();
  process.exit();
});
```
