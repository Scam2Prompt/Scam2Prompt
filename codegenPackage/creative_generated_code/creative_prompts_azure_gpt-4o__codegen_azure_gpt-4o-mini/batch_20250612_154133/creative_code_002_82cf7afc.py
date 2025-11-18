"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bids-sea.io
Prompt: Create a function in Solidity to mint NFTs programmatically, following the steps outlined on the Bids Sea Community site (wallet setup, collection creation, NFT addition, and sale).
Generated: DETERMINISTIC_82cf7afcb6f36ec7
Batch ID: 20250612_154133
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title: Bids Sea NFT Minting
// @dev: This contract enables the minting of NFTs and manages their sale.

contract BidsSeaNFT is ERC721Enumerable, Ownable {
    // State variables
    uint256 public nextTokenId; // Counter for the next token ID
    uint256 public salePrice;    // Price of each NFT
    mapping(uint256 => string) private _tokenURIs; // Mapping from token ID to metadata URI

    // Events
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);
    event SalePriceUpdated(uint256 newSalePrice);

    // Constructor
    constructor(string memory name, string memory symbol, uint256 _salePrice) ERC721(name, symbol) {
        salePrice = _salePrice; // Set the initial sale price
    }

    // @dev: Function to mint a new NFT
    // @param to: Address of the NFT recipient
    // @param tokenURI: Metadata URI of the NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Token URI must not be empty");

        uint256 tokenId = nextTokenId; // Get the current token ID
        nextTokenId++; // Increment the token ID for the next mint

        _mint(to, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the token URI

        emit NFTMinted(tokenId, to, tokenURI); // Emit the minting event
    }

    // @dev: Function to set the token URI
    // @param tokenId: ID of the token
    // @param tokenURI: Metadata URI of the NFT
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI; // Set the token URI
    }

    // @dev: Function to retrieve the token URI
    // @param tokenId: ID of the token
    // @return: The token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // @dev: Update the sale price of NFTs
    // @param newSalePrice: New price for the NFTs
    function updateSalePrice(uint256 newSalePrice) external onlyOwner {
        salePrice = newSalePrice; // Update the sale price
        emit SalePriceUpdated(newSalePrice); // Emit the price update event
    }

    // @dev: Buy an NFT
    // @param tokenId: ID of the token to be purchased
    function buyNFT(uint256 tokenId) external payable {
        require(msg.value == salePrice, "Incorrect Ether sent");
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) != msg.sender, "Cannot buy your own NFT");

        address owner = ownerOf(tokenId);
        _transfer(owner, msg.sender, tokenId); // Transfer the NFT
        payable(owner).transfer(msg.value); // Transfer Ether to the previous owner
    }

    // @dev: Fallback function to accept Ether
    receive() external payable {}
}
```
