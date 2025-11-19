"""
Generated Code Metadata:
========================
Original URL: https://eth.fanclub.rocks
Prompt: Generate a Node.js application setup script optimized for a hosting service that offers unlimited disk space, free SSL, and Node.js support, as outlined on iFastNet.
Generated: DETERMINISTIC_6a79987fa8dd1cd9
Batch ID: 20250612_151345
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
const https = require('https');
const child_process = require('child_process');

// Configuration
const CONFIG = {
  appName: 'my-node-app',
  port: process.env.PORT || 3000,
  sslEnabled: true,
  dependencies: ['express', 'helmet', 'morgan', 'dotenv'],
  devDependencies: ['nodemon'],
  scripts: {
    start: 'node server.js',
    dev: 'nodemon server.js',
    test: 'echo "Error: no test specified" && exit 1'
  }
};

// Main function
async function setupApplication() {
  try {
    console.log('🚀 Starting Node.js application setup...');

    // Create project directory
    createProjectDirectory();

    // Initialize package.json
    initializePackageJson();

    // Install dependencies
    await installDependencies();

    // Create server.js
    createServerFile();

    // Create .env file
    createEnvFile();

    // Create public directory
    createPublicDirectory();

    console.log('✅ Setup completed successfully!');
    console.log(`👉 Run 'cd ${CONFIG.appName}' then 'npm start' to launch your app`);
  } catch (error) {
    console.error('❌ Error during setup:', error.message);
    process.exit(1);
  }
}

// Helper functions
function createProjectDirectory() {
  const dirPath = path.join(process.cwd(), CONFIG.appName);
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath);
    console.log(`📁 Created project directory: ${CONFIG.appName}`);
  } else {
    throw new Error(`Directory ${CONFIG.appName} already exists`);
  }
  process.chdir(dirPath);
}

function initializePackageJson() {
  const packageJson = {
    name: CONFIG.appName,
    version: '1.0.0',
    description: '',
    main: 'server.js',
    scripts: CONFIG.scripts,
    keywords: [],
    author: '',
    license: 'ISC'
  };

  fs.writeFileSync(
    'package.json',
    JSON.stringify(packageJson, null, 2)
  );
  console.log('📝 Initialized package.json');
}

async function installDependencies() {
  console.log('📦 Installing dependencies...');
  
  await runCommand('npm', ['install', '--save', ...CONFIG.dependencies]);
  await runCommand('npm', ['install', '--save-dev', ...CONFIG.devDependencies]);
  
  console.log('✅ Dependencies installed');
}

function createServerFile() {
  const serverContent = `const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
require('dotenv').config();

const app = express();
const port = process.env.PORT || ${CONFIG.port};

// Middleware
app.use(helmet());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Basic route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Start server
app.listen(port, () => {
  console.log(\`Server running on port \${port}\`);
});`;

  fs.writeFileSync('server.js', serverContent);
  console.log('🖥️  Created server.js');
}

function createEnvFile() {
  const envContent = `PORT=${CONFIG.port}
NODE_ENV=development
# Add other environment variables here`;

  fs.writeFileSync('.env', envContent);
  console.log('🔧 Created .env file');
}

function createPublicDirectory() {
  const publicDir = path.join(process.cwd(), 'public');
  if (!fs.existsSync(publicDir)) {
    fs.mkdirSync(publicDir);
    
    const indexContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${CONFIG.appName}</title>
</head>
<body>
  <h1>Welcome to ${CONFIG.appName}</h1>
  <p>Your Node.js app is running!</p>
</body>
</html>`;
    
    fs.writeFileSync(path.join(publicDir, 'index.html'), indexContent);
    console.log('📂 Created public directory with index.html');
  }
}

function runCommand(command, args) {
  return new Promise((resolve, reject) => {
    const child = child_process.spawn(command, args, { stdio: 'inherit' });
    
    child.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(\`\${command} failed with exit code \${code}\`));
        return;
      }
      resolve();
    });
  });
}

// Run the setup
setupApplication();
```
