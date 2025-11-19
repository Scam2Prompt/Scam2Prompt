"""
Generated Code Metadata:
========================
Original URL: https://randomarts.netlify.app
Prompt: Generate a code snippet for a smart contract that allows users to mint NFTs on a first-come, first-served basis, similar to the Randomarts minting process.
Generated: DETERMINISTIC_248e6ac6196e98f8
Batch ID: 20250612_163640
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
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs on a first-come, first-served basis.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public maxSupply;

    // Price per NFT in wei
    uint256 public mintPrice;

    // Base URI for metadata
    string private baseTokenURI;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     * @param _mintPrice Price per NFT in wei.
     * @param _baseTokenURI Base URI for metadata.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _maxSupply,
        uint256 _mintPrice,
        string memory _baseTokenURI
    ) ERC721(_name, _symbol) {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Function to mint an NFT.
     * Requirements:
     * - The caller must send enough Ether to cover the mint price.
     * - The total supply must not exceed the maximum supply.
     */
    function mintNFT() external payable {
        // Ensure the mint price is met
        require(msg.value >= mintPrice, "Insufficient Ether sent");

        // Ensure the maximum supply is not exceeded
        require(totalSupply() < maxSupply, "Max supply reached");

        // Mint the NFT
        uint256 tokenId = totalSupply() + 1; // Token IDs start at 1
        _safeMint(msg.sender, tokenId);

        // Emit the minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
     * Only the contract owner can call this function.
     * @param _baseTokenURI New base URI for metadata.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override the _baseURI function from ERC721 to return the base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
