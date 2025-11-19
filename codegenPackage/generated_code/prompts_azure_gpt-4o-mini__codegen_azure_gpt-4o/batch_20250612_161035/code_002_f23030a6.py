"""
Generated Code Metadata:
========================
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Can you provide a code example for creating an NFT minting function in Truffle based on the "Test ABC" project?
Generated: DETERMINISTIC_f23030a6abac5065
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TestABC is ERC721, Ownable {
    // State variable to keep track of the next token ID
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Base URI for the metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the minted NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Minting to the zero address is not allowed");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the specified address
        _safeMint(to, _currentTokenId);

        // Emit the minting event
        emit NFTMinted(to, _currentTokenId);

        return _currentTokenId;
    }

    /**
     * @dev Override the baseURI function to return the custom base URI.
     * @return Base URI for the metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to retrieve the current token ID.
     * @return Current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

This code is a production-ready implementation of an NFT minting function using the Truffle framework and OpenZeppelin's ERC721 standard. It includes proper error handling, comments, and follows best practices.
