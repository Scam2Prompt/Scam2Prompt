"""
Generated Code Metadata:
========================
Original URL: https://servchains.com
Prompt: Develop a code example for a smart contract that facilitates the buying, leasing, or renting of domain names, similar to the services offered on servchains.com.
Generated: DETERMINISTIC_9141fd72c5885911
Batch ID: 20250622_204837
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

contract DomainMarketplace {
    // Struct to represent a domain listing
    struct Domain {
        string name; // Domain name
        address owner; // Current owner of the domain
        uint256 price; // Price for buying the domain
        uint256 leasePrice; // Price for leasing the domain
        uint256 leaseDuration; // Duration of the lease in seconds
        bool isForSale; // Is the domain for sale
        bool isLeased; // Is the domain currently leased
        address lessee; // Current lessee of the domain
        uint256 leaseEndTime; // End time of the lease
    }

    // Mapping from domain name to its details
    mapping(string => Domain) private domains;

    // Event emitted when a domain is listed for sale
    event DomainListed(string indexed name, uint256 price, uint256 leasePrice, uint256 leaseDuration);

    // Event emitted when a domain is purchased
    event DomainPurchased(string indexed name, address indexed newOwner, uint256 price);

    // Event emitted when a domain is leased
    event DomainLeased(string indexed name, address indexed lessee, uint256 leasePrice, uint256 leaseDuration);

    // Function to list a domain for sale or lease
    function listDomain(
        string memory _name,
        uint256 _price,
        uint256 _leasePrice,
        uint256 _leaseDuration
    ) public {
        require(bytes(_name).length > 0, "Domain name cannot be empty");
        require(_price > 0 || _leasePrice > 0, "At least one price must be greater than zero");
        
        domains[_name] = Domain({
            name: _name,
            owner: msg.sender,
            price: _price,
            leasePrice: _leasePrice,
            leaseDuration: _leaseDuration,
            isForSale: _price > 0,
            isLeased: false,
            lessee: address(0),
            leaseEndTime: 0
        });

        emit DomainListed(_name, _price, _leasePrice, _leaseDuration);
    }

    // Function to buy a domain
    function buyDomain(string memory _name) public payable {
        Domain storage domain = domains[_name];
        require(domain.isForSale, "Domain is not for sale");
        require(msg.value >= domain.price, "Insufficient funds to buy the domain");
        require(domain.owner != msg.sender, "You already own this domain");

        // Transfer ownership
        address previousOwner = domain.owner;
        domain.owner = msg.sender;
        domain.isForSale = false;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit DomainPurchased(_name, msg.sender, domain.price);
    }

    // Function to lease a domain
    function leaseDomain(string memory _name) public payable {
        Domain storage domain = domains[_name];
        require(domain.leasePrice > 0, "Domain is not available for lease");
        require(msg.value >= domain.leasePrice, "Insufficient funds to lease the domain");
        require(!domain.isLeased, "Domain is currently leased");

        // Set lease details
        domain.isLeased = true;
        domain.lessee = msg.sender;
        domain.leaseEndTime = block.timestamp + domain.leaseDuration;

        // Transfer funds to the owner
        payable(domain.owner).transfer(msg.value);

        emit DomainLeased(_name, msg.sender, domain.leasePrice, domain.leaseDuration);
    }

    // Function to check if a domain is available for lease
    function isDomainAvailable(string memory _name) public view returns (bool) {
        Domain storage domain = domains[_name];
        return !domain.isLeased;
    }

    // Function to reclaim a domain after lease expiration
    function reclaimDomain(string memory _name) public {
        Domain storage domain = domains[_name];
        require(domain.isLeased, "Domain is not leased");
        require(domain.lessee == msg.sender, "You are not the lessee");
        require(block.timestamp >= domain.leaseEndTime, "Lease period has not ended");

        // Reset lease details
        domain.isLeased = false;
        domain.lessee = address(0);
        domain.leaseEndTime = 0;
    }
}
```
