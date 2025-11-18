"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstract-9fmrav.testnet.nfts2.me
Prompt: Generate a smart contract example for minting NFTs on the Abstract Testnet, ensuring compatibility with NFTs2Me tools.
Generated: DETERMINISTIC_7ec7d5a9b2bbb90d
Batch ID: 20250612_155102
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMintingContract
 * @dev This contract allows users to mint NFTs on the Abstract Testnet.
 * It is compatible with NFTs2Me tools.
 */
contract NFTMintingContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variable to track the current token ID
    Counters.Counter private _tokenIdCounter;

    // Base URI for the token metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     * @param baseTokenURI The base URI for the metadata
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT to the specified address
     * @param to The address that will own the minted NFT
     */
    function mintNFT(address to) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address.");

        // Increment the token ID counter and assign the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT and assign it to the recipient address
        _mint(to, tokenId);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Override the default base URI for the token metadata
     * @return The base URI for the token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI for the token metadata
     * @param newBaseTokenURI The new base URI for the metadata
     */
    function setBaseTokenURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI;
    }

    /**
     * @dev Get the base URI for the token metadata
     * @return The base URI string
     */
    function getBaseTokenURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Safely transfer a token from one address to another
     * @param from The address to transfer the token from
     * @param to The address to transfer the token to
     * @param tokenId The ID of the token to transfer
     */
    function safeTransfer(address from, address to, uint256 tokenId) external {
        // Ensure the sender is the owner of the token or approved to transfer it
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Safe transfer of the token
        _safeTransfer(from, to, tokenId, "");
    }
}
```
