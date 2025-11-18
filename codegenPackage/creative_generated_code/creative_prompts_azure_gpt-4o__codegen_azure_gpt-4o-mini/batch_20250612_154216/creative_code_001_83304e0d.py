"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Create a Hardhat script to deploy a smart contract and connect it to a frontend built with Next.js and daisyUI.
Generated: DETERMINISTIC_83304e0d79670091
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// deploy.js - A Hardhat script to deploy a smart contract

// Import required packages
const { ethers } = require("hardhat");
const fs = require("fs");
const path = require("path");

// Main function to deploy the contract
async function main() {
    // Get the Contract factory
    const ContractFactory = await ethers.getContractFactory("YourSmartContract");

    // Deploy the contract
    const contract = await ContractFactory.deploy();

    // Wait for the transaction to be mined
    await contract.deployed();

    console.log(`Contract deployed to: ${contract.address}`);

    // Save the contract address to a JSON file for frontend use
    saveContractAddress(contract.address);
}

// Function to save the deployed contract address
function saveContractAddress(address) {
    const addressFilePath = path.join(__dirname, "contract-address.json");
    const data = JSON.stringify({ address }, null, 2);

    // Write to file with error handling
    fs.writeFileSync(addressFilePath, data, (err) => {
        if (err) {
            console.error("Error saving contract address:", err);
        }
    });

    console.log("Contract address saved to:", addressFilePath);
}

// Error handling for main function execution
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error during deployment:", error);
        process.exit(1);
    });
```

```javascript
// frontend.js - A Next.js component to connect to the deployed smart contract

import { useEffect, useState } from "react";
import { ethers } from "ethers";
import contractAddress from "../contract-address.json"; // Path to the saved address
import YourSmartContract from "../artifacts/contracts/YourSmartContract.sol/YourSmartContract.json"; // ABI

const FrontendComponent = () => {
    const [contract, setContract] = useState(null);
    const [account, setAccount] = useState("");

    // Connect to the Ethereum provider and contract
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                await window.ethereum.request({ method: "eth_requestAccounts" });
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                const signer = provider.getSigner();
                const contractInstance = new ethers.Contract(contractAddress.address, YourSmartContract.abi, signer);
                setContract(contractInstance);
                const accounts = await provider.listAccounts();
                setAccount(accounts[0]);
            } catch (error) {
                console.error("Error connecting to wallet:", error);
            }
        } else {
            console.error("Please install MetaMask!");
        }
    };

    useEffect(() => {
        if (contract) {
            // Any additional logic after the contract is connected can be placed here
        }
    }, [contract]);

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold">Connect to Smart Contract</h1>
            <button className="btn btn-primary" onClick={connectWallet}>
                Connect Wallet
            </button>
            {account && <p>Connected Account: {account}</p>}
        </div>
    );
};

export default FrontendComponent;
```

```json
// contract-address.json - A JSON file to store the deployed contract address
{
    "address": "YOUR_DEPLOYED_CONTRACT_ADDRESS"
}
```

Make sure to replace `"YourSmartContract"` in the Hardhat script with the actual name of your smart contract and update the paths as necessary in the frontend component.
