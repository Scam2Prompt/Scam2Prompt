"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script using the Agoric SDK to initialize a new project and start the local Agoric server, referencing the `agoric init` and `agoric start` commands described in the documentation.
Generated: DETERMINISTIC_54a3ce776d71f099
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
#!/usr/bin/env node

// Import necessary modules
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Utility function to execute shell commands asynchronously
function executeCommand(command, options = {}) {
  return new Promise((resolve, reject) => {
    const process = exec(command, options, (error, stdout, stderr) => {
      if (error) {
        reject(new Error(`Error executing command: ${error.message}\n${stderr}`));
        return;
      }
      resolve(stdout.trim());
    });

    // Pipe output to console for better visibility
    process.stdout.pipe(process.stdout);
    process.stderr.pipe(process.stderr);
  });
}

// Main function to initialize and start an Agoric project
async function main() {
  try {
    console.log('Initializing Agoric project...');

    // Verify the Agoric CLI is installed
    const agoricVersion = await executeCommand('agoric --version');
    console.log(`Agoric CLI Version: ${agoricVersion}`);

    // Define project directory
    const projectDir = path.resolve(process.cwd(), 'agoric-project');
    if (fs.existsSync(projectDir)) {
      throw new Error(`Directory "${projectDir}" already exists. Please choose a different name or delete the existing directory.`);
    }

    // Initialize the Agoric project
    await executeCommand(`agoric init ${projectDir}`);
    console.log('Agoric project initialized successfully.');

    // Change into the project directory
    process.chdir(projectDir);

    // Start the local Agoric server
    console.log('Starting Agoric server...');
    await executeCommand('agoric start --reset');
    console.log('Agoric server started successfully. Ready for development!');
  } catch (error) {
    console.error('An error occurred:', error.message);
    process.exit(1); // Exit with an error code
  }
}

// Execute the main function
main();
```

### Notes:
1. Make sure Node.js and the Agoric CLI are installed on the system before running this script.
2. The script assumes the current working directory is writable and sets up a new project named `agoric-project`. Modify `projectDir` as needed.
