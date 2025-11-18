"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Write a smart contract in Solidity for minting unique NFTs, ensuring each token is generated using AI algorithms as described in the Cyber Lama project roadmap.
Generated: DETERMINISTIC_728f2f117a24aab4
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the OpenZeppelin ERC721 implementation and helper libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Cyber Lama NFT Contract
/// @notice This contract facilitates the minting of AI-generated unique NFTs
/// @dev Extends OpenZeppelin's ERC721 and Ownable for secure and efficient implementation
contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track the token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata URIs for each token
    mapping(uint256 => string) private _tokenURIs;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @notice Event emitted when a new NFT is minted
    /// @param tokenId The unique ID of the minted NFT
    /// @param to The address of the NFT recipient
    event NFTMinted(uint256 indexed tokenId, address indexed to);

    /// @dev Constructor initializes the contract with a name and symbol
    /// @param name Name of the NFT collection (e.g., "Cyber Lama")
    /// @param symbol Symbol for the NFT collection (e.g., "CLNFT")
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new NFT with AI-generated metadata
    /// @param to Address of the recipient
    /// @param metadataURI Unique metadata URI for the NFT
    function mint(address to, string memory metadataURI) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Safely mint the new token and assign it to the recipient
        _safeMint(to, tokenId);

        // Set the metadata URI for the newly minted token
        _setTokenURI(tokenId, metadataURI);

        // Emit an event to track the minting
        emit NFTMinted(tokenId, to);
    }

    /// @notice Internal function to set the metadata URI for a token
    /// @param tokenId ID of the token
    /// @param metadataURI Metadata URI to associate with the token
    function _setTokenURI(uint256 tokenId, string memory metadataURI) internal {
        require(_exists(tokenId), "CyberLamaNFT: URI set for nonexistent token");
        _tokenURIs[tokenId] = metadataURI;
    }

    /// @notice Function to get the metadata URI for a specific token
    /// @param tokenId ID of the token
    /// @return string Metadata URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "CyberLamaNFT: Query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /// @notice Function to set the base URI for all tokens
    /// @param baseURI The base URI string
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Function to get the base URI
    /// @return string Base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
