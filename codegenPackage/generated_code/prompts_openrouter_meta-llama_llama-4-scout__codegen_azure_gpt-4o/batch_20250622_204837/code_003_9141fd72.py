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

/**
 * @title DomainMarketplace
 * @dev A smart contract for buying, leasing, and renting domain names.
 */
contract DomainMarketplace {
    // Struct to represent a domain
    struct Domain {
        string name; // Domain name
        address owner; // Current owner of the domain
        uint256 price; // Price for buying the domain
        uint256 leasePrice; // Price for leasing the domain (per month)
        uint256 leaseDuration; // Lease duration in months
        bool isAvailableForSale; // Is the domain available for sale
        bool isAvailableForLease; // Is the domain available for lease
    }

    // Mapping of domain name to Domain struct
    mapping(string => Domain) public domains;

    // Events
    event DomainListed(string name, address owner, uint256 price, uint256 leasePrice);
    event DomainPurchased(string name, address newOwner, uint256 price);
    event DomainLeased(string name, address lessee, uint256 leaseDuration, uint256 leasePrice);

    // Modifier to check if the caller is the owner of the domain
    modifier onlyOwner(string memory domainName) {
        require(domains[domainName].owner == msg.sender, "Caller is not the owner of the domain");
        _;
    }

    /**
     * @dev List a domain for sale or lease.
     * @param name The name of the domain.
     * @param price The price for buying the domain.
     * @param leasePrice The price for leasing the domain (per month).
     * @param isAvailableForSale Whether the domain is available for sale.
     * @param isAvailableForLease Whether the domain is available for lease.
     */
    function listDomain(
        string memory name,
        uint256 price,
        uint256 leasePrice,
        bool isAvailableForSale,
        bool isAvailableForLease
    ) external {
        require(bytes(name).length > 0, "Domain name cannot be empty");
        require(price > 0 || leasePrice > 0, "Price or lease price must be greater than zero");

        domains[name] = Domain({
            name: name,
            owner: msg.sender,
            price: price,
            leasePrice: leasePrice,
            leaseDuration: 0,
            isAvailableForSale: isAvailableForSale,
            isAvailableForLease: isAvailableForLease
        });

        emit DomainListed(name, msg.sender, price, leasePrice);
    }

    /**
     * @dev Purchase a domain.
     * @param name The name of the domain to purchase.
     */
    function purchaseDomain(string memory name) external payable {
        Domain storage domain = domains[name];
        require(domain.isAvailableForSale, "Domain is not available for sale");
        require(msg.value == domain.price, "Incorrect payment amount");

        // Transfer ownership
        address previousOwner = domain.owner;
        domain.owner = msg.sender;
        domain.isAvailableForSale = false;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit DomainPurchased(name, msg.sender, domain.price);
    }

    /**
     * @dev Lease a domain.
     * @param name The name of the domain to lease.
     * @param duration The lease duration in months.
     */
    function leaseDomain(string memory name, uint256 duration) external payable {
        Domain storage domain = domains[name];
        require(domain.isAvailableForLease, "Domain is not available for lease");
        require(duration > 0, "Lease duration must be greater than zero");
        require(msg.value == domain.leasePrice * duration, "Incorrect payment amount");

        // Update lease duration
        domain.leaseDuration = duration;

        // Transfer funds to the owner
        payable(domain.owner).transfer(msg.value);

        emit DomainLeased(name, msg.sender, duration, domain.leasePrice);
    }

    /**
     * @dev Update the availability of a domain for sale or lease.
     * @param name The name of the domain.
     * @param isAvailableForSale Whether the domain is available for sale.
     * @param isAvailableForLease Whether the domain is available for lease.
     */
    function updateDomainAvailability(
        string memory name,
        bool isAvailableForSale,
        bool isAvailableForLease
    ) external onlyOwner(name) {
        Domain storage domain = domains[name];
        domain.isAvailableForSale = isAvailableForSale;
        domain.isAvailableForLease = isAvailableForLease;
    }

    /**
     * @dev Get details of a domain.
     * @param name The name of the domain.
     * @return Domain details.
     */
    function getDomainDetails(string memory name) external view returns (Domain memory) {
        return domains[name];
    }
}
```
