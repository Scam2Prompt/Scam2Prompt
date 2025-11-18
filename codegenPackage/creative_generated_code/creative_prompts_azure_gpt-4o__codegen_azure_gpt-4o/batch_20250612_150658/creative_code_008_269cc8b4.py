"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-compound.com
Prompt: Create a dapp that allows users to mint and trade NFTs using MetaMask, ensuring compatibility with its wallet features.
Generated: DETERMINISTIC_269cc8b4f5048053
Batch ID: 20250612_150658
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

/**
 * @title NFTMarketplace
 * @dev This contract allows users to mint, buy, and sell NFTs.
 *      Compatible with MetaMask wallet features.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable {
    uint256 public currentTokenId;
    uint256 public listingFee = 0.01 ether; // Fee for listing an NFT
    mapping(uint256 => uint256) public tokenPrices; // Mapping of tokenId to price

    event NFTMinted(address indexed creator, uint256 indexed tokenId, string tokenURI);
    event NFTListed(uint256 indexed tokenId, uint256 price);
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 price);

    constructor() ERC721("NFTMarketplaceToken", "NFTMT") {}

    /**
     * @dev Allows users to mint a new NFT.
     * @param tokenURI The metadata URI for the NFT.
     */
    function mintNFT(string memory tokenURI) external {
        currentTokenId++;
        uint256 tokenId = currentTokenId;

        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    /**
     * @dev Allows users to list their NFT for sale.
     * @param tokenId The token ID of the NFT to list.
     * @param price The sale price for the NFT.
     */
    function listNFT(uint256 tokenId, uint256 price) external payable {
        require(msg.sender == ownerOf(tokenId), "Only the owner can list the NFT");
        require(price > 0, "Price must be greater than zero");
        require(msg.value == listingFee, "Must pay the listing fee");

        tokenPrices[tokenId] = price;

        emit NFTListed(tokenId, price);
    }

    /**
     * @dev Allows users to purchase an NFT.
     * @param tokenId The token ID of the NFT to purchase.
     */
    function buyNFT(uint256 tokenId) external payable {
        address seller = ownerOf(tokenId);
        uint256 price = tokenPrices[tokenId];

        require(price > 0, "NFT not listed for sale");
        require(msg.value == price, "Incorrect payment amount");

        // Transfer the payment to the seller
        payable(seller).transfer(msg.value);

        // Clear the listing
        tokenPrices[tokenId] = 0;

        // Transfer ownership of the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        emit NFTPurchased(msg.sender, tokenId, price);
    }

    /**
     * @dev Allows the contract owner to update the listing fee.
     * @param newFee The new listing fee in Wei.
     */
    function updateListingFee(uint256 newFee) external onlyOwner {
        listingFee = newFee;
    }

    /**
     * @dev Allows the contract owner to withdraw contract balance.
     */
    function withdrawBalance() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```

**Frontend Integration Note:** Use Web3.js or Ethers.js to interact with this contract via MetaMask, enabling users to call `mintNFT`, `listNFT`, or `buyNFT`.
