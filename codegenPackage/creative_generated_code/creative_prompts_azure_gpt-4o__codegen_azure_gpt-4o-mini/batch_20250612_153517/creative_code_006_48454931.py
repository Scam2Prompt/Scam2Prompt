"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerfairdrop.vercel.app
Prompt: Write a Solidity function to revoke token ownership after deployment, inspired by $Slerf's ownership revocation mechanism.
Generated: DETERMINISTIC_48454931014745e4
Batch ID: 20250612_153517
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
 * @title TokenOwnershipRevocation
 * @dev This contract allows the owner to revoke their ownership of the contract after deployment.
 */
contract TokenOwnershipRevocation {
    address private _owner; // Variable to store the owner's address
    bool private _isOwnershipRevoked; // Variable to track if ownership has been revoked

    // Event emitted when ownership is revoked
    event OwnershipRevoked(address indexed previousOwner);

    /**
     * @dev Constructor sets the original owner of the contract to the sender account.
     */
    constructor() {
        _owner = msg.sender; // Set the deployer as the initial owner
        _isOwnershipRevoked = false; // Ownership is initially valid
    }

    /**
     * @dev Modifier to restrict functionality to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == _owner, "Not the contract owner");
        require(!_isOwnershipRevoked, "Ownership has been revoked");
        _;
    }

    /**
     * @dev Function to revoke ownership of the contract.
     * Can only be called by the current owner.
     * Emits an OwnershipRevoked event upon successful revocation.
     */
    function revokeOwnership() external onlyOwner {
        emit OwnershipRevoked(_owner); // Emit event with previous owner's address
        _owner = address(0); // Set the owner to the zero address, effectively revoking ownership
        _isOwnershipRevoked = true; // Mark ownership as revoked
    }

    /**
     * @dev Function to check the current owner of the contract.
     * @return address of the current owner.
     */
    function getOwner() external view returns (address) {
        return _owner; // Return the current owner's address
    }

    /**
     * @dev Function to check if ownership has been revoked.
     * @return bool indicating if the ownership has been revoked.
     */
    function isOwnershipRevoked() external view returns (bool) {
        return _isOwnershipRevoked; // Return the revocation status
    }
}
```
