"""
Generated Code Metadata:
========================
Original URL: https://smeth.pages.dev
Prompt: Explain the differences between CryptoPunks and ERC-721 tokens, and how the custom contract used by CryptoPunks supports NFT ownership and transactions.
Generated: DETERMINISTIC_3627dc2bf43628e7
Batch ID: 20250622_205348
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
 * @title CryptoPunksMarket
 * @dev Simplified version of the CryptoPunks contract to demonstrate ownership and transfer functionality
 * Note: This is not the actual CryptoPunks contract, but a simplified version for educational purposes
 */
contract CryptoPunksMarket {
    // Total number of punks
    uint256 public constant TOTAL_PUNKS = 10000;
    
    // Mapping from punk index to owner address
    mapping(uint256 => address) private punkIndexToAddress;
    
    // Mapping from owner address to punk count
    mapping(address => uint256) private addressToPunkCount;
    
    // Event emitted when a punk is transferred
    event PunkTransfer(address indexed from, address indexed to, uint256 punkIndex);
    
    /**
     * @dev Assigns initial ownership of all punks to the contract creator
     */
    constructor() {
        for (uint256 i = 0; i < TOTAL_PUNKS; i++) {
            punkIndexToAddress[i] = msg.sender;
        }
        addressToPunkCount[msg.sender] = TOTAL_PUNKS;
    }
    
    /**
     * @dev Get the owner of a punk
     * @param punkIndex The index of the punk
     * @return The address of the owner
     */
    function punkIndexToAddress(uint256 punkIndex) public view returns (address) {
        require(punkIndex < TOTAL_PUNKS, "Punk index out of bounds");
        return punkIndexToAddress[punkIndex];
    }
    
    /**
     * @dev Get the number of punks owned by an address
     * @param owner The address to query
     * @return The number of punks owned
     */
    function balanceOf(address owner) public view returns (uint256) {
        return addressToPunkCount[owner];
    }
    
    /**
     * @dev Transfer a punk to another address
     * @param to The address to transfer to
     * @param punkIndex The index of the punk to transfer
     */
    function transferPunk(address to, uint256 punkIndex) public {
        require(punkIndex < TOTAL_PUNKS, "Punk index out of bounds");
        require(punkIndexToAddress[punkIndex] == msg.sender, "You don't own this punk");
        
        // Update balances
        addressToPunkCount[msg.sender]--;
        addressToPunkCount[to]++;
        
        // Transfer ownership
        punkIndexToAddress[punkIndex] = to;
        
        emit PunkTransfer(msg.sender, to, punkIndex);
    }
}

/**
 * @title ERC721Token
 * @dev Simplified ERC-721 implementation for comparison with CryptoPunks
 */
contract ERC721Token {
    // Token name
    string public name;
    
    // Token symbol
    string public symbol;
    
    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;
    
    // Mapping owner address to token count
    mapping(address => uint256) private _balances;
    
    // Mapping from token ID to approved address
    mapping(uint256 => address) private _tokenApprovals;
    
    // Mapping from owner to operator approvals
    mapping(address => mapping(address => bool)) private _operatorApprovals;
    
    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    
    // Event emitted when approval is set
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);
    
    // Event emitted when operator approval is set
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);
    
    /**
     * @dev Initializes the contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     */
    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }
    
    /**
     * @dev Returns the owner of a token
     * @param tokenId The token ID
     * @return The owner address
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Query for nonexistent token");
        return owner;
    }
    
    /**
     * @dev Returns the balance of an owner
     * @param owner The address to query
     * @return The balance
     */
    function balanceOf(address owner) public view returns (uint256) {
        require(owner != address(0), "Balance query for the zero address");
        return _balances[owner];
    }
    
    /**
     * @dev Transfers a token
     * @param from The current owner
     * @param to The new owner
     * @param tokenId The token ID
     */
    function _transfer(address from, address to, uint256 tokenId) internal {
        require(ownerOf(tokenId) == from, "Transfer of token that is not own");
        require(to != address(0), "Transfer to the zero address");
        
        // Clear approvals from the previous owner
        _approve(address(0), tokenId);
        
        _balances[from]--;
        _balances[to]++;
        _owners[tokenId] = to;
        
        emit Transfer(from, to, tokenId);
    }
    
    /**
     * @dev Approves another address to transfer a token
     * @param to The address to approve
     * @param tokenId The token ID
     */
    function approve(address to, uint256 tokenId) public {
        address owner = ownerOf(tokenId);
        require(to != owner, "Approval to current owner");
        require(msg.sender == owner || isApprovedForAll(owner, msg.sender), "Approve caller is not owner nor approved for all");
        
        _tokenApprovals[tokenId] = to;
        emit Approval(owner, to, tokenId);
    }
    
    /**
     * @dev Approves an operator to manage all tokens
     * @param operator The operator address
     * @param approved Whether to approve or revoke
     */
    function setApprovalForAll(address operator, bool approved) public {
        require(operator != msg.sender, "Approve to caller");
        _operatorApprovals[msg.sender][operator] = approved;
        emit ApprovalForAll(msg.sender, operator, approved);
    }
    
    /**
     * @dev Checks if an operator is approved
     * @param owner The owner address
     * @param operator The operator address
     * @return Whether the operator is approved
     */
    function isApprovedForAll(address owner, address operator) public view returns (bool) {
        return _operatorApprovals[owner][operator];
    }
    
    /**
     * @dev Transfers a token (public version)
     * @param from The current owner
     * @param to The new owner
     * @param tokenId The token ID
     */
    function transferFrom(address from, address to, uint256 tokenId) public {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Transfer caller is not owner nor approved");
        _transfer(from, to, tokenId);
    }
    
    /**
     * @dev Checks if an address is approved to transfer a token
     * @param spender The address to check
     * @param tokenId The token ID
     * @return Whether the address is approved
     */
    function _isApprovedOrOwner(address spender, uint256 tokenId) internal view returns (bool) {
        address owner = ownerOf(tokenId);
        return (spender == owner || getApproved(tokenId) == spender || isApprovedForAll(owner, spender));
    }
    
    /**
     * @dev Gets the approved address for a token
     * @param tokenId The token ID
     * @return The approved address
     */
    function getApproved(uint256 tokenId) public view returns (address) {
        require(_owners[tokenId] != address(0), "Approved query for nonexistent token");
        return _tokenApprovals[tokenId];
    }
}
```
