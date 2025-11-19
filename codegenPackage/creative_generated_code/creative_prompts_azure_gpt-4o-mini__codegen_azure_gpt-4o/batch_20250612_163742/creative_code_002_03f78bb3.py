"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-astraworld.pages.dev
Prompt: Create a Solidity smart contract that allows users to mint a Black Pass NFT for accessing the Astra Nova ecosystem and earning $RVV tokens.
Generated: DETERMINISTIC_03f78bb3bcf2c13c
Batch ID: 20250612_163742
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

// Import ERC721 and Ownable from OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title BlackPassNFT - A smart contract for minting NFTs for the Astra Nova ecosystem.
/// @author [Your Name]
/// @notice This contract allows users to mint a Black Pass NFT.
/// @dev Inherits ERC721Enumerable for easy enumeration of NFTs.
contract BlackPassNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIds;

    // Mapping to track the address that owns a Black Pass
    mapping(address => bool) private _hasMinted;

    // Metadata base URI
    string private _baseTokenURI;

    // Event to be emitted when a new Black Pass is minted
    event BlackPassMinted(address indexed minter, uint256 tokenId);

    /// @dev Constructor to initialize the contract with token name and symbol.
    /// @param baseURI The base URI for the metadata of tokens.
    constructor(string memory baseURI) ERC721("Black Pass NFT", "BPASS") {
        _baseTokenURI = baseURI;
    }

    /// @notice Mint a new Black Pass NFT.
    /// @dev Each address can only mint one Black Pass NFT. The owner can mint unlimited tokens.
    function mintBlackPass() external {
        require(!_hasMinted[msg.sender], "BlackPassNFT: Address has already minted a Black Pass");

        // Increment token ID
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mark that the user has minted
        _hasMinted[msg.sender] = true;

        // Mint the NFT
        _safeMint(msg.sender, newTokenId);

        // Emit the event
        emit BlackPassMinted(msg.sender, newTokenId);
    }

    /// @notice Get the base URI for metadata.
    /// @dev Overrides the default `_baseURI` function in ERC721.
    /// @return The base URI for all token metadata.
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Set the base URI for metadata.
    /// @dev Only the owner can call this function.
    /// @param baseURI The new base URI for metadata.
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Check if an address has already minted a Black Pass.
    /// @param user The address to check.
    /// @return True if the address has minted, false otherwise.
    function hasMinted(address user) external view returns (bool) {
        return _hasMinted[user];
    }
}
```
