"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: "Create a deployment script for a Next.js Dapp using Hardhat and Web3, with 1-click deployment."
Generated: DETERMINISTIC_5197e51bd67394ec
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
#!/usr/bin/env node

require('dotenv').config();
const { ethers } = require('hardhat');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const CONTRACT_NAME = 'MyDappContract';
const DEPLOYMENT_DIR = path.join(__dirname, '../deployments');
const FRONTEND_DIR = path.join(__dirname, '../frontend');
const CONTRACT_ARTIFACT_PATH = path.join(__dirname, `../artifacts/contracts/${CONTRACT_NAME}.sol/${CONTRACT_NAME}.json`);

// Ensure deployment directory exists
if (!fs.existsSync(DEPLOYMENT_DIR)) {
  fs.mkdirSync(DEPLOYMENT_DIR, { recursive: true });
}

// Deployment function
async function deployContract() {
  try {
    console.log('🚀 Starting deployment...');

    // Compile contracts
    console.log('🔧 Compiling contracts...');
    execSync('npx hardhat compile', { stdio: 'inherit' });

    // Get contract factory
    const ContractFactory = await ethers.getContractFactory(CONTRACT_NAME);
    console.log(`📦 Deploying ${CONTRACT_NAME}...`);

    // Deploy contract
    const contract = await ContractFactory.deploy();
    await contract.deployed();
    console.log(`✅ Contract deployed to: ${contract.address}`);

    // Save deployment info
    const deploymentInfo = {
      network: 'localhost',
      contractName: CONTRACT_NAME,
      address: contract.address,
      abi: JSON.parse(fs.readFileSync(CONTRACT_ARTIFACT_PATH)).abi,
      timestamp: new Date().toISOString()
    };

    const deploymentFile = path.join(DEPLOYMENT_DIR, `${CONTRACT_NAME}.json`);
    fs.writeFileSync(deploymentFile, JSON.stringify(deploymentInfo, null, 2));
    console.log(`📄 Deployment info saved to: ${deploymentFile}`);

    // Update frontend config if exists
    if (fs.existsSync(FRONTEND_DIR)) {
      const frontendConfigPath = path.join(FRONTEND_DIR, 'src', 'contracts', 'contract-address.json');
      const frontendAbiPath = path.join(FRONTEND_DIR, 'src', 'contracts', 'contract-abi.json');
      
      fs.writeFileSync(frontendConfigPath, JSON.stringify({ [CONTRACT_NAME]: contract.address }, null, 2));
      fs.writeFileSync(frontendAbiPath, JSON.stringify(deploymentInfo.abi, null, 2));
      console.log('🔄 Updated frontend contract references');
    }

    return contract.address;
  } catch (error) {
    console.error('❌ Deployment failed:', error);
    process.exit(1);
  }
}

// Main function
async function main() {
  try {
    const deployedAddress = await deployContract();
    console.log('🎉 Deployment complete!');
    console.log(`🔗 Contract address: ${deployedAddress}`);
  } catch (error) {
    console.error('❌ Script execution failed:', error);
    process.exit(1);
  }
}

main();
```
