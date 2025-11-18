"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.misphits-mint.xyz
Prompt: Write a smart contract in Solidity to handle NFT minting and wallet connection for a project similar to Misphits.
Generated: DETERMINISTIC_3471b34d8b02557c
Batch ID: 20250612_151611
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

// Importing OpenZeppelin's ERC721 and Ownable contracts for NFT functionality and access control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MisphitsNFT
 * @dev A contract for minting NFTs similar to Misphits, allowing users to connect their wallets and mint tokens.
 */
contract MisphitsNFT is ERC721Enumerable, Ownable {
    // Base URI for token metadata
    string private _baseTokenURI;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to set the initial values for the contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseURI The base URI for token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
        _tokenIdCounter = 0;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param recipient The address that will receive the minted NFT.
     */
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid address: recipient is the zero address");

        // Increment token ID counter
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the new NFT
        _mint(recipient, newTokenId);

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId);
    }

    /**
     * @dev Function to get the base URI for metadata.
     * @return The base URI for token metadata.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to set a new base URI for metadata.
     * @param baseURI The new base URI for token metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to get the total number of minted NFTs.
     * @return The total number of minted NFTs.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter;
    }

    /**
     * @dev Function to retrieve the token ID of the NFT owned by an address at a specific index.
     * @param owner The address of the NFT owner.
     * @param index The index of the NFT owned by the owner.
     * @return The token ID at the specified index.
     */
    function tokenOfOwnerByIndex(address owner, uint256 index) external view returns (uint256) {
        return super.tokenOfOwnerByIndex(owner, index);
    }
}
```
