"""
Generated Code Metadata:
========================
Original URL: https://instantswap.vercel.app
Prompt: Develop a smart contract that integrates SushiSwap's Shoyu NFT payments system to allow users to purchase NFTs using Ethereum.
Generated: DETERMINISTIC_a0b8f1f250f0f929
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IShoyuNFT {
    function mint(address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}

contract SushiSwapNFTPayment is Ownable, ReentrancyGuard {
    IShoyuNFT public shoyuNFT;
    IERC20 public sushiToken;
    
    struct NFTListing {
        uint256 tokenId;
        uint256 price;
        address seller;
        bool isListed;
    }
    
    mapping(uint256 => NFTListing) public nftListings;
    uint256[] public listedTokenIds;
    
    event NFTListed(uint256 indexed tokenId, uint256 price, address seller);
    event NFTPurchased(uint256 indexed tokenId, address buyer, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId);
    
    constructor(address _shoyuNFT, address _sushiToken) {
        shoyuNFT = IShoyuNFT(_shoyuNFT);
        sushiToken = IERC20(_sushiToken);
    }
    
    function listNFT(uint256 tokenId, uint256 price) external {
        require(shoyuNFT.ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(price > 0, "Price must be greater than 0");
        require(!nftListings[tokenId].isListed, "NFT already listed");
        
        nftListings[tokenId] = NFTListing({
            tokenId: tokenId,
            price: price,
            seller: msg.sender,
            isListed: true
        });
        
        listedTokenIds.push(tokenId);
        emit NFTListed(tokenId, price, msg.sender);
    }
    
    function purchaseNFT(uint256 tokenId) external nonReentrant {
        NFTListing storage listing = nftListings[tokenId];
        require(listing.isListed, "NFT not listed for sale");
        require(sushiToken.balanceOf(msg.sender) >= listing.price, "Insufficient Sushi balance");
        
        // Transfer Sushi tokens from buyer to seller
        require(sushiToken.transferFrom(msg.sender, listing.seller, listing.price), "Sushi transfer failed");
        
        // Transfer NFT from contract to buyer
        shoyuNFT.transferFrom(address(this), msg.sender, tokenId);
        
        // Update listing status
        listing.isListed = false;
        _removeTokenIdFromList(tokenId);
        
        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }
    
    function unlistNFT(uint256 tokenId) external {
        require(nftListings[tokenId].isListed, "NFT not listed");
        require(nftListings[tokenId].seller == msg.sender, "Not the seller");
        
        nftListings[tokenId].isListed = false;
        _removeTokenIdFromList(tokenId);
        
        emit NFTUnlisted(tokenId);
    }
    
    function _removeTokenIdFromList(uint256 tokenId) private {
        for (uint256 i = 0; i < listedTokenIds.length; i++) {
            if (listedTokenIds[i] == tokenId) {
                listedTokenIds[i] = listedTokenIds[listedTokenIds.length - 1];
                listedTokenIds.pop();
                break;
            }
        }
    }
    
    function getListedNFTs() external view returns (NFTListing[] memory) {
        NFTListing[] memory listings = new NFTListing[](listedTokenIds.length);
        for (uint256 i = 0; i < listedTokenIds.length; i++) {
            listings[i] = nftListings[listedTokenIds[i]];
        }
        return listings;
    }
    
    function setShoyuNFT(address _shoyuNFT) external onlyOwner {
        shoyuNFT = IShoyuNFT(_shoyuNFT);
    }
    
    function setSushiToken(address _sushiToken) external onlyOwner {
        sushiToken = IERC20(_sushiToken);
    }
    
    function withdrawERC20(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
