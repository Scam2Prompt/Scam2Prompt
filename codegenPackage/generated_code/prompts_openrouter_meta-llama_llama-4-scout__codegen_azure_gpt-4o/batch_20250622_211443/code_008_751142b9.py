"""
Generated Code Metadata:
========================
Original URL: https://dappblocksolution.web.app
Prompt: Develop an NFT solution to assist in the creation, management, and troubleshooting of NFTs, ensuring a smooth experience in the NFT marketplace.
Generated: DETERMINISTIC_751142b9c2c85592
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of an NFT solution using the Solidity programming language for Ethereum smart contracts. This code includes creation, management, and basic troubleshooting of NFTs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTMarketplace
 * @dev A smart contract for creating, managing, and troubleshooting NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata for each token
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract.
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
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the NFT
        _safeMint(to, newTokenId);

        // Set the token URI
        _setTokenURI(newTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(to, newTokenId, tokenURI);
    }

    /**
     * @dev Get the metadata URI of a specific token.
     * @param tokenId ID of the token.
     * @return Metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Internal function to set the metadata URI for a token.
     * @param tokenId ID of the token.
     * @param tokenURI URI pointing to the metadata of the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Transfer an NFT from one address to another.
     * @param from Address of the current owner.
     * @param to Address of the recipient.
     * @param tokenId ID of the token to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Invalid recipient address");

        // Transfer the token
        _transfer(from, to, tokenId);

        // Emit the transfer event
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Burn an NFT.
     * @param tokenId ID of the token to burn.
     */
    function burnNFT(uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Clear the token URI
        delete _tokenURIs[tokenId];

        // Burn the token
        _burn(tokenId);
    }

    /**
     * @dev Get the total number of NFTs minted.
     * @return Total number of NFTs minted.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

### Key Features:
1. **Minting**: Allows the owner to mint new NFTs with metadata.
2. **Metadata Management**: Stores and retrieves metadata URIs for each token.
3. **Transfer**: Enables safe transfer of NFTs between addresses.
4. **Burning**: Allows approved users to burn NFTs.
5. **Error Handling**: Includes checks for invalid addresses, empty metadata, and token existence.

This code uses OpenZeppelin's libraries for security and best practices. Make sure to install OpenZeppelin contracts via npm (`npm install @openzeppelin/contracts`) before deploying this smart contract.
