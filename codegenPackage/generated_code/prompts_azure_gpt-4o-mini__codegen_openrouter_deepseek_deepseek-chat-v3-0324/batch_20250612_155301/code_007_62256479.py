"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: How can I implement an open, permissionless DNS using Ethereum technology?
Generated: DETERMINISTIC_6225647943d40c07
Batch ID: 20250612_155301
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
 * @title PermissionlessDNS
 * @dev A decentralized DNS system on Ethereum allowing anyone to register and resolve domain names
 */
contract PermissionlessDNS {
    // Domain struct to store domain information
    struct Domain {
        address owner;
        string ipAddress;
        uint256 registrationTimestamp;
        uint256 expirationTimestamp;
    }

    // Mapping from domain name to Domain struct
    mapping(string => Domain) public domains;

    // Event emitted when a domain is registered
    event DomainRegistered(
        string indexed domainName,
        address indexed owner,
        string ipAddress,
        uint256 registrationTimestamp,
        uint256 expirationTimestamp
    );

    // Event emitted when a domain is updated
    event DomainUpdated(
        string indexed domainName,
        address indexed owner,
        string ipAddress
    );

    // Event emitted when a domain is transferred
    event DomainTransferred(
        string indexed domainName,
        address indexed oldOwner,
        address indexed newOwner
    );

    // Minimum registration duration in seconds (1 year)
    uint256 public constant MIN_REGISTRATION_DURATION = 365 days;

    // Domain registration fee in wei
    uint256 public registrationFee;

    // Contract owner
    address public owner;

    /**
     * @dev Constructor sets the initial registration fee and contract owner
     * @param _registrationFee Initial registration fee in wei
     */
    constructor(uint256 _registrationFee) {
        registrationFee = _registrationFee;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to check if the caller is the domain owner
     * @param domainName The domain name to check ownership of
     */
    modifier onlyDomainOwner(string memory domainName) {
        require(
            domains[domainName].owner == msg.sender,
            "PermissionlessDNS: Caller is not the domain owner"
        );
        _;
    }

    /**
     * @dev Modifier to check if the caller is the contract owner
     */
    modifier onlyOwner() {
        require(
            msg.sender == owner,
            "PermissionlessDNS: Caller is not the contract owner"
        );
        _;
    }

    /**
     * @dev Register a new domain or renew an existing one
     * @param domainName The domain name to register
     * @param ipAddress The IP address associated with the domain
     * @param duration The duration to register the domain for (in seconds)
     */
    function registerDomain(
        string memory domainName,
        string memory ipAddress,
        uint256 duration
    ) external payable {
        require(
            bytes(domainName).length > 0,
            "PermissionlessDNS: Domain name cannot be empty"
        );
        require(
            bytes(ipAddress).length > 0,
            "PermissionlessDNS: IP address cannot be empty"
        );
        require(
            duration >= MIN_REGISTRATION_DURATION,
            "PermissionlessDNS: Registration duration too short"
        );
        require(
            msg.value >= registrationFee,
            "PermissionlessDNS: Insufficient registration fee"
        );

        Domain storage domain = domains[domainName];

        // If domain exists, only owner can renew
        if (domain.owner != address(0)) {
            require(
                domain.owner == msg.sender,
                "PermissionlessDNS: Only domain owner can renew"
            );
            require(
                block.timestamp >= domain.expirationTimestamp,
                "PermissionlessDNS: Domain not yet expired"
            );
        }

        uint256 currentTimestamp = block.timestamp;
        uint256 expirationTimestamp = currentTimestamp + duration;

        domain.owner = msg.sender;
        domain.ipAddress = ipAddress;
        domain.registrationTimestamp = currentTimestamp;
        domain.expirationTimestamp = expirationTimestamp;

        emit DomainRegistered(
            domainName,
            msg.sender,
            ipAddress,
            currentTimestamp,
            expirationTimestamp
        );
    }

    /**
     * @dev Update the IP address of a domain
     * @param domainName The domain name to update
     * @param newIpAddress The new IP address for the domain
     */
    function updateDomain(
        string memory domainName,
        string memory newIpAddress
    ) external onlyDomainOwner(domainName) {
        require(
            bytes(newIpAddress).length > 0,
            "PermissionlessDNS: IP address cannot be empty"
        );
        require(
            block.timestamp < domains[domainName].expirationTimestamp,
            "PermissionlessDNS: Domain has expired"
        );

        domains[domainName].ipAddress = newIpAddress;

        emit DomainUpdated(domainName, msg.sender, newIpAddress);
    }

    /**
     * @dev Transfer domain ownership to another address
     * @param domainName The domain name to transfer
     * @param newOwner The address of the new owner
     */
    function transferDomainOwnership(
        string memory domainName,
        address newOwner
    ) external onlyDomainOwner(domainName) {
        require(
            newOwner != address(0),
            "PermissionlessDNS: New owner cannot be zero address"
        );
        require(
            block.timestamp < domains[domainName].expirationTimestamp,
            "PermissionlessDNS: Domain has expired"
        );

        address oldOwner = domains[domainName].owner;
        domains[domainName].owner = newOwner;

        emit DomainTransferred(domainName, oldOwner, newOwner);
    }

    /**
     * @dev Resolve a domain name to its IP address
     * @param domainName The domain name to resolve
     * @return The IP address associated with the domain
     */
    function resolveDomain(
        string memory domainName
    ) external view returns (string memory) {
        require(
            domains[domainName].owner != address(0),
            "PermissionlessDNS: Domain not registered"
        );
        require(
            block.timestamp < domains[domainName].expirationTimestamp,
            "PermissionlessDNS: Domain has expired"
        );

        return domains[domainName].ipAddress;
    }

    /**
     * @dev Set a new registration fee (only callable by owner)
     * @param newFee The new registration fee in wei
     */
    function setRegistrationFee(uint256 newFee) external onlyOwner {
        registrationFee = newFee;
    }

    /**
     * @dev Withdraw contract balance (only callable by owner)
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Get domain information
     * @param domainName The domain name to query
     * @return owner The owner of the domain
     * @return ipAddress The IP address associated with the domain
     * @return registrationTimestamp When the domain was registered
     * @return expirationTimestamp When the domain expires
     */
    function getDomainInfo(
        string memory domainName
    )
        external
        view
        returns (
            address owner,
            string memory ipAddress,
            uint256 registrationTimestamp,
            uint256 expirationTimestamp
        )
    {
        Domain memory domain = domains[domainName];
        return (
            domain.owner,
            domain.ipAddress,
            domain.registrationTimestamp,
            domain.expirationTimestamp
        );
    }
}
```
