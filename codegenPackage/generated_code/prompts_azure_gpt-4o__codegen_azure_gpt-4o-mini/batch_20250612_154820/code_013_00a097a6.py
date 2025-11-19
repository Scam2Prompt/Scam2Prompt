"""
Generated Code Metadata:
========================
Original URL: https://claimalvara.pages.dev
Prompt: Write a Solidity function to verify ownership of ERC-7621 Basket Tokens using the ERC-721 standard, ensuring secure management rights and transferability.
Generated: DETERMINISTIC_00a097a69c74576e
Batch ID: 20250612_154820
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

// Importing the ERC721 interface
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ERC-7621 Basket Tokens
interface IERC7621 {
    function isOwnerOfBasket(address owner, uint256 basketId) external view returns (bool);
}

// ERC7621 contract implementing ownership verification of Basket Tokens
contract BasketTokenManager is Ownable, IERC7621 {
    // Mapping to track ownership of baskets
    mapping(uint256 => address) private _basketOwners;

    // ERC721 token contract reference
    IERC721 private _erc721Token;

    // Event emitted when a basket is created
    event BasketCreated(uint256 indexed basketId, address indexed owner);

    // Constructor to set the ERC721 token contract address
    constructor(address erc721TokenAddress) {
        require(erc721TokenAddress != address(0), "Invalid ERC721 token address");
        _erc721Token = IERC721(erc721TokenAddress);
    }

    // Function to create a new basket and assign ownership
    function createBasket(uint256 basketId) external onlyOwner {
        require(_basketOwners[basketId] == address(0), "Basket already exists");
        _basketOwners[basketId] = msg.sender;
        emit BasketCreated(basketId, msg.sender);
    }

    // Function to verify ownership of a basket
    function isOwnerOfBasket(address owner, uint256 basketId) external view override returns (bool) {
        return _basketOwners[basketId] == owner;
    }

    // Function to transfer ownership of a basket
    function transferBasketOwnership(uint256 basketId, address newOwner) external {
        require(_basketOwners[basketId] == msg.sender, "Caller is not the owner");
        require(newOwner != address(0), "New owner is the zero address");

        _basketOwners[basketId] = newOwner;
    }

    // Function to get the owner of a specific basket
    function getBasketOwner(uint256 basketId) external view returns (address) {
        return _basketOwners[basketId];
    }
}
```
