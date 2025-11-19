"""
Generated Code Metadata:
========================
Original URL: https://degen-4g1.pages.dev
Prompt: "Create a smart contract on Polygon for a limited edition NFT series, inspired by Highlight's open edition collections like ProFlies Pictures (xBAA) v2."
Generated: DETERMINISTIC_605580c346c1e048
Batch ID: 20250622_210803
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
 * @title LimitedEditionNFT
 * @dev A smart contract for creating a limited edition NFT series on Polygon.
 * Inspired by Highlight's open edition collections.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedEditionNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs in the collection
    uint256 public maxSupply;

    // Base URI for metadata
    string private baseTokenURI;

    // Price per NFT
    uint256 public mintPrice;

    // Tracks the number of NFTs minted
    uint256 public totalMinted;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _maxSupply Maximum number of NFTs in the collection.
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
        require(_maxSupply > 0, "Max supply must be greater than zero");
        require(_mintPrice > 0, "Mint price must be greater than zero");

        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Public function to mint an NFT.
     * Requires payment of the mint price and checks for max supply.
     */
    function mint() external payable {
        require(totalMinted < maxSupply, "Max supply reached");
        require(msg.value == mintPrice, "Incorrect payment amount");

        uint256 tokenId = totalMinted + 1;
        totalMinted++;

        _safeMint(msg.sender, tokenId);

        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Owner-only function to set the base URI for metadata.
     * @param _baseTokenURI New base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override function to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Owner-only function to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
