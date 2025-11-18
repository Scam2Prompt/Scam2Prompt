"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfarcade.vercel.app
Prompt: Develop a smart contract in Solidity that mimics the functionality of minting an Arcade Pass, inspired by the https://nfarcade.vercel.app site.
Generated: DETERMINISTIC_c59b2ec101740e37
Batch ID: 20250612_145218
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ArcadePass
 * @dev A smart contract that allows users to mint an Arcade Pass as an ERC721 token.
 */
contract ArcadePass is ERC721, Ownable {
    using Counters for Counters.Counter; // Using Counters for managing token IDs

    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    string private _baseTokenURI; // Base URI for the token metadata

    // Event emitted when a new Arcade Pass is minted
    event ArcadePassMinted(address indexed recipient, uint256 tokenId);

    /**
     * @dev Sets the name and symbol for the Arcade Pass NFT
     * @param name Name of the token
     * @param symbol Symbol of the token
     * @param baseTokenURI Base URI for token metadata
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Allows the owner to mint a new Arcade Pass to a specified address.
     * @param recipient The address to receive the minted Arcade Pass
     */
    function mintArcadePass(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address"); // Ensure recipient is not zero address
        
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _safeMint(recipient, tokenId); // Mint the token safely
        
        emit ArcadePassMinted(recipient, tokenId); // Emit the mint event
        _tokenIdCounter.increment(); // Increment the token ID counter
    }

    /**
     * @dev Override the baseURI function to return the base token URI.
     * @return The base URI for the token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI; // Return the base URI
    }

    /**
     * @dev Allows the contract owner to update the base URI for the token metadata.
     * @param newBaseTokenURI The new base URI for token metadata
     */
    function setBaseTokenURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI; // Update the base URI
    }

    /**
     * @dev Returns the total number of minted Arcade Passes.
     * @return The total number of minted tokens
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the current count of minted tokens
    }
}
```
