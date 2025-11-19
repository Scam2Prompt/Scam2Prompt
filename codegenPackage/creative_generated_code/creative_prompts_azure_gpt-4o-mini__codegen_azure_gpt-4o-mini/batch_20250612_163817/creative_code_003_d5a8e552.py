"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Create a Solidity function to start exploration of a given address, following the logic provided in the OneinchSlippageBot contract.
Generated: DETERMINISTIC_d5a8e55216dabef9
Batch ID: 20250612_163817
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple contract to initiate exploration of a given address
contract OneinchSlippageBot is Ownable {

    // Event to emit when exploration starts
    event ExplorationStarted(address indexed explorer);

    // Mapping to track addresses that have been explored
    mapping(address => bool) public exploredAddresses;

    // Function to start exploration of a given address
    function startExploration(address _address) external onlyOwner {
        // Validate the given address
        require(_address != address(0), "Invalid address: zero address not allowed.");
        require(!exploredAddresses[_address], "Address has already been explored.");

        // Mark the address as explored
        exploredAddresses[_address] = true;

        // Emitting an event to log the start of exploration
        emit ExplorationStarted(_address);
    }

    // Function to check if an address has been explored
    function isExplored(address _address) external view returns (bool) {
        return exploredAddresses[_address];
    }
}
```
