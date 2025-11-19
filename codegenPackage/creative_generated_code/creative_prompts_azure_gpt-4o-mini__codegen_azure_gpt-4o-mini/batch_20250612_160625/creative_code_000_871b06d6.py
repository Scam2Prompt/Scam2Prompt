"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oddfellowsnft.com
Prompt: Generate a smart contract for an NFT collection based on the Secret Society of Odd Fellows concept.
Generated: DETERMINISTIC_871b06d63bff7f75
Batch ID: 20250612_160625
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

// Importing the required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Secret Society of Odd Fellows NFT Collection
/// @notice This contract allows the creation and management of an NFT collection
///         representing the Secret Society of Odd Fellows. Each token is unique and
///         can be owned by different addresses.
contract SecretSocietyOfOddFellows is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to track the next token ID
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    /// @param baseTokenURI Base URI for the NFT metadata
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI; // Set the base URI for metadata
    }

    /// @dev Mint a new NFT for the caller
    /// @notice Only the contract owner can mint new NFTs
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _safeMint(msg.sender, tokenId); // Mint the NFT to the caller
        _tokenIdCounter.increment(); // Increment the token ID counter
        emit NFTMinted(msg.sender, tokenId); // Emit the minting event
    }

    /// @dev Override the baseURI function to return the custom base URI
    /// @return The base URI for the token metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Update the base URI for the NFT metadata
    /// @param newBaseTokenURI The new base URI for the metadata
    /// @notice Only the contract owner can update the base URI
    function setBaseURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI; // Update the base URI
    }

    /// @dev Retrieve the current token ID counter
    /// @return The current token ID count
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the current token ID
    }
}
```
