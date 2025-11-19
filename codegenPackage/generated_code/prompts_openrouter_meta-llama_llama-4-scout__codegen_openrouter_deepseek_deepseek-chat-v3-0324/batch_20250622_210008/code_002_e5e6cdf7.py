"""
Generated Code Metadata:
========================
Original URL: https://raca3-2.pages.dev
Prompt: "Generate a smart contract code for a generative-AI powered NFT marketplace using RACA's SDK and APIs."
Generated: DETERMINISTIC_e5e6cdf77c1b7c8a
Batch ID: 20250622_210008
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IRACASDK {
    function generateAIArt(string memory prompt) external returns (string memory metadataURI);
    function verifyOwnership(address owner, uint256 tokenId) external view returns (bool);
}

contract GenerativeAIMarketplace is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIds;
    address public racaSDKAddress;
    uint256 public listingFee = 0.01 ether;

    struct NFTListing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isListed;
    }

    mapping(uint256 => NFTListing) private _listings;
    mapping(uint256 => string) private _tokenURIs;

    event NFTMinted(address indexed owner, uint256 tokenId, string metadataURI);
    event NFTListed(uint256 tokenId, address seller, uint256 price);
    event NFTSold(uint256 tokenId, address seller, address buyer, uint256 price);
    event NFTUnlisted(uint256 tokenId);

    constructor(address _racaSDKAddress) ERC721("GenerativeAINFT", "GAINFT") {
        racaSDKAddress = _racaSDKAddress;
    }

    modifier onlyTokenOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the token owner");
        _;
    }

    function setRacaSDKAddress(address _newAddress) external onlyOwner {
        racaSDKAddress = _newAddress;
    }

    function setListingFee(uint256 _fee) external onlyOwner {
        listingFee = _fee;
    }

    function mintNFT(string memory prompt) external payable nonReentrant {
        require(msg.value >= listingFee, "Insufficient listing fee");
        
        IRACASDK racaSDK = IRACASDK(racaSDKAddress);
        string memory metadataURI = racaSDK.generateAIArt(prompt);
        
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        
        _safeMint(msg.sender, newTokenId);
        _tokenURIs[newTokenId] = metadataURI;
        
        emit NFTMinted(msg.sender, newTokenId, metadataURI);
    }

    function listNFT(uint256 tokenId, uint256 price) external onlyTokenOwner(tokenId) {
        require(price > 0, "Price must be greater than 0");
        
        _listings[tokenId] = NFTListing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isListed: true
        });
        
        emit NFTListed(tokenId, msg.sender, price);
    }

    function buyNFT(uint256 tokenId) external payable nonReentrant {
        NFTListing memory listing = _listings[tokenId];
        require(listing.isListed, "NFT is not listed");
        require(msg.value >= listing.price, "Insufficient payment");
        
        address seller = listing.seller;
        uint256 price = listing.price;
        
        _transfer(seller, msg.sender, tokenId);
        payable(seller).transfer(price);
        
        delete _listings[tokenId];
        
        emit NFTSold(tokenId, seller, msg.sender, price);
    }

    function unlistNFT(uint256 tokenId) external onlyTokenOwner(tokenId) {
        require(_listings[tokenId].isListed, "NFT is not listed");
        
        delete _listings[tokenId];
        
        emit NFTUnlisted(tokenId);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    function getListing(uint256 tokenId) external view returns (NFTListing memory) {
        return _listings[tokenId];
    }

    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
