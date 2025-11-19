"""
Generated Code Metadata:
========================
Original URL: https://randomarts.netlify.app
Prompt: Provide a code example for integrating a free minting feature for NFTs, as seen in the Randomarts project.
Generated: DETERMINISTIC_bf36e4b08da7d81c
Batch ID: 20250612_163640
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RandomArtsNFT
 * @dev A contract for free minting NFTs with limited supply
 */
contract RandomArtsNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Token counter
    Counters.Counter private _tokenIdCounter;
    
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 1000;
    
    // Base URI for token metadata
    string private _baseTokenURI;
    
    // Flag to control minting availability
    bool public mintingEnabled = true;
    
    /**
     * @dev Constructor initializes the ERC721 token with name and symbol
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("RandomArts", "RART") {
        _baseTokenURI = baseURI;
    }
    
    /**
     * @dev Public mint function that allows users to mint one NFT for free
     */
    function mint() external {
        require(mintingEnabled, "Minting is currently disabled");
        require(totalSupply() < MAX_SUPPLY, "Maximum supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
    }
    
    /**
     * @dev Returns the total supply minted so far
     * @return uint256 The total number of tokens minted
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
    
    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
    
    /**
     * @dev Toggles the minting status
     */
    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }
    
    /**
     * @dev Overrides the base URI function
     * @return string The base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
    
    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }
}
```
