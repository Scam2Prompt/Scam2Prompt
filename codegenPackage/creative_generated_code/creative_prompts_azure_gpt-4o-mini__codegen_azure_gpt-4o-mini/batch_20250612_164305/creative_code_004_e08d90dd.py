"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of how to adjust collateral factors at the Silo level in a decentralized finance application.
Generated: DETERMINISTIC_e08d90dd1474127f
Batch ID: 20250612_164305
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

import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Silo contract
interface ISilo {
    function setCollateralFactor(address asset, uint256 newFactor) external;
}

// SiloManager contract to adjust collateral factors at the Silo level
contract SiloManager is Ownable {
    // Mapping to track the Silo contracts
    mapping(address => ISilo) public silos;

    // Event emitted when a collateral factor is adjusted
    event CollateralFactorAdjusted(address indexed asset, uint256 newFactor);

    // Modifier to check if the asset is managed by a registered Silo
    modifier onlyRegisteredSilo(address siloAddress) {
        require(address(silos[siloAddress]) != address(0), "Silo not registered");
        _;
    }

    // Function to register a new Silo contract
    function registerSilo(address siloAddress) external onlyOwner {
        require(siloAddress != address(0), "Invalid address");
        silos[siloAddress] = ISilo(siloAddress);
    }

    // Function to adjust the collateral factor for a specific asset in a Silo
    function adjustCollateralFactor(address siloAddress, address asset, uint256 newFactor) 
        external 
        onlyOwner 
        onlyRegisteredSilo(siloAddress) 
    {
        // Validate the new collateral factor
        require(newFactor >= 0 && newFactor <= 1e18, "Collateral factor must be between 0 and 1e18");
        
        // Adjust the collateral factor in the Silo
        try silos[siloAddress].setCollateralFactor(asset, newFactor) {
            emit CollateralFactorAdjusted(asset, newFactor);
        } catch {
            revert("Failed to adjust collateral factor");
        }
    }
}
```
