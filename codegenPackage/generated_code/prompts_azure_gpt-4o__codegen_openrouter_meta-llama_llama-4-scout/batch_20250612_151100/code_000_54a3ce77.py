"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script using the Agoric SDK to initialize a new project and start the local Agoric server, referencing the `agoric init` and `agoric start` commands described in the documentation.
Generated: DETERMINISTIC_54a3ce776d71f099
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
#!/usr/bin/env node

/**
 * Initialize a new Agoric project and start the local Agoric server.
 * 
 * This script uses the Agoric SDK to create a new project and start the local server.
 * 
 * @author [Your Name]
 */

// Import required modules
const { execSync } = require('child_process');
const { existsSync } = require('fs');
const path = require('path');

// Define constants
const AGORIC_INIT_CMD = 'agoric init';
const AGORIC_START_CMD = 'agoric start';

/**
 * Initialize a new Agoric project.
 * 
 * @param {string} projectName - The name of the project to initialize.
 */
function initProject(projectName) {
    try {
        // Check if project directory already exists
        if (existsSync(projectName)) {
            console.error(`Project directory ${projectName} already exists.`);
            process.exit(1);
        }

        // Run agoric init command
        console.log(`Initializing new project ${projectName}...`);
        execSync(`${AGORIC_INIT_CMD} ${projectName}`, { stdio: 'inherit' });
        console.log(`Project ${projectName} initialized successfully.`);
    } catch (error) {
        console.error(`Error initializing project: ${error.message}`);
        process.exit(1);
    }
}

/**
 * Start the local Agoric server.
 * 
 * @param {string} projectName - The name of the project to start the server for.
 */
function startServer(projectName) {
    try {
        // Change into project directory
        process.chdir(path.join(process.cwd(), projectName));

        // Run agoric start command
        console.log('Starting local Agoric server...');
        execSync(AGORIC_START_CMD, { stdio: 'inherit' });
        console.log('Local Agoric server started successfully.');
    } catch (error) {
        console.error(`Error starting server: ${error.message}`);
        process.exit(1);
    }
}

// Main function
function main() {
    // Get project name from command line arguments
    const projectName = process.argv[2];

    if (!projectName) {
        console.error('Please provide a project name.');
        process.exit(1);
    }

    // Initialize project
    initProject(projectName);

    // Start server
    startServer(projectName);
}

// Run main function
main();
```
