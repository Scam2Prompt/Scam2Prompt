"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Write a Solidity function that triggers an NFT reveal process after a sellout, mimicking the reveal mechanism described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_f985c60b4769487f
Batch ID: 20250612_142622
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

contract NFTReveal is ERC721Enumerable, Ownable {
    // State variables
    string private baseURI;
    string private unrevealedURI;
    uint256 public totalSupply;
    uint256 public maxSupply;
    bool public revealed = false;

    // Events
    event RevealTriggered(uint256 totalSupply, string baseURI);

    // Constructor to initialize the NFT collection
    constructor(string memory name, string memory symbol, string memory _unrevealedURI, uint256 _maxSupply) 
        ERC721(name, symbol) {
        unrevealedURI = _unrevealedURI;
        maxSupply = _maxSupply;
    }

    // Function to mint new NFTs
    function mintNFT(address to) external onlyOwner {
        require(totalSupply < maxSupply, "All NFTs have been minted");
        totalSupply++;
        _mint(to, totalSupply);
    }

    // Function to trigger the reveal process
    function triggerReveal(string memory _baseURI) external onlyOwner {
        require(!revealed, "Already revealed");
        
        // Update the base URI
        baseURI = _baseURI;
        revealed = true;

        emit RevealTriggered(totalSupply, baseURI);
    }

    // Function to set the base URI for the revealed NFTs
    function _baseURI() internal view virtual override returns (string memory) {
        return revealed ? baseURI : unrevealedURI;
    }

    // Function to get the URI of a specific token
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI(), "/", tokenId.toString()));
    }
}
```

### Notes:
- This code implements an NFT minting and revealing mechanism, following best practices.
- The `_baseURI` function provides the correct base URI based on the reveal state.
- Proper error handling is included to ensure that actions are only performed when conditions are met.
