"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Generate a smart contract for an NFT collection that allows minting with a supply limit of 10,000 and a maximum of 10 NFTs per transaction, ensuring no royalties are collected.
Generated: DETERMINISTIC_cb73ac6e1aac6fde
Batch ID: 20250612_155701
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTCollection
 * @dev A smart contract for an NFT collection with a supply limit and minting restrictions.
 */
contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the total supply of NFTs minted
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Maximum NFTs that can be minted in a single transaction
    uint256 public constant MAX_PER_TRANSACTION = 10;

    // Mapping to track if an address has minted an NFT
    mapping(address => bool) public hasMinted;

    // Event emitted when NFTs are minted
    event Minted(address indexed to, uint256 quantity);

    /**
     * @dev Constructor to initialize the NFT collection with a name and symbol.
     */
    constructor() ERC721("MyNFTCollection", "MNFT") {}

    /**
     * @dev Function to mint new NFTs.
     * @param quantity The number of NFTs to mint.
     */
    function mint(uint256 quantity) external {
        // Check if the quantity is within the allowed limit
        require(quantity > 0 && quantity <= MAX_PER_TRANSACTION, "Invalid quantity");
        
        // Check if the total supply will exceed the maximum supply
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            _mintNFT(msg.sender);
        }

        emit Minted(msg.sender, quantity);
    }

    /**
     * @dev Internal function to mint a single NFT.
     * @param to The address to receive the minted NFT.
     */
    function _mintNFT(address to) internal {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);
    }

    /**
     * @dev Override the supportsInterface function to ensure compatibility with ERC721.
     * @param interfaceId The interface identifier.
     * @return True if the contract supports the interface, false otherwise.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC165) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    /**
     * @dev Function to withdraw any Ether sent to the contract (if applicable).
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
