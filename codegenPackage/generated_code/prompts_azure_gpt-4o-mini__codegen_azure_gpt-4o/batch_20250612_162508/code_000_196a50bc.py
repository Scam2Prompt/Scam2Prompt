"""
Generated Code Metadata:
========================
Original URL: https://cyberlamas.pages.dev
Prompt: How can I use AI to generate unique NFTs for the Cyber Lama project, and what are the key features of the smart contracts involved?
Generated: DETERMINISTIC_196a50bc22400e3f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a smart contract for generating unique NFTs for the "Cyber Lama" project using Solidity. The contract includes key features such as minting, metadata storage, and ownership transfer. It assumes the use of the ERC-721 standard.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(string memory baseURI) ERC721("Cyber Lama", "CLAMA") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override the _baseURI function to return the base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * Only the owner of the contract can call this function.
     * @param to Address to receive the minted NFT.
     */
    function mintNFT(address to) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
     * Only the owner of the contract can call this function.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to get the current token ID counter value.
     * Useful for tracking the total number of NFTs minted.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

### Key Features:
1. **ERC-721 Standard**: The contract uses OpenZeppelin's implementation of ERC-721 for NFT functionality.
2. **Minting**: The `mintNFT` function allows the owner to mint unique NFTs.
3. **Metadata**: The `_baseURI` function provides a base URI for metadata storage.
4. **Ownership**: The contract uses OpenZeppelin's `Ownable` module to restrict certain functions to the contract owner.
5. **Event Emission**: The `NFTMinted` event is emitted whenever a new NFT is minted.
6. **Error Handling**: The `onlyOwner` modifier ensures that only the contract owner can perform sensitive operations.

### Deployment:
To deploy this contract, you'll need a Solidity development environment like Remix or Hardhat, and you'll need to provide a base URI for the metadata when initializing the contract.
