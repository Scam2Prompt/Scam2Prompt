"""
Generated Code Metadata:
========================
Original URL: https://riftproject.pages.dev
Prompt: Design a simple smart contract in Solidity for an NFT minting system that could be used in conjunction with the Rift Swap platform.
Generated: DETERMINISTIC_d0d9a8ed8e1b80ed
Batch ID: 20250622_210348
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RiftSwapNFT
 * @dev A simple NFT minting contract compatible with Rift Swap platform
 * @notice This contract allows minting NFTs with unique token IDs and metadata URIs
 */
contract RiftSwapNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs (0 for unlimited)
    uint256 public maxSupply;

    // Price per NFT mint
    uint256 public mintPrice;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor function
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseTokenURI_ Base URI for token metadata
     * @param maxSupply_ Maximum supply of NFTs (0 for unlimited)
     * @param mintPrice_ Price per NFT mint in wei
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_,
        uint256 maxSupply_,
        uint256 mintPrice_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
        maxSupply = maxSupply_;
        mintPrice = mintPrice_;
    }

    /**
     * @dev Mint a new NFT to the specified address
     * @param to Address to mint the NFT to
     * @notice Requires payment of mintPrice if not zero
     */
    function mint(address to) external payable {
        require(maxSupply == 0 || _tokenIdCounter.current() < maxSupply, "Max supply reached");
        if (mintPrice > 0) {
            require(msg.value >= mintPrice, "Insufficient payment");
        }

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        emit Minted(to, tokenId);
    }

    /**
     * @dev Update the base URI for token metadata
     * @param baseTokenURI_ New base URI
     * @notice Only callable by owner
     */
    function setBaseURI(string memory baseTokenURI_) external onlyOwner {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Update the mint price
     * @param newPrice New mint price in wei
     * @notice Only callable by owner
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Withdraw contract balance
     * @notice Only callable by owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the total number of minted tokens
     * @return Total supply
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
