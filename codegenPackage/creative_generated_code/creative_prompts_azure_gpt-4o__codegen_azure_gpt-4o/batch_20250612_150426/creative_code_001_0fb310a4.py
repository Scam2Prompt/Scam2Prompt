"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Generate a script using Hardhat to deploy a smart contract and connect it to a DApp built with the Dapp Starter kit.
Generated: DETERMINISTIC_0fb310a4e5cc8eed
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Hardhat deployment script for deploying a smart contract 
// and connecting it to a DApp built with Dapp Starter kit.

const { ethers } = require("hardhat");

async function main() {
  // Load the contract factory
  const ContractName = "YourSmartContract"; // Replace with your smart contract name
  const ContractFactory = await ethers.getContractFactory(ContractName);

  console.log("Deploying contract...");

  // Deploy the contract
  const deployedContract = await ContractFactory.deploy();

  // Wait for the deployment transaction to be mined
  await deployedContract.deployed();

  console.log(`${ContractName} deployed to:`, deployedContract.address);

  // Create the connection file for the DApp
  createConnectionFile(deployedContract.address, ContractName);
}

/**
 * Create a connection file for the DApp Starter kit containing
 * the deployed contract address and its ABI.
 * 
 * @param {string} contractAddress - The address of the deployed contract.
 * @param {string} contractName - The name of the contract.
 */
function createConnectionFile(contractAddress, contractName) {
  const fs = require("fs");
  const path = require("path");

  // Load the contract's ABI
  const contractArtifact = require(`../artifacts/contracts/${contractName}.sol/${contractName}.json`);
  const contractABI = contractArtifact.abi;

  // Define the connection object
  const connectionDetails = {
    address: contractAddress,
    abi: contractABI
  };

  // Define the output path
  const outputDir = path.resolve(__dirname, "../dapp/src/contracts");
  const outputFile = path.join(outputDir, `${contractName}.json`);

  // Ensure the output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Write the connection details to a JSON file
  fs.writeFileSync(outputFile, JSON.stringify(connectionDetails, null, 2));

  console.log(`Connection details saved to: ${outputFile}`);
}

// Catch and handle errors during execution
main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error("Error deploying contract:", error);
    process.exit(1);
  });
```

To execute this script, save it in the `scripts` directory of your Hardhat project (e.g., `scripts/deploy.js`) and run it using the Hardhat CLI:

```bash
npx hardhat run scripts/deploy.js --network your-network-name
```

Make sure to replace `your-network-name` with the appropriate network (e.g., localhost, rinkeby) and update `YourSmartContract` with your actual smart contract name.
