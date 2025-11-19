"""
Generated Code Metadata:
========================
Original URL: https://nft-shibonk-wl.web.app
Prompt: Create a basic smart contract in Solidity for managing NFT whitelist minting, including free minting for token holders with a limited supply.
Generated: DETERMINISTIC_d123145b8f6845f8
Batch ID: 20250622_210443
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

// Basic NFT Whitelist Minting Contract
contract NFTWhitelistMint is Ownable, ERC721Enumerable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public constant MAX_SUPPLY = 1000; // Maximum supply of NFTs
    uint256 public constant FREE_MINT_LIMIT = 1; // Free mint limit for token holders
    mapping(address => bool) public whitelisted; // Whitelist mapping
    mapping(address => uint256) public freeMints; // Track free mints per address

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("WhitelistNFT", "WNFT") {}

    // Function to add an address to the whitelist
    function addToWhitelist(address _address) external onlyOwner {
        require(!whitelisted[_address], "Address is already whitelisted");
        whitelisted[_address] = true;
    }

    // Function to remove an address from the whitelist
    function removeFromWhitelist(address _address) external onlyOwner {
        require(whitelisted[_address], "Address is not whitelisted");
        whitelisted[_address] = false;
    }

    // Function to mint a new NFT
    function mint() external {
        require(whitelisted[msg.sender], "You are not whitelisted");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        // Check if the sender is eligible for a free mint
        if (freeMints[msg.sender] < FREE_MINT_LIMIT) {
            freeMints[msg.sender]++;
        } else {
            revert("No free mints available for this address");
        }

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        emit Minted(msg.sender, tokenId);
    }

    // Function to get the total supply of minted NFTs
    function totalMinted() external view returns (uint256) {
        return totalSupply();
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address _address) external view returns (bool) {
        return whitelisted[_address];
    }
}
```
