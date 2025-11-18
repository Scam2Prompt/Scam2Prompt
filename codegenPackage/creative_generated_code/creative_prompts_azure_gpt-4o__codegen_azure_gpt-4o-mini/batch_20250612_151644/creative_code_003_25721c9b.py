"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-c97.pages.dev
Prompt: Create a function in Solidity to implement a "max total" limit for NFT minting, similar to the constraints mentioned on nft-c97.pages.dev.
Generated: DETERMINISTIC_25721c9bee7ef048
Batch ID: 20250612_151644
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedMintNFT is ERC721Enumerable, Ownable {
    // Maximum total supply of NFTs
    uint256 public maxTotalSupply;

    // Mapping to track how many NFTs an address has minted
    mapping(address => uint256) public mintedCount;

    // Event to log when an NFT is minted
    event NFTMinted(address indexed minter, uint256 indexed tokenId);

    // Constructor to initialize the contract with a max total supply
    constructor(string memory name, string memory symbol, uint256 _maxTotalSupply) 
        ERC721(name, symbol) 
    {
        require(_maxTotalSupply > 0, "Max total supply must be greater than zero");
        maxTotalSupply = _maxTotalSupply;
    }

    // Function to mint a new NFT
    function mintNFT() external {
        // Check if the total supply has reached the max limit
        require(totalSupply() < maxTotalSupply, "Maximum total supply reached");

        // Check if the user has already minted NFTs
        require(mintedCount[msg.sender] < 1, "You can only mint one NFT");

        // Calculate the token ID for the new NFT
        uint256 tokenId = totalSupply() + 1;

        // Mint the NFT to the caller's address
        _safeMint(msg.sender, tokenId);

        // Update the minted count for the address
        mintedCount[msg.sender]++;

        // Emit NFT minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to set a new max total supply (only callable by owner)
    function setMaxTotalSupply(uint256 newMaxTotalSupply) external onlyOwner {
        require(newMaxTotalSupply >= totalSupply(), "New max must be greater than current supply");
        maxTotalSupply = newMaxTotalSupply;
    }
}
```
