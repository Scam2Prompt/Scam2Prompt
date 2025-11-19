"""
Generated Code Metadata:
========================
Original URL: https://grand-baseio.pages.dev
Prompt: "Generate a smart contract code for minting and managing gAssets (synthetic RWAs) on the Base blockchain, inspired by Grand Base's implementation."
Generated: DETERMINISTIC_fdc613409cac2aa0
Batch ID: 20250622_211011
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
 * @title gAssetManager
 * @dev Smart contract for minting and managing synthetic RWAs (gAssets) on the Base blockchain.
 * Inspired by Grand Base's implementation.
 */
contract gAssetManager {
    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total supply of gAssets

    // Mapping to track balances of gAssets for each address
    mapping(address => uint256) public balances;

    // Events
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint new gAssets.
     * @param to Address to receive the minted gAssets.
     * @param amount Amount of gAssets to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[to] += amount;
        totalSupply += amount;

        emit Mint(to, amount);
    }

    /**
     * @dev Function to burn gAssets.
     * @param from Address from which gAssets will be burned.
     * @param amount Amount of gAssets to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[from] >= amount, "Insufficient balance to burn");

        balances[from] -= amount;
        totalSupply -= amount;

        emit Burn(from, amount);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to get the balance of gAssets for a specific address.
     * @param account Address to query the balance for.
     * @return Balance of gAssets for the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
