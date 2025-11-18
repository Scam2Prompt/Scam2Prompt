"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Develop a Solidity-based smart contract for AKCB partnerships, enabling collaboration with brands and startups while tracking shared ownership of creative works.
Generated: DETERMINISTIC_1dae343e6fa673ea
Batch ID: 20250612_150226
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

/// @title AKCB Partnerships Smart Contract
/// @author Your Name
/// @notice This contract enables collaboration between brands and startups
/// while tracking shared ownership of creative works.
contract AKCBPartnerships {
    // Event emitted when a new partnership is created
    event PartnershipCreated(uint256 indexed partnershipId, address indexed brand, address indexed startup, string creativeWork);
    
    // Event emitted when ownership is transferred
    event OwnershipTransferred(uint256 indexed partnershipId, address indexed newOwner);
    
    // Structure to hold partnership data
    struct Partnership {
        address brand;
        address startup;
        string creativeWork;
        uint256 ownershipFraction; // Ownership represented as a percentage (0-100)
        bool isActive;              // Status of the partnership
    }

    // Mapping of partnership ID to Partnership details
    mapping(uint256 => Partnership) public partnerships;
    uint256 public nextPartnershipId; // Counter for partnership IDs

    /// @dev Modifier to check if the caller is the brand of the partnership
    modifier onlyBrand(uint256 partnershipId) {
        require(msg.sender == partnerships[partnershipId].brand, "Caller is not the brand");
        _;
    }

    /// @dev Modifier to check if the caller is the startup of the partnership
    modifier onlyStartup(uint256 partnershipId) {
        require(msg.sender == partnerships[partnershipId].startup, "Caller is not the startup");
        _;
    }

    /// @dev Creates a new partnership
    /// @param _startup The address of the startup involved in the partnership
    /// @param _creativeWork The title or description of the creative work
    /// @param _ownershipFraction The percentage of ownership (0-100)
    function createPartnership(address _startup, string memory _creativeWork, uint256 _ownershipFraction) public {
        require(_startup != address(0), "Invalid startup address");
        require(_ownershipFraction <= 100, "Ownership fraction must be between 0 and 100");

        // Create a new partnership
        partnerships[nextPartnershipId] = Partnership({
            brand: msg.sender,
            startup: _startup,
            creativeWork: _creativeWork,
            ownershipFraction: _ownershipFraction,
            isActive: true
        });

        emit PartnershipCreated(nextPartnershipId, msg.sender, _startup, _creativeWork);
        nextPartnershipId++;
    }

    /// @dev Transfers ownership of the creative work to a new owner
    /// @param partnershipId The ID of the partnership
    /// @param newOwner The address of the new owner
    function transferOwnership(uint256 partnershipId, address newOwner) public onlyBrand(partnershipId) {
        require(newOwner != address(0), "Invalid new owner address");

        // Update the startup in the partnership
        partnerships[partnershipId].startup = newOwner;
        
        emit OwnershipTransferred(partnershipId, newOwner);
    }

    /// @dev Deactivates a partnership
    /// @param partnershipId The ID of the partnership to deactivate
    function deactivatePartnership(uint256 partnershipId) public onlyBrand(partnershipId) {
        partnerships[partnershipId].isActive = false;
    }

    /// @dev Retrieves partnership details
    /// @param partnershipId The ID of the partnership
    /// @return brand The address of the brand
    /// @return startup The address of the startup
    /// @return creativeWork The creative work description
    /// @return ownershipFraction The ownership fraction
    /// @return isActive The active status of the partnership
    function getPartnership(uint256 partnershipId) public view returns (address brand, address startup, string memory creativeWork, uint256 ownershipFraction, bool isActive) {
        Partnership memory partnership = partnerships[partnershipId];
        return (partnership.brand, partnership.startup, partnership.creativeWork, partnership.ownershipFraction, partnership.isActive);
    }
}
```
