"""
Generated Code Metadata:
========================
Original URL: https://app-kzna.com
Prompt: Generate a Solidity smart contract for creating and distributing Mikazuki and Kakuyūgō NFTs on the Ethereum network, incorporating details about the crescent moon and nuclear fusion symbolism.
Generated: DETERMINISTIC_3f156913a8edd549
Batch ID: 20250622_205842
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
 * @title MikazukiAndKakuyugoNFT
 * @dev A smart contract for creating and distributing Mikazuki (crescent moon) and Kakuyūgō (nuclear fusion) NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MikazukiAndKakuyugoNFT is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId, string tokenType);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a Mikazuki (crescent moon) NFT.
     * @param recipient Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintMikazuki(address recipient, string memory tokenURI) external onlyOwner {
        _mintNFT(recipient, tokenURI, "Mikazuki");
    }

    /**
     * @dev Mint a Kakuyūgō (nuclear fusion) NFT.
     * @param recipient Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintKakuyugo(address recipient, string memory tokenURI) external onlyOwner {
        _mintNFT(recipient, tokenURI, "Kakuyūgō");
    }

    /**
     * @dev Internal function to mint an NFT.
     * @param recipient Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @param tokenType Type of the NFT (e.g., Mikazuki or Kakuyūgō).
     */
    function _mintNFT(address recipient, string memory tokenURI, string memory tokenType) internal {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty.");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(recipient, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(recipient, _currentTokenId, tokenType);
    }

    /**
     * @dev Get the current token ID.
     * @return The current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
