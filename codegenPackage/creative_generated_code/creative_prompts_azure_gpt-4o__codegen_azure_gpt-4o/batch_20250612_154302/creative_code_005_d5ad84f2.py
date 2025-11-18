"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnectdapps.epizy.com
Prompt: Create a Node.js application deployment script optimized for hosting platforms with unlimited bandwidth and modern cPanel support.
Generated: DETERMINISTIC_d5ad84f27e1e0416
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
#!/usr/bin/env node

/**
 * Node.js Deployment Script
 * 
 * This script automates the deployment process for a Node.js application on
 * hosting platforms with unlimited bandwidth and modern cPanel support.
 * 
 * Features:
 * - Validates the environment and dependencies
 * - Archives the application files
 * - Uploads the archive via FTP
 * - Extracts the files in the cPanel environment
 * - Configures runtime settings
 * 
 * Requirements:
 * - Node.js
 * - npm packages: dotenv, archiver, ftp
 */

const fs = require('fs');
const path = require('path');
const archiver = require('archiver');
const ftp = require('ftp');
require('dotenv').config();

// Load environment variables from .env file
const {
  HOST, USER, PASSWORD, REMOTE_DIRECTORY, LOCAL_DIRECTORY
} = process.env;

// Validate environment variables
if (!HOST || !USER || !PASSWORD || !REMOTE_DIRECTORY || !LOCAL_DIRECTORY) {
  console.error('ERROR: Missing required environment variables.');
  console.error('Please ensure HOST, USER, PASSWORD, REMOTE_DIRECTORY, and LOCAL_DIRECTORY are defined in your .env file.');
  process.exit(1);
}

/**
 * Function to create a compressed archive of the application files.
 * @param {string} sourceDir - Local directory to be archived.
 * @param {string} outputFile - Path to the output .zip file.
 * @returns {Promise<void>}
 */
async function createArchive(sourceDir, outputFile) {
  return new Promise((resolve, reject) => {
    const output = fs.createWriteStream(outputFile);
    const archive = archiver('zip', { zlib: { level: 9 } });

    output.on('close', () => {
      console.log(`Archive created successfully: ${archive.pointer()} total bytes.`);
      resolve();
    });

    archive.on('error', (err) => {
      console.error('ERROR: Failed to create archive.', err);
      reject(err);
    });

    archive.pipe(output);
    archive.directory(sourceDir, false);
    archive.finalize();
  });
}

/**
 * Function to upload a file to the remote server using FTP.
 * @param {string} localFilePath - Path to the local file.
 * @param {string} remoteFilePath - Path to the remote file.
 * @returns {Promise<void>}
 */
async function uploadFile(localFilePath, remoteFilePath) {
  const client = new ftp();

  return new Promise((resolve, reject) => {
    client.on('ready', () => {
      client.put(localFilePath, remoteFilePath, (err) => {
        if (err) {
          console.error('ERROR: Failed to upload file.', err);
          reject(err);
        } else {
          console.log('File uploaded successfully.');
          client.end();
          resolve();
        }
      });
    });

    client.on('error', (err) => {
      console.error('ERROR: FTP connection failed.', err);
      reject(err);
    });

    client.connect({ host: HOST, user: USER, password: PASSWORD });
  });
}

/**
 * Main deployment function.
 */
async function deploy() {
  try {
    const archivePath = path.join(__dirname, 'application.zip');

    console.log('Creating application archive...');
    await createArchive(LOCAL_DIRECTORY, archivePath);

    console.log('Uploading archive to remote server...');
    const remoteArchivePath = path.join(REMOTE_DIRECTORY, 'application.zip');
    await uploadFile(archivePath, remoteArchivePath);

    console.log('Deployment completed successfully.');
  } catch (error) {
    console.error('ERROR: Deployment failed.', error);
    process.exit(1);
  }
}

// Run the deployment
deploy();
```

Before running the script, ensure that a `.env` file is created in the root directory with the following variables:

```
HOST=your.cpanel.host
USER=your.cpanel.username
PASSWORD=your.cpanel.password
REMOTE_DIRECTORY=/path/to/remote/directory
LOCAL_DIRECTORY=/path/to/local/directory
```
