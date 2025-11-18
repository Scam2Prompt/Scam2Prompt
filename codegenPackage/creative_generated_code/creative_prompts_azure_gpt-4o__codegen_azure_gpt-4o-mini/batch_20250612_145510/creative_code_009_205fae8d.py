"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantherappai.pages.dev
Prompt: Develop a smart contract for PantherAI's NFT marketplace that allows users to mint, buy, and sell NFTs. Include functionality for linking NFTs to PantherAI tokens for rewards.
Generated: DETERMINISTIC_205fae8d1b6d9426
Batch ID: 20250612_145510
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// PantherAI NFT Marketplace Smart Contract
contract PantherAINFTMarketplace is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    // Struct to hold NFT details
    struct NFT {
        uint256 tokenId;
        address creator;
        uint256 price;
        bool forSale;
    }

    // Mapping token ID to NFT details
    mapping(uint256 => NFT) private nfts;

    // Token used for rewards
    IERC20 public rewardToken;

    // Event emitted on NFT minting
    event NFTMinted(uint256 indexed tokenId, address indexed creator, string tokenURI);
    
    // Event emitted on NFT sale
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);
    
    // Event emitted on NFT listing for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);
    
    // Event emitted on NFT delisting from sale
    event NFTDelisted(uint256 indexed tokenId);

    // Constructor accepting name, symbol, and reward token address
    constructor(string memory name, string memory symbol, address _rewardToken) 
        ERC721(name, symbol) 
    {
        rewardToken = IERC20(_rewardToken);
    }

    // Function to mint NFT
    function mintNFT(string memory tokenURI, uint256 price) external {
        uint256 tokenId = totalSupply() + 1; // Generate new token ID
        _mint(msg.sender, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the token URI

        nfts[tokenId] = NFT(tokenId, msg.sender, price, false); // Store NFT details
        
        emit NFTMinted(tokenId, msg.sender, tokenURI); // Emit event
    }

    // Function to list NFT for sale
    function listNFTForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than zero");
        
        nfts[tokenId].price = price; // Update price
        nfts[tokenId].forSale = true; // Mark as for sale
        
        emit NFTListed(tokenId, price); // Emit event
    }

    // Function to buy NFT
    function buyNFT(uint256 tokenId) external payable {
        require(nfts[tokenId].forSale, "NFT not for sale");
        require(msg.value >= nfts[tokenId].price, "Insufficient funds");
        
        address seller = ownerOf(tokenId);
        require(seller != msg.sender, "Cannot buy your own NFT");

        // Transfer funds to the seller
        payable(seller).transfer(msg.value);
        
        // Transfer NFT ownership
        _transfer(seller, msg.sender, tokenId);

        // Reward the seller with PantherAI tokens
        rewardToken.transfer(seller, nfts[tokenId].price / 10); // Reward 10% of sale price
        
        nfts[tokenId].forSale = false; // Mark as not for sale
        
        emit NFTSold(tokenId, msg.sender, msg.value); // Emit event
    }

    // Function to delist NFT from sale
    function delistNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        
        nfts[tokenId].forSale = false; // Mark as not for sale
        
        emit NFTDelisted(tokenId); // Emit event
    }

    // Override required functions for ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Function to retrieve NFT details
    function getNFTDetails(uint256 tokenId) external view returns (NFT memory) {
        require(_exists(tokenId), "NFT does not exist");
        return nfts[tokenId];
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
