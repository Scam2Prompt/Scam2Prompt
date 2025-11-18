"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okqlktwji.metisdao.depkzzlkwyi.metisdao.de
Prompt: Write a Solidity function to fetch and validate domain details stored on the MetisDAO blockchain.
Generated: DETERMINISTIC_c9c468c4143d2180
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
 * @title DomainManager
 * @dev A contract to fetch and validate domain details stored on the MetisDAO blockchain.
 */
contract DomainManager {
    // Struct to store domain details
    struct Domain {
        string name;         // Domain name
        string owner;        // Owner of the domain
        uint256 expiryDate;  // Expiry date of the domain (UNIX timestamp)
        bool isValid;        // Validation flag
    }

    // Mapping to store domain details by domain ID
    mapping(uint256 => Domain) private domains;

    // Event emitted when a domain is fetched and validated
    event DomainValidated(uint256 indexed domainId, string name, bool isValid);

    /**
     * @dev Fetch and validate domain details.
     * @param domainId The ID of the domain to fetch.
     * @return name The name of the domain.
     * @return owner The owner of the domain.
     * @return expiryDate The expiry date of the domain.
     * @return isValid Whether the domain is valid.
     */
    function fetchAndValidateDomain(uint256 domainId)
        external
        view
        returns (string memory name, string memory owner, uint256 expiryDate, bool isValid)
    {
        // Ensure the domain exists
        require(bytes(domains[domainId].name).length > 0, "Domain does not exist");

        // Fetch the domain details
        Domain memory domain = domains[domainId];

        // Validate the domain based on expiry date
        bool domainValidity = domain.expiryDate > block.timestamp;

        // Return domain details and validation result
        return (domain.name, domain.owner, domain.expiryDate, domainValidity);
    }

    /**
     * @dev Add a new domain to the contract (only for demonstration purposes).
     * @param domainId The ID of the domain.
     * @param name The name of the domain.
     * @param owner The owner of the domain.
     * @param expiryDate The expiry date of the domain.
     */
    function addDomain(uint256 domainId, string memory name, string memory owner, uint256 expiryDate) external {
        // Ensure the domain ID does not already exist
        require(bytes(domains[domainId].name).length == 0, "Domain ID already exists");

        // Add the domain
        domains[domainId] = Domain({
            name: name,
            owner: owner,
            expiryDate: expiryDate,
            isValid: true
        });
    }

    /**
     * @dev Update the validation flag of a domain manually.
     * @param domainId The ID of the domain to update.
     * @param isValid The new validation status.
     */
    function updateDomainValidation(uint256 domainId, bool isValid) external {
        // Ensure the domain exists
        require(bytes(domains[domainId].name).length > 0, "Domain does not exist");

        // Update the domain validation status
        domains[domainId].isValid = isValid;
    }
}
```
