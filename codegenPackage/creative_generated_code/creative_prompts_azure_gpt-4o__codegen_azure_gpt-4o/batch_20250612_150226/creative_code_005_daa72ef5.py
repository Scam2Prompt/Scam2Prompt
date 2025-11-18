"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website2-70z.pages.dev
Prompt: Create a smart contract in Solidity that supports inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_daa72ef51d347c80
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
 * @title InclusiveOwnership
 * @dev A smart contract to support inclusive ownership models, reflecting the values of Innodapter ApS.
 * Owners can collectively manage and transfer ownership shares.
 */
contract InclusiveOwnership {
    // Struct to represent ownership details
    struct Owner {
        uint256 share; // Percentage ownership (out of 10000 for precision, e.g., 2500 means 25%)
        bool exists; // Flag to check if the owner exists
    }

    // Mapping to store owners and their shares
    mapping(address => Owner) private owners;

    // Total shares distributed among all owners (out of 10000 for full ownership)
    uint256 public totalShares;

    // Events
    event OwnershipGranted(address indexed owner, uint256 share);
    event OwnershipRevoked(address indexed owner);
    event OwnershipTransferred(address indexed from, address indexed to, uint256 share);

    // Modifier to ensure that only valid owners can execute certain functions
    modifier onlyOwner() {
        require(owners[msg.sender].exists, "Caller is not an owner");
        _;
    }

    /**
     * @dev Constructor
     * The deployer of the contract automatically becomes the first owner with full ownership.
     */
    constructor() {
        owners[msg.sender] = Owner({share: 10000, exists: true});
        totalShares = 10000;
        emit OwnershipGranted(msg.sender, 10000);
    }

    /**
     * @dev Grant ownership to a new address.
     * @param newOwner Address of the new owner.
     * @param share Percentage ownership to grant (out of 10000).
     */
    function grantOwnership(address newOwner, uint256 share) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        require(!owners[newOwner].exists, "Owner already exists");
        require(share > 0 && totalShares + share <= 10000, "Invalid share amount");

        owners[newOwner] = Owner({share: share, exists: true});
        totalShares += share;

        emit OwnershipGranted(newOwner, share);
    }

    /**
     * @dev Revoke ownership from an existing owner.
     * @param owner Address of the owner to revoke.
     */
    function revokeOwnership(address owner) external onlyOwner {
        require(owner != address(0), "Invalid owner address");
        require(owners[owner].exists, "Owner does not exist");

        uint256 share = owners[owner].share;
        totalShares -= share;

        delete owners[owner];

        emit OwnershipRevoked(owner);
    }

    /**
     * @dev Transfer a portion of ownership share to another address.
     * @param to Address to receive ownership shares.
     * @param share Amount of ownership share to transfer (out of 10000).
     */
    function transferOwnership(address to, uint256 share) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(owners[to].exists || totalShares + share <= 10000, "Recipient exceeds total shares");
        require(share > 0 && owners[msg.sender].share >= share, "Invalid share amount");

        // Deduct shares from sender
        owners[msg.sender].share -= share;

        // Add shares to recipient
        if (owners[to].exists) {
            owners[to].share += share;
        } else {
            owners[to] = Owner({share: share, exists: true});
        }

        emit OwnershipTransferred(msg.sender, to, share);
    }

    /**
     * @dev Get ownership share of a specific address.
     * @param owner Address to query.
     * @return share Ownership percentage (out of 10000).
     */
    function getShare(address owner) external view returns (uint256 share) {
        if (owners[owner].exists) {
            return owners[owner].share;
        }
        return 0;
    }

    /**
     * @dev Check if an address is an owner.
     * @param owner Address to query.
     * @return exists True if the address is an owner, false otherwise.
     */
    function isOwner(address owner) external view returns (bool exists) {
        return owners[owner].exists;
    }
}
```
