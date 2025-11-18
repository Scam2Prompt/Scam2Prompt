"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Generate a script using Hardhat to compile and deploy a smart contract, and connect it to a frontend built with Next.js and Web3 React.
Generated: DETERMINISTIC_71bce2aeac72ba47
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Hardhat Script: deploy.js
// Script to compile and deploy the smart contract
const hre = require("hardhat");

async function main() {
  try {
    // Compile the contract
    console.log("Compiling the contract...");
    await hre.run("compile");

    // Deploy the contract
    console.log("Deploying the contract...");
    const ContractFactory = await hre.ethers.getContractFactory("YourContract");
    const contract = await ContractFactory.deploy();

    // Wait for deployment to complete
    await contract.deployed();
    console.log(`Contract deployed to: ${contract.address}`);
  } catch (error) {
    console.error("Error during deployment:", error);
    process.exit(1);
  }
}

// Execute the deployment script
main().then(() => process.exit(0)).catch((error) => {
  console.error("Unhandled error:", error);
  process.exit(1);
});
```

```javascript
// Next.js Frontend: pages/index.js
// Connects to the deployed smart contract using Web3 React
import { useEffect, useState } from "react";
import Web3 from "web3";
import { useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";

// Define the injected connector for MetaMask
const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet & testnets
});

export default function Home() {
  const { activate, active, account, library } = useWeb3React();
  const [contract, setContract] = useState(null);
  const [contractAddress, setContractAddress] = useState(""); // Replace with your deployed contract address
  const [contractABI, setContractABI] = useState([]); // Replace with your contract ABI

  useEffect(() => {
    if (library && contractAddress && contractABI.length > 0) {
      const web3 = new Web3(library.provider);
      const deployedContract = new web3.eth.Contract(contractABI, contractAddress);
      setContract(deployedContract);
    }
  }, [library, contractAddress, contractABI]);

  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error("Wallet connection failed:", error);
    }
  };

  return (
    <div>
      <h1>Web3 React & Smart Contract Integration</h1>
      {!active ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <p>Smart Contract Address: {contractAddress || "Not specified"}</p>
          {/* Interaction with the contract can be implemented here */}
          {/* Example: Call a function or display contract data */}
        </div>
      )}
    </div>
  );
}
```

```javascript
// Components: web3-provider.js
// Provides Web3 React context to the application
import { Web3ReactProvider } from "@web3-react/core";
import Web3 from "web3";

function getLibrary(provider) {
  return new Web3(provider); // Create and return a Web3 instance
}

export default function Web3Provider({ children }) {
  return <Web3ReactProvider getLibrary={getLibrary}>{children}</Web3ReactProvider>;
}
```

```javascript
// Next.js: pages/_app.js
// Wraps the application with the Web3 React provider
import Web3Provider from "../components/web3-provider";

export default function App({ Component, pageProps }) {
  return (
    <Web3Provider>
      <Component {...pageProps} />
    </Web3Provider>
  );
}
```

```solidity
// Solidity Contract: contracts/YourContract.sol
// Simple example smart contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract YourContract {
    string public message;

    constructor(string memory _message) {
        message = _message;
    }

    function setMessage(string memory _newMessage) public {
        message = _newMessage;
    }
}
```

```json
// Hardhat Configuration: hardhat.config.js
// Configures Hardhat for the project
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  networks: {
    hardhat: {},
    // Add configuration for additional networks if needed
  },
};
```
