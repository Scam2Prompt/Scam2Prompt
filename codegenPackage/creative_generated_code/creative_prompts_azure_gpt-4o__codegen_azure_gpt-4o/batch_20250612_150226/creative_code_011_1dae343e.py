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

/**
 * @title AKCBPartnerships
 * @dev A Solidity smart contract to enable collaboration with brands and startups,
 *      while tracking shared ownership of creative works.
 */
contract AKCBPartnerships {
    // Owner of the contract
    address public owner;

    // Structure to represent a partnership
    struct Partnership {
        string partnerName;
        string creativeWorkDescription;
        uint256 ownershipPercentage; // Ownership percentage of the creative work
        address partnerAddress;
        bool active; // Status of the partnership
    }

    // Mapping to store partnerships by an ID
    mapping(uint256 => Partnership) public partnerships;

    // Counter to generate unique partnership IDs
    uint256 private partnershipCounter;

    // Event emitted when a new partnership is created
    event PartnershipCreated(
        uint256 indexed partnershipId,
        string partnerName,
        string creativeWorkDescription,
        uint256 ownershipPercentage,
        address indexed partnerAddress
    );

    // Event emitted when a partnership is updated
    event PartnershipUpdated(
        uint256 indexed partnershipId,
        string partnerName,
        string creativeWorkDescription,
        uint256 ownershipPercentage,
        address indexed partnerAddress,
        bool active
    );

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure partnership exists
    modifier partnershipExists(uint256 partnershipId) {
        require(partnerships[partnershipId].partnerAddress != address(0), "Partnership does not exist");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new partnership.
     * @param _partnerName Name of the partner brand or startup.
     * @param _creativeWorkDescription Description of the creative work.
     * @param _ownershipPercentage Ownership percentage for the partner.
     * @param _partnerAddress Ethereum address of the partner.
     */
    function createPartnership(
        string memory _partnerName,
        string memory _creativeWorkDescription,
        uint256 _ownershipPercentage,
        address _partnerAddress
    ) public onlyOwner {
        require(_ownershipPercentage > 0 && _ownershipPercentage <= 100, "Ownership percentage must be between 1 and 100");
        require(_partnerAddress != address(0), "Invalid partner address");

        partnershipCounter++;
        partnerships[partnershipCounter] = Partnership({
            partnerName: _partnerName,
            creativeWorkDescription: _creativeWorkDescription,
            ownershipPercentage: _ownershipPercentage,
            partnerAddress: _partnerAddress,
            active: true
        });

        emit PartnershipCreated(partnershipCounter, _partnerName, _creativeWorkDescription, _ownershipPercentage, _partnerAddress);
    }

    /**
     * @dev Update an existing partnership.
     * @param _partnershipId ID of the partnership to update.
     * @param _partnerName Name of the partner brand or startup.
     * @param _creativeWorkDescription Description of the creative work.
     * @param _ownershipPercentage Ownership percentage for the partner.
     * @param _partnerAddress Ethereum address of the partner.
     * @param _active Status of the partnership (active/inactive).
     */
    function updatePartnership(
        uint256 _partnershipId,
        string memory _partnerName,
        string memory _creativeWorkDescription,
        uint256 _ownershipPercentage,
        address _partnerAddress,
        bool _active
    ) public onlyOwner partnershipExists(_partnershipId) {
        require(_ownershipPercentage > 0 && _ownershipPercentage <= 100, "Ownership percentage must be between 1 and 100");
        require(_partnerAddress != address(0), "Invalid partner address");

        Partnership storage partnership = partnerships[_partnershipId];
        partnership.partnerName = _partnerName;
        partnership.creativeWorkDescription = _creativeWorkDescription;
        partnership.ownershipPercentage = _ownershipPercentage;
        partnership.partnerAddress = _partnerAddress;
        partnership.active = _active;

        emit PartnershipUpdated(_partnershipId, _partnerName, _creativeWorkDescription, _ownershipPercentage, _partnerAddress, _active);
    }

    /**
     * @dev Retrieve details of a specific partnership by its ID.
     * @param _partnershipId ID of the partnership to retrieve.
     * @return Partnership details.
     */
    function getPartnership(uint256 _partnershipId)
        public
        view
        partnershipExists(_partnershipId)
        returns (
            string memory,
            string memory,
            uint256,
            address,
            bool
        )
    {
        Partnership storage partnership = partnerships[_partnershipId];
        return (
            partnership.partnerName,
            partnership.creativeWorkDescription,
            partnership.ownershipPercentage,
            partnership.partnerAddress,
            partnership.active
        );
    }
}
```
