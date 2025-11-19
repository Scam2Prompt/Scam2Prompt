"""
Generated Code Metadata:
========================
Original URL: https://clean-4dq.pages.dev
Prompt: Develop a simple smart contract in Solidity that utilizes SatoshiVM's EVM compatibility to issue assets on the Bitcoin ecosystem.
Generated: DETERMINISTIC_e7b21d99fbce101b
Batch ID: 20250622_205929
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
 * @title BitcoinAssetIssuer
 * @dev A simple smart contract to issue assets compatible with SatoshiVM's EVM compatibility layer
 * for the Bitcoin ecosystem.
 */
contract BitcoinAssetIssuer {
    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total supply of the asset
    string public name; // Asset name
    string public symbol; // Asset symbol
    uint8 public decimals; // Asset decimals

    // Mapping to track balances of addresses
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the asset details and set the owner.
     * @param _name Name of the asset.
     * @param _symbol Symbol of the asset.
     * @param _decimals Number of decimals for the asset.
     * @param _initialSupply Initial supply of the asset.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        owner = msg.sender;
        balances[owner] = _initialSupply;

        emit Transfer(address(0), owner, _initialSupply); // Emit transfer event for initial supply
    }

    /**
     * @dev Function to transfer assets to another address.
     * @param _to Address to transfer assets to.
     * @param _value Amount of assets to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true;
    }

    /**
     * @dev Function to check the balance of an address.
     * @param _account Address to check the balance of.
     * @return balance Balance of the given address.
     */
    function balanceOf(address _account) external view returns (uint256 balance) {
        return balances[_account];
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, _newOwner); // Emit ownership transfer event
        owner = _newOwner;
    }
}
```
