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
// Import necessary modules from Hardhat
const { ethers } = require("hardhat");

// Main function to compile and deploy the smart contract
async function main() {
    // Compile the smart contract
    await hre.run('compile');

    // Fetch the contract to deploy
    const Contract = await ethers.getContractFactory("YourContractName");

    // Deploy the contract
    const contract = await Contract.deploy();
    
    // Wait for the contract to be deployed
    await contract.deployed();

    console.log("Contract deployed to:", contract.address);

    // Save contract address to a JSON file for frontend usage
    const fs = require('fs');
    const path = require('path');

    const addresses = {
        YourContractName: contract.address,
    };

    fs.writeFileSync(path.join(__dirname, 'frontend/src/constants/addresses.json'), JSON.stringify(addresses, null, 2));
}

// Execute the main function and handle errors
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error deploying contract:", error);
        process.exit(1);
    });
```

**Next.js Frontend Setup:**

```javascript
// frontend/src/pages/index.js
import { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import YourContract from '../constants/YourContractName.json';
import addresses from '../constants/addresses.json';

const Home = () => {
    const [contract, setContract] = useState(null);
    const [data, setData] = useState(null);

    // Function to connect to Ethereum and your contract
    const connectWallet = async () => {
        if (window.ethereum) {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contractInstance = new ethers.Contract(addresses.YourContractName, YourContract.abi, signer);
            setContract(contractInstance);
        } else {
            console.error("Ethereum interface not found. Install MetaMask.");
        }
    };

    // Fetch data from the contract
    const fetchData = async () => {
        if (contract) {
            try {
                const response = await contract.yourReadFunction(); // replace with your actual function
                setData(response);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }
    };

    // Use effect to call fetchData when contract is set
    useEffect(() => {
        fetchData();
    }, [contract]);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">DApp with Next.js & DaisyUI</h1>
            <button onClick={connectWallet} className="btn btn-primary mt-4">Connect Wallet</button>
            {data && <div className="mt-4">Data from contract: {data.toString()}</div>}
        </div>
    );
};

export default Home;
```

**Install Dependencies:**

Make sure to install the necessary dependencies in your frontend project:

```bash
npm install ethers daisyui
```

**Tailwind CSS Configuration:**

Ensure Tailwind CSS and DaisyUI are properly set up in your project for styling. Add the following to your `tailwind.config.js`:

```javascript
module.exports = {
  // ...
  plugins: [require('daisyui')],
}
```

Remember to replace `"YourContractName"` and `"yourReadFunction"` with the actual names used in your smart contract.
