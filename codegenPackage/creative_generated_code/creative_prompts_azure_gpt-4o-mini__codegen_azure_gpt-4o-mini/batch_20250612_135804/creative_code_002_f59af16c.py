"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfarcade.vercel.app
Prompt: Write a code snippet for a smart contract that manages the minting of Arcade Passes for a gaming platform.
Generated: DETERMINISTIC_f59af16c89604893
Batch ID: 20250612_135804
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

// @title ArcadePass 
// @dev A smart contract for managing the minting of Arcade Passes on a gaming platform
contract ArcadePass is ERC721Enumerable, Ownable {
    // Base URI for the metadata
    string private _baseTokenURI;

    // Mapping from token ID to whether it is minted
    mapping(uint256 => bool) private _minted;

    // Event emitted when a new Arcade Pass is minted
    event ArcadePassMinted(uint256 indexed tokenId, address indexed owner);

    // Constructor to initialize the token name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // @dev Function to mint a new Arcade Pass
    // @param tokenId The ID of the Arcade Pass to mint
    function mintArcadePass(uint256 tokenId) external onlyOwner {
        require(!_minted[tokenId], "ArcadePass: Token ID already minted");

        // Mint the token to the caller
        _safeMint(msg.sender, tokenId);
        _minted[tokenId] = true; // Mark this token ID as minted

        emit ArcadePassMinted(tokenId, msg.sender);
    }

    // @dev Function to set a new base URI
    // @param baseTokenURI The new base URI for metadata
    function setBaseURI(string calldata baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // @dev Override the _baseURI function to return the base URI for the token metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // @dev Function to withdraw any ether from the contract (if necessary)
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
