"""
Generated Code Metadata:
========================
Original URL: https://dappchainweb.rf.gd
Prompt: Generate a Node.js application setup script optimized for deployment on a hosting platform that supports Node.js and offers unlimited bandwidth, as detailed on iFastNet.
Generated: DETERMINISTIC_eab98a9cfaa19bd4
Batch ID: 20250612_154651
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
const { execSync } = require('child_process');

// Configuration constants
const APP_NAME = 'my-node-app';
const PORT = process.env.PORT || 3000;
const PACKAGE_JSON = {
  name: APP_NAME,
  version: '1.0.0',
  description: 'Node.js application optimized for iFastNet hosting',
  main: 'server.js',
  scripts: {
    start: 'node server.js',
    dev: 'nodemon server.js',
    test: 'jest'
  },
  keywords: [],
  author: '',
  license: 'ISC',
  dependencies: {
    express: '^4.18.2',
    dotenv: '^16.3.1',
    morgan: '^1.10.0',
    cors: '^2.8.5'
  },
  devDependencies: {
    nodemon: '^3.0.2',
    jest: '^29.7.0'
  }
};

// Create project directory
function createProjectDirectory() {
  try {
    if (!fs.existsSync(APP_NAME)) {
      fs.mkdirSync(APP_NAME);
      process.chdir(APP_NAME);
      console.log(`Created project directory: ${APP_NAME}`);
    } else {
      console.error(`Error: Directory ${APP_NAME} already exists.`);
      process.exit(1);
    }
  } catch (err) {
    console.error('Error creating project directory:', err);
    process.exit(1);
  }
}

// Initialize package.json
function initPackageJson() {
  try {
    fs.writeFileSync('package.json', JSON.stringify(PACKAGE_JSON, null, 2));
    console.log('Initialized package.json');
  } catch (err) {
    console.error('Error creating package.json:', err);
    process.exit(1);
  }
}

// Create server.js file
function createServerFile() {
  const serverContent = `const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = process.env.PORT || ${PORT};

// Middleware
app.use(morgan('dev'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Health check endpoint
app.get('/', (req, res) => {
  res.status(200).json({ status: 'ok', message: 'Server is running' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(port, () => {
  console.log(\`Server running on port \${port}\`);
});

module.exports = app;`;

  try {
    fs.writeFileSync('server.js', serverContent);
    console.log('Created server.js');
  } catch (err) {
    console.error('Error creating server.js:', err);
    process.exit(1);
  }
}

// Create .env file
function createEnvFile() {
  const envContent = `PORT=${PORT}
NODE_ENV=development
`;

  try {
    fs.writeFileSync('.env', envContent);
    console.log('Created .env file');
  } catch (err) {
    console.error('Error creating .env file:', err);
    process.exit(1);
  }
}

// Create .gitignore file
function createGitignore() {
  const gitignoreContent = `node_modules/
.env
.DS_Store
npm-debug.log
`;

  try {
    fs.writeFileSync('.gitignore', gitignoreContent);
    console.log('Created .gitignore file');
  } catch (err) {
    console.error('Error creating .gitignore file:', err);
    process.exit(1);
  }
}

// Install dependencies
function installDependencies() {
  try {
    console.log('Installing dependencies...');
    execSync('npm install', { stdio: 'inherit' });
    console.log('Dependencies installed successfully');
  } catch (err) {
    console.error('Error installing dependencies:', err);
    process.exit(1);
  }
}

// Main function
function main() {
  console.log('Setting up Node.js application for iFastNet hosting...');
  
  createProjectDirectory();
  initPackageJson();
  createServerFile();
  createEnvFile();
  createGitignore();
  installDependencies();
  
  console.log('\nSetup completed successfully!');
  console.log('To start the application:');
  console.log(`1. cd ${APP_NAME}`);
  console.log('2. npm start');
}

// Run the setup
main();
```
