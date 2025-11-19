"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Generate code for minting, trading, and collateralizing NFTs on Linea's zkEVM using Ethereum battle-tested components.
Generated: DETERMINISTIC_641d6c78d06e9bf7
Batch ID: 20250622_212312
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the NFT marketplace
interface INFTMarketplace {
    function listNFT(uint256 tokenId, uint256 price) external;
    function buyNFT(uint256 tokenId) external payable;
}

// NFT contract for minting, trading, and collateralizing
contract NFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to collateral amount
    mapping(uint256 => uint256) public collateral;

    // Event emitted when an NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner);

    // Event emitted when collateral is added
    event CollateralAdded(uint256 indexed tokenId, uint256 amount);

    // Event emitted when collateral is withdrawn
    event CollateralWithdrawn(uint256 indexed tokenId, uint256 amount);

    // Constructor to initialize the NFT contract
    constructor() ERC721("LineaNFT", "LNFT") {}

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit NFTMinted(tokenId, msg.sender);
    }

    // Function to add collateral to an NFT
    function addCollateral(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(msg.value > 0, "Collateral must be greater than zero");

        collateral[tokenId] += msg.value;
        emit CollateralAdded(tokenId, msg.value);
    }

    // Function to withdraw collateral from an NFT
    function withdrawCollateral(uint256 tokenId, uint256 amount) external onlyOwner {
        require(_exists(tokenId), "NFT does not exist");
        require(collateral[tokenId] >= amount, "Insufficient collateral");

        collateral[tokenId] -= amount;
        payable(msg.sender).transfer(amount);
        emit CollateralWithdrawn(tokenId, amount);
    }

    // Function to list an NFT for sale on the marketplace
    function listNFTForSale(INFTMarketplace marketplace, uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");

        // Call the marketplace to list the NFT
        marketplace.listNFT(tokenId, price);
    }

    // Function to buy an NFT from the marketplace
    function buyNFT(INFTMarketplace marketplace, uint256 tokenId) external payable {
        require(msg.value > 0, "Payment must be greater than zero");

        // Call the marketplace to buy the NFT
        marketplace.buyNFT{value: msg.value}(tokenId);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
