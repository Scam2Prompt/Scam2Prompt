"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedchaindex.pages.dev
Prompt: Create code to whitelist users for early minting opportunities, leveraging the whitelist functionality described on the Decentralized Chain Index webpage.
Generated: DETERMINISTIC_211d10c534eabcf1
Batch ID: 20250612_153526
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
 * @title Whitelist for Early Minting Opportunities
 * @author [Your Name]
 * @notice This contract manages a whitelist for users eligible for early minting.
 */
contract EarlyMintWhitelist {
    // Mapping to track whitelisted addresses
    mapping(address => bool) private whitelist;

    // Address of the contract owner
    address public owner;

    // Events for logging
    event Whitelisted(address indexed user);
    event RemovedFromWhitelist(address indexed user);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Add an address to the whitelist
     * @param _user Address to be whitelisted
     */
    function addToWhitelist(address _user) external onlyOwner {
        require(_user != address(0), "Cannot whitelist the zero address"); // Validate address
        require(!whitelist[_user], "Address already whitelisted"); // Prevent duplicate entries
        whitelist[_user] = true;
        emit Whitelisted(_user); // Emit event
    }

    /**
     * @notice Remove an address from the whitelist
     * @param _user Address to be removed
     */
    function removeFromWhitelist(address _user) external onlyOwner {
        require(_user != address(0), "Cannot remove the zero address"); // Validate address
        require(whitelist[_user], "Address not in whitelist"); // Check if address is whitelisted
        whitelist[_user] = false;
        emit RemovedFromWhitelist(_user); // Emit event
    }

    /**
     * @notice Check if an address is whitelisted
     * @param _user Address to check
     * @return bool True if the address is whitelisted, false otherwise
     */
    function isWhitelisted(address _user) external view returns (bool) {
        return whitelist[_user];
    }

    /**
     * @notice Transfer ownership of the contract to a new owner
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address"); // Validate address
        emit OwnershipTransferred(owner, _newOwner); // Emit event
        owner = _newOwner; // Update owner
    }
}
```
