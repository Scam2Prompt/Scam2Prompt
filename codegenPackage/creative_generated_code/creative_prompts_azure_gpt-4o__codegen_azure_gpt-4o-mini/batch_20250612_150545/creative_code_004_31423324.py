"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stealt-mint.web.app
Prompt: Create a function to limit NFT minting to three per wallet, as per the restrictions mentioned in the Magic Box stealth mint details.
Generated: DETERMINISTIC_31423324fa945ae8
Batch ID: 20250612_150545
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

// Import necessary OpenZeppelin contracts for safe math and ERC721
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedMintNFT is ERC721, Ownable {
    // Mapping to keep track of how many NFTs each wallet has minted
    mapping(address => uint256) private _mintCount;

    // Total supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;
    // Max NFTs allowed to mint per wallet
    uint256 public constant MAX_PER_WALLET = 3;

    // Event to emit when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    // Counter for tracking the total number of minted NFTs
    uint256 private _tokenIdCounter;

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("LimitedMintNFT", "LMNFT") {
        _tokenIdCounter = 0;
    }

    // Function to mint a new NFT
    function mint() external {
        // Check if the max supply has been reached
        require(_tokenIdCounter < MAX_SUPPLY, "Max supply reached");
        
        // Check if the wallet has already minted the maximum allowed NFTs
        require(_mintCount[msg.sender] < MAX_PER_WALLET, "Wallet has already minted the maximum amount");

        // Increment the token ID counter for the new NFT
        _tokenIdCounter++;

        // Mint the NFT to the sender's address
        _mint(msg.sender, _tokenIdCounter);

        // Increment the mint count for the sender's wallet
        _mintCount[msg.sender]++;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, _tokenIdCounter);
    }

    // Function to get the mint count for a specific wallet
    function getMintCount(address wallet) external view returns (uint256) {
        return _mintCount[wallet];
    }

    // Function to get the total minted NFTs count
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```
