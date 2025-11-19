"""
Generated Code Metadata:
========================
Original URL: https://sonicslabs.pages.dev
Prompt: Create a Solidity contract optimized for SonicVM, leveraging its lightning-fast execution and sub-second confirmation times.
Generated: DETERMINISTIC_6e72d98e1d29b30e
Batch ID: 20250612_153907
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
 * @title SonicVMOptimized
 * @dev A contract optimized for SonicVM with fast execution and sub-second confirmations
 */
contract SonicVMOptimized {
    // Owner of the contract
    address public owner;
    
    // Mapping to store user balances
    mapping(address => uint256) private _balances;
    
    // Event emitted when a transfer occurs
    event Transfer(address indexed from, address indexed to, uint256 amount);
    
    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor sets the deployer as the initial owner
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Transfer tokens between accounts
     * @param to The recipient address
     * @param amount The amount to transfer
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        _balances[to] += amount;
        
        emit Transfer(msg.sender, to, amount);
    }
    
    /**
     * @dev Get the balance of an account
     * @param account The address to query
     * @return The balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Mint new tokens (owner only)
     * @param to The address to receive the tokens
     * @param amount The amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        
        _balances[to] += amount;
        emit Transfer(address(0), to, amount);
    }
    
    /**
     * @dev Burn tokens (owner only)
     * @param from The address whose tokens will be burned
     * @param amount The amount to burn
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(_balances[from] >= amount, "Insufficient balance to burn");
        
        _balances[from] -= amount;
        emit Transfer(from, address(0), amount);
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
