"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate code for a Web3 application using Hardhat and React, with a focus on 1-click deployment.
Generated: DETERMINISTIC_47b0b9fb689758b0
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**hardhat.config.js**
```javascript
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");
require("hardhat-deploy");

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.8.10",
  networks: {
    mainnet: {
      url: process.env.ALCHEMY_MAINNET_URL,
      accounts: [process.env.METAMASK_PRIVATE_KEY],
    },
    testnet: {
      url: process.env.ALCHEMY_TESTNET_URL,
      accounts: [process.env.METAMASK_PRIVATE_KEY],
    },
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
  namedAccounts: {
    deployer: {
      default: 0,
    },
  },
};
```

**deploy.js**
```javascript
const { ethers, upgrades } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log(`Deploying contracts with the account: ${deployer.address}`);

  // Deploy contract
  const YourContract = await ethers.getContractFactory("YourContract");
  const yourContract = await upgrades.deployProxy(YourContract, []);

  await yourContract.deployed();

  console.log(`YourContract deployed to: ${yourContract.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

**src/App.js**
```javascript
import React, { useState, useEffect } from "react";
import { useWeb3 } from "@3rdweb/hooks";
import Web3 from "web3";

function App() {
  const { connect, disconnect, account, provider } = useWeb3();
  const [yourContract, setYourContract] = useState(null);

  useEffect(() => {
    if (provider) {
      const web3 = new Web3(provider);
      const contractAddress = "YOUR_CONTRACT_ADDRESS";
      const contractABI = [...]; // Your contract ABI

      const yourContract = new web3.eth.Contract(contractABI, contractAddress);
      setYourContract(yourContract);
    }
  }, [provider]);

  const handleDeploy = async () => {
    try {
      // Call deploy script using ethers.js
      const response = await fetch("/deploy", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      {account ? (
        <button onClick={handleDeploy}>Deploy Contract</button>
      ) : (
        <button onClick={connect}>Connect Wallet</button>
      )}
      {yourContract && <p>Contract Address: {yourContract.options.address}</p>}
    </div>
  );
}

export default App;
```

**src/index.js**
```javascript
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { Web3Provider } from "@3rdweb/hooks";

ReactDOM.render(
  <Web3Provider>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Web3Provider>,
  document.getElementById("root")
);
```

**server.js**
```javascript
const express = require("express");
const { exec } = require("child_process");

const app = express();

app.use(express.json());

app.post("/deploy", (req, res) => {
  exec("npx hardhat run scripts/deploy.js --network testnet", (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      res.status(500).send({ message: "Deploy failed" });
      return;
    }
    console.log(`stdout: ${stdout}`);
    res.send({ message: "Contract deployed successfully" });
  });
});

const port = 3001;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**package.json**
```json
{
  "name": "web3-app",
  "version": "0.1.0",
  "scripts": {
    "start": "node server.js",
    "build": "react-scripts build",
    "test": "react-scripts test"
  },
  "dependencies": {
    "@3rdweb/hooks": "^0.2.5",
    "@testing-library/jest-dom": "^5.16.1",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web3": "^1.8.0",
    "web3.js": "^1.8.0"
  },
  "devDependencies": {
    "@nomiclabs/hardhat": "^2.9.2",
    "hardhat-deploy": "^0.11.14",
    "ethers": "^5.4.1"
  }
}
```
