"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Provide a code snippet demonstrating how to set up a local zkSync Layer 2 test network using Hardhat plugins and deploy a sample smart contract.
Generated: DETERMINISTIC_5703d6748ca27a3d
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required packages
require("@nomiclabs/hardhat-waffle");
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-zksync-solc");

// Hardhat configuration
module.exports = {
    solidity: {
        version: "0.8.4", // Specify the Solidity version
        settings: {
            optimizer: {
                enabled: true, // Enable optimizer for gas efficiency
                runs: 200, // Number of optimization runs
            },
        },
    },
    zksync: {
        version: "0.1.0", // Specify zkSync version
    },
};

// Sample smart contract
const fs = require("fs");

// Define a simple storage contract
const contractSource = `
pragma solidity ^0.8.4;

contract SimpleStorage {
    uint256 private value;

    function setValue(uint256 _value) public {
        value = _value;
    }

    function getValue() public view returns (uint256) {
        return value;
    }
}
`;

// Write the contract to a file
fs.writeFileSync("contracts/SimpleStorage.sol", contractSource);

// Deploy script
async function main() {
    // Get the contract factory
    const SimpleStorage = await ethers.getContractFactory("SimpleStorage");

    // Deploy the contract
    const simpleStorage = await SimpleStorage.deploy();

    // Wait for the deployment to be confirmed
    await simpleStorage.deployed();

    console.log("SimpleStorage deployed to:", simpleStorage.address);
}

// Error handling for the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error deploying contract:", error);
        process.exit(1);
    });
```

### Instructions to run

1. Ensure you have Node.js and npm installed.
2. Create a new directory for your project and navigate into it.
3. Run `npm init -y` to initialize a new Node.js project.
4. Install the required dependencies:
   ```bash
   npm install --save-dev hardhat @nomiclabs/hardhat-waffle @nomiclabs/hardhat-ethers @nomiclabs/hardhat-zksync-solc
   ```
5. Create a directory named `contracts` and add the provided Solidity contract code into a file named `SimpleStorage.sol`.
6. Place the deployment script in a file named `deploy.js` in the root directory.
7. Run your Hardhat local network:
   ```bash
   npx hardhat node
   ```
8. In a new terminal, deploy your contract:
   ```bash
   npx hardhat run --network localhost deploy.js
   ``` 

This setup provides a running local zkSync Layer 2 test network and deploys a sample smart contract.
