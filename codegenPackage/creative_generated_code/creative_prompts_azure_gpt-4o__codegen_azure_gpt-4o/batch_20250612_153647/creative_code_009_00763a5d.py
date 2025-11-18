"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Write a deployment script for a Next.js-based DApp starter kit that integrates blockchain tools like MetaMask, WalletConnect, and Hardhat.
Generated: DETERMINISTIC_00763a5d168128ad
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// deployment-script.js

/**
 * Deployment script for a Next.js-based DApp starter kit
 * integrating blockchain tools like MetaMask, WalletConnect, and Hardhat.
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Utility function to execute shell commands
function executeCommand(command) {
  try {
    console.log(`Executing: ${command}`);
    const output = execSync(command, { stdio: 'inherit' });
    return output;
  } catch (error) {
    console.error(`Error executing command: ${command}`);
    process.exit(1);
  }
}

// Step 1: Ensure dependencies for the starter kit are installed
function installDependencies() {
  console.log('Installing dependencies...');
  executeCommand('npm install');
}

// Step 2: Set up Hardhat for blockchain development
function setupHardhat() {
  console.log('Setting up Hardhat...');

  // Check if Hardhat config file exists
  const hardhatConfigPath = path.join(process.cwd(), 'hardhat.config.js');
  if (!fs.existsSync(hardhatConfigPath)) {
    console.log('Hardhat is not initialized. Setting it up...');
    executeCommand('npx hardhat init');
  } else {
    console.log('Hardhat is already initialized.');
  }
}

// Step 3: Configure WalletConnect and MetaMask
function configureBlockchainIntegrations() {
  console.log('Configuring blockchain integrations...');
  const envPath = path.join(process.cwd(), '.env');

  // Check if environment file exists
  if (!fs.existsSync(envPath)) {
    console.log('Creating .env file...');
    const envContent = `
NEXT_PUBLIC_INFURA_API_KEY=<Your_Infura_API_Key>
NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID=<Your_WalletConnect_Project_ID>
NEXT_PUBLIC_CHAIN_ID=1
    `;
    fs.writeFileSync(envPath, envContent.trim());
    console.log('Blockchain integrations are successfully configured. Update .env file with actual values.');
  } else {
    console.log('.env file already exists. Ensure it has the correct configurations.');
  }
}

// Step 4: Build the Next.js application
function buildApplication() {
  console.log('Building Next.js application...');
  executeCommand('npm run build');
}

// Step 5: Deploy the application (can integrate with hosting services like Vercel or Netlify)
function deployApplication() {
  console.log('Deploying Application...');

  // For example, deploying to Vercel
  const vercelCommand = 'npx vercel --prod';
  console.log('Deploying via Vercel...');
  executeCommand(vercelCommand);
}

// Main function to execute deployment steps
function main() {
  console.log('Starting deployment script for Next.js DApp starter kit...');
  
  installDependencies();     // Step 1
  setupHardhat();            // Step 2
  configureBlockchainIntegrations(); // Step 3
  buildApplication();        // Step 4
  deployApplication();       // Step 5
  
  console.log('Deployment completed successfully!');
}

// Execute the script
main();
```
