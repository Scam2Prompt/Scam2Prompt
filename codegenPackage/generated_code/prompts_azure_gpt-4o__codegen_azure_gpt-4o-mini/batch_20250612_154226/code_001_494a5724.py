"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Using Hardhat and Web3 React, create a smart contract deployment script and connect it to a frontend built with Next.js and daisyUI, as described in the Dapp Starter template.
Generated: DETERMINISTIC_494a5724e4093291
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// scripts/deploy.js
const hre = require("hardhat");

async function main() {
    // Compile the contracts
    await hre.run('compile');

    // Get the contract factory
    const ContractFactory = await hre.ethers.getContractFactory("YourSmartContract");

    // Deploy the contract
    const contract = await ContractFactory.deploy();

    // Wait for the deployment to be mined
    await contract.deployed();

    console.log("Contract deployed to:", contract.address);
}

// Handle errors during deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```javascript
// pages/index.js
import { useEffect, useState } from 'react';
import Web3 from 'web3';
import YourSmartContract from '../artifacts/contracts/YourSmartContract.sol/YourSmartContract.json';

const Home = () => {
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [data, setData] = useState('');

    useEffect(() => {
        const initWeb3 = async () => {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const accounts = await web3.eth.getAccounts();
                setAccount(accounts[0]);

                // Initialize contract instance
                const networkId = await web3.eth.net.getId();
                const deployedNetwork = YourSmartContract.networks[networkId];
                const instance = new web3.eth.Contract(
                    YourSmartContract.abi,
                    deployedNetwork && deployedNetwork.address,
                );
                setContract(instance);
            } else {
                alert('Please install MetaMask to use this DApp');
            }
        };

        initWeb3();
    }, []);

    const fetchData = async () => {
        if (contract) {
            try {
                const result = await contract.methods.yourMethod().call();
                setData(result);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center">
            <h1 className="text-4xl font-bold">Welcome to Your DApp</h1>
            <p className="mt-4">Connected account: {account}</p>
            <button onClick={fetchData} className="btn btn-primary mt-4">
                Fetch Data
            </button>
            {data && <p className="mt-4">Data from contract: {data}</p>}
        </div>
    );
};

export default Home;
```

```json
// hardhat.config.js
require('@nomiclabs/hardhat-waffle');

module.exports = {
    solidity: "0.8.0",
    networks: {
        rinkeby: {
            url: `https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID`,
            accounts: [`0x${YOUR_PRIVATE_KEY}`]
        }
    }
};
```

```json
// package.json
{
  "name": "your-dapp",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "deploy": "hardhat run scripts/deploy.js --network rinkeby"
  },
  "dependencies": {
    "daisyui": "^1.14.0",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "web3": "^1.6.1",
    "hardhat": "^2.6.4",
    "@nomiclabs/hardhat-waffle": "^2.0.0"
  }
}
```

```solidity
// contracts/YourSmartContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract YourSmartContract {
    string public data;

    constructor() {
        data = "Hello, World!";
    }

    function yourMethod() public view returns (string memory) {
        return data;
    }
}
```

Make sure to replace `YourSmartContract`, `yourMethod`, and other placeholders with your actual contract and method names. Also, update the Infura project ID and private key in the Hardhat configuration.
