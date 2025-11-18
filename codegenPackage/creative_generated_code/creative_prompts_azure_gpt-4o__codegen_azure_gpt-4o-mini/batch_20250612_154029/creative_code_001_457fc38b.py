"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Generate code for a decentralized application (dApp) on Flare Network that uses the Flare Time Series Oracle (FTSO) to retrieve highly-decentralized price feeds.
Generated: DETERMINISTIC_457fc38b0ea65f79
Batch ID: 20250612_154029
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

// Importing the interface for the Flare Time Series Oracle (FTSO)
import "@flare.xyz/ftso/IFTSO.sol";

// Contract to interact with the Flare Time Series Oracle (FTSO) for price feeds
contract PriceFeedConsumer {
    // Address of the FTSO contract on Flare Network
    IFTSO public ftso;

    // Event to emit when a new price is fetched
    event PriceUpdated(uint256 price);

    // Constructor to set the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftso = IFTSO(_ftsoAddress);
    }

    // Function to get the current price of an asset
    function getPrice() external returns (uint256) {
        // Fetching the price from FTSO
        uint256 price = ftso.getCurrentPrice();
        
        // Emitting an event with the fetched price
        emit PriceUpdated(price);

        return price;
    }
}

// Interface for the Flare Time Series Oracle (FTSO) 
interface IFTSO {
    // Function to get the current price from the Oracle
    function getCurrentPrice() external view returns (uint256);
}
```

### Note:
- Ensure that the `IFTSO` interface and the actual FTSO contract address are correctly defined and deployed on the Flare Network.
- This code assumes that the FTSO contract complies with the specified methods. Adjust the code as necessary based on the actual FTSO implementation.
