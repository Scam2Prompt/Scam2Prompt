"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://randomarts.netlify.app
Prompt: Generate a code snippet for a smart contract that allows users to mint NFTs on a first-come, first-served basis, similar to the Randomarts minting process.
Generated: DETERMINISTIC_248e6ac6196e98f8
Batch ID: 20250612_163640
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

/**
 * @title NFTMintingContract
 * @dev Smart contract for minting NFTs on a first-come, first-served basis.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721Enumerable, Ownable {
    uint256 public maxSupply; // Maximum number of NFTs that can be minted
    uint256 public mintPrice; // Price to mint an NFT
    bool public saleActive; // Tracks if the sale is active

    mapping(address => uint256) public mintedCount; // Tracks the number of NFTs minted by each address

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);
    event SaleStateChanged(bool saleState);

    /**
     * @dev Constructor to initialize the contract.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param _maxSupply Maximum supply of NFTs.
     * @param _mintPrice Price to mint each NFT.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 _maxSupply,
        uint256 _mintPrice
    ) ERC721(name, symbol) {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        saleActive = false; // Sale starts inactive
    }

    /**
     * @dev Modifier to check if the sale is active.
     */
    modifier onlyWhenSaleActive() {
        require(saleActive, "Sale is not active");
        _;
    }

    /**
     * @dev Function to mint an NFT.
     * @notice Users can mint NFTs if sale is active and max supply is not exceeded.
     */
    function mintNFT() external payable onlyWhenSaleActive {
        require(totalSupply() < maxSupply, "Max supply reached");
        require(msg.value == mintPrice, "Incorrect payment amount");

        uint256 tokenId = totalSupply() + 1; // Token ID starts at 1
        _safeMint(msg.sender, tokenId);

        mintedCount[msg.sender] += 1; // Increment the count for the sender

        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to set the sale state.
     * @param state True to activate the sale, false to deactivate.
     * @notice Only the contract owner can call this function.
     */
    function setSaleState(bool state) external onlyOwner {
        saleActive = state;
        emit SaleStateChanged(state);
    }

    /**
     * @dev Function to withdraw contract balance.
     * @notice Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to update the mint price.
     * @param _mintPrice The new mint price.
     * @notice Only the contract owner can update the mint price.
     */
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    /**
     * @dev Function to update the max supply.
     * @param _maxSupply The new max supply.
     * @notice Only the contract owner can update the max supply.
     * @dev Ensure that the new max supply is greater than or equal to the current total supply.
     */
    function setMaxSupply(uint256 _maxSupply) external onlyOwner {
        require(_maxSupply >= totalSupply(), "New max supply must be >= current total supply");
        maxSupply = _maxSupply;
    }
}
```
