"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.vercel.app
Prompt: Create a smart contract example for minting NFTs that can be sold on the PolyMarket 1.0 marketplace.
Generated: DETERMINISTIC_f7d3e9bc4d8c5c67
Batch ID: 20250612_145821
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

/// @title NFT Minting Contract for PolyMarket 1.0 Compatibility
/// @notice This contract allows the minting of NFTs that can be sold on PolyMarket 1.0 marketplace
/// @dev The contract follows the ERC721 standard and includes minting and marketplace compatibility features.

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PolyMarketNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of the current token ID
    Counters.Counter private _tokenIds;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    /// @notice Constructor to set up the NFT contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /// @notice Mint a new NFT
    /// @param to The address to receive the NFT
    /// @return tokenId The ID of the minted NFT
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Mint to the zero address is not allowed");

        // Increment the token ID counter
        _tokenIds.increment();
        tokenId = _tokenIds.current();

        // Mint the NFT
        _mint(to, tokenId);

        // Emit the minting event
        emit NFTMinted(to, tokenId);
    }

    /// @notice Set the base URI for token metadata
    /// @param baseURI The new base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Get the base URI for token metadata
    /// @return The base URI string
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Override isApprovedForAll to support PolyMarket marketplace
    /// @dev Approves the marketplace's proxy contract for easier trading
    /// @param owner The owner of the NFTs
    /// @param operator The operator to check approval for
    /// @return True if the operator is approved, false otherwise
    function isApprovedForAll(address owner, address operator)
        public
        view
        override
        returns (bool)
    {
        // PolyMarket proxy contract address (example: replace with actual address)
        address polyMarketProxyAddress = 0x1234567890abcdef1234567890abcdef12345678;

        // Automatically approve the PolyMarket proxy contract for trading
        if (operator == polyMarketProxyAddress) {
            return true;
        }

        // Otherwise, use the default implementation
        return super.isApprovedForAll(owner, operator);
    }

    /// @notice Withdraw contract funds (if applicable)
    /// @dev This is optional but useful for any future payable features
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @notice Fallback function to accept ETH if needed
    receive() external payable {}
}
```
