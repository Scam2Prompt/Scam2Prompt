"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script to modify a Zoe contract in the Agoric SDK, rebuild it using `yarn build`, and restart the local server with `agoric start --reset`.
Generated: DETERMINISTIC_a704b77f72e3b09e
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
import fs from 'fs-extra';
import path from 'path';

// Promisify exec for easier async/await usage
const execAsync = promisify(exec);

// Define the main function to modify the Zoe contract
async function modifyZoeContract() {
    try {
        // Path to the Zoe contract file
        const contractPath = path.join(__dirname, 'path/to/your/zoe/contract.js');

        // Check if the contract file exists
        if (!fs.existsSync(contractPath)) {
            throw new Error(`Contract file not found: ${contractPath}`);
        }

        // Read the current contract code
        let contractCode = await fs.readFile(contractPath, 'utf8');

        // Modify the contract code as needed
        // Example modification: Add a comment or change a function
        contractCode = contractCode.replace('// TODO: Modify this comment', '// Modified contract code');

        // Write the modified code back to the contract file
        await fs.writeFile(contractPath, contractCode, 'utf8');
        console.log('Zoe contract modified successfully.');

        // Build the project using yarn
        await execAsync('yarn build');
        console.log('Project built successfully.');

        // Restart the local server
        await execAsync('agoric start --reset');
        console.log('Local server restarted successfully.');

    } catch (error) {
        // Handle errors gracefully
        console.error('Error modifying Zoe contract:', error.message);
        process.exit(1); // Exit the process with an error code
    }
}

// Call the main function to execute the script
modifyZoeContract();
```

Make sure to replace `'path/to/your/zoe/contract.js'` with the actual path to your Zoe contract file.
