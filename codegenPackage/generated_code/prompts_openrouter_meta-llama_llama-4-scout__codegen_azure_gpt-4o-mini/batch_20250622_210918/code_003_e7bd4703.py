"""
Generated Code Metadata:
========================
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Design a simple smart contract in Solidity that enables the minting of NFTs with unique Japanese designs, reflecting the spirit of "和(Wa: Harmony)".
Generated: DETERMINISTIC_e7bd47036b4fb80c
Batch ID: 20250622_210918
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting NFTs with unique Japanese designs
contract WaHarmonyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string design);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(string memory design) external onlyOwner {
        require(bytes(design).length > 0, "Design cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, design);
    }

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base token URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the total supply of NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
