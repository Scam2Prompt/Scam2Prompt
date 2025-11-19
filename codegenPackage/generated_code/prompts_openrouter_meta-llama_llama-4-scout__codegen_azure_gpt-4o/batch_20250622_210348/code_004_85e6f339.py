"""
Generated Code Metadata:
========================
Original URL: https://riftperceptivescaling.pages.dev
Prompt: "Create a basic example of how to mint an NFT using a smart contract on Ethereum, similar to the $RIFT NFT mint feature."
Generated: DETERMINISTIC_85e6f3397c255a37
Batch ID: 20250622_210348
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

/**
 * @title BasicNFT
 * @dev A simple ERC721 contract for minting NFTs
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BasicNFT is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the contract with a name and symbol
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     * @param baseTokenURI Base URI for the metadata
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT
     * @param to Address to receive the minted NFT
     * @return tokenId The ID of the newly minted NFT
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        return _currentTokenId;
    }

    /**
     * @dev Override the base URI function to return the custom base URI
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI
     * @param baseTokenURI New base URI for metadata
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to get the current token ID
     * @return Current token ID
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

### Notes:
- This code uses OpenZeppelin's `ERC721` and `Ownable` contracts for security and standardization.
- The `mintNFT` function allows the contract owner to mint new NFTs.
- The `_baseURI` function is overridden to provide a custom base URI for metadata.
- Proper error handling is included (e.g., checking for invalid addresses).
- The contract is production-ready and follows best practices.
