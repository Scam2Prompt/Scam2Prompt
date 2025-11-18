"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bncdgndkdfrjkxicebgmgjnguqfdgekftxkingptwqqeb.66ghz.com
Prompt: Generate code to configure Node.js support on a hosting service that offers unlimited bandwidth and modern cPanel, similar to iFastNet's hosting features.
Generated: DETERMINISTIC_e7d940ea6f535fe5
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const fs = require('fs');
const path = require('path');

// Configuration settings for Node.js app
const configureNodeApp = (appName, rootDir, port) => {
  try {
    // Validate input parameters
    if (!appName || !rootDir || !port) {
      throw new Error('Invalid input parameters. Provide appName, rootDir, and port.');
    }

    // Ensure the root directory exists
    if (!fs.existsSync(rootDir)) {
      throw new Error(`Root directory "${rootDir}" does not exist.`);
    }

    // Paths for application files
    const appDir = path.join(rootDir, appName);
    const appFile = path.join(appDir, 'app.js');
    const packageFile = path.join(appDir, 'package.json');

    // Ensure the app directory is created
    if (!fs.existsSync(appDir)) {
      fs.mkdirSync(appDir, { recursive: true });
    }

    // Create the app.js file
    const appContent = `
      const express = require('express');
      const app = express();

      // Basic route for app testing
      app.get('/', (req, res) => {
        res.send('Hello World! Your Node.js app is running!');
      });

      // Start listening on the specified port
      app.listen(${port}, () => {
        console.log(\`Node.js app "${appName}" is running on port ${port}\`);
      });
    `;

    fs.writeFileSync(appFile, appContent.trim());

    // Create the package.json file
    const packageJson = {
      name: appName,
      version: '1.0.0',
      description: 'A Node.js app configured for hosting service',
      main: 'app.js',
      scripts: {
        start: `node app.js`
      },
      dependencies: {
        express: '^4.17.1'
      }
    };

    fs.writeFileSync(packageFile, JSON.stringify(packageJson, null, 2));

    console.log(`Node.js app "${appName}" has been successfully configured.`);
    console.log(`App directory: ${appDir}`);
    console.log(`Run "npm install" in the app directory to install dependencies.`);
  } catch (error) {
    console.error(`Error configuring Node.js app: ${error.message}`);
  }
};

// Example usage
configureNodeApp('my-node-app', '/var/www/my-node-apps', 3000);
```
