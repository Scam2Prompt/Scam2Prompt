"""
Generated Code Metadata:
========================
Original URL: https://claimpooh.pages.dev
Prompt: Create a POOH-themed NFT collection using a suitable blockchain platform and smart contract.
Generated: DETERMINISTIC_5412284720045805
Batch ID: 20250622_210802
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
 * @title POOH NFT Collection
 * @dev This contract implements an ERC721-based NFT collection themed around POOH.
 * It allows minting unique NFTs with metadata and follows best practices for security and efficiency.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract POOHNFTCollection is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Get the current token ID counter.
     * @return The current token ID.
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Withdraw funds from the contract (if applicable).
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether (if needed for minting fees).
     */
    receive() external payable {}
}
```

### Notes:
- This code uses OpenZeppelin's ERC721 implementation for security and standardization.
- The `mintNFT` function allows the contract owner to mint NFTs with metadata.
- Proper error handling is included for invalid inputs.
- The contract includes a `withdraw` function for the owner to retrieve funds if the contract accepts Ether.
- Ensure you install OpenZeppelin contracts (`npm install @openzeppelin/contracts`) before deploying this code.
