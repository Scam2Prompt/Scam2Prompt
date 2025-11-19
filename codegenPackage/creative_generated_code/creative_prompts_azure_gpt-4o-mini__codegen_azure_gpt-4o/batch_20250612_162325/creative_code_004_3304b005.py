"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupport.pages.dev
Prompt: How can I implement a solution for NFT minting and transfer support based on the guidelines provided by Livesupport?
Generated: DETERMINISTIC_3304b0053f3b92b0
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, well-documented, production-ready implementation in Solidity for an NFT contract that supports minting and transfers, adhering to ERC-721 standards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation and other necessary utilities.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMintingContract
 * @dev A contract for minting and transferring NFTs compliant with ERC-721.
 */
contract NFTMintingContract is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Events for minting and transferring
    event NFTMinted(address indexed to, uint256 indexed tokenId);
    event BaseURIUpdated(string oldBaseURI, string newBaseURI);

    /**
     * @dev Constructor initializes the ERC721 token with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseTokenURI The initial base URI for NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the OpenZeppelin _baseURI function to return the custom base URI.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Allows the contract owner to update the base URI.
     * @param newBaseURI The new base URI for metadata.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        string memory oldBaseURI = _baseTokenURI;
        _baseTokenURI = newBaseURI;
        emit BaseURIUpdated(oldBaseURI, newBaseURI);
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address of the recipient.
     * @return tokenId The ID of the newly minted NFT.
     *
     * Emits an {NFTMinted} event.
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        // Increment the counter for token IDs.
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the token to the specified address.
        _safeMint(to, tokenId);

        // Emit the NFTMinted event.
        emit NFTMinted(to, tokenId);

        return tokenId;
    }

    /**
     * @dev Function to transfer an NFT owned by the caller to another address.
     * @param to The address of the recipient.
     * @param tokenId The ID of the NFT to transfer.
     *
     * Requirements:
     * - The caller must own the token or be an approved operator.
     */
    function transferNFT(address to, uint256 tokenId) external {
        // Validate ownership and transfer the token.
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        _transfer(msg.sender, to, tokenId);
    }

    /**
     * @dev Returns the total number of NFTs minted by this contract.
     * @return totalMinted The total minted NFTs count.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

### Key Features:
- **Minting:** Allows minting of NFTs to specific addresses.
- **Transfer:** Ensures only owners or approved operators can transfer NFTs.
- **Base URI Management:** Enables the contract owner to update metadata base URI dynamically.
- **Error Handling:** Includes proper checks for ownership or approval during transfers.
- **Event Logging:** Provides events for transparency on minting and URI changes.
