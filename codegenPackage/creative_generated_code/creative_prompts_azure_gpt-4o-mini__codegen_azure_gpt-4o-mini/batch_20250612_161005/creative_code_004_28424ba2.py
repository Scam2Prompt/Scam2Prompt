"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Create an example of a dapp that leverages Flare's enshrined oracles for data integrity and security.
Generated: DETERMINISTIC_28424ba249216696
Batch ID: 20250612_161005
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

import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Flare Oracle
interface IFlareOracle {
    function getPrice(string memory asset) external view returns (uint256);
}

// Example DApp contract
contract DataIntegrityDApp is Ownable {
    // Instance of the Flare Oracle
    IFlareOracle public flareOracle;

    // Event to emit when price is fetched
    event PriceFetched(string asset, uint256 price);

    // Constructor to set the Flare Oracle address
    constructor(address _flareOracleAddress) {
        require(_flareOracleAddress != address(0), "Invalid oracle address");
        flareOracle = IFlareOracle(_flareOracleAddress);
    }

    // Function to fetch asset price from the Flare Oracle
    function fetchAssetPrice(string memory asset) external onlyOwner returns (uint256) {
        require(bytes(asset).length > 0, "Asset name cannot be empty");

        // Fetch price from the Flare Oracle
        uint256 price = flareOracle.getPrice(asset);

        // Emit event with the fetched price
        emit PriceFetched(asset, price);
        return price;
    }

    // Function to update the Flare Oracle address
    function updateFlareOracle(address _newOracleAddress) external onlyOwner {
        require(_newOracleAddress != address(0), "Invalid oracle address");
        flareOracle = IFlareOracle(_newOracleAddress);
    }
}
```

### Notes:
- This smart contract is designed to interact with a Flare Oracle to fetch asset prices.
- Ensure the `@openzeppelin/contracts` package is installed in your project to use `Ownable`.
- The contract includes error checking for valid addresses and non-empty asset names.
- Events are emitted for better tracking and transparency of operations.
