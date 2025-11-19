"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Write a smart contract on the Binance Smart Chain for minting NFTs that represent cryptographically protected Private Label Rights (PLR) licenses, using the ERC20 token standard for integration with $PLRT.
Generated: DETERMINISTIC_f9b2f2ac026d6016
Batch ID: 20250612_154520
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for minting NFTs representing PLR licenses
contract PLRNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to PLR license details
    mapping(uint256 => string) private _plrLicenses;

    // Event emitted when a new NFT is minted
    event PLRNFTMinted(address indexed owner, uint256 indexed tokenId, string plrLicense);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor() ERC721("PLR License NFT", "PLRNFT") {}

    // Function to mint a new NFT with a PLR license
    // Only the contract owner can mint new NFTs
    function mintPLRNFT(string memory plrLicense) external onlyOwner {
        require(bytes(plrLicense).length > 0, "PLR license cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the owner of the contract
        _mint(msg.sender, tokenId);

        // Store the PLR license details
        _plrLicenses[tokenId] = plrLicense;

        // Emit the minting event
        emit PLRNFTMinted(msg.sender, tokenId, plrLicense);
    }

    // Function to retrieve the PLR license associated with a token ID
    function getPLRLicense(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token ID does not exist");
        return _plrLicenses[tokenId];
    }

    // Function to check if a token ID exists
    function _exists(uint256 tokenId) internal view override returns (bool) {
        return super._exists(tokenId);
    }
}
```
