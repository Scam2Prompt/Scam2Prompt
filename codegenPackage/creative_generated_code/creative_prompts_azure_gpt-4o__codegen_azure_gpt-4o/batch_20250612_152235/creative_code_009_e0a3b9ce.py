"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Create a Solidity contract for issuing NFTs with integrated AI-generated metadata, ensuring each token is unique and collectible, as described in the Cyber Lama project.
Generated: DETERMINISTIC_e0a3b9ce3c202aaf
Batch ID: 20250612_152235
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

/**
 * @title CyberLamaNFT
 * @dev A smart contract for issuing NFTs with AI-generated metadata.
 * Each token is unique and collectible, following ERC721 standard.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CyberLamaNFT is ERC721URIStorage, Ownable {
    uint256 private _currentTokenId; // Counter for token IDs
    string private _baseMetadataURI; // Base URI for AI-generated metadata

    event NFTMinted(uint256 tokenId, address recipient, string tokenURI);

    constructor(string memory name, string memory symbol, string memory baseMetadataURI) ERC721(name, symbol) {
        _baseMetadataURI = baseMetadataURI;
    }

    /**
     * @dev Set the base URI for AI-generated metadata.
     * @param baseMetadataURI The new base URI to be set.
     */
    function setBaseMetadataURI(string memory baseMetadataURI) external onlyOwner {
        _baseMetadataURI = baseMetadataURI;
    }

    /**
     * @dev Mint a new NFT with AI-generated metadata.
     * @param recipient The address that will receive the NFT.
     */
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");

        _currentTokenId += 1; // Increment token ID
        uint256 newTokenId = _currentTokenId;

        // Generate token URI using base URI and the unique token ID
        string memory tokenURI = string(abi.encodePacked(_baseMetadataURI, "/", uint2str(newTokenId)));

        _mint(recipient, newTokenId); // Mint the token
        _setTokenURI(newTokenId, tokenURI); // Set token metadata

        emit NFTMinted(newTokenId, recipient, tokenURI); // Emit event
    }

    /**
     * @dev Utility function to convert a uint256 to a string.
     * @param value The uint256 value to convert.
     * @return The string representation of the uint256 value.
     */
    function uint2str(uint256 value) internal pure returns (string memory) {
        if (value == 0) {
            return "0";
        }
        uint256 tempValue = value;
        uint256 digits;
        while (tempValue != 0) {
            digits++;
            tempValue /= 10;
        }
        bytes memory buffer = new bytes(digits);
        uint256 index = digits - 1;
        tempValue = value;
        while (tempValue != 0) {
            buffer[index--] = bytes1(uint8(48 + tempValue % 10));
            tempValue /= 10;
        }
        return string(buffer);
    }

    /**
     * @dev Retrieve the base URI for metadata.
     * @return The current base URI.
     */
    function baseMetadataURI() external view returns (string memory) {
        return _baseMetadataURI;
    }

    /**
     * @dev Get the current token ID count.
     * @return The latest token ID minted.
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
