"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Provide example code for integrating decentralized art projects into a blockchain platform, inspired by the artistic experiences highlighted at ETHBerlin04.
Generated: DETERMINISTIC_6a5cffce9aa88aa8
Batch ID: 20250612_150554
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

/**
 * @title DecentralizedArtNFT
 * @dev A smart contract for minting and managing decentralized art as NFTs.
 */
contract DecentralizedArtNFT is ERC721, Ownable {
    // Event emitted when a new art piece is minted
    event ArtMinted(uint256 indexed tokenId, string tokenURI, address owner);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping from token ID to art metadata (token URI)
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor for the contract setting the name and symbol for the NFT collection.
     */
    constructor() ERC721("DecentralizedArtNFT", "DART") {
        _tokenIdCounter = 0;
    }

    /**
     * @dev Mint a new art NFT.
     * @param tokenURI The metadata URI for the art piece.
     */
    function mintArt(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment token ID counter and assign it to a new token
        uint256 tokenId = _tokenIdCounter;
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit ArtMinted(tokenId, tokenURI, msg.sender);

        // Increment the token ID counter for the next mint
        _tokenIdCounter += 1;
    }

    /**
     * @dev Set the token URI for a token.
     * @param tokenId The ID of the token.
     * @param tokenURI The metadata URI for the art piece.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI; // Store the token URI
    }

    /**
     * @dev Retrieve the token URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Get the current token ID counter.
     * @return The current token ID counter.
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```

### Note:
This Solidity smart contract implements a basic NFT minting functionality for decentralized art projects. It uses the OpenZeppelin library to ensure common practices for security and functionality. This code should be thoroughly tested in a development environment before deploying to any live blockchain.
