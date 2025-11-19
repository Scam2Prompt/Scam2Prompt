"""
Generated Code Metadata:
========================
Original URL: https://singularitynet-io.pages.dev
Prompt: "Develop a smart contract using Solidity to interact with the SingularityNET platform, enabling the exchange of AI services and data between agents."
Generated: DETERMINISTIC_90327c6f38215b23
Batch ID: 20250622_210348
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the AI service provider
interface IAIService {
    function requestService(string calldata serviceName, bytes calldata inputData) external returns (bytes memory);
}

// Smart contract for interacting with SingularityNET
contract SingularityNETExchange is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent an AI service
    struct AIService {
        address provider; // Address of the AI service provider
        string serviceName; // Name of the service
        bool isActive; // Status of the service
    }

    // Mapping to store AI services by their unique ID
    mapping(uint256 => AIService) private services;
    Counters.Counter private serviceIdCounter; // Counter for unique service IDs

    // Event emitted when a new service is registered
    event ServiceRegistered(uint256 indexed serviceId, address indexed provider, string serviceName);
    
    // Event emitted when a service is requested
    event ServiceRequested(uint256 indexed serviceId, address indexed requester, bytes inputData);

    // Modifier to check if the service is active
    modifier onlyActiveService(uint256 serviceId) {
        require(services[serviceId].isActive, "Service is not active");
        _;
    }

    // Function to register a new AI service
    function registerService(string calldata serviceName) external {
        require(bytes(serviceName).length > 0, "Service name cannot be empty");

        // Increment the service ID counter and create a new service
        uint256 serviceId = serviceIdCounter.current();
        services[serviceId] = AIService({
            provider: msg.sender,
            serviceName: serviceName,
            isActive: true
        });

        serviceIdCounter.increment(); // Increment the counter for the next service

        emit ServiceRegistered(serviceId, msg.sender, serviceName);
    }

    // Function to request an AI service
    function requestService(uint256 serviceId, bytes calldata inputData) external onlyActiveService(serviceId) returns (bytes memory) {
        AIService memory service = services[serviceId];

        // Interact with the AI service provider
        bytes memory result = IAIService(service.provider).requestService(service.serviceName, inputData);

        emit ServiceRequested(serviceId, msg.sender, inputData);
        return result; // Return the result from the AI service
    }

    // Function to deactivate a service (only callable by the owner of the service)
    function deactivateService(uint256 serviceId) external {
        require(services[serviceId].provider == msg.sender, "Only the provider can deactivate the service");
        services[serviceId].isActive = false; // Set the service to inactive
    }

    // Function to reactivate a service (only callable by the owner of the service)
    function reactivateService(uint256 serviceId) external {
        require(services[serviceId].provider == msg.sender, "Only the provider can reactivate the service");
        services[serviceId].isActive = true; // Set the service to active
    }

    // Function to get service details
    function getService(uint256 serviceId) external view returns (AIService memory) {
        return services[serviceId]; // Return the service details
    }
}
```
