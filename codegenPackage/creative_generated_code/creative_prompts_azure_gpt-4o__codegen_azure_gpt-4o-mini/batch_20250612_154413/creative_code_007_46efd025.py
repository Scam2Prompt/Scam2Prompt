"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Write a Node.js script to configure a hosting environment that supports multiple programming languages, including Python and PHP, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_46efd02524ff9da5
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Define the configuration options for different programming languages
const config = {
    pythonVersion: '3.8', // specify the desired Python version
    phpVersion: '7.4',    // specify the desired PHP version
    webRoot: '/var/www/html', // root directory for web files
};

// Function to install Python
function installPython(version) {
    return new Promise((resolve, reject) => {
        console.log(`Installing Python ${version}...`);
        exec(`sudo apt-get install -y python${version}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error installing Python: ${stderr}`);
                return reject(error);
            }
            console.log(`Python ${version} installed successfully.`);
            resolve(stdout);
        });
    });
}

// Function to install PHP
function installPHP(version) {
    return new Promise((resolve, reject) => {
        console.log(`Installing PHP ${version}...`);
        exec(`sudo apt-get install -y php${version}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error installing PHP: ${stderr}`);
                return reject(error);
            }
            console.log(`PHP ${version} installed successfully.`);
            resolve(stdout);
        });
    });
}

// Function to configure web server
function configureWebServer() {
    return new Promise((resolve, reject) => {
        console.log('Configuring web server...');
        const serverConfig = `
        <VirtualHost *:80>
            DocumentRoot ${config.webRoot}
            <Directory ${config.webRoot}>
                AllowOverride All
                Require all granted
            </Directory>
        </VirtualHost>
        `;
        const configFilePath = path.join('/etc/apache2/sites-available/', '000-default.conf');

        fs.writeFile(configFilePath, serverConfig, (err) => {
            if (err) {
                console.error(`Error writing server configuration: ${err}`);
                return reject(err);
            }
            console.log('Web server configuration updated successfully.');
            resolve();
        });
    });
}

// Main function to orchestrate the installation and configuration
async function setupHostingEnvironment() {
    try {
        await installPython(config.pythonVersion);
        await installPHP(config.phpVersion);
        await configureWebServer();
        console.log('Hosting environment setup completed successfully.');
    } catch (error) {
        console.error('Failed to set up hosting environment:', error);
    }
}

// Execute the setup function
setupHostingEnvironment();
```
