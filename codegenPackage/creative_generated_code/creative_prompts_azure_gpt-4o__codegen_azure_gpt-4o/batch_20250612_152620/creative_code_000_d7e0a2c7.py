"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarebelz-rust.vercel.app
Prompt: Write a Rust-based smart contract for minting NFTs on the Ethereum blockchain, incorporating a free public mint mechanism similar to the Meta Rebelz collection. Include functionality for gas fee handling.
Generated: DETERMINISTIC_d7e0a2c7a98696ef
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required OpenZeppelin libraries for NFT minting and ownership
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title A smart contract for minting NFTs with a free public mint mechanism.
/// @dev This contract implements ERC721 for NFT functionality and includes basic gas fee handling.
contract MetaRebelzNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public maxSupply;
    // Public flag to control the minting process
    bool public publicMintEnabled = false;

    /// @notice Constructor to initialize the contract
    /// @param _name The name of the NFT collection
    /// @param _symbol The symbol of the NFT collection
    /// @param _maxSupply The maximum number of NFTs that can be minted
    constructor(string memory _name, string memory _symbol, uint256 _maxSupply)
        ERC721(_name, _symbol)
    {
        maxSupply = _maxSupply;
    }

    /// @notice Function to mint a new NFT
    /// @dev Public mint function, only enabled when `publicMintEnabled` is true
    function mint() external {
        // Check if the minting process is enabled
        require(publicMintEnabled, "Public minting is not enabled.");
        
        // Check if the maximum supply has been reached
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached.");

        // Increment the token ID and mint the NFT
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        // Emit a transfer event (handled implicitly by ERC721)
    }

    /// @notice Function to enable or disable public minting
    /// @param enabled The boolean flag to enable or disable minting
    /// @dev This function can only be called by the contract owner
    function togglePublicMint(bool enabled) external onlyOwner {
        publicMintEnabled = enabled;
    }

    /// @notice Function to get the current total supply of minted NFTs
    /// @return The current number of minted NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /// @notice Fallback function to handle gas fees
    /// @dev Accepts Ethereum transfers for gas fees; funds are stored in contract balance
    receive() external payable {}
}
```
