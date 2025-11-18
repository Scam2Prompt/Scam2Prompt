"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oddfellowsnft.com
Prompt: Create a smart contract in Solidity for an NFT project named "Secret Society of Odd Fellows (SSOF)" that includes unique token metadata and supports JavaScript-based integration.
Generated: DETERMINISTIC_46897f95c95de8fd
Batch ID: 20250612_154653
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
 * @title Secret Society of Odd Fellows (SSOF) NFT Contract
 * @dev ERC721 implementation for minting unique NFTs with metadata
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SSOFNFT is ERC721URIStorage, Ownable {
    uint256 private _currentTokenId; // Counter for token IDs
    string public baseURI; // Base URI for metadata

    event TokenMinted(address indexed mintedTo, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor sets the name and symbol of the NFT collection and initializes a base URI
     * @param name Name of the NFT collection (e.g., "Secret Society of Odd Fellows")
     * @param symbol Symbol for the NFT collection (e.g., "SSOF")
     * @param _baseURI Initial base URI for the metadata
     */
    constructor(string memory name, string memory symbol, string memory _baseURI) ERC721(name, symbol) {
        baseURI = _baseURI;
    }

    /**
     * @dev Internal function to concatenate the base URI and token-specific metadata URI
     * @param _tokenURI Token-specific metadata URI
     */
    function _fullTokenURI(string memory _tokenURI) internal view returns (string memory) {
        return string(abi.encodePacked(baseURI, _tokenURI));
    }

    /**
     * @dev Function to mint a new NFT with metadata
     * @param recipient Address that will receive the newly minted NFT
     * @param tokenURI Metadata URI for the token (should be unique for each token)
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        _currentTokenId++; // Increment the token ID
        uint256 newTokenId = _currentTokenId;

        _safeMint(recipient, newTokenId); // Mint the token
        _setTokenURI(newTokenId, _fullTokenURI(tokenURI)); // Set the metadata URI

        emit TokenMinted(recipient, newTokenId, _fullTokenURI(tokenURI));
    }

    /**
     * @dev Function to update the base URI
     * @param _baseURI New base URI for metadata
     */
    function updateBaseURI(string memory _baseURI) external onlyOwner {
        require(bytes(_baseURI).length > 0, "Base URI cannot be empty");
        baseURI = _baseURI;
    }

    /**
     * @dev Function to retrieve the current token ID counter
     * @return Current token ID
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Function to check if a token exists
     * @param tokenId ID of the token to check
     * @return Boolean indicating whether the token exists
     */
    function tokenExists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}
```
