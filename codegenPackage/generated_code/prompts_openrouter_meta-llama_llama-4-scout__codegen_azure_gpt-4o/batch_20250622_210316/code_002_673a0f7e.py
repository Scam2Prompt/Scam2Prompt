"""
Generated Code Metadata:
========================
Original URL: https://acidmonkeysdrop.pages.dev
Prompt: Generate a Solidity smart contract code snippet for minting and claiming NFTs from the Acid Monkeys Drop collection of 5,555 exclusive hand-drawn characters.
Generated: DETERMINISTIC_673a0f7e4941f99d
Batch ID: 20250622_210316
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
 * @title AcidMonkeysNFT
 * @dev A smart contract for minting and claiming NFTs from the Acid Monkeys Drop collection.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AcidMonkeysNFT is ERC721Enumerable, Ownable {
    // Maximum supply of Acid Monkeys NFTs
    uint256 public constant MAX_SUPPLY = 5555;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mint price per NFT
    uint256 public mintPrice = 0.05 ether;

    // Tracks the number of NFTs minted
    uint256 public totalMinted;

    // Mapping to track claimed NFTs
    mapping(address => bool) public hasClaimed;

    // Events
    event NFTMinted(address indexed minter, uint256 tokenId);
    event NFTClaimed(address indexed claimer, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param baseURI The base URI for metadata.
     */
    constructor(string memory baseURI) ERC721("Acid Monkeys", "ACID") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Modifier to ensure minting does not exceed the maximum supply.
     */
    modifier canMint(uint256 quantity) {
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        _;
    }

    /**
     * @dev Public function to mint NFTs.
     * @param quantity The number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable canMint(quantity) {
        require(quantity > 0, "Quantity must be greater than zero");
        require(msg.value >= mintPrice * quantity, "Insufficient payment");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalMinted + 1;
            _safeMint(msg.sender, tokenId);
            totalMinted++;
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    /**
     * @dev Public function to claim a free NFT (one per address).
     */
    function claim() external canMint(1) {
        require(!hasClaimed[msg.sender], "Already claimed");
        
        uint256 tokenId = totalMinted + 1;
        _safeMint(msg.sender, tokenId);
        totalMinted++;
        hasClaimed[msg.sender] = true;

        emit NFTClaimed(msg.sender, tokenId);
    }

    /**
     * @dev Owner-only function to set the base URI for metadata.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Owner-only function to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Internal function to return the base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
