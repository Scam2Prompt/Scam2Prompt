"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-9dc.pages.dev
Prompt: Create a step-by-step guide for deploying a Pepe 2.0 NFT smart contract on the Ethereum blockchain, including integration with the minting and token claim features described on the website.
Generated: DETERMINISTIC_284f4bff3d0676e6
Batch ID: 20250612_151605
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

// Import the OpenZeppelin contracts for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Pepe2NFT
 * @dev A smart contract for deploying a Pepe 2.0 NFT collection
 */
contract Pepe2NFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for the token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public maxSupply;

    // Price per NFT mint
    uint256 public mintPrice;

    // Base URI for metadata
    string private baseTokenURI;

    // Constructor to initialize the NFT contract
    constructor(
        string memory name,
        string memory symbol,
        uint256 _maxSupply,
        uint256 _mintPrice,
        string memory _baseTokenURI
    ) ERC721(name, symbol) {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT
     * @param quantity Number of NFTs to mint
     */
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than 0");
        require(
            msg.value == mintPrice * quantity,
            "Incorrect ether value sent"
        );
        require(
            _tokenIdCounter.current() + quantity <= maxSupply,
            "Exceeds max supply"
        );

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Owner-only function to set the base URI for metadata
     * @param _baseTokenURI The new base URI
     */
    function setBaseTokenURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Internal function to return the base URI for metadata
     * @return Base URI as a string
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw all funds from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to claim tokens on behalf of users
     * @param recipient Address to receive the NFT
     */
    function claim(address recipient) external onlyOwner {
        require(
            _tokenIdCounter.current() < maxSupply,
            "Exceeds max supply"
        );
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(recipient, tokenId);
    }
}
```
