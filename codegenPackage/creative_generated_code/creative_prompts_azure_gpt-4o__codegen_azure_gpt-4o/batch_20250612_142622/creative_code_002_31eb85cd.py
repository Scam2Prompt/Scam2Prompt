"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Create an Ethereum smart contract that enforces CC0 licensing for an NFT collection, as described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_31eb85cd2c79b806
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.17;

/**
 * @title CC0NFTCollection
 * @dev An Ethereum smart contract for creating an NFT collection that enforces CC0 licensing.
 * CC0 (Creative Commons Zero) ensures that the content is dedicated to the public domain.
 * This contract strictly adheres to CC0 principles.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CC0NFTCollection is ERC721Enumerable, Ownable {
    // Metadata base URI
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Price per NFT
    uint256 public mintPrice;

    // NFT minting pause status
    bool public paused = false;

    // Event emitted on minting
    event NFTMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Base URI for the metadata.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     * @param _mintPrice Price per NFT in wei.
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _maxSupply,
        uint256 _mintPrice
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
    }

    /**
     * @dev Modifier to check if minting is paused.
     */
    modifier notPaused() {
        require(!paused, "Minting is paused");
        _;
    }

    /**
     * @dev Public mint function allowing users to mint NFTs.
     * Requires payment of `mintPrice` and ensures the total supply does not exceed `maxSupply`.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable notPaused {
        require(quantity > 0, "Quantity must be greater than 0");
        require(totalSupply() + quantity <= maxSupply, "Exceeds maximum supply");
        require(msg.value >= mintPrice * quantity, "Insufficient ETH for minting");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    /**
     * @dev Owner-only function to set the base URI for metadata.
     * @param baseTokenURI New base URI.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Owner-only function to update the minting price.
     * @param _mintPrice New mint price in wei.
     */
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    /**
     * @dev Owner-only function to pause or unpause minting.
     * @param state New pause state (true to pause, false to unpause).
     */
    function setPaused(bool state) external onlyOwner {
        paused = state;
    }

    /**
     * @dev Override for the base URI function used by ERC721.
     * @return The base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Withdraw function for the contract owner to collect funds from minting.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
