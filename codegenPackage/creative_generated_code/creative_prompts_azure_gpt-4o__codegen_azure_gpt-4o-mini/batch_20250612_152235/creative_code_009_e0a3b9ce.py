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

// Import OpenZeppelin's ERC721 contract for NFT implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CyberLamaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the NFT collection with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with AI-generated metadata.
     * @param recipient The address that will receive the minted NFT.
     * @param metadataURI The URI containing the AI-generated metadata for the NFT.
     */
    function mintNFT(address recipient, string memory metadataURI) external onlyOwner {
        require(recipient != address(0), "Cannot mint to the zero address");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment the token ID counter and assign it to a new token
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the token to the recipient
        _mint(recipient, newTokenId);
        
        // Set the metadata URI for the new token
        _setTokenURI(newTokenId, metadataURI);

        // Emit event for the minted token
        emit TokenMinted(newTokenId, metadataURI);
    }

    /**
     * @dev Set the metadata URI for a specific token.
     * @param tokenId The ID of the token for which to set the URI.
     * @param uri The URI to associate with the token.
     */
    function _setTokenURI(uint256 tokenId, string memory uri) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @dev Retrieve the metadata URI for a specific token.
     * @param tokenId The ID of the token whose URI to retrieve.
     * @return The metadata URI associated with the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive ether. 
     * Not used for this contract but enables receiving funds.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle calls to non-existent functions.
     */
    fallback() external payable {}
}
```
