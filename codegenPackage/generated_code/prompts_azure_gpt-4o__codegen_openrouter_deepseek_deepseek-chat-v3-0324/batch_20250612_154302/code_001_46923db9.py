"""
Generated Code Metadata:
========================
Original URL: https://btc5000.epizy.com
Prompt: Generate code to configure Node.js hosting on a platform that offers multiple versions of PHP and Node.js support, as mentioned on iFastNet.
Generated: DETERMINISTIC_46923db9c75de29d
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * Configures Node.js hosting environment based on specified version
 * @param {Object} options - Configuration options
 * @param {string} options.nodeVersion - Desired Node.js version (e.g., '14.17.0')
 * @param {string} options.appRoot - Application root directory
 * @param {string} [options.startScript='start'] - npm start script name
 * @throws {Error} If configuration fails
 */
function configureNodeHosting(options) {
    const { nodeVersion, appRoot, startScript = 'start' } = options;

    // Validate inputs
    if (!nodeVersion || !appRoot) {
        throw new Error('nodeVersion and appRoot are required parameters');
    }

    if (!fs.existsSync(appRoot)) {
        throw new Error(`App root directory does not exist: ${appRoot}`);
    }

    try {
        // Create necessary configuration files
        const packageJsonPath = path.join(appRoot, 'package.json');
        
        // Ensure package.json exists
        if (!fs.existsSync(packageJsonPath)) {
            fs.writeFileSync(packageJsonPath, JSON.stringify({
                name: 'node-app',
                version: '1.0.0',
                scripts: {
                    [startScript]: 'node server.js'
                },
                engines: {
                    node: nodeVersion
                }
            }, null, 2));
        } else {
            // Update existing package.json with node version constraint
            const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
            packageJson.engines = packageJson.engines || {};
            packageJson.engines.node = nodeVersion;
            fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 2));
        }

        // Create .htaccess for Node.js configuration (if using Apache)
        const htaccessPath = path.join(appRoot, '.htaccess');
        const htaccessContent = `
# Node.js configuration
Options +ExecCGI
AddHandler fcgid-script .js

# Set the correct Node.js version
FcgidInitialEnv NODE_PATH ${path.join(appRoot, 'node_modules')}
FcgidInitialEnv NODE_ENV production
FcgidInitialEnv NODE_VERSION ${nodeVersion}

# Point to your Node.js application
FcgidWrapper "/usr/bin/node ${path.join(appRoot, 'server.js')}" virtual
`.trim();

        fs.writeFileSync(htaccessPath, htaccessContent);

        // Create a basic server.js if it doesn't exist
        const serverJsPath = path.join(appRoot, 'server.js');
        if (!fs.existsSync(serverJsPath)) {
            fs.writeFileSync(serverJsPath, `
const http = require('http');
const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello from Node.js\\n');
});

server.listen(port, () => {
    console.log(\`Server running on port \${port}\`);
});
`.trim());
        }

        console.log(`Successfully configured Node.js ${nodeVersion} hosting environment`);
    } catch (error) {
        throw new Error(`Failed to configure Node.js hosting: ${error.message}`);
    }
}

// Example usage:
// configureNodeHosting({
//     nodeVersion: '14.17.0',
//     appRoot: '/path/to/your/app',
//     startScript: 'start'
// });

module.exports = { configureNodeHosting };
```
