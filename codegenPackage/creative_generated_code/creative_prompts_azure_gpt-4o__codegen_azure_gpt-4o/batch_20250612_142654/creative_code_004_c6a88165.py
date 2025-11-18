"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://randomarts.netlify.app
Prompt: Create a smart contract template for a free NFT minting event, incorporating unique identifiers for collections such as "Randomrats" and ensuring compatibility with wallet connection features.
Generated: DETERMINISTIC_c6a88165a772ce90
Batch ID: 20250612_142654
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
 * @title RandomRatsNFT
 * @dev A smart contract template for free NFT minting events.
 *      Ensures compatibility with wallet connections and generates unique identifiers for the collection.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RandomRatsNFT is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Event for minting
    event NFTMinted(address indexed minter, uint256 tokenId);

    // Base URI for collection metadata
    string private baseURI;

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol for the NFT collection.
     */
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {}

    /**
     * @dev Function to mint a free NFT during the event.
     *      Each wallet can mint only one NFT.
     */
    function mint() external {
        require(totalSupply() < MAX_SUPPLY, "Minting has ended: Maximum supply reached");
        require(balanceOf(msg.sender) == 0, "Each wallet can mint only one NFT");

        // Generate the next token ID based on total supply
        uint256 tokenId = totalSupply() + 1;

        // Mint the NFT to the sender's wallet
        _safeMint(msg.sender, tokenId);

        // Emit the minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
     *      Can only be called by the contract owner.
     * @param _baseURI The base URI string.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Function to view the base URI for metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
