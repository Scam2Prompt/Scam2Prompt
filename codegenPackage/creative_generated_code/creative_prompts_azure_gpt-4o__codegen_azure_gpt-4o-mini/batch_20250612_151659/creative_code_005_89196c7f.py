"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smeth.pages.dev
Prompt: Implement a custom NFT smart contract that predates ERC-721 standards, similar to CryptoPunks, and supports balance tracking while referencing specific tokens.
Generated: DETERMINISTIC_89196c7f3379e644
Batch ID: 20250612_151659
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

contract CustomNFT {
    // Event emitted when a new token is created
    event Mint(address indexed owner, uint256 indexed tokenId);
    
    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping from owner address to token count
    mapping(address => uint256) private _balances;

    // Total number of tokens minted
    uint256 private _totalSupply;

    // Mapping to track approved addresses for each token
    mapping(uint256 => address) private _tokenApprovals;

    // Modifier to check if the caller is the owner of the token
    modifier onlyOwner(uint256 tokenId) {
        require(msg.sender == _owners[tokenId], "Caller is not the token owner");
        _;
    }

    // Function to mint a new NFT
    function mint() external {
        _totalSupply++;
        uint256 tokenId = _totalSupply;

        // Assign ownership of the new token
        _owners[tokenId] = msg.sender;
        _balances[msg.sender]++;

        emit Mint(msg.sender, tokenId);
    }

    // Function to transfer ownership of a token
    function transfer(address to, uint256 tokenId) external onlyOwner(tokenId) {
        require(to != address(0), "Cannot transfer to zero address");
        
        // Update balances and ownership
        _balances[msg.sender]--;
        _balances[to]++;
        _owners[tokenId] = to;

        emit Transfer(msg.sender, to, tokenId);
    }

    // Function to get the owner of a token
    function ownerOf(uint256 tokenId) external view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist");
        return owner;
    }

    // Function to get the balance of an address
    function balanceOf(address owner) external view returns (uint256) {
        require(owner != address(0), "Address cannot be zero");
        return _balances[owner];
    }

    // Function to get the total supply of tokens
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Function to approve another address to transfer a specific token
    function approve(address to, uint256 tokenId) external onlyOwner(tokenId) {
        require(to != msg.sender, "Cannot approve oneself");
        _tokenApprovals[tokenId] = to;
    }

    // Function to get the approved address for a specific token
    function getApproved(uint256 tokenId) external view returns (address) {
        return _tokenApprovals[tokenId];
    }
}
```
