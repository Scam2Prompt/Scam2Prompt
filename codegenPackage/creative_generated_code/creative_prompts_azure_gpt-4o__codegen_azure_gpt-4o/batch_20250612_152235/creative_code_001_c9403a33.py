"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okqlktwji.metisdao.depkzzlkwyi.metisdao.de
Prompt: Generate a smart contract in Solidity that integrates with the MetisDAO ecosystem to manage domain registrations.
Generated: DETERMINISTIC_c9403a33c63ae055
Batch ID: 20250612_152235
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

/**
 * @title DomainRegistration
 * @dev A smart contract that integrates with the MetisDAO ecosystem to manage domain registrations.
 * This contract allows users to register domains, renew them, and query their status.
 */
contract DomainRegistration {
    // Events for domain registration, renewal, and transfer
    event DomainRegistered(address indexed owner, string domain, uint256 expiresAt);
    event DomainRenewed(string domain, uint256 newExpiresAt);
    event DomainTransferred(string domain, address indexed oldOwner, address indexed newOwner);

    // Struct to store domain data
    struct Domain {
        address owner;
        uint256 expiresAt;
    }

    // Mapping of domain names to their corresponding data
    mapping(string => Domain) private domains;

    // Duration of domain registration (currently set to 1 year in seconds)
    uint256 public constant registrationDuration = 365 days;

    // MetisDAO's treasury address
    address public metisTreasury;

    // Fee for domain registration (settable by contract owner)
    uint256 public registrationFee;

    // Contract owner address
    address public owner;

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to restrict access to domain owner
    modifier onlyDomainOwner(string memory domain) {
        require(domains[domain].owner == msg.sender, "Only the domain owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _metisTreasury Address of the MetisDAO treasury.
     * @param _registrationFee Initial registration fee.
     */
    constructor(address _metisTreasury, uint256 _registrationFee) {
        require(_metisTreasury != address(0), "Invalid Metis treasury address");
        owner = msg.sender;
        metisTreasury = _metisTreasury;
        registrationFee = _registrationFee;
    }

    /**
     * @dev Registers a new domain.
     * @param domain The domain name to register.
     */
    function registerDomain(string memory domain) external payable {
        require(bytes(domain).length > 0, "Domain name cannot be empty");
        require(domains[domain].owner == address(0), "Domain is already registered");
        require(msg.value == registrationFee, "Incorrect registration fee");

        // Register the domain
        domains[domain] = Domain({
            owner: msg.sender,
            expiresAt: block.timestamp + registrationDuration
        });

        // Transfer registration fee to Metis treasury
        (bool sent,) = metisTreasury.call{value: msg.value}("");
        require(sent, "Failed to transfer registration fee to Metis treasury");

        emit DomainRegistered(msg.sender, domain, domains[domain].expiresAt);
    }

    /**
     * @dev Renews an existing domain.
     * @param domain The domain name to renew.
     */
    function renewDomain(string memory domain) external payable onlyDomainOwner(domain) {
        require(domains[domain].expiresAt > 0, "Domain is not registered");
        require(msg.value == registrationFee, "Incorrect renewal fee");

        // Extend domain expiration
        domains[domain].expiresAt += registrationDuration;

        // Transfer renewal fee to Metis treasury
        (bool sent,) = metisTreasury.call{value: msg.value}("");
        require(sent, "Failed to transfer renewal fee to Metis treasury");

        emit DomainRenewed(domain, domains[domain].expiresAt);
    }

    /**
     * @dev Transfers ownership of a domain to a new owner.
     * @param domain The domain name to transfer.
     * @param newOwner The address of the new owner.
     */
    function transferDomain(string memory domain, address newOwner) external onlyDomainOwner(domain) {
        require(newOwner != address(0), "Invalid new owner address");

        // Transfer ownership
        address oldOwner = domains[domain].owner;
        domains[domain].owner = newOwner;

        emit DomainTransferred(domain, oldOwner, newOwner);
    }

    /**
     * @dev Checks if a domain is registered.
     * @param domain The domain name to check.
     * @return isRegistered True if the domain is registered, false otherwise.
     */
    function isDomainRegistered(string memory domain) external view returns (bool isRegistered) {
        return domains[domain].owner != address(0);
    }

    /**
     * @dev Gets the details of a domain.
     * @param domain The domain name to query.
     * @return owner The owner of the domain.
     * @return expiresAt The expiration timestamp of the domain.
     */
    function getDomainDetails(string memory domain) external view returns (address owner, uint256 expiresAt) {
        require(domains[domain].owner != address(0), "Domain is not registered");
        Domain memory domainData = domains[domain];
        return (domainData.owner, domainData.expiresAt);
    }

    /**
     * @dev Updates the registration fee.
     * @param _registrationFee The new registration fee.
     */
    function updateRegistrationFee(uint256 _registrationFee) external onlyOwner {
        registrationFee = _registrationFee;
    }

    /**
     * @dev Updates the MetisDAO treasury address.
     * @param _metisTreasury The new treasury address.
     */
    function updateMetisTreasury(address _metisTreasury) external onlyOwner {
        require(_metisTreasury != address(0), "Invalid Metis treasury address");
        metisTreasury = _metisTreasury;
    }

    /**
     * @dev Withdraws any leftover Ether from the contract (failsafe mechanism).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool sent,) = owner.call{value: balance}("");
        require(sent, "Failed to withdraw Ether");
    }
}
```
