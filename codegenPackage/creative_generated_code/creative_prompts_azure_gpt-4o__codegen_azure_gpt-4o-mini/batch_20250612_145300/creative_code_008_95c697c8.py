"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Write code for minting NFTs with a maximum supply limit, similar to the 420 Player Card NFTs mentioned on the $MPEPE website.
Generated: DETERMINISTIC_95c697c8f859b460
Batch ID: 20250612_145300
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title PlayerCardNFT
 * @dev A contract for minting Player Card NFTs with a maximum supply limit.
 */
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public constant MAX_SUPPLY = 420; // Maximum supply limit
    string private _baseTokenURI; // Base URI for metadata

    // Event emitted when a new token is minted
    event TokenMinted(address indexed to, uint256 indexed tokenId);
    
    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI; // Set base URI for metadata
    }

    /**
     * @dev Mint a new NFT for the caller.
     * Requirements:
     * - The total supply must be less than the maximum supply limit.
     */
    function mint() external {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached"); // Check supply limit
        
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the counter for the next token ID
        
        // Mint the NFT and assign it to the caller
        _safeMint(msg.sender, tokenId); 
        
        emit TokenMinted(msg.sender, tokenId); // Emit minting event
    }

    /**
     * @dev Set a new base URI for the token metadata.
     * @param baseTokenURI The new base URI to set.
     * Requirements:
     * - Only the contract owner can call this function.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI; // Update base URI
    }
    
    /**
     * @dev Override the baseURI function from ERC721 to return the custom base URI.
     * @return string The base URI for the token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI; // Return the base URI
    }

    /**
     * @dev Get the total supply of minted NFTs.
     * @return uint256 The total supply count.
     */
    function totalMinted() external view returns (uint256) {
        return totalSupply(); // Return total supply
    }
}
```
