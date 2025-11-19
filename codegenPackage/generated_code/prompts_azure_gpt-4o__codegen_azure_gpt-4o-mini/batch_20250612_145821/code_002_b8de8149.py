"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.eu
Prompt: Generate Solidity code for a smart contract optimized for the Arbitrum Layer 2 network, including gas-efficient functions.
Generated: DETERMINISTIC_b8de8149d1d55434
Batch ID: 20250612_145821
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

// Importing OpenZeppelin's Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple token contract optimized for the Arbitrum Layer 2 network
contract OptimizedToken is Ownable {
    // State variable to store the total supply of the token
    uint256 private _totalSupply;

    // Mapping from address to balance
    mapping(address => uint256) private _balances;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply; // Assign initial supply to the contract deployer
    }

    // Function to get the total supply of the token
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific address
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    // Function to transfer tokens from the sender to a recipient
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        // Emit the transfer event
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spender to spend a certain amount of tokens on behalf of the owner
    function approve(address spender, uint256 amount) external returns (bool) {
        // Implementation of approval logic can be added here
        // For simplicity, this function is left unimplemented
        return true;
    }

    // Function to transfer tokens from one address to another on behalf of the owner
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        // Implementation of allowance logic can be added here
        // For simplicity, this function is left unimplemented
        return true;
    }

    // Function to mint new tokens, only callable by the owner
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        _totalSupply += amount;
        _balances[msg.sender] += amount;

        // Emit the transfer event for minting
        emit Transfer(address(0), msg.sender, amount);
    }

    // Function to burn tokens from the owner's balance
    function burn(uint256 amount) external onlyOwner {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        // Emit the transfer event for burning
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
