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

// Importing the ERC721 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Custom contract for CryptoPunks, implementing ERC721
contract CryptoPunks is Context, Ownable, IERC721, IERC721Metadata {
    using Address for address;
    using Strings for uint256;

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping from owner address to token count
    mapping(address => uint256) private _balances;

    // Mapping from token ID to approved address
    mapping(uint256 => address) private _tokenApprovals;

    // Total supply of CryptoPunks
    uint256 private _totalSupply;

    // Name and symbol for the NFT collection
    string private _name;
    string private _symbol;

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    // Event emitted when an approval is set
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);

    // Constructor to initialize the contract with name and symbol
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }

    // Function to return the name of the NFT collection
    function name() external view override returns (string memory) {
        return _name;
    }

    // Function to return the symbol of the NFT collection
    function symbol() external view override returns (string memory) {
        return _symbol;
    }

    // Function to return the owner of a specific token ID
    function ownerOf(uint256 tokenId) external view override returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist");
        return owner;
    }

    // Function to return the balance of a specific address
    function balanceOf(address owner) external view override returns (uint256) {
        require(owner != address(0), "Address is zero");
        return _balances[owner];
    }

    // Function to approve another address to manage a specific token
    function approve(address to, uint256 tokenId) external override {
        address owner = ownerOf(tokenId);
        require(to != owner, "Cannot approve current owner");
        require(_msgSender() == owner, "Caller is not the owner");

        _tokenApprovals[tokenId] = to;
        emit Approval(owner, to, tokenId);
    }

    // Function to transfer ownership of a token
    function transferFrom(address from, address to, uint256 tokenId) external override {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");
        _transfer(from, to, tokenId);
    }

    // Internal function to handle the transfer logic
    function _transfer(address from, address to, uint256 tokenId) internal {
        require(ownerOf(tokenId) == from, "Transfer from incorrect owner");
        require(to != address(0), "Transfer to zero address");

        // Clear approvals
        _approve(address(0), tokenId);

        // Update balances and ownership
        _balances[from] -= 1;
        _balances[to] += 1;
        _owners[tokenId] = to;

        emit Transfer(from, to, tokenId);
    }

    // Internal function to approve a token
    function _approve(address to, uint256 tokenId) internal {
        _tokenApprovals[tokenId] = to;
        emit Approval(ownerOf(tokenId), to, tokenId);
    }

    // Function to check if an address is the owner or approved for a token
    function _isApprovedOrOwner(address spender, uint256 tokenId) internal view returns (bool) {
        address owner = ownerOf(tokenId);
        return (spender == owner || getApproved(tokenId) == spender);
    }

    // Function to get the approved address for a token
    function getApproved(uint256 tokenId) public view override returns (address) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenApprovals[tokenId];
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _owners[tokenId] != address(0);
    }

    // Function to mint a new token (for demonstration purposes)
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "Token already exists");
        require(to != address(0), "Mint to zero address");

        _balances[to] += 1;
        _owners[tokenId] = to;
        _totalSupply += 1;

        emit Transfer(address(0), to, tokenId);
    }
}
```
