"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Develop a code snippet in Solidity to implement a whitelist (WL) and allowlist (FCFS) system for minting NFTs in groups, similar to the MegaRabbit collection.
Generated: DETERMINISTIC_35d01a2f9b7bca21
Batch ID: 20250622_212626
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
 * @title Whitelist and Allowlist NFT Minting Contract
 * @dev Implements a whitelist and first-come-first-serve (FCFS) allowlist system for minting NFTs.
 */
contract MegaRabbitMinting {
    // State variables
    address public owner; // Contract owner
    uint256 public maxSupply; // Maximum number of NFTs
    uint256 public totalMinted; // Total number of NFTs minted
    uint256 public mintPrice; // Price per NFT

    mapping(address => bool) public whitelist; // Whitelist mapping
    mapping(address => bool) public allowlist; // Allowlist mapping

    // Events
    event Mint(address indexed minter, uint256 quantity);
    event AddedToWhitelist(address indexed account);
    event AddedToAllowlist(address indexed account);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier isWhitelisted() {
        require(whitelist[msg.sender], "Caller is not whitelisted");
        _;
    }

    modifier isAllowlisted() {
        require(allowlist[msg.sender], "Caller is not allowlisted");
        _;
    }

    modifier canMint(uint256 quantity) {
        require(totalMinted + quantity <= maxSupply, "Exceeds max supply");
        require(msg.value >= mintPrice * quantity, "Insufficient funds");
        _;
    }

    // Constructor
    constructor(uint256 _maxSupply, uint256 _mintPrice) {
        owner = msg.sender;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
        emit AddedToWhitelist(account);
    }

    // Function to add an address to the allowlist
    function addToAllowlist(address account) external onlyOwner {
        allowlist[account] = true;
        emit AddedToAllowlist(account);
    }

    // Whitelist minting function
    function mintWhitelist(uint256 quantity) external payable isWhitelisted canMint(quantity) {
        totalMinted += quantity;
        emit Mint(msg.sender, quantity);
    }

    // Allowlist minting function (FCFS)
    function mintAllowlist(uint256 quantity) external payable isAllowlisted canMint(quantity) {
        totalMinted += quantity;
        emit Mint(msg.sender, quantity);
    }

    // Withdraw contract balance to owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
