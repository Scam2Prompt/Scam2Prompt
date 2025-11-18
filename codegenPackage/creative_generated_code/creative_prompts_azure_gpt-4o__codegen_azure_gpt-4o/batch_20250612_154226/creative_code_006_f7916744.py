"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Write a Hardhat script to compile and deploy a smart contract, then connect it to a frontend built with Next.js and styled using daisyUI, as demonstrated in the Dapp Starter template.
Generated: DETERMINISTIC_f791674405d16167
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Hardhat script: compile and deploy a smart contract
// Save this file as "scripts/deploy.js"

const hre = require("hardhat");

async function main() {
  // Compile the smart contract
  console.log("Compiling contracts...");
  await hre.run('compile');

  // Deploy the smart contract
  console.log("Deploying contract...");
  const ContractFactory = await hre.ethers.getContractFactory("MyContract"); // Replace 'MyContract' with your contract name
  const contract = await ContractFactory.deploy(); // Deploy the contract

  await contract.deployed(); // Wait for deployment to complete

  console.log(`Contract deployed to address: ${contract.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Error during deployment:", error);
    process.exit(1);
  });
```

```javascript
// Next.js frontend: Connect to the deployed smart contract
// Save this file in your Next.js project as "pages/index.js"

import { useState, useEffect } from "react";
import { ethers } from "ethers";

export default function Home() {
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState(null);
  const [contractData, setContractData] = useState(null);

  const contractAddress = "0xYourContractAddress"; // Replace with your deployed contract address
  const contractABI = [/* Add your contract ABI here */]; // Replace with your contract's ABI

  useEffect(() => {
    // Connect to MetaMask wallet
    async function connectWallet() {
      if (window.ethereum) {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          const signer = provider.getSigner();
          const accounts = await window.ethereum.request({
            method: "eth_requestAccounts",
          });

          setAccount(accounts[0]);
          const contractInstance = new ethers.Contract(
            contractAddress,
            contractABI,
            signer
          );
          setContract(contractInstance);
        } catch (error) {
          console.error("Failed to connect wallet:", error);
        }
      } else {
        console.error("MetaMask not found");
        alert("Please install MetaMask to interact with this Dapp.");
      }
    }

    connectWallet();
  }, []);

  // Example interaction - Fetch contract data
  async function fetchContractData() {
    if (!contract) return;

    try {
      const data = await contract.someMethod(); // Replace 'someMethod' with a function from your contract
      setContractData(data);
    } catch (error) {
      console.error("Error fetching contract data:", error);
    }
  }

  return (
    <div className="bg-base-200 min-h-screen flex flex-col items-center justify-center p-4">
      <h1 className="text-4xl font-bold mb-4">My Dapp</h1>
      <div className="mb-4">
        <p className="text-lg">Connected Account: {account || "None"}</p>
      </div>
      <button
        className="btn btn-primary"
        onClick={fetchContractData}
        disabled={!contract}
      >
        Fetch Contract Data
      </button>
      {contractData && (
        <div className="mt-4">
          <p className="text-lg">Contract Data: {contractData.toString()}</p>
        </div>
      )}
    </div>
  );
}
```

```json
// package.json: Add dependencies for the Next.js frontend
{
  "name": "nextjs-dapp",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "^13.0.0", // Replace with the latest version
    "react": "^18.0.0", // Replace with the latest version
    "react-dom": "^18.0.0", // Replace with the latest version
    "ethers": "^5.7.0", // Replace with the latest version
    "daisyui": "^2.51.0" // Replace with the latest version
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "eslint-config-next": "^13.0.0"
  }
}
```

```javascript
// tailwind.config.js: Configure Tailwind CSS with DaisyUI for styling
module.exports = {
  content: ['./pages/**/*.{js,jsx,ts,tsx}', './components/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
};
```

```bash
# Install dependencies for the Next.js frontend
npm install next react react-dom ethers daisyui
npm install --save-dev tailwindcss postcss autoprefixer
npx tailwindcss init
```
