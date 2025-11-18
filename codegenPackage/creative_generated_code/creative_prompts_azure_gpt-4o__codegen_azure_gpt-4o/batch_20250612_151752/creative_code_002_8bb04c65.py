"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3exodus.click
Prompt: Generate a smart contract using Solidity for managing NFT ownership, inspired by the creative strategies from the Web3Exodus training.
Generated: DETERMINISTIC_8bb04c65fd43b247
Batch ID: 20250612_151752
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
 * @title NFTOwnership
 * @dev A smart contract for managing NFT ownership inspired by Web3Exodus strategies.
 *      This contract uses ERC721 standards for non-fungible token management.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTOwnership is ERC721, Ownable {
    // Counter to track token IDs
    uint256 private _currentTokenId;

    // Mapping to store token URIs
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor initializes the contract with a name and symbol for the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT and assign it to the caller.
     * @param tokenURI A URI pointing to the metadata of the token.
     * Requirements:
     * - The caller must be the contract owner.
     */
    function mintNFT(string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the token to the caller (contract owner)
        _mint(msg.sender, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit an event for the newly minted NFT
        emit NFTMinted(msg.sender, _currentTokenId, tokenURI);
    }

    /**
     * @dev Override built-in ERC721 function to return the token URI.
     * @param tokenId The ID of the token.
     * @return The URI associated with the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Private function to set the token URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI The URI to associate with the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) private {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Function to retrieve the current token ID. 
     * This can be useful for tracking the latest minted token.
     * @return The current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Function to transfer ownership of an NFT.
     * @param from The current owner of the NFT.
     * @param to The new owner of the NFT.
     * @param tokenId The ID of the NFT to transfer.
     * Requirements:
     * - The `from` address must own the token.
     * - The `to` address cannot be the zero address.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(ownerOf(tokenId) == from, "Sender is not the token owner");
        require(to != address(0), "Cannot transfer to the zero address");

        // Perform the safe transfer
        safeTransferFrom(from, to, tokenId);
    }
}
```
