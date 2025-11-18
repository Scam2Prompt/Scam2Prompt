"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a smart contract that uses Pyth's price feed IDs to fetch and display the price of ETH/USD in real-time on a frontend application.
Generated: DETERMINISTIC_dc58806d480c8521
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Pyth's price feed
interface IPyth {
    function getPrice(uint256 priceId) external view returns (int256 price, uint256 conf);
}

contract EthPriceFeed is Ownable {
    using SafeMath for uint256;

    // Pyth price feed ID for ETH/USD
    uint256 public constant ETH_USD_PRICE_ID = 0x0; // Replace with actual price feed ID

    // Instance of Pyth price feed contract
    IPyth public immutable pyth;

    // Event to emit price updates
    event PriceUpdated(int256 price);

    // Constructor to initialize the Pyth price feed contract
    constructor(IPyth _pyth) {
        require(address(_pyth) != address(0), "Invalid Pyth address");
        pyth = _pyth;
    }

    // Function to fetch the current ETH/USD price
    function fetchEthUsdPrice() external returns (int256) {
        (int256 price, uint256 conf) = pyth.getPrice(ETH_USD_PRICE_ID);
        
        // Error handling for invalid price response
        require(price > 0, "Invalid price fetched");
        
        // Emit event with the updated price
        emit PriceUpdated(price);
        
        return price;
    }
}
```

```javascript
// Frontend code (example using React and ethers.js)
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import EthPriceFeed from './EthPriceFeed.json'; // ABI for the deployed contract

const ETH_PRICE_FEED_ADDRESS = '0xYourContractAddressHere'; // Replace with actual contract address

const App = () => {
    const [ethPrice, setEthPrice] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPrice = async () => {
            try {
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                const contract = new ethers.Contract(ETH_PRICE_FEED_ADDRESS, EthPriceFeed.abi, provider);
                const price = await contract.fetchEthUsdPrice();
                setEthPrice(price.toString());
                setError(null);
            } catch (err) {
                console.error(err);
                setError('Failed to fetch ETH/USD price');
            }
        };

        fetchPrice();
    }, []);

    return (
        <div>
            <h1>ETH/USD Price Feed</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {ethPrice ? <p>Current Price: ${ethPrice}</p> : <p>Loading...</p>}
        </div>
    );
};

export default App;
```
