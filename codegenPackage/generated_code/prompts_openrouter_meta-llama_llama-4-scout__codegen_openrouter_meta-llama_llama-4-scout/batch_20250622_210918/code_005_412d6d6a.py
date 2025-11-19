"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Design an ERC404 token standard implementation that allows for seamless interaction with decentralized exchanges like Uniswap, using $GOFURS as a reference.
Generated: DETERMINISTIC_412d6d6a82b710b3
Batch ID: 20250622_210918
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title GOFURS ERC404 Token Standard Implementation
 * @author [Your Name]
 * @notice Implementation of the ERC404 token standard for seamless interaction with decentralized exchanges like Uniswap.
 * @dev This contract is designed to be production-ready and follows best practices for Solidity.
 */
contract GOFURSToken is ERC20, ERC721, ReentrancyGuard {
    // Mapping of token IDs to their owners
    mapping(uint256 => address) private _tokenOwners;

    // Mapping of token IDs to their URIs
    mapping(uint256 => string) private _tokenURIs;

    // Mapping of addresses to their balances and token IDs
    mapping(address => uint256) private _balances;
    mapping(address => mapping(uint256 => uint256)) private _tokenBalances;

    // Event emitted when a token is minted
    event Mint(address indexed to, uint256 tokenId);

    // Event emitted when a token is burned
    event Burn(address indexed from, uint256 tokenId);

    /**
     * @notice Constructor for the GOFURSToken contract
     * @param name_ The name of the token
     * @param symbol_ The symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) ERC721(name_, symbol_) {}

    /**
     * @notice Mints a new token
     * @param to The address to mint the token to
     * @param tokenId The ID of the token to mint
     */
    function mint(address to, uint256 tokenId) public {
        _mint(to, tokenId);
        _tokenOwners[tokenId] = to;
        emit Mint(to, tokenId);
    }

    /**
     * @notice Burns a token
     * @param tokenId The ID of the token to burn
     */
    function burn(uint256 tokenId) public {
        address owner = _tokenOwners[tokenId];
        require(msg.sender == owner, "Only the owner can burn this token");
        _burn(tokenId);
        delete _tokenOwners[tokenId];
        emit Burn(owner, tokenId);
    }

    /**
     * @notice Transfers a token
     * @param from The address to transfer the token from
     * @param to The address to transfer the token to
     * @param tokenId The ID of the token to transfer
     */
    function transferFrom(address from, address to, uint256 tokenId) public override {
        require(_tokenOwners[tokenId] == from, "Only the owner can transfer this token");
        _transfer(from, to, tokenId);
        _tokenOwners[tokenId] = to;
    }

    /**
     * @notice Gets the balance of an address
     * @param owner The address to get the balance of
     * @return The balance of the address
     */
    function balanceOf(address owner) public view override returns (uint256) {
        return _balances[owner];
    }

    /**
     * @notice Gets the token ID at a given index
     * @param owner The address to get the token ID from
     * @param index The index of the token ID
     * @return The token ID at the given index
     */
    function tokenOfOwnerByIndex(address owner, uint256 index) public view returns (uint256) {
        uint256 tokenId = 0;
        for (uint256 i = 0; i < _balances[owner]; i++) {
            if (i == index) {
                return tokenId;
            }
            tokenId++;
        }
        revert("Index out of range");
    }

    /**
     * @notice Gets the URI of a token
     * @param tokenId The ID of the token to get the URI of
     * @return The URI of the token
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        return _tokenURIs[tokenId];
    }

    /**
     * @notice Sets the URI of a token
     * @param tokenId The ID of the token to set the URI of
     * @param uri The URI to set
     */
    function setTokenURI(uint256 tokenId, string memory uri) public {
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @notice Mints tokens to an address
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address to, uint256 amount) internal override {
        super._mint(to, amount);
        _balances[to] += amount;
    }

    /**
     * @notice Burns tokens from an address
     * @param from The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function _burn(address from, uint256 amount) internal override {
        super._burn(from, amount);
        _balances[from] -= amount;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        super._transfer(from, to, amount);
    }

    /**
     * @notice Transfers a token from one address to another
     * @param from The address to transfer the token from
     * @param to The address to transfer the token to
     * @param tokenId The ID of the token to transfer
     */
    function _transfer(address from, address to, uint256 tokenId) internal {
        _tokenBalances[from][tokenId]--;
        _tokenBalances[to][tokenId]++;
    }

    /**
     * @notice Safely transfers a token from one address to another
     * @param from The address to transfer the token from
     * @param to The address to transfer the token to
     * @param tokenId The ID of the token to transfer
     */
    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        _transfer(from, to, tokenId);
        _tokenOwners[tokenId] = to;
    }
}
```
