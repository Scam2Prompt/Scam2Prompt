"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Develop a basic smart contract in Solidity that utilizes DOP's selective transparency feature to control the visibility of specific tokens or asset amounts on a blockchain.
Generated: DETERMINISTIC_58803024f7212a7f
Batch ID: 20250622_205117
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
 * @title SelectiveTransparencyToken
 * @dev A smart contract demonstrating DOP's selective transparency feature
 * that allows controlling visibility of specific tokens/amounts on blockchain.
 */
contract SelectiveTransparencyToken {
    // Owner of the contract
    address public owner;
    
    // Mapping to store token balances (publicly visible)
    mapping(address => uint256) public balances;
    
    // Mapping to store private balances (not publicly visible)
    mapping(address => uint256) private privateBalances;
    
    // Mapping to store which addresses have transparency enabled
    mapping(address => bool) public transparencyEnabled;
    
    // Event for token transfers
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    // Event for private transfers (not logged on public chain)
    event PrivateTransfer(address indexed from, address indexed to, uint256 value);
    
    // Modifier to check if caller is owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor sets the initial owner
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Mint new tokens (owner only)
     * @param to Address to receive tokens
     * @param amount Amount of tokens to mint
     * @param isPrivate Whether tokens should be private
     */
    function mint(address to, uint256 amount, bool isPrivate) external onlyOwner {
        if (isPrivate) {
            privateBalances[to] += amount;
        } else {
            balances[to] += amount;
        }
    }
    
    /**
     * @dev Transfer tokens between accounts
     * @param to Recipient address
     * @param amount Amount to transfer
     * @param isPrivate Whether transfer should be private
     */
    function transfer(address to, uint256 amount, bool isPrivate) external {
        if (isPrivate) {
            require(privateBalances[msg.sender] >= amount, "Insufficient private balance");
            privateBalances[msg.sender] -= amount;
            privateBalances[to] += amount;
            emit PrivateTransfer(msg.sender, to, amount);
        } else {
            require(balances[msg.sender] >= amount, "Insufficient balance");
            balances[msg.sender] -= amount;
            balances[to] += amount;
            emit Transfer(msg.sender, to, amount);
        }
    }
    
    /**
     * @dev Toggle transparency for an address (owner only)
     * @param account Address to toggle transparency for
     * @param enabled Whether to enable or disable transparency
     */
    function setTransparency(address account, bool enabled) external onlyOwner {
        transparencyEnabled[account] = enabled;
    }
    
    /**
     * @dev Get combined balance (public + private) for an address
     * Only visible to owner or if transparency is enabled for the account
     * @param account Address to check balance for
     */
    function getFullBalance(address account) external view returns (uint256) {
        require(
            msg.sender == owner || transparencyEnabled[account],
            "Transparency not enabled for this account"
        );
        return balances[account] + privateBalances[account];
    }
    
    /**
     * @dev Transfer ownership of the contract (owner only)
     * @param newOwner Address of new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
