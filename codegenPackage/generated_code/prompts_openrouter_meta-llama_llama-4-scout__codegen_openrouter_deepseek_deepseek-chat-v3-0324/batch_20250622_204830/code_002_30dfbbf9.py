"""
Generated Code Metadata:
========================
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Design a smart contract for the issuance and trading of NFTs on a blockchain platform, inspired by Cyber Lama AI's NFT collection.
Generated: DETERMINISTIC_30dfbbf940c3e6bb
Batch ID: 20250622_204830
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CyberLamaNFT is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // NFT price in wei
    uint256 public mintPrice = 0.1 ether;
    
    // Maximum supply of NFTs
    uint256 public maxSupply = 10000;
    
    // Base URI for token metadata
    string public baseTokenURI;

    // Royalty percentage (e.g., 100 = 1%)
    uint256 public royaltyPercentage = 500; // 5%
    
    // Marketplace address for royalty payments
    address payable public marketplaceAddress;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);
    event NFTSold(address indexed seller, address indexed buyer, uint256 tokenId, uint256 price);
    event RoyaltyPaid(address indexed receiver, uint256 amount);

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _baseTokenURI,
        address payable _marketplaceAddress
    ) ERC721(_name, _symbol) {
        baseTokenURI = _baseTokenURI;
        marketplaceAddress = _marketplaceAddress;
    }

    // Mint a new NFT
    function mintNFT(string memory _tokenURI) public payable {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, _tokenURI);
        
        emit NFTMinted(msg.sender, tokenId, _tokenURI);
    }

    // Buy an NFT from another user
    function buyNFT(uint256 _tokenId) public payable {
        address seller = ownerOf(_tokenId);
        require(seller != msg.sender, "Cannot buy your own NFT");
        require(msg.value > 0, "Invalid price");

        // Calculate royalty
        uint256 royaltyAmount = msg.value.mul(royaltyPercentage).div(10000);
        uint256 sellerAmount = msg.value.sub(royaltyAmount);

        // Transfer ownership
        _transfer(seller, msg.sender, _tokenId);

        // Transfer funds
        payable(seller).transfer(sellerAmount);
        marketplaceAddress.transfer(royaltyAmount);

        emit NFTSold(seller, msg.sender, _tokenId, msg.value);
        emit RoyaltyPaid(marketplaceAddress, royaltyAmount);
    }

    // Set mint price (only owner)
    function setMintPrice(uint256 _newPrice) public onlyOwner {
        mintPrice = _newPrice;
    }

    // Set royalty percentage (only owner)
    function setRoyaltyPercentage(uint256 _newPercentage) public onlyOwner {
        require(_newPercentage <= 2000, "Royalty too high"); // Max 20%
        royaltyPercentage = _newPercentage;
    }

    // Set marketplace address (only owner)
    function setMarketplaceAddress(address payable _newAddress) public onlyOwner {
        marketplaceAddress = _newAddress;
    }

    // Set base URI (only owner)
    function setBaseURI(string memory _newBaseURI) public onlyOwner {
        baseTokenURI = _newBaseURI;
    }

    // Withdraw contract balance (only owner)
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override required functions
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    // Get total minted NFTs
    function totalMinted() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
