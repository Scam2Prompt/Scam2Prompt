"""
Generated Code Metadata:
========================
Original URL: https://hypurrnft.org
Prompt: Generate a smart contract in Solidity for minting NFTs, specifically for a Genesis Collection, and include terms and conditions handling as outlined on the Hypurr NFT Mint Portal.
Generated: DETERMINISTIC_89b37bd154fa5d47
Batch ID: 20250612_153854
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GenesisNFT
 * @dev A smart contract for minting NFTs as part of a Genesis Collection.
 * This contract allows users to mint NFTs while accepting terms and conditions.
 */
contract GenesisNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to track if a user has accepted terms and conditions
    mapping(address => bool) private _termsAccepted;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Error messages
    error TermsNotAccepted();
    error MintingClosed();

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT. The caller must accept the terms and conditions.
     */
    function mint() external {
        // Check if the user has accepted the terms
        if (!_termsAccepted[msg.sender]) {
            revert TermsNotAccepted();
        }

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Accept the terms and conditions.
     */
    function acceptTerms() external {
        _termsAccepted[msg.sender] = true;
    }

    /**
     * @dev Set the base URI for the NFT metadata.
     * @param baseTokenURI The new base URI.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the baseURI function to return the base URI.
     * @return The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get the acceptance status of terms and conditions for a user.
     * @param user The address of the user.
     * @return True if the user has accepted the terms, false otherwise.
     */
    function hasAcceptedTerms(address user) external view returns (bool) {
        return _termsAccepted[user];
    }

    /**
     * @dev Get the total supply of minted NFTs.
     * @return The total number of minted NFTs.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
