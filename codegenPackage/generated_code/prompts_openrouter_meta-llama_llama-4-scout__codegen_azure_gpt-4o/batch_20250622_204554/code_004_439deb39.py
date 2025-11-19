"""
Generated Code Metadata:
========================
Original URL: https://nft.stoneinno.com
Prompt: "Create a simple smart contract using Solidity to create and manage NFTs on the Binance Smart Chain."
Generated: DETERMINISTIC_439deb39a6e0d70f
Batch ID: 20250622_204554
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

<<<<<<< HEAD
// Importing OpenZeppelin's ERC721 implementation
=======
// Importing OpenZeppelin's ERC721 implementation for NFTs
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SimpleNFT
<<<<<<< HEAD
 * @dev A simple smart contract to create and manage NFTs on the Binance Smart Chain.
=======
 * @dev A smart contract to create and manage NFTs on the Binance Smart Chain.
 * Inherits from OpenZeppelin's ERC721 and Ownable contracts.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
 */
contract SimpleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
<<<<<<< HEAD
     * @param baseTokenURI Base URI for the metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
=======
     * @param baseURI Base URI for the metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the NFT.
<<<<<<< HEAD
     */
    function mintNFT(address to) external onlyOwner {
=======
     * Emits a Transfer event.
     */
    function mint(address to) external onlyOwner {
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
<<<<<<< HEAD
     * @param baseTokenURI New base URI for metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the baseURI function from ERC721 to return the custom base URI.
=======
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override the _baseURI function from ERC721 to return the custom base URI.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
     * @return Base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to get the current token ID counter value.
<<<<<<< HEAD
     * @return Current token ID counter value.
     */
    function getCurrentTokenId() external view returns (uint256) {
=======
     * @return Current token ID.
     */
    function currentTokenId() external view returns (uint256) {
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        return _tokenIdCounter.current();
    }
}
```

<<<<<<< HEAD
**Note:** This code assumes that the OpenZeppelin library is installed in your project. You can install it using `npm install @openzeppelin/contracts`. Make sure to deploy this contract on the Binance Smart Chain using a compatible wallet and deployment tool.
=======
This code is a simple NFT smart contract that uses OpenZeppelin's libraries for security and standardization. It includes functionality for minting NFTs, setting a base URI for metadata, and querying the current token ID. It is production-ready and adheres to best practices.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
