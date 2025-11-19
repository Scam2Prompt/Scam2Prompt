"""
Generated Code Metadata:
========================
Original URL: https://alphaspherearts.com
Prompt: Develop a smart contract using Solidity to create, buy, and sell NFTs on a platform like Alpha Sphere Arts.
Generated: DETERMINISTIC_783f77ad8e05085b
Batch ID: 20250622_212600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title AlphaSphereArtsNFT
 * @author [Your Name]
 * @notice A smart contract for creating, buying, and selling NFTs on Alpha Sphere Arts platform.
 */
contract AlphaSphereArtsNFT {
    // Mapping of NFT owners
    mapping (address => mapping (uint256 => uint256)) public nftOwners;

    // Mapping of NFT metadata
    mapping (uint256 => NFT) public nftMetadata;

    // Mapping of NFT prices
    mapping (uint256 => uint256) public nftPrices;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is bought
    event NFTBought(uint256 indexed tokenId, address indexed buyer);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed seller);

    // Struct to represent NFT metadata
    struct NFT {
        string name;
        string description;
        string imageURI;
    }

    // Total supply of NFTs
    uint256 public totalSupply;

    // Mapping of allowed minters
    mapping (address => bool) public minters;

    /**
     * @dev Constructor
     */
    constructor() public {
        // Initialize total supply
        totalSupply = 0;
    }

    /**
     * @dev Add a minter
     * @param minter Address of the minter to add
     */
    function addMinter(address minter) public onlyOwner {
        minters[minter] = true;
    }

    /**
     * @dev Remove a minter
     * @param minter Address of the minter to remove
     */
    function removeMinter(address minter) public onlyOwner {
        minters[minter] = false;
    }

    /**
     * @dev Create a new NFT
     * @param name Name of the NFT
     * @param description Description of the NFT
     * @param imageURI URI of the NFT image
     */
    function createNFT(string memory name, string memory description, string memory imageURI) public {
        require(minters[msg.sender], "Only minters can create NFTs");

        // Create a new NFT
        NFT memory nft = NFT(name, description, imageURI);
        uint256 tokenId = totalSupply + 1;
        nftMetadata[tokenId] = nft;
        nftOwners[msg.sender][tokenId] = tokenId;
        totalSupply++;

        // Emit event
        emit NFTCreated(tokenId, msg.sender);
    }

    /**
     * @dev Buy an NFT
     * @param tokenId ID of the NFT to buy
     */
    function buyNFT(uint256 tokenId) public payable {
        // Check if NFT exists
        require(nftMetadata[tokenId].name != "", "NFT does not exist");

        // Check if NFT is for sale
        require(nftPrices[tokenId] > 0, "NFT is not for sale");

        // Check if buyer has enough ether
        require(msg.value >= nftPrices[tokenId], "Buyer does not have enough ether");

        // Transfer ownership
        address seller = getOwnerOf(tokenId);
        nftOwners[seller][tokenId] = 0;
        nftOwners[msg.sender][tokenId] = tokenId;

        // Update price
        nftPrices[tokenId] = 0;

        // Emit events
        emit NFTBought(tokenId, msg.sender);
        emit NFTSold(tokenId, seller);
    }

    /**
     * @dev Sell an NFT
     * @param tokenId ID of the NFT to sell
     * @param price Price of the NFT
     */
    function sellNFT(uint256 tokenId, uint256 price) public {
        // Check if NFT exists
        require(nftMetadata[tokenId].name != "", "NFT does not exist");

        // Check if seller is the owner
        require(getOwnerOf(tokenId) == msg.sender, "Only owner can sell NFT");

        // Update price
        nftPrices[tokenId] = price;
    }

    /**
     * @dev Get the owner of an NFT
     * @param tokenId ID of the NFT
     * @return address Owner of the NFT
     */
    function getOwnerOf(uint256 tokenId) public view returns (address) {
        for (address owner in nftOwners) {
            if (nftOwners[owner][tokenId] == tokenId) {
                return owner;
            }
        }
        return address(0);
    }

    /**
     * @dev Get the metadata of an NFT
     * @param tokenId ID of the NFT
     * @return NFT Metadata of the NFT
     */
    function getNFT(uint256 tokenId) public view returns (NFT memory) {
        return nftMetadata[tokenId];
    }

    /**
     * @dev Get the price of an NFT
     * @param tokenId ID of the NFT
     * @return uint256 Price of the NFT
     */
    function getNFTPrice(uint256 tokenId) public view returns (uint256) {
        return nftPrices[tokenId];
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Owner of the contract
    address public owner;

    /**
     * @dev Constructor
     */
    constructor() public {
        owner = msg.sender;
    }
}
```
