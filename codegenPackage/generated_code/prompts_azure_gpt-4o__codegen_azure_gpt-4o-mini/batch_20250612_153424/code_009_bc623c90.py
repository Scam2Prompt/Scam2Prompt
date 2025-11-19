"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity example of using Open Ocean to implement a feature-as-a-service model, where multiple client contracts can securely access modular functionality.
Generated: DETERMINISTIC_bc623c90cf8269a1
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenOcean interface for interaction with the protocol
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the modular functionality
interface IFeature {
    function executeFeature(address client) external;
}

// Example of a modular feature contract
contract ModularFeature is IFeature, Ownable {
    // Event to log feature execution
    event FeatureExecuted(address indexed client);

    // Function to execute the feature for a client
    function executeFeature(address client) external override onlyOwner {
        require(client != address(0), "Invalid client address");
        
        // Implement the feature logic here
        // For example, transferring tokens, updating state, etc.

        emit FeatureExecuted(client);
    }
}

// Main contract to manage client contracts and feature access
contract FeatureAsAService is Ownable {
    // Mapping to track registered client contracts
    mapping(address => bool) public clients;
    // Instance of the modular feature contract
    ModularFeature public featureContract;

    // Event to log client registration
    event ClientRegistered(address indexed client);
    event ClientDeregistered(address indexed client);

    // Constructor to initialize the modular feature contract
    constructor(address _featureContract) {
        require(_featureContract != address(0), "Invalid feature contract address");
        featureContract = ModularFeature(_featureContract);
    }

    // Function to register a new client contract
    function registerClient(address client) external onlyOwner {
        require(client != address(0), "Invalid client address");
        require(!clients[client], "Client already registered");

        clients[client] = true;
        emit ClientRegistered(client);
    }

    // Function to deregister a client contract
    function deregisterClient(address client) external onlyOwner {
        require(clients[client], "Client not registered");

        clients[client] = false;
        emit ClientDeregistered(client);
    }

    // Function for clients to access the feature
    function accessFeature() external {
        require(clients[msg.sender], "Caller is not a registered client");

        // Call the feature execution
        featureContract.executeFeature(msg.sender);
    }
}
```
