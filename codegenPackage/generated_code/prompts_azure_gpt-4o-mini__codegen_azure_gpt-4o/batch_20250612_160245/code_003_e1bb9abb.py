"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a code example for integrating Hardhat with a DApp, referencing the tools highlighted on the Dapp Starter webpage.
Generated: DETERMINISTIC_e1bb9abbb1bb1a5c
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and dependencies
const { ethers } = require("hardhat");
const fs = require("fs");
const path = require("path");

// Configuration for deployment
const DEPLOYMENT_CONFIG = {
  contractName: "MyDAppContract", // Replace with your contract name
  outputPath: "./frontend/src/contracts", // Path to save contract artifacts
};

// Main deployment function
async function main() {
  console.log("Starting deployment...");

  // Get the contract factory
  const ContractFactory = await ethers.getContractFactory(DEPLOYMENT_CONFIG.contractName);

  // Deploy the contract
  console.log(`Deploying ${DEPLOYMENT_CONFIG.contractName}...`);
  const contractInstance = await ContractFactory.deploy();

  // Wait for the deployment to complete
  await contractInstance.deployed();
  console.log(`${DEPLOYMENT_CONFIG.contractName} deployed to: ${contractInstance.address}`);

  // Save contract artifacts for frontend integration
  saveContractArtifacts(contractInstance);
}

// Function to save contract artifacts (ABI and address) for frontend integration
function saveContractArtifacts(contractInstance) {
  try {
    const artifactsPath = path.resolve(DEPLOYMENT_CONFIG.outputPath);

    // Ensure the output directory exists
    if (!fs.existsSync(artifactsPath)) {
      fs.mkdirSync(artifactsPath, { recursive: true });
    }

    // Save contract address
    const addressFilePath = path.join(artifactsPath, "contract-address.json");
    fs.writeFileSync(
      addressFilePath,
      JSON.stringify({ address: contractInstance.address }, null, 2)
    );
    console.log(`Contract address saved to ${addressFilePath}`);

    // Save contract ABI
    const abiFilePath = path.join(artifactsPath, "contract-abi.json");
    const contractArtifact = artifacts.readArtifactSync(DEPLOYMENT_CONFIG.contractName);
    fs.writeFileSync(abiFilePath, JSON.stringify(contractArtifact.abi, null, 2));
    console.log(`Contract ABI saved to ${abiFilePath}`);
  } catch (error) {
    console.error("Error saving contract artifacts:", error);
  }
}

// Error handling for the deployment script
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Deployment failed:", error);
    process.exit(1);
  });
```

### Notes:
- Replace `MyDAppContract` with the name of your contract.
- Ensure the `frontend/src/contracts` directory exists or adjust the `outputPath` to match your project structure.
- Install Hardhat and required dependencies (`npm install hardhat ethers`) before running the script.
- Run the script using `npx hardhat run scripts/deploy.js --network <network-name>` where `<network-name>` is your target network.
