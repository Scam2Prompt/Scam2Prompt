"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial for building a decentralized application (dApp) that utilizes Chainlink's market data feeds for real-time pricing.
Generated: DETERMINISTIC_ed1e1a30bc3dcd8f
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Chainlink Aggregator interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Contract to fetch and store real-time price data using Chainlink oracles
contract PriceFeedConsumer {
    // State variable to hold the price feed contract address
    AggregatorV3Interface internal priceFeed;

    // Event to emit when the price is updated
    event PriceUpdated(int256 price);

    // Constructor to initialize the price feed contract
    constructor(address _priceFeedAddress) {
        // Set the price feed address
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    // Function to get the latest price from the Chainlink price feed
    function getLatestPrice() public returns (int256) {
        // Fetch the latest price data
        (
            , // Ignoring the round ID
            int256 price, // Latest price
            , // Ignoring the timestamp
            , // Ignoring the answered in round
            // Ignoring the decimals
        ) = priceFeed.latestRoundData();

        // Emit the price updated event
        emit PriceUpdated(price);

        // Return the latest price
        return price;
    }
}
```

```javascript
// Frontend code using React and ethers.js to interact with the smart contract

import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import PriceFeedConsumer from './PriceFeedConsumer.json'; // ABI of the contract

const App = () => {
    const [price, setPrice] = useState(null);
    const [error, setError] = useState(null);
    const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your deployed contract address

    // Function to fetch the latest price from the smart contract
    const fetchPrice = async () => {
        try {
            // Requesting access to the user's Ethereum account
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const contract = new ethers.Contract(contractAddress, PriceFeedConsumer.abi, provider);
            
            // Calling the getLatestPrice function from the contract
            const latestPrice = await contract.getLatestPrice();
            setPrice(latestPrice.toString());
        } catch (err) {
            // Handling errors and setting the error state
            console.error(err);
            setError('Failed to fetch price. Please try again.');
        }
    };

    // Effect to fetch price on component mount
    useEffect(() => {
        fetchPrice();
    }, []);

    return (
        <div>
            <h1>Real-Time Price Feed</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {price ? <p>Latest Price: {price}</p> : <p>Loading...</p>}
            <button onClick={fetchPrice}>Refresh Price</button>
        </div>
    );
};

export default App;
```

```json
// package.json for the React frontend
{
  "name": "dapp-price-feed",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "ethers": "^5.0.0",
    "react": "^17.0.0",
    "react-dom": "^17.0.0",
    "react-scripts": "4.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```bash
# Instructions to set up the project
# 1. Install Node.js and npm if not already installed.
# 2. Create a new React app using Create React App:
npx create-react-app dapp-price-feed
cd dapp-price-feed

# 3. Install ethers.js:
npm install ethers

# 4. Replace the contents of src/App.js with the provided React code.

# 5. Create a new file src/PriceFeedConsumer.json and add the ABI of your deployed contract.

# 6. Replace 'YOUR_CONTRACT_ADDRESS' in the React code with your deployed contract address.

# 7. Start the React app:
npm start
```

This code provides a complete dApp that interacts with a Chainlink price feed, including a smart contract and a React frontend. Make sure to replace placeholders with actual values and deploy the smart contract on a suitable Ethereum network.
