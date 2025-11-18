"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlamas.pages.dev
Prompt: Develop a Solidity smart contract that includes circulation-limiting mechanisms for NFTs, as described in the Cyber Lama NFT collection roadmap.
Generated: DETERMINISTIC_710a16ff142e91e1
Batch ID: 20250612_153648
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

/**
 * @title CyberLamaNFT
 * @dev This contract implements a circulation-limiting mechanism for the Cyber Lama NFT collection.
 */
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;
    
    // Base URI for token metadata
    string private baseTokenURI;
    
    // Mapping to track if the NFT has been minted
    mapping(uint256 => bool) private mintedTokens;

    // Events for logging
    event TokenMinted(address indexed owner, uint256 indexed tokenId);
    event BaseURIUpdated(string newBaseURI);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _baseTokenURI Base URI for token metadata.
     */
    constructor(string memory _name, string memory _symbol, string memory _baseTokenURI) 
        ERC721(_name, _symbol) {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT.
     * @param tokenId The ID of the token to mint.
     */
    function mintToken(uint256 tokenId) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(tokenId > 0 && tokenId <= MAX_SUPPLY, "Token ID invalid");
        require(!mintedTokens[tokenId], "Token already minted");

        // Mark the token as minted
        mintedTokens[tokenId] = true;

        // Mint the token to the owner of this contract
        _safeMint(msg.sender, tokenId);
        emit TokenMinted(msg.sender, tokenId);
    }

    /**
     * @dev Update the base URI for the token metadata.
     * @param newBaseURI The new base URI.
     */
    function updateBaseURI(string memory newBaseURI) external onlyOwner {
        baseTokenURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    /**
     * @dev Override the baseURI function to return the base token URI.
     * @return The base URI for the token metadata.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }
    
    /**
     * @dev Retrieve the token's metadata URI.
     * @param tokenId The ID of the token.
     * @return The metadata URI for the given token ID.
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseURI(), tokenId.toString()));
    }
}
```

Note: This code assumes that you have installed the OpenZeppelin Contracts library for ERC721 and Ownable functionalities. Ensure that `@openzeppelin/contracts` is part of your project dependencies.
