"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write a script to test hot module replacement (HMR) updates in a Next.js DApp, as demonstrated in the Dapp Starter kit.
Generated: DETERMINISTIC_37adb8c8d80624d7
Batch ID: 20250612_150426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/dappstarter/dappstarter": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: test-hmr.js
// Purpose: Script to test Hot Module Replacement (HMR) updates in a Next.js DApp
// Assumes you are using the Dapp Starter Kit (https://github.com/dappstarter/dappstarter)

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Configurations
const NEXT_JS_APP_DIR = path.resolve(__dirname, './dapp'); // Path to your Next.js DApp directory
const TEST_FILE_PATH = path.join(NEXT_JS_APP_DIR, 'pages', 'index.js'); // File to be modified for HMR test
const BACKUP_FILE_PATH = `${TEST_FILE_PATH}.backup`; // Backup file to restore original state

/**
 * Perform HMR test
 * 1. Start the development server
 * 2. Modify a file to trigger HMR
 * 3. Watch for changes in browser or server-side logs
 */
async function runHMRTest() {
  try {
    console.log('Starting HMR test...');

    // Step 1: Backup the original file
    if (!fs.existsSync(BACKUP_FILE_PATH)) {
      fs.copyFileSync(TEST_FILE_PATH, BACKUP_FILE_PATH);
      console.log('Backup created for index.js file.');
    }

    // Step 2: Start the Next.js development server
    console.log('Starting Next.js dev server...');
    const devServer = exec('npm run dev', { cwd: NEXT_JS_APP_DIR });

    // Log server output to the console
    devServer.stdout.on('data', (data) => {
      console.log(`[Dev Server]: ${data}`);
    });

    devServer.stderr.on('data', (err) => {
      console.error(`[Dev Server Error]: ${err}`);
    });

    // Step 3: Modify the index.js file to trigger HMR
    setTimeout(() => {
      console.log('Modifying index.js file to trigger HMR...');
      const timestamp = new Date().toISOString();
      const newContent = `
        // This is a test change for HMR
        export default function Home() {
          return (
            <div>
              <h1>Hello, DApp Starter Kit! Updated at ${timestamp}</h1>
            </div>
          );
        }
      `;

      fs.writeFileSync(TEST_FILE_PATH, newContent);
      console.log('index.js file updated. Check browser or logs for HMR updates.');

      // Step 4: Restore the original file after a short delay
      setTimeout(() => {
        console.log('Restoring original index.js file...');
        if (fs.existsSync(BACKUP_FILE_PATH)) {
          fs.copyFileSync(BACKUP_FILE_PATH, TEST_FILE_PATH);
          fs.unlinkSync(BACKUP_FILE_PATH); // Remove the backup file
          console.log('Original index.js file restored.');
        }

        // Stop the development server
        devServer.kill();
        console.log('HMR test completed.');
      }, 10000); // 10 seconds delay for observation
    }, 5000); // 5 seconds delay to allow server startup
  } catch (err) {
    console.error('An error occurred during the HMR test:', err.message);
  }
}

// Run the HMR test
runHMRTest();
```
