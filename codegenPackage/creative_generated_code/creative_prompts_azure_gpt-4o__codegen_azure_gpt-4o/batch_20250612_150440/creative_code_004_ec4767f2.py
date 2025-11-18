"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledqinlv.com
Prompt: Create a Solidity smart contract template for minting NFTs that can be listed and sold on OpenSea, including metadata customization.
Generated: DETERMINISTIC_ec4767f215630b3f
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Import ERC721 and other required contracts from OpenZeppelin library
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MyNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIds;

    // Base URI for metadata (optional, can be empty or customizable)
    string private _baseTokenURI;

    // Event emitted when an NFT is minted
    event NFTMinted(address recipient, uint256 tokenId, string tokenURI);

    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI; // Initialize the base URI
    }

    /**
     * @dev Function to mint a new NFT.
     * @param recipient Address that will receive the NFT.
     * @param tokenURI URI pointing to the metadata for the NFT.
     * @return tokenId The ID of the minted NFT.
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the new token and set its URI
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId, tokenURI);

        return newTokenId;
    }

    /**
     * @dev Function to set a new base URI for metadata.
     * @param baseTokenURI New base URI for metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the base URI function to include the custom base URI.
     * @return The base URI used for all token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback and receive functions to accept ETH (if NFTs are sold via the contract)
    receive() external payable {}
    fallback() external payable {}
}
```
