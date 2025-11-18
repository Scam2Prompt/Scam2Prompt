"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market.pages.dev
Prompt: Generate a smart contract in Solidity that supports a whitelisting portal for token purchases, similar to the Whales Market's whitelisting system for $WHALES tokens.
Generated: DETERMINISTIC_b10296c1ac4ef69d
Batch ID: 20250612_152620
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
 * @title WhitelistTokenPurchase
 * @dev A smart contract to manage a whitelisting portal for token purchases.
 */
contract WhitelistTokenPurchase {
    // Address of the token owner/admin
    address public owner;

    // Mapping to store whitelisted addresses
    mapping(address => bool) public whitelisted;

    // Event emitted when an address is added to the whitelist
    event AddressWhitelisted(address indexed user);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed user);

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed user, uint256 amount);

    // Modifier to restrict access to certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if the caller is whitelisted
    modifier onlyWhitelisted() {
        require(whitelisted[msg.sender], "Address is not whitelisted");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add an address to the whitelist.
     * @param _address The address to be added to the whitelist.
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        require(!whitelisted[_address], "Address is already whitelisted");

        whitelisted[_address] = true;
        emit AddressWhitelisted(_address);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param _address The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        require(whitelisted[_address], "Address is not whitelisted");

        whitelisted[_address] = false;
        emit AddressRemovedFromWhitelist(_address);
    }

    /**
     * @dev Function for a whitelisted user to purchase tokens.
     * @param _amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable onlyWhitelisted {
        require(_amount > 0, "Token amount must be greater than zero");
        require(msg.value == _amount * 1 ether, "Incorrect Ether value sent"); // Example: 1 token = 1 Ether.

        emit TokensPurchased(msg.sender, _amount);

        // Logic for transferring tokens to `msg.sender` goes here.
        // For simplicity, this contract does not implement actual token transfers.
    }

    /**
     * @dev Function to withdraw collected Ether from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
