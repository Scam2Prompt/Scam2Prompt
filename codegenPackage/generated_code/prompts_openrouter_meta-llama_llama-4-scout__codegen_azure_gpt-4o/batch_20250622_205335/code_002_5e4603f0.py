"""
Generated Code Metadata:
========================
Original URL: https://cknft.pages.dev
Prompt: Generate a smart contract in Solidity for an NFT project that grants exclusive access to events and merchandise for holders, similar to the Blvck Alpha Membership benefits.
Generated: DETERMINISTIC_5e4603f0db48436e
Batch ID: 20250622_205335
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
 * @title ExclusiveAccessNFT
 * @dev A smart contract for an NFT project that grants exclusive access to events and merchandise for holders.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ExclusiveAccessNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT
    uint256 public constant PRICE = 0.05 ether;

    // Mapping to track event access for NFT holders
    mapping(uint256 => bool) public eventAccess;

    // Mapping to track merchandise access for NFT holders
    mapping(uint256 => bool) public merchandiseAccess;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);
    event EventAccessGranted(uint256 indexed tokenId);
    event MerchandiseAccessGranted(uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Base URI for metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value >= PRICE * quantity, "Insufficient payment");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    /**
     * @dev Function to grant event access to an NFT holder.
     * @param tokenId ID of the NFT.
     */
    function grantEventAccess(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        eventAccess[tokenId] = true;
        emit EventAccessGranted(tokenId);
    }

    /**
     * @dev Function to grant merchandise access to an NFT holder.
     * @param tokenId ID of the NFT.
     */
    function grantMerchandiseAccess(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        merchandiseAccess[tokenId] = true;
        emit MerchandiseAccessGranted(tokenId);
    }

    /**
     * @dev Function to check if an NFT holder has event access.
     * @param tokenId ID of the NFT.
     * @return True if the holder has event access, false otherwise.
     */
    function hasEventAccess(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return eventAccess[tokenId];
    }

    /**
     * @dev Function to check if an NFT holder has merchandise access.
     * @param tokenId ID of the NFT.
     * @return True if the holder has merchandise access, false otherwise.
     */
    function hasMerchandiseAccess(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return merchandiseAccess[tokenId];
    }

    /**
     * @dev Function to set the base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override function to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
