"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.com
Prompt: How can I deploy an AVS (Authenticated Verifiable Service) using EigenLayer's infrastructure to leverage Ethereum's security?
Generated: DETERMINISTIC_461be8fddea6b65d
Batch ID: 20250612_155751
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

// Import necessary interfaces from EigenLayer for AVS
import "@eigenlayer/contracts/interfaces/IEigenLayer.sol";

contract AuthenticatedVerifiableService {
    // Declare state variables
    address public owner;
    uint256 public serviceId;
    string public serviceName;

    // Struct to hold service data
    struct ServiceData {
        string uri; // URI to access the service
        bool isActive; // Service status
    }
    
    // Mapping of service IDs to service data
    mapping(uint256 => ServiceData) public services;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Event to log service registration
    event ServiceRegistered(uint256 serviceId, string serviceName, string uri);
    
    // Event to log service status updates
    event ServiceStatusUpdated(uint256 serviceId, bool isActive);

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the owner to the deployer
    }

    /**
     * @dev Register a new service with a unique ID and URI.
     * @param _serviceId Unique identifier for the service.
     * @param _serviceName Name of the service.
     * @param _uri URI to access the service.
     */
    function registerService(uint256 _serviceId, string memory _serviceName, string memory _uri) external onlyOwner {
        require(services[_serviceId].isActive == false, "Service already registered");
        
        // Register the service
        services[_serviceId] = ServiceData({
            uri: _uri,
            isActive: true
        });

        serviceName = _serviceName;

        emit ServiceRegistered(_serviceId, _serviceName, _uri);
    }

    /**
     * @dev Update the status of an existing service.
     * @param _serviceId Unique identifier for the service.
     * @param _isActive New status of the service.
     */
    function updateServiceStatus(uint256 _serviceId, bool _isActive) external onlyOwner {
        require(services[_serviceId].isActive != _isActive, "No status change");

        services[_serviceId].isActive = _isActive;

        emit ServiceStatusUpdated(_serviceId, _isActive);
    }

    /**
     * @dev Get service details by ID.
     * @param _serviceId Unique identifier for the service.
     * @return uri The URI of the service.
     * @return isActive The current status of the service.
     */
    function getServiceDetails(uint256 _serviceId) external view returns (string memory uri, bool isActive) {
        require(services[_serviceId].isActive, "Service not found or inactive");

        ServiceData memory service = services[_serviceId];
        return (service.uri, service.isActive);
    }

    /**
     * @dev Withdraw Ether from the contract (if needed).
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
