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
// Node.js configuration for iFastNet hosting platform

// Import required modules
const fs = require('fs');
const path = require('path');

// Define configuration class
class NodeJsConfig {
  /**
   * Constructor for NodeJsConfig
   * @param {string} nodeVersion - Version of Node.js to use
   * @param {string} documentRoot - Document root for the application
   * @param {string} serverFile - Server file (e.g., server.js)
   */
  constructor(nodeVersion, documentRoot, serverFile) {
    this.nodeVersion = nodeVersion;
    this.documentRoot = documentRoot;
    this.serverFile = serverFile;
  }

  /**
   * Create a new Node.js configuration file
   * @returns {Promise<void>}
   */
  async createConfigFile() {
    try {
      // Define configuration file content
      const configContent = `{
        "node_version": "${this.nodeVersion}",
        "document_root": "${this.documentRoot}",
        "server_file": "${this.serverFile}"
      }`;

      // Write configuration file to disk
      const configFilePath = path.join(__dirname, 'nodejs.config.json');
      fs.writeFileSync(configFilePath, configContent);

      console.log(`Node.js configuration file created at ${configFilePath}`);
    } catch (error) {
      console.error('Error creating Node.js configuration file:', error);
      throw error;
    }
  }

  /**
   * Validate Node.js version
   * @returns {boolean}
   */
  validateNodeVersion() {
    // List of supported Node.js versions on iFastNet
    const supportedVersions = ['14.17.0', '16.15.0', '18.12.0'];

    // Check if the specified Node.js version is supported
    return supportedVersions.includes(this.nodeVersion);
  }

  /**
   * Validate document root
   * @returns {boolean}
   */
  validateDocumentRoot() {
    // Check if the document root exists
    return fs.existsSync(this.documentRoot);
  }

  /**
   * Validate server file
   * @returns {boolean}
   */
  validateServerFile() {
    // Check if the server file exists
    return fs.existsSync(path.join(this.documentRoot, this.serverFile));
  }

  /**
   * Validate configuration
   * @returns {boolean}
   */
  validateConfig() {
    return this.validateNodeVersion() && this.validateDocumentRoot() && this.validateServerFile();
  }
}

// Example usage
async function main() {
  try {
    // Create a new Node.js configuration
    const config = new NodeJsConfig('16.15.0', '/path/to/document/root', 'server.js');

    // Validate configuration
    if (!config.validateConfig()) {
      console.error('Invalid configuration');
      return;
    }

    // Create a new Node.js configuration file
    await config.createConfigFile();
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
