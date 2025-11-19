"""
Generated Code Metadata:
========================
Original URL: https://pullixmarkets.pages.dev
Prompt: Implement a whitelisting system for minting, using a decentralized protocol and open-source software ecosystem, as featured on the Pullix Markets website.
Generated: DETERMINISTIC_daca898ccfa326dd
Batch ID: 20250622_205218
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
 * @title WhitelistMinting
 * @dev A contract for managing a whitelisting system for minting tokens.
 *      This contract uses decentralized principles and is designed to be production-ready.
 */
contract WhitelistMinting {
    // Owner of the contract
    address public owner;

    // Mapping to store whitelisted addresses
    mapping(address => bool) public whitelist;

    // Event emitted when an address is added to the whitelist
    event AddressWhitelisted(address indexed account);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed account);

    // Event emitted when a token is minted
    event TokenMinted(address indexed account, uint256 tokenId);

    // Counter for token IDs
    uint256 private tokenIdCounter;

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if the caller is whitelisted
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Caller is not whitelisted");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add an address to the whitelist.
     * @param account The address to be added to the whitelist.
     */
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(!whitelist[account], "Address already whitelisted");

        whitelist[account] = true;
        emit AddressWhitelisted(account);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param account The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(whitelist[account], "Address not in whitelist");

        whitelist[account] = false;
        emit AddressRemovedFromWhitelist(account);
    }

    /**
     * @dev Function to mint a token. Only whitelisted addresses can mint.
     */
    function mintToken() external onlyWhitelisted {
        tokenIdCounter++;
        uint256 newTokenId = tokenIdCounter;

        // Emit the minting event
        emit TokenMinted(msg.sender, newTokenId);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param account The address to check.
     * @return True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address account) external view returns (bool) {
        return whitelist[account];
    }
}
```
