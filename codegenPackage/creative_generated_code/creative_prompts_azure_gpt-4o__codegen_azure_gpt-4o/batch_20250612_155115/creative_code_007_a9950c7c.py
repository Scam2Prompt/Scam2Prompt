"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artistichive.io
Prompt: Create a tutorial for using Ethereum smart contracts to tokenize digital art and manage ownership verification, referencing the NFT creation process described on ArtisticHive.io.
Generated: DETERMINISTIC_a9950c7c1b060f12
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the clean and production-ready code for creating an Ethereum smart contract for tokenizing digital art and managing ownership verification as an NFT. This leverages the ERC721 standard, which is widely used for NFTs:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC721 library
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DigitalArtToken
 * @dev A smart contract for tokenizing digital art and managing ownership as NFTs (ERC721 standard).
 */
contract DigitalArtToken is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT for digital art.
     * @param recipient The address of the recipient of the NFT.
     * @param tokenURI The metadata URI associated with the digital art (e.g., link to IPFS/ArtisticHive).
     * @return The ID of the newly minted NFT token.
     */
    function mintDigitalArt(address recipient, string memory tokenURI) external onlyOwner returns (uint256) {
        // Increment the token ID counter
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the token and assign ownership to the recipient
        _mint(recipient, newTokenId);

        // Set the metadata URI for the token
        _setTokenURI(newTokenId, tokenURI);

        // Return the newly minted token ID
        return newTokenId;
    }

    /**
     * @dev Internal function to set the metadata URI for a token.
     * @param tokenId The ID of the token to set the URI for.
     * @param tokenURI The metadata URI to associate with the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Public function to retrieve the metadata URI of a token.
     * @param tokenId The ID of the token to query.
     * @return The metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}
```

### Deployment Instructions

Use tools like Remix IDE, Hardhat, or Truffle to deploy this contract. Ensure you have access to a wallet like MetaMask for signing transactions. Install the OpenZeppelin library if deploying via Hardhat or Truffle by running:

```bash
npm install @openzeppelin/contracts
```
