"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchaindappc.pages.dev
Prompt: Provide code to whitelist a wallet for NFT transactions, incorporating the functionality described on Blockchain Dapp Sync.
Generated: DETERMINISTIC_95e3f58b330f2948
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title NFT Whitelist Contract
/// @author Your Name
/// @notice This contract manages a whitelist of addresses permitted for NFT transactions
/// @dev Uses a mapping to track whitelisted addresses and emits events for state changes

contract NFTWhitelist {
    // State variable to track whitelisted addresses
    mapping(address => bool) private whitelistedAddresses;

    // Event emitted when a wallet is added to the whitelist
    event AddressWhitelisted(address indexed wallet);

    // Event emitted when a wallet is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed wallet);

    /// @notice Adds an address to the whitelist
    /// @param wallet The address to be added to the whitelist
    /// @dev Only the contract owner can call this function
    function addAddressToWhitelist(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address: cannot be zero address");
        require(!whitelistedAddresses[wallet], "This address is already whitelisted");

        whitelistedAddresses[wallet] = true;
        emit AddressWhitelisted(wallet);
    }

    /// @notice Removes an address from the whitelist
    /// @param wallet The address to be removed from the whitelist
    /// @dev Only the contract owner can call this function
    function removeAddressFromWhitelist(address wallet) external onlyOwner {
        require(whitelistedAddresses[wallet], "This address is not whitelisted");

        whitelistedAddresses[wallet] = false;
        emit AddressRemovedFromWhitelist(wallet);
    }

    /// @notice Checks if an address is whitelisted
    /// @param wallet The address to check
    /// @return bool True if the address is whitelisted, false otherwise
    function isWhitelisted(address wallet) external view returns (bool) {
        return whitelistedAddresses[wallet];
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // State variable for contract owner
    address private owner;

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
