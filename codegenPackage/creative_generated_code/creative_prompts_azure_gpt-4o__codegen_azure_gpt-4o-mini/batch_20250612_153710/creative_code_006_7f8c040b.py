"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmeme.net
Prompt: Provide a code example in Solidity for creating an NFT contract that could be used for the exclusive TRUMP MEME NFTs mentioned in the roadmap.
Generated: DETERMINISTIC_7f8c040bcd84a4fa
Batch ID: 20250612_153710
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

// Import the OpenZeppelin contracts for ERC721 implementation and Ownable feature
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title TrumpMemesNFT
// @dev This contract implements an ERC721 NFT for exclusive Trump Meme NFTs
contract TrumpMemesNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    string private _baseTokenURI; // Base URI for metadata

    // Event emitted when a new token is minted
    event TokenMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI; // Set the base token URI
    }

    // Function to mint a new NFT
    // @param to The address to receive the minted NFT
    // @return tokenId The ID of the newly minted token
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Cannot mint to the zero address"); // Ensure address is valid
        
        // Increment the token ID counter and assign it to the new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId); // Mint the NFT to the specified address
        emit TokenMinted(to, tokenId); // Emit the TokenMinted event
        
        return tokenId; // Return the minted token ID
    }

    // Function to set the base URI for the NFT metadata
    // @param baseURI The base URI to set
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI; // Update the base token URI
    }

    // Override the baseURI function to return the custom base URI
    // @return The base URI for the NFT metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI; // Return the base token URI
    }

    // Function to get the current token ID counter
    // @return The current token ID
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the current token ID counter
    }
}
```
