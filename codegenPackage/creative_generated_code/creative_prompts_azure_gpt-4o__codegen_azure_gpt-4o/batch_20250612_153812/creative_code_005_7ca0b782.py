"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-an.web.app
Prompt: Write a Solidity function for whitelisting addresses in the Kendu Inu ecosystem, ensuring only approved wallets can participate in staking or minting NFTs.
Generated: DETERMINISTIC_7ca0b78298c83964
Batch ID: 20250612_153812
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
 * @title KenduInuWhitelist
 * @dev Smart contract for managing a whitelist of approved addresses in the Kendu Inu ecosystem.
 */
contract KenduInuWhitelist {

    // Owner of the contract
    address public owner;

    // Mapping to track whitelisted addresses
    mapping(address => bool) private whitelist;

    // Events for logging whitelist updates
    event AddressWhitelisted(address indexed account);
    event AddressRemovedFromWhitelist(address indexed account);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner.");
        _;
    }

    /**
     * @dev Constructor to set the deployer as the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add an address to the whitelist.
     * @param _wallet The address to be added to the whitelist.
     */
    function addToWhitelist(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Cannot whitelist the zero address.");
        require(!whitelist[_wallet], "Address is already whitelisted.");

        whitelist[_wallet] = true;
        emit AddressWhitelisted(_wallet);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param _wallet The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Cannot remove the zero address.");
        require(whitelist[_wallet], "Address is not whitelisted.");

        whitelist[_wallet] = false;
        emit AddressRemovedFromWhitelist(_wallet);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param _wallet The address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address _wallet) external view returns (bool) {
        return whitelist[_wallet];
    }
}
```
