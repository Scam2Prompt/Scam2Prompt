"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-base.com
Prompt: Write a function to mint an onchain digital book, such as "NOBS — Digital Book (Onchain Edition)," using Base ecosystem protocols.
Generated: DETERMINISTIC_29ca2a024e9e5455
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code to mint an on-chain digital book using Base ecosystem protocols. The implementation uses Solidity, assuming the use of ERC721 standards for NFTs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NOBS Digital Book Onchain Edition
/// @author Your Name
/// @notice This contract allows minting of onchain digital books as ERC721 NFTs
/// @dev Uses OpenZeppelin's ERC721 standard for implementation
contract DigitalBookMinting is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    /// @notice Constructor to initialize the contract
    /// @param name Name of the ERC721 token
    /// @param symbol Symbol of the ERC721 token
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new digital book NFT
    /// @dev Mints an ERC721 token and assigns it a metadata URI
    /// @param to Address to receive the minted token
    /// @param tokenURI URI pointing to the metadata of the digital book
    function mintDigitalBook(address to, string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter++;

        // Mint the token to the specified address
        _safeMint(to, _tokenIdCounter);

        // Set the token metadata URI
        _setTokenURI(_tokenIdCounter, tokenURI);

        // Emit event indicating successful minting (optional)
        emit DigitalBookMinted(to, _tokenIdCounter, tokenURI);
    }

    /// @notice Get the current token ID counter
    /// @dev This can be used to track the total number of minted tokens
    /// @return The current token ID counter
    function getTokenIdCounter() external view returns (uint256) {
        return _tokenIdCounter;
    }

    // Event declaration for minting (optional)
    event DigitalBookMinted(address indexed to, uint256 indexed tokenId, string tokenURI);
}
```

### Deployment and Usage Notes:
1. Install OpenZeppelin contracts in your project using: `npm install @openzeppelin/contracts`.
2. Ensure the Base ecosystem is compatible with Ethereum standards to support ERC721 contracts.
3. Deploy the contract, and the `mintDigitalBook` function can be used to mint new digital books on-chain.
