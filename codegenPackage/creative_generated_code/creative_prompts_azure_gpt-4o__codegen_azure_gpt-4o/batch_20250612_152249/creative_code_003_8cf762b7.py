"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3nw7cyq2q2jw5zaaxhqznmxmr6ano4kkfjked4sebtl2biznzfy.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that manages a whitelist for a public pre-sale, allowing users to register using their Web3 wallet addresses.
Generated: DETERMINISTIC_8cf762b784ccf42e
Batch ID: 20250612_152249
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
 * @title Whitelist Contract for Pre-Sale
 * @dev This contract enables users to register their wallet addresses on a whitelist for an upcoming public pre-sale.
 */
contract Whitelist {
    // Maximum number of addresses allowed on the whitelist
    uint256 public maxWhitelistSize;
    // Total number of addresses currently whitelisted
    uint256 public whitelistCount;
    // Address of the contract owner
    address public owner;
    // Mapping to track whitelisted addresses
    mapping(address => bool) public isWhitelisted;

    // Event emitted when a new address is added to the whitelist
    event AddressWhitelisted(address indexed wallet);

    // Event emitted when an address is removed from the whitelist
    event AddressRemoved(address indexed wallet);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure whitelist capacity is not exceeded
    modifier whitelistNotFull() {
        require(whitelistCount < maxWhitelistSize, "Whitelist is full");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _maxWhitelistSize The maximum number of addresses that can be whitelisted.
     */
    constructor(uint256 _maxWhitelistSize) {
        require(_maxWhitelistSize > 0, "Max whitelist size must be greater than zero");
        owner = msg.sender;
        maxWhitelistSize = _maxWhitelistSize;
        whitelistCount = 0;
    }

    /**
     * @dev Function for users to register their wallet address on the whitelist.
     * Emits an `AddressWhitelisted` event upon success.
     */
    function register() external whitelistNotFull {
        require(!isWhitelisted[msg.sender], "Address is already whitelisted");

        isWhitelisted[msg.sender] = true;
        whitelistCount += 1;

        emit AddressWhitelisted(msg.sender);
    }

    /**
     * @dev Function for the owner to remove an address from the whitelist.
     * @param _wallet The wallet address to remove from the whitelist.
     * Emits an `AddressRemoved` event upon success.
     */
    function removeFromWhitelist(address _wallet) external onlyOwner {
        require(isWhitelisted[_wallet], "Address is not whitelisted");

        isWhitelisted[_wallet] = false;
        whitelistCount -= 1;

        emit AddressRemoved(_wallet);
    }

    /**
     * @dev Function for the owner to update the maximum whitelist size.
     * @param _newMaxSize The new maximum whitelist size.
     */
    function updateMaxWhitelistSize(uint256 _newMaxSize) external onlyOwner {
        require(_newMaxSize >= whitelistCount, "New max size must be greater than or equal to current whitelist count");
        maxWhitelistSize = _newMaxSize;
    }
}
```
