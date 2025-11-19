"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract for an NFT collection, similar to the Pablo Cartel NFT Collection, with functionality for minting, buying, and selling NFTs, and integrating it with the $PABLO token ecosystem.
Generated: DETERMINISTIC_a02f1698a9f0bcf8
Batch ID: 20250622_204809
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title PabloCartelNFT
 * @dev A smart contract for an NFT collection with minting, buying, and selling functionalities.
 */
contract PabloCartelNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to price
    mapping(uint256 => uint256) private _tokenPrices;

    // Address of the $PABLO token contract
    IERC20 public pabToken;

    // Event emitted when an NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is listed for sale
    event ListedForSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event Sold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    /**
     * @dev Constructor to initialize the contract with the token name and symbol.
     * @param _pabToken Address of the $PABLO token contract.
     */
    constructor(address _pabToken) ERC721("Pablo Cartel NFT", "PABLO") {
        pabToken = IERC20(_pabToken);
    }

    /**
     * @dev Mint a new NFT.
     * @param to The address that will own the minted NFT.
     */
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();
        emit Minted(tokenId, to);
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId The ID of the NFT to list.
     * @param price The price in $PABLO tokens.
     */
    function listForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than zero");

        _tokenPrices[tokenId] = price;
        emit ListedForSale(tokenId, price);
    }

    /**
     * @dev Buy an NFT.
     * @param tokenId The ID of the NFT to buy.
     */
    function buy(uint256 tokenId) external {
        uint256 price = _tokenPrices[tokenId];
        require(price > 0, "NFT not for sale");
        require(pabToken.balanceOf(msg.sender) >= price, "Insufficient $PABLO balance");

        address seller = ownerOf(tokenId);
        pabToken.transferFrom(msg.sender, seller, price);
        _transfer(seller, msg.sender, tokenId);

        // Clear the price after sale
        delete _tokenPrices[tokenId];
        emit Sold(tokenId, msg.sender, price);
    }

    /**
     * @dev Get the price of an NFT.
     * @param tokenId The ID of the NFT.
     * @return The price in $PABLO tokens.
     */
    function getPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Withdraw $PABLO tokens from the contract.
     * @param amount The amount of $PABLO tokens to withdraw.
     */
    function withdrawPablo(uint256 amount) external onlyOwner {
        require(pabToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        pabToken.transfer(msg.sender, amount);
    }
}
```
