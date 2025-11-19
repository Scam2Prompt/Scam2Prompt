"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: How can I implement an open, permissionless DNS using Ethereum technology?
Generated: DETERMINISTIC_6225647943d40c07
Batch ID: 20250612_155301
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

// OpenDNS is a simple smart contract for storing domain names and their corresponding Ethereum addresses.
contract OpenDNS {
    // Mapping from domain names to addresses
    mapping(string => address) private domainToAddress;

    // Event to log when a domain is registered
    event DomainRegistered(string domain, address owner);

    // Event to log when a domain is updated
    event DomainUpdated(string domain, address newOwner);

    // Error to be thrown when the domain is already taken
    error DomainAlreadyTaken(string domain);

    // Error to be thrown when the domain is not registered
    error DomainNotRegistered(string domain);

    // Register a new domain
    function registerDomain(string calldata domain) external {
        // Check if the domain is already taken
        if (domainToAddress[domain] != address(0)) {
            revert DomainAlreadyTaken(domain);
        }

        // Set the caller as the owner of the domain
        domainToAddress[domain] = msg.sender;

        // Emit the DomainRegistered event
        emit DomainRegistered(domain, msg.sender);
    }

    // Update the owner of an existing domain
    function updateDomain(string calldata domain, address newOwner) external {
        // Ensure the domain is registered
        if (domainToAddress[domain] == address(0)) {
            revert DomainNotRegistered(domain);
        }

        // Ensure the caller is the owner of the domain
        require(domainToAddress[domain] == msg.sender, "Only the owner can update the domain");

        // Update the domain ownership
        domainToAddress[domain] = newOwner;

        // Emit the DomainUpdated event
        emit DomainUpdated(domain, newOwner);
    }

    // Retrieve the owner of a domain
    function getDomainOwner(string calldata domain) external view returns (address) {
        // Check if the domain is registered
        if (domainToAddress[domain] == address(0)) {
            revert DomainNotRegistered(domain);
        }

        return domainToAddress[domain];
    }
}
```
