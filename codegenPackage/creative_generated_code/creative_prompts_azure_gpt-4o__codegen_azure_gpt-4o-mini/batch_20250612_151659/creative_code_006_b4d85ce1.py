"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monkeypagelab.com
Prompt: Develop a smart contract that supports the minting of NFTs containing webpage data, compatible with the Monkey Page Lab platform.
Generated: DETERMINISTIC_b4d85ce192cec640
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WebpageDataNFT
 * @dev This contract allows the minting of NFTs that contain webpage data.
 * Compatible with the Monkey Page Lab platform.
 */
contract WebpageDataNFT is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor that sets the name and symbol for the NFT collection.
     */
    constructor() ERC721("WebpageDataNFT", "WDNFT") {
        _tokenIdCounter = 0; // Initialize token ID counter
    }

    /**
     * @dev Function to mint a new NFT with webpage data.
     * @param to The address to receive the minted NFT.
     * @param tokenURI The metadata URI containing the webpage data.
     * Requirements:
     * - `to` cannot be the zero address.
     * - `tokenURI` must not be an empty string.
     */
    function mintNFT(address to, string memory tokenURI) public onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Token URI must not be empty");

        // Increment the token ID counter
        _tokenIdCounter++;

        // Mint the NFT
        _mint(to, _tokenIdCounter);
        // Set the token URI for the newly minted NFT
        _setTokenURI(_tokenIdCounter, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(to, _tokenIdCounter, tokenURI);
    }

    /**
     * @dev Function to retrieve the current token ID counter.
     * @return The current token ID counter.
     */
    function currentTokenId() public view returns (uint256) {
        return _tokenIdCounter;
    }
}
```
