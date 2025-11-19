"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial for building a decentralized application (dApp) that utilizes Chainlink's market data feeds for real-time pricing.
Generated: DETERMINISTIC_ed1e1a30bc3dcd8f
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Chainlink Price Feed interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Smart contract for the decentralized application (dApp)
contract PriceConsumer {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Ethereum Mainnet
     * Aggregator: ETH/USD
     * Address: 0x5f4eC3Df9cbd43714fe2740f5e3616155c5B8419
     */
    constructor() {
        // Initialize the price feed contract
        priceFeed = AggregatorV3Interface(0x5f4eC3Df9cbd43714fe2740f5e3616155c5B8419);
    }

    /**
     * Returns the latest price
     * @return (uint256) The latest ETH price in USD
     */
    function getLatestPrice() public view returns (uint256) {
        // Fetch the latest price data
        (
            /* uint80 roundID */,
            int256 price,
            /* uint256 startedAt */,
            /* uint256 timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        
        // Ensure price is greater than zero
        require(price > 0, "Price must be greater than zero");

        return uint256(price);
    }
}

// Frontend code example (JavaScript)

// Importing ethers.js library for interaction with Ethereum
import { ethers } from "ethers";

// Function to connect to Ethereum and get the latest price
async function fetchLatestPrice() {
    // Connect to Ethereum network
    if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const signer = provider.getSigner();

        // Address of the deployed PriceConsumer contract
        const contractAddress = "YOUR_CONTRACT_ADDRESS";
        const contractABI = [
            // ABI of the getLatestPrice function
            {
                "inputs": [],
                "name": "getLatestPrice",
                "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
                "stateMutability": "view",
                "type": "function"
            }
        ];

        const priceConsumerContract = new ethers.Contract(contractAddress, contractABI, signer);

        try {
            // Call the getLatestPrice function
            const price = await priceConsumerContract.getLatestPrice();
            console.log(`Latest ETH Price in USD: $${ethers.utils.formatUnits(price, 18)}`);
        } catch (error) {
            console.error("Error fetching price:", error);
        }
    } else {
        console.error("Ethereum object not found. Please install MetaMask!");
    }
}

// Example of calling the fetchLatestPrice function on button click
document.getElementById("fetch-price-button").addEventListener("click", fetchLatestPrice);
```

### Notes:
- Replace `YOUR_CONTRACT_ADDRESS` with the actual deployed contract address.
- Ensure to import the necessary libraries (like `ethers.js`) in your project.
