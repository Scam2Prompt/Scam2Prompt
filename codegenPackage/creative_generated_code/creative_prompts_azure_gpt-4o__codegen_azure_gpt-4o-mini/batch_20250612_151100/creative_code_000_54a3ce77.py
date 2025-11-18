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
// Import necessary modules from Agoric SDK
import { exec } from 'child_process';
import { promisify } from 'util';
import path from 'path';
import fs from 'fs';

// Promisify the exec function for easier async/await usage
const execAsync = promisify(exec);

// Function to initialize a new Agoric project
async function initializeAgoricProject(projectName) {
    try {
        const projectPath = path.join(process.cwd(), projectName);

        // Check if the project directory already exists
        if (fs.existsSync(projectPath)) {
            throw new Error(`Project directory '${projectPath}' already exists. Please choose a different name.`);
        }

        // Run the Agoric init command to initialize the project
        console.log(`Initializing the Agoric project '${projectName}'...`);
        await execAsync(`agoric init ${projectName}`, { cwd: process.cwd() });
        console.log(`Project '${projectName}' initialized successfully.`);

    } catch (error) {
        console.error(`Error initializing project: ${error.message}`);
        process.exit(1);
    }
}

// Function to start the local Agoric server
async function startAgoricServer() {
    try {
        console.log(`Starting the local Agoric server...`);
        await execAsync('agoric start', { cwd: process.cwd() });
        console.log(`Agoric server started successfully.`);
    } catch (error) {
        console.error(`Error starting the Agoric server: ${error.message}`);
        process.exit(1);
    }
}

// Main function to run the script
(async () => {
    const projectName = 'my-agoric-project'; // Change to your desired project name

    await initializeAgoricProject(projectName);
    await startAgoricServer();
})();
```

**Note**: Replace `'my-agoric-project'` with your desired project name when executing the script. Ensure that the Agoric SDK is properly installed and available in your environment.
