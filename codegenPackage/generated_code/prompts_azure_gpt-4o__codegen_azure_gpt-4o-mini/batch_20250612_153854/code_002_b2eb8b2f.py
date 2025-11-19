"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Generate Solidity code for a smart contract that implements a minting mechanism similar to the MegaRabbit NFT collection, including features like mint groups, wallet limits, and maximum supply.
Generated: DETERMINISTIC_b2eb8b2f31db223d
Batch ID: 20250612_153854
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract MegaRabbitNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public maxSupply; // Maximum supply of NFTs
    uint256 public maxMintPerWallet; // Maximum NFTs a wallet can mint
    mapping(address => uint256) public walletMintCount; // Track mint count per wallet

    // Minting groups
    struct MintGroup {
        uint256 price; // Price for the mint group
        uint256 maxMint; // Maximum NFTs that can be minted in this group
        bool isActive; // Is the mint group active
    }
    MintGroup[] public mintGroups; // Array of mint groups

    // Events
    event Mint(address indexed to, uint256 indexed tokenId);

    // Constructor
    constructor(uint256 _maxSupply, uint256 _maxMintPerWallet) ERC721("MegaRabbitNFT", "MRNFT") {
        maxSupply = _maxSupply;
        maxMintPerWallet = _maxMintPerWallet;
    }

    // Function to add a new mint group
    function addMintGroup(uint256 price, uint256 maxMint) external onlyOwner {
        mintGroups.push(MintGroup({
            price: price,
            maxMint: maxMint,
            isActive: true
        }));
    }

    // Function to mint NFTs
    function mint(uint256 groupId, uint256 quantity) external payable {
        require(groupId < mintGroups.length, "Invalid mint group");
        MintGroup storage group = mintGroups[groupId];
        require(group.isActive, "Mint group is not active");
        require(quantity > 0, "Quantity must be greater than 0");
        require(quantity <= group.maxMint, "Exceeds max mint limit for group");
        require(walletMintCount[msg.sender] + quantity <= maxMintPerWallet, "Exceeds wallet mint limit");
        require(totalSupply() + quantity <= maxSupply, "Exceeds maximum supply");
        require(msg.value >= group.price * quantity, "Insufficient payment");

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(msg.sender, tokenId);
            emit Mint(msg.sender, tokenId);
        }

        // Update wallet mint count
        walletMintCount[msg.sender] += quantity;
    }

    // Function to withdraw contract balance
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to toggle mint group active status
    function toggleMintGroupActive(uint256 groupId) external onlyOwner {
        require(groupId < mintGroups.length, "Invalid mint group");
        mintGroups[groupId].isActive = !mintGroups[groupId].isActive;
    }

    // Function to get the current token ID counter
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to get mint group details
    function getMintGroup(uint256 groupId) external view returns (MintGroup memory) {
        require(groupId < mintGroups.length, "Invalid mint group");
        return mintGroups[groupId];
    }
}
```
