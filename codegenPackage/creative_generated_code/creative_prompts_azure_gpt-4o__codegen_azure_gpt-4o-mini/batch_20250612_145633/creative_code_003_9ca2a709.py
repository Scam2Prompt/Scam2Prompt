"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: Create a deployment configuration for a JavaScript-based web app using the Azure App Service Deployment Center.
Generated: DETERMINISTIC_9ca2a7092496546a
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// deployment-config.js

/**
 * Azure App Service Deployment Center Configuration for a JavaScript Web App
 * This script automates the deployment process to Azure App Service.
 */

const { exec } = require('child_process');
const path = require('path');

/**
 * Function to deploy the application to Azure App Service
 * @param {string} appName - The name of the Azure App Service
 * @param {string} resourceGroup - The resource group of the App Service
 * @param {string} sourcePath - The path of the source code to deploy
 */
async function deployToAzure(appName, resourceGroup, sourcePath) {
    try {
        // Change directory to the source path
        process.chdir(sourcePath);

        // Build the application (Assuming a typical Node.js app)
        await runCommand('npm install');
        await runCommand('npm run build');

        // Deploy the application using Azure CLI
        await runCommand(`az webapp up --name ${appName} --resource-group ${resourceGroup} --location "East US" --sku F1`);
        
        console.log(`Deployment successful for ${appName}.`);
    } catch (error) {
        console.error('Deployment failed:', error.message);
        process.exit(1); // Exit with failure code
    }
}

/**
 * Function to run shell commands and return a promise
 * @param {string} command - The shell command to execute
 * @returns {Promise<void>} - Resolves if command is successful, rejects if there is an error
 */
function runCommand(command) {
    return new Promise((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
            if (error) {
                reject(`Error: ${stderr || stdout}`);
            } else {
                console.log(stdout);
                resolve();
            }
        });
    });
}

// Example usage
const appName = process.argv[2]; // Get app name from command line arguments
const resourceGroup = process.argv[3]; // Get resource group from command line arguments
const sourcePath = path.resolve(process.argv[4] || '.'); // Get source path or default to current directory

if (!appName || !resourceGroup) {
    console.error('Usage: node deployment-config.js <appName> <resourceGroup> [sourcePath]');
    process.exit(1);
}

// Start deployment
deployToAzure(appName, resourceGroup, sourcePath);
```

### Instructions for Running
1. Ensure you have Azure CLI installed and logged in.
2. Save the above code to a file named `deployment-config.js`.
3. Run the script using Node.js with the following command:
   ```
   node deployment-config.js <appName> <resourceGroup> [sourcePath]
   ```
   Replace `<appName>` and `<resourceGroup>` with your Azure App Service name and resource group, respectively. The `sourcePath` is optional and defaults to the current directory.
