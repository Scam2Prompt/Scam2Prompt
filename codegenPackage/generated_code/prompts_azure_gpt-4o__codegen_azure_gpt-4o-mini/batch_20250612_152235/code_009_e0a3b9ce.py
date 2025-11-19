"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Create a Solidity contract for issuing NFTs with integrated AI-generated metadata, ensuring each token is unique and collectible, as described in the Cyber Lama project.
Generated: DETERMINISTIC_e0a3b9ce3c202aaf
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for AI-generated metadata service
interface IMetadataGenerator {
    function generateMetadata(uint256 tokenId) external view returns (string memory);
}

// CyberLama NFT contract
contract CyberLama is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to its metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Address of the AI metadata generator contract
    IMetadataGenerator public metadataGenerator;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(address _metadataGeneratorAddress) ERC721("Cyber Lama", "CLAMA") {
        require(_metadataGeneratorAddress != address(0), "Invalid metadata generator address");
        metadataGenerator = IMetadataGenerator(_metadataGeneratorAddress);
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Generate metadata for the new token
        string memory tokenURI = metadataGenerator.generateMetadata(tokenId);
        require(bytes(tokenURI).length > 0, "Generated metadata is empty");

        // Mint the NFT
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    // Function to update the metadata generator address
    function updateMetadataGenerator(address newGenerator) external onlyOwner {
        require(newGenerator != address(0), "Invalid metadata generator address");
        metadataGenerator = IMetadataGenerator(newGenerator);
    }
}
```
