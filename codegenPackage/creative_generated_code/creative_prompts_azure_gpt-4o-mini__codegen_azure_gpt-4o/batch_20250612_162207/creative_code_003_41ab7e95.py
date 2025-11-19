"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toto1m.pages.dev
Prompt: Develop a smart contract that integrates with the POON ecosystem, highlighting the partnerships and community aspects discussed on the site.
Generated: DETERMINISTIC_41ab7e95981f020f
Batch ID: 20250612_162207
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
 * @title POONPartnershipsContract
 * @dev A smart contract that integrates with the POON ecosystem, emphasizing partnerships and community aspects.
 */
contract POONPartnershipsContract {
    // Address of the contract owner
    address public owner;

    // Mapping to track partnerships. Each partner has a name and an active status.
    struct Partnership {
        string name;
        bool isActive;
    }
    mapping(address => Partnership) public partnerships;

    // Event emitted when a new partnership is added
    event PartnershipAdded(address indexed partner, string name);

    // Event emitted when a partnership is updated
    event PartnershipUpdated(address indexed partner, bool isActive);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functionality.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    /**
     * @dev Constructor to set the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }

    /**
     * @dev Function to add a new partnership to the system.
     * @param partner Address of the partner.
     * @param name Name of the partner.
     */
    function addPartnership(address partner, string memory name) external onlyOwner {
        require(partner != address(0), "Partner address cannot be zero");
        require(bytes(name).length > 0, "Partner name cannot be empty");
        partnerships[partner] = Partnership(name, true);
        emit PartnershipAdded(partner, name);
    }

    /**
     * @dev Function to update the active status of a partnership.
     * @param partner Address of the partner.
     * @param isActive New active status of the partnership.
     */
    function updatePartnershipStatus(address partner, bool isActive) external onlyOwner {
        require(partnerships[partner].isActive != isActive, "New status is the same as the current status");
        partnerships[partner].isActive = isActive;
        emit PartnershipUpdated(partner, isActive);
    }

    /**
     * @dev Public function to retrieve partnership details.
     * @param partner Address of the partner.
     * @return name Name of the partner.
     * @return isActive Active status of the partnership.
     */
    function getPartnershipDetails(address partner) external view returns (string memory name, bool isActive) {
        require(bytes(partnerships[partner].name).length > 0, "Partner does not exist");
        Partnership memory partnership = partnerships[partner];
        return (partnership.name, partnership.isActive);
    }
}
```
