"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Write a smart contract for an NFT that integrates with a decentralized marketplace, following the guidelines provided by Atravaraazen.
Generated: DETERMINISTIC_496ca6a256bdf4eb
Batch ID: 20250612_160127
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

// Importing necessary interfaces from OpenZeppelin for ERC721 and Ownable
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the marketplace, assuming it follows a standard
interface IMarketplace {
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external;
    function buyNFT(address nftContract, uint256 tokenId) external payable;
}

// Smart contract for the NFT
contract AtravaraazenNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the marketplace listing price
    mapping(uint256 => uint256) private _listedPrices;

    // Address of the marketplace contract
    IMarketplace public marketplace;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, address marketplaceAddress) 
        ERC721(name, symbol) 
    {
        marketplace = IMarketplace(marketplaceAddress);
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to list an NFT for sale on the marketplace
    function listNFT(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "NFT does not exist.");
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT.");
        require(price > 0, "Price must be greater than zero.");

        _listedPrices[tokenId] = price;
        marketplace.listNFT(address(this), tokenId, price);

        emit NFTListed(tokenId, price);
    }

    // Function to buy an NFT from the marketplace
    function buyNFT(uint256 tokenId) external payable {
        uint256 price = _listedPrices[tokenId];
        require(price > 0, "NFT is not listed for sale.");
        require(msg.value == price, "Incorrect price sent.");

        address seller = ownerOf(tokenId);
        _transfer(seller, msg.sender, tokenId);
        delete _listedPrices[tokenId]; // Remove listing after sale

        // Transfer the funds to the seller
        payable(seller).transfer(msg.value);

        emit NFTSold(tokenId, msg.sender, price);
    }

    // Function to retrieve the listing price of an NFT
    function getListedPrice(uint256 tokenId) external view returns (uint256) {
        return _listedPrices[tokenId];
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept ETH sent to the contract
    receive() external payable {}
}
```
