"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Can you provide a code example for creating an NFT minting function in Truffle based on the "Test ABC" project?
Generated: DETERMINISTIC_f23030a6abac5065
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title TestABC NFT Contract
// @notice This contract enables the minting of NFTs for the Test ABC project
contract TestABCNFT is ERC721, Ownable {
    using Counters for Counters.Counter; // Using Counters library for token ID management

    Counters.Counter private _tokenIdCounter; // Counter for tracking token IDs

    // @dev Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // @dev Event emitted when a new NFT is minted
    event NFTMinted(address recipient, uint256 tokenId, string tokenURI);

    // @param name The name of the NFT collection
    // @param symbol The symbol for the NFT collection
    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) 
    {}

    // @notice Mints a new NFT to the specified recipient with a given tokenURI
    // @param recipient The address to receive the minted NFT
    // @param tokenURI The metadata URI associated with the NFT
    // @dev Only callable by the contract owner
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Invalid address: recipient cannot be zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: must not be empty");

        // Incrementing the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Minting the NFT
        _mint(recipient, tokenId);

        // Setting the token URI
        _setTokenURI(tokenId, tokenURI);

        // Emitting the NFTMinted event
        emit NFTMinted(recipient, tokenId, tokenURI);
    }

    // @notice Internal function to set the token URI
    // @param tokenId The ID of the token
    // @param tokenURI The metadata URI to set
    // @dev This function overrides the default _setTokenURI function
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI; // Storing the token URI
    }

    // @notice Retrieves the token URI for a given token ID
    // @param tokenId The ID of the token being queried
    // @return The metadata URI associated with the token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _tokenURIs[tokenId]; // Returning the stored token URI
    }
}
```
