"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://post-customsgovua.infinityfreeapp.com
Prompt: Generate a Node.js application setup script optimized for hosting on iFastNet, ensuring compatibility with multiple versions of Node.js.
Generated: DETERMINISTIC_0ac6083839672e89
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// setup.js
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration for the Node.js application
const config = {
    appName: 'myNodeApp',
    nodeVersions: ['14.x', '16.x', '18.x'], // List of Node.js versions to support
    startScript: 'index.js', // Entry point of the application
    packageJson: {
        name: 'myNodeApp',
        version: '1.0.0',
        main: 'index.js',
        scripts: {
            start: 'node index.js', // Start command for the application
        },
        dependencies: {
            express: '^4.17.1' // Example dependency
        }
    }
};

// Create a package.json file with the predefined configuration
function createPackageJson() {
    const packageJsonPath = path.join(__dirname, 'package.json');
    fs.writeFileSync(packageJsonPath, JSON.stringify(config.packageJson, null, 2), 'utf8');
    console.log('package.json created successfully.');
}

// Install the specified version of Node.js using nvm (Node Version Manager)
function installNodeVersion(version) {
    return new Promise((resolve, reject) => {
        exec(`nvm install ${version}`, (error, stdout, stderr) => {
            if (error) {
                return reject(`Error installing Node.js version ${version}: ${stderr}`);
            }
            console.log(`Node.js version ${version} installed successfully.`);
            resolve();
        });
    });
}

// Set the specified Node.js version as the default
function setNodeVersion(version) {
    return new Promise((resolve, reject) => {
        exec(`nvm use ${version}`, (error, stdout, stderr) => {
            if (error) {
                return reject(`Error setting Node.js version ${version}: ${stderr}`);
            }
            console.log(`Node.js version ${version} set successfully.`);
            resolve();
        });
    });
}

// Install the application dependencies
function installDependencies() {
    return new Promise((resolve, reject) => {
        exec('npm install', (error, stdout, stderr) => {
            if (error) {
                return reject(`Error installing dependencies: ${stderr}`);
            }
            console.log('Dependencies installed successfully.');
            resolve();
        });
    });
}

// Main function to set up the Node.js application
async function setup() {
    try {
        // Create package.json file
        createPackageJson();
        
        // Install each specified Node.js version and set it as default
        for (const version of config.nodeVersions) {
            await installNodeVersion(version);
            await setNodeVersion(version);
        }
        
        // Install project dependencies
        await installDependencies();

        console.log('Node.js application setup completed successfully.');
    } catch (error) {
        console.error('Setup failed:', error);
    }
}

// Start the setup process
setup();
```
