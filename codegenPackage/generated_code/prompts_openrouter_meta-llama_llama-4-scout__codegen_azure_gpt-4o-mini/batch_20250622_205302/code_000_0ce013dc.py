"""
Generated Code Metadata:
========================
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a smart contract in Solidity for minting 10,000 unique digital art pieces, with 50% of the proceeds going to a charitable foundation like GiveWell.
Generated: DETERMINISTIC_0ce013dc7b603cff
Batch ID: 20250622_205302
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

/// @title DigitalArtNFT
/// @dev A smart contract for minting unique digital art pieces as NFTs
contract DigitalArtNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Charity address to receive proceeds
    address payable private _charityAddress;

    // Total number of NFTs to mint
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT
    uint256 public constant PRICE_PER_NFT = 0.05 ether;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    /// @dev Constructor to initialize the contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    /// @param baseTokenURI The base URI for the NFT metadata
    /// @param charityAddress The address of the charity to receive proceeds
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        address payable charityAddress
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        _charityAddress = charityAddress;
    }

    /// @dev Mint a new NFT
    /// @param quantity The number of NFTs to mint
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Must mint at least one NFT");
        require(quantity <= MAX_SUPPLY - totalSupply(), "Exceeds max supply");
        require(msg.value == PRICE_PER_NFT * quantity, "Incorrect Ether value");

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            require(tokenId < MAX_SUPPLY, "Max supply reached");

            _mint(msg.sender, tokenId);
            emit Minted(msg.sender, tokenId);
            _tokenIdCounter.increment();
        }

        // Transfer 50% of proceeds to charity
        uint256 charityAmount = msg.value / 2;
        (bool success, ) = _charityAddress.call{value: charityAmount}("");
        require(success, "Transfer to charity failed");
    }

    /// @dev Override baseURI function to return the base URI
    /// @return The base URI for the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Withdraw remaining funds to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @dev Fallback function to receive Ether
    receive() external payable {}
}
```
