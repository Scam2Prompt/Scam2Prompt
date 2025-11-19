"""
Generated Code Metadata:
========================
Original URL: https://pudgypenguins.pages.dev
Prompt: Design a smart contract for Pudgy Penguins that allows for the creation, buying, and selling of these NFTs on the Ethereum blockchain.
Generated: DETERMINISTIC_f074f7dbd544b653
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Pudgy Penguins NFT Smart Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PudgyPenguins is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Token counter
    Counters.Counter private _tokenIdCounter;
    
    // Base URI for metadata
    string private _baseTokenURI;
    
    // Max supply of Pudgy Penguins
    uint256 public constant MAX_SUPPLY = 8888;
    
    // Price per token (in wei)
    uint256 public price = 0.08 ether;
    
    // Sale active flag
    bool public saleIsActive = false;
    
    // Mapping from token ID to listing price
    mapping(uint256 => uint256) private _tokenPrices;
    
    // Events
    event TokenPriceSet(uint256 indexed tokenId, uint256 price);
    event TokenPurchased(uint256 indexed tokenId, address buyer, uint256 price);
    
    constructor(string memory baseURI) ERC721("Pudgy Penguins", "PPG") {
        setBaseURI(baseURI);
    }
    
    // Override base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }
    
    // Set base URI (only owner)
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }
    
    // Flip sale state (only owner)
    function flipSaleState() public onlyOwner {
        saleIsActive = !saleIsActive;
    }
    
    // Set price (only owner)
    function setPrice(uint256 newPrice) public onlyOwner {
        price = newPrice;
    }
    
    // Mint new tokens (only owner)
    function reservePenguins(uint256 count) public onlyOwner {
        require(totalSupply() + count <= MAX_SUPPLY, "Exceeds max supply");
        
        for (uint256 i = 0; i < count; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current());
            _tokenIdCounter.increment();
        }
    }
    
    // Public minting function
    function mintPenguin() public payable nonReentrant {
        require(saleIsActive, "Sale is not active");
        require(totalSupply() < MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= price, "Ether sent is not correct");
        
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);
        _tokenIdCounter.increment();
    }
    
    // List a token for sale
    function listForSale(uint256 tokenId, uint256 salePrice) public {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        _tokenPrices[tokenId] = salePrice;
        emit TokenPriceSet(tokenId, salePrice);
    }
    
    // Buy a listed token
    function buyToken(uint256 tokenId) public payable nonReentrant {
        uint256 salePrice = _tokenPrices[tokenId];
        require(salePrice > 0, "Token not for sale");
        require(msg.value >= salePrice, "Insufficient payment");
        
        address seller = ownerOf(tokenId);
        _transfer(seller, msg.sender, tokenId);
        
        // Reset price
        _tokenPrices[tokenId] = 0;
        
        // Transfer payment to seller
        (bool success, ) = seller.call{value: msg.value}("");
        require(success, "Transfer failed");
        
        emit TokenPurchased(tokenId, msg.sender, salePrice);
    }
    
    // Get price of a token
    function getTokenPrice(uint256 tokenId) public view returns (uint256) {
        return _tokenPrices[tokenId];
    }
    
    // Withdraw contract balance (only owner)
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }
    
    // Override required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
    
    // Override required by Solidity
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
