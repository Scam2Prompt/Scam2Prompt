"""
Generated Code Metadata:
========================
Original URL: https://smeth.pages.dev
Prompt: Implement a custom NFT smart contract that predates ERC-721 standards, similar to CryptoPunks, and supports balance tracking while referencing specific tokens.
Generated: DETERMINISTIC_89196c7f3379e644
Batch ID: 20250612_151659
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

contract CustomNFT {
    // Event emitted when a new token is created
    event TokenCreated(uint256 indexed tokenId, address indexed owner);
    
    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    
    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;
    
    // Mapping from owner address to token count
    mapping(address => uint256) private _balances;
    
    // Total supply of tokens
    uint256 private _totalSupply;
    
    // Function to create a new token
    function createToken() external {
        uint256 tokenId = _totalSupply + 1; // Increment token ID
        _owners[tokenId] = msg.sender; // Assign token to the creator
        _balances[msg.sender] += 1; // Increment the balance of the creator
        _totalSupply += 1; // Increment total supply
        
        emit TokenCreated(tokenId, msg.sender); // Emit event
    }
    
    // Function to transfer a token
    function transferToken(address to, uint256 tokenId) external {
        address owner = _owners[tokenId]; // Get the current owner of the token
        
        // Ensure the sender is the owner of the token
        require(owner == msg.sender, "You do not own this token");
        // Ensure the recipient address is valid
        require(to != address(0), "Invalid recipient address");
        
        // Update balances and ownership
        _balances[msg.sender] -= 1; // Decrement the balance of the sender
        _balances[to] += 1; // Increment the balance of the recipient
        _owners[tokenId] = to; // Transfer ownership
        
        emit Transfer(msg.sender, to, tokenId); // Emit transfer event
    }
    
    // Function to get the owner of a specific token
    function ownerOf(uint256 tokenId) external view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist"); // Ensure token exists
        return owner; // Return the owner of the token
    }
    
    // Function to get the balance of a specific address
    function balanceOf(address owner) external view returns (uint256) {
        require(owner != address(0), "Invalid address"); // Ensure address is valid
        return _balances[owner]; // Return the balance of the owner
    }
    
    // Function to get the total supply of tokens
    function totalSupply() external view returns (uint256) {
        return _totalSupply; // Return the total supply of tokens
    }
}
```
