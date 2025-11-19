"""
Generated Code Metadata:
========================
Original URL: https://flareairdrop.com
Prompt: Write a Solidity contract that utilizes Flare's layer-1 smart contract platform to implement a decentralized cloud service.
Generated: DETERMINISTIC_53232a35e33a2fc1
Batch ID: 20250612_152018
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

// Contract for a decentralized cloud service
contract DecentralizedCloudService is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a cloud service
    struct CloudService {
        uint256 id;
        string name;
        string description;
        address provider;
        uint256 price; // Price in wei
        bool isActive;
    }

    // Mapping to store cloud services by their ID
    mapping(uint256 => CloudService) private services;
    Counters.Counter private serviceIdCounter;

    // Event emitted when a new service is created
    event ServiceCreated(uint256 indexed id, string name, address indexed provider, uint256 price);
    
    // Event emitted when a service is updated
    event ServiceUpdated(uint256 indexed id, string name, uint256 price, bool isActive);
    
    // Event emitted when a service is deleted
    event ServiceDeleted(uint256 indexed id);

    // Function to create a new cloud service
    function createService(string memory _name, string memory _description, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        // Increment the service ID counter and create a new service
        serviceIdCounter.increment();
        uint256 newServiceId = serviceIdCounter.current();

        services[newServiceId] = CloudService({
            id: newServiceId,
            name: _name,
            description: _description,
            provider: msg.sender,
            price: _price,
            isActive: true
        });

        emit ServiceCreated(newServiceId, _name, msg.sender, _price);
    }

    // Function to update an existing cloud service
    function updateService(uint256 _id, string memory _name, uint256 _price, bool _isActive) external onlyOwner {
        CloudService storage service = services[_id];
        require(service.provider == msg.sender, "Only the provider can update the service");
        require(service.id != 0, "Service does not exist");

        service.name = _name;
        service.price = _price;
        service.isActive = _isActive;

        emit ServiceUpdated(_id, _name, _price, _isActive);
    }

    // Function to delete a cloud service
    function deleteService(uint256 _id) external onlyOwner {
        CloudService storage service = services[_id];
        require(service.id != 0, "Service does not exist");

        delete services[_id];

        emit ServiceDeleted(_id);
    }

    // Function to retrieve service details
    function getService(uint256 _id) external view returns (CloudService memory) {
        CloudService memory service = services[_id];
        require(service.id != 0, "Service does not exist");
        return service;
    }

    // Function to retrieve all active services
    function getActiveServices() external view returns (CloudService[] memory) {
        uint256 totalServices = serviceIdCounter.current();
        CloudService[] memory activeServices = new CloudService[](totalServices);
        uint256 count = 0;

        for (uint256 i = 1; i <= totalServices; i++) {
            if (services[i].isActive) {
                activeServices[count] = services[i];
                count++;
            }
        }

        // Resize the array to the actual number of active services
        assembly {
            mstore(activeServices, count)
        }

        return activeServices;
    }
}
```
