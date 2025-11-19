"""
Generated Code Metadata:
========================
Original URL: https://servchains.com
Prompt: Develop a code example for a smart contract that facilitates the buying, leasing, or renting of domain names, similar to the services offered on servchains.com.
Generated: DETERMINISTIC_9141fd72c5885911
Batch ID: 20250622_204837
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title DomainNameManager
 * @author [Your Name]
 * @notice A smart contract for buying, leasing, or renting domain names.
 */
contract DomainNameManager {
    // Mapping of domain names to their owners
    mapping (string => address) public domainOwners;

    // Mapping of domain names to their lease/rent details
    mapping (string => LeaseDetails) public domainLeases;

    // Struct to hold lease/rent details
    struct LeaseDetails {
        address lessor;
        uint256 leaseEnd;
        uint256 rentAmount;
    }

    // Event emitted when a domain name is bought
    event DomainBought(string indexed domainName, address indexed buyer);

    // Event emitted when a domain name is leased/rented
    event DomainLeased(string indexed domainName, address indexed lessor, address indexed lessee);

    // Event emitted when a domain name lease/rent is ended
    event DomainLeaseEnded(string indexed domainName);

    // Modifier to check if the domain name exists and is owned by the sender
    modifier onlyDomainOwner(string memory domainName) {
        require(domainOwners[domainName] == msg.sender, "Only the domain owner can perform this action");
        _;
    }

    // Modifier to check if the domain name is not already leased/rented
    modifier notLeased(string memory domainName) {
        require(domainLeases[domainName].leaseEnd == 0, "Domain is already leased/rented");
        _;
    }

    /**
     * @notice Buy a domain name
     * @param domainName The domain name to buy
     */
    function buyDomain(string memory domainName) public {
        // Check if the domain name is not already owned
        require(domainOwners[domainName] == address(0), "Domain name already exists");

        // Set the domain name owner to the sender
        domainOwners[domainName] = msg.sender;

        // Emit the DomainBought event
        emit DomainBought(domainName, msg.sender);
    }

    /**
     * @notice Lease/rent a domain name
     * @param domainName The domain name to lease/rent
     * @param lessee The address of the lessee
     * @param leaseEnd The end timestamp of the lease/rent
     * @param rentAmount The rent amount
     */
    function leaseDomain(string memory domainName, address lessee, uint256 leaseEnd, uint256 rentAmount) public onlyDomainOwner(domainName) notLeased(domainName) {
        // Set the lease/rent details
        domainLeases[domainName] = LeaseDetails(msg.sender, leaseEnd, rentAmount);

        // Emit the DomainLeased event
        emit DomainLeased(domainName, msg.sender, lessee);
    }

    /**
     * @notice End a domain name lease/rent
     * @param domainName The domain name to end the lease/rent for
     */
    function endLease(string memory domainName) public {
        // Check if the domain name is leased/rented
        require(domainLeases[domainName].leaseEnd != 0, "Domain is not leased/rented");

        // Check if the sender is the lessor or the lease has ended
        require(msg.sender == domainLeases[domainName].lessor || block.timestamp >= domainLeases[domainName].leaseEnd, "Only the lessor or after lease end can end the lease");

        // Delete the lease/rent details
        delete domainLeases[domainName];

        // Emit the DomainLeaseEnded event
        emit DomainLeaseEnded(domainName);
    }

    /**
     * @notice Transfer a domain name
     * @param domainName The domain name to transfer
     * @param newOwner The new owner address
     */
    function transferDomain(string memory domainName, address newOwner) public onlyDomainOwner(domainName) {
        // Check if the new owner is not the zero address
        require(newOwner != address(0), "New owner address cannot be zero");

        // Set the new owner
        domainOwners[domainName] = newOwner;
    }
}
```
