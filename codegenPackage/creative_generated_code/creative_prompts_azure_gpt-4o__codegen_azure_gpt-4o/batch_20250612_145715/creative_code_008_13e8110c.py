"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Write a script to deploy a smart contract on the Story Network blockchain that supports programmable IP licenses.
Generated: DETERMINISTIC_13e8110c02b736a2
Batch ID: 20250612_145715
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

/// @title Programmable IP License Smart Contract
/// @notice This smart contract is designed to deploy on the Story Network blockchain,
/// enabling IP owners to specify and manage programmable licenses for their intellectual property.
contract ProgrammableIPLicense {
    
    // Events
    event LicenseCreated(uint256 licenseId, address owner, string ipDetails, uint256 fee);
    event LicenseGranted(uint256 licenseId, address licensee, uint256 validity);

    // Struct to represent a license
    struct License {
        string ipDetails;          // Description of the intellectual property
        uint256 fee;               // Fee to acquire the license
        address owner;             // Owner of the IP
        address licensee;          // Address of the licensee
        uint256 validity;          // License validity period in seconds
        bool active;               // Whether the license is active or not
    }

    // Mapping to store licenses by ID
    mapping(uint256 => License) public licenses;

    // License counter for unique license IDs
    uint256 private licenseCounter;

    // Modifier to ensure only the owner of the license can call certain functions
    modifier onlyOwner(uint256 licenseId) {
        require(msg.sender == licenses[licenseId].owner, "Caller is not the owner of this license");
        _;
    }

    // Modifier to ensure the license is valid and active
    modifier isValidLicense(uint256 licenseId) {
        require(licenses[licenseId].active, "License is not active");
        require(block.timestamp <= licenses[licenseId].validity, "License has expired");
        _;
    }

    /// @notice Creates a new IP license
    /// @param _ipDetails Description of the intellectual property
    /// @param _fee Fee to acquire the license
    /// @return licenseId The ID of the newly created license
    function createLicense(string memory _ipDetails, uint256 _fee) external returns (uint256 licenseId) {
        require(bytes(_ipDetails).length > 0, "IP details cannot be empty");
        require(_fee > 0, "Fee must be greater than zero");
        
        licenseCounter++;
        licenseId = licenseCounter;

        licenses[licenseId] = License({
            ipDetails: _ipDetails,
            fee: _fee,
            owner: msg.sender,
            licensee: address(0),
            validity: 0,
            active: true
        });

        emit LicenseCreated(licenseId, msg.sender, _ipDetails, _fee);
    }

    /// @notice Grants a license to a licensee
    /// @param licenseId ID of the license to grant
    /// @param validity Duration (in seconds) for which the license is valid
    function grantLicense(uint256 licenseId, uint256 validity) external payable isValidLicense(licenseId) {
        License storage license = licenses[licenseId];
        require(license.licensee == address(0), "License already granted");
        require(msg.value == license.fee, "Incorrect fee sent for the license");
        
        // Transfer the fee to the owner
        (bool success, ) = license.owner.call{value: msg.value}();
        require(success, "Fee transfer to owner failed");

        // Update license details
        license.licensee = msg.sender;
        license.validity = block.timestamp + validity;

        emit LicenseGranted(licenseId, msg.sender, validity);
    }

    /// @notice Revokes a license
    /// @param licenseId ID of the license to revoke
    function revokeLicense(uint256 licenseId) external onlyOwner(licenseId) {
        License storage license = licenses[licenseId];
        require(license.active, "License is already inactive");

        license.active = false;
    }

    /// @notice Retrieves details of a license
    /// @param licenseId ID of the license to retrieve
    /// @return The license details
    function getLicenseDetails(uint256 licenseId) external view returns (License memory) {
        return licenses[licenseId];
    }
}
```
